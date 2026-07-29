# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# PyTorch + CUDA 11.8 + cuDNN 8 — requires NVIDIA GPU + nvidia-container-toolkit on the host
# Run with: docker run --gpus all ...
FROM pytorch/pytorch:2.4.1-cuda11.8-cudnn9-runtime

# Avoid interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# System deps (Pillow needs libjpeg/libpng)
RUN apt-get update && apt-get install -y --no-install-recommends \
        libjpeg-turbo8 \
        libpng16-16 \
        git \
        gcc \
    && rm -rf /var/lib/apt/lists/*
RUN apt update && apt install -y libsm6 libxext6 libxrender-dev

COPY ./environment/requirements.txt .
RUN pip install -r requirements.txt


# Uncomment the following to upgrade to latest jupyterlab
RUN pip install --upgrade jupyterlab==4.2.0
RUN pip install ipywidgets==8.1.2

ENV SHELL=/bin/bash
ENV PYTHONPATH=/dli
WORKDIR /dli/
COPY . .

WORKDIR /dli/tutorials

EXPOSE 8888

CMD ["jupyter", "lab", \
     "--ip=0.0.0.0", \
     "--allow-root", \
     "--no-browser", \
     "--NotebookApp.token=", \
     "--NotebookApp.password="]
