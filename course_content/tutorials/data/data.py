# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import kagglehub
import os
import shutil
import torch
import torch.nn as nn

import numpy as np
import pandas as pd

from datasets import load_dataset
from pathlib import Path


# Classes excluded from training — digits and letters requiring hand motion.
ASL_EXCLUDE = frozenset({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Z'})


def download_asl_dataset(data_dir="data/asl_data", exclude=None):
    """Download the ASL-HG dataset from HuggingFace Hub and return as DataFrames.

    If sign_mnist_train.csv and sign_mnist_valid.csv already exist in *data_dir*,
    they are loaded and returned directly (no network access).  Otherwise the
    dataset is downloaded from HuggingFace Hub, each image is converted to a
    28×28 grayscale representation and flattened, and the results are saved as
    CSV files before being returned.

    The CSV format intentionally mirrors the original sign-language MNIST layout:
        label  pixel1  pixel2  ...  pixel784

    where *label* is a contiguous integer in [0, 23] and the pixel values are
    uint8 integers in [0, 255].

    Label mapping (alphabetical order after exclusions):
        A=0  B=1  C=2  D=3  E=4  F=5  G=6  H=7  I=8
        K=9  L=10 M=11 N=12 O=13 P=14 Q=15 R=16 S=17
        T=18 U=19 V=20 W=21 X=22 Y=23

    Args:
        data_dir : directory for the cached CSV files (default: "data/asl_data")
        exclude  : set of class-name strings to skip (default: ASL_EXCLUDE)

    Returns:
        (train_df, valid_df) — pandas DataFrames ready for MyDataset
    """
    data_dir = Path(data_dir)
    train_csv = data_dir / "sign_mnist_train.csv"
    valid_csv = data_dir / "sign_mnist_valid.csv"

    if train_csv.exists() and valid_csv.exists():
        print(f"Loading cached dataset from '{data_dir}' …")
        return pd.read_csv(train_csv), pd.read_csv(valid_csv)

    print("Downloading ASL dataset from HuggingFace Hub …")

    exclude  = ASL_EXCLUDE if exclude is None else frozenset(exclude)
    hf_ds    = load_dataset("juanjodurillo/asl-hg")

    # Build label mapping: original integer → new contiguous integer (sorted alphabetically)
    all_classes      = hf_ds["train"].features["label"].names   # list[str], indexed by label int
    keep_sorted      = sorted(c for c in all_classes if c not in exclude)
    name_to_new      = {c: i for i, c in enumerate(keep_sorted)}
    old_to_new       = {idx: name_to_new[name]
                        for idx, name in enumerate(all_classes)
                        if name in name_to_new}

    pixel_cols = [f"pixel{i + 1}" for i in range(784)]
    split_map  = {"train": train_csv, "test": valid_csv}  # HF "test" → our "valid"

    data_dir.mkdir(parents=True, exist_ok=True)
    result = {}

    for hf_split, csv_path in split_map.items():
        ds = hf_ds[hf_split]
        print(f"Processing {hf_split} ({len(ds):,} images) …")

        rows = []
        for item in ds:
            orig_idx = item["label"]
            if orig_idx not in old_to_new:
                continue
            new_label = old_to_new[orig_idx]
            # Convert to 28×28 grayscale, flatten to 784 uint8 values
            pixels = np.array(
                item["image"].convert("L").resize((28, 28)),
                dtype=np.uint8
            ).flatten().tolist()
            rows.append([new_label] + pixels)

        df = pd.DataFrame(rows, columns=["label"] + pixel_cols)
        df.to_csv(csv_path, index=False)
        split_label = "valid" if hf_split == "test" else hf_split
        print(f"  {len(df):,} rows saved → '{csv_path}'")
        result[split_label] = df

    print("Dataset ready.")
    return result["train"], result["valid"]


def download_kagglehub_dataset(dataset_name, source_folder, destination_folder):
    folder = Path(destination_folder)
    
    if folder.is_dir():
        print("Data already downloaded.")
    else:
        os.environ["KAGGLEHUB_CACHE"] = "./data"
        path = kagglehub.dataset_download(dataset_name)
        print(f"Success! Dataset downloaded and unzipped to: {destination_folder}")
    
        shutil.move(source_folder, destination_folder)
        shutil.rmtree("data/datasets/")