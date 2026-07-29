# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import torch.nn as nn
from pathlib import Path
import numpy as np
import pandas as pd
from datasets import load_dataset

class MyConvBlock(nn.Module):
    def __init__(self, in_ch, out_ch, dropout_p):
        kernel_size = 3
        super().__init__()

        self.model = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, kernel_size, stride=1, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(),
            nn.Dropout(dropout_p),
            nn.MaxPool2d(2, stride=2)
        )

    def forward(self, x):
        return self.model(x)


def get_batch_accuracy(output, y, N):
    pred = output.argmax(dim=1, keepdim=True)
    correct = pred.eq(y.view_as(pred)).sum().item()
    return correct / N


def train(model, train_loader, train_N, random_trans, optimizer, loss_function, device):
    loss = torch.zeros((), device=device)
    correct = torch.zeros((), device=device)

    model.train()
    for x, y in train_loader:
        output = model(random_trans(x))
        optimizer.zero_grad()
        batch_loss = loss_function(output, y)
        batch_loss.backward()
        optimizer.step()

        loss    += batch_loss.detach()
        correct += output.argmax(dim=1).eq(y).sum()

    accuracy = correct / train_N
    print('Train - Loss: {:.4f} Accuracy: {:.4f}'.format(loss.item(), accuracy.item()))


def validate(model, valid_loader, valid_N, loss_function, device):
    loss = torch.zeros((), device=device)
    correct = torch.zeros((), device=device)

    model.eval()
    with torch.no_grad():
        for x, y in valid_loader:
            output = model(x)
            loss    += loss_function(output, y)
            correct += output.argmax(dim=1).eq(y).sum()

    accuracy = correct / valid_N
    print('Valid - Loss: {:.4f} Accuracy: {:.4f}'.format(loss.item(), accuracy.item()))
