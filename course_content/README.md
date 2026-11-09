# Fundamentals of Deep Learning Course Notebooks

This repository contains Jupyter notebooks and environment setup files for a hands-on deep learning course. The notebooks introduce  image classification, convolutional neural networks, data augmentation, model deployment, transfer learning, and natural language processing.

## Repository Contents

```text
.
├── Dockerfile
├── environment/
│   ├── entrypoint.sh
│   └── requirements.txt
└── tutorials/
    ├── 00_jupyterlab.ipynb
    ├── 01_mnist.ipynb
    ├── 02_asl.ipynb
    ├── 03_asl_cnn.ipynb
    ├── 04a_asl_augmentation.ipynb
    ├── 04b_asl_predictions.ipynb
    ├── 05a_doggy_door.ipynb
    ├── 05b_corgi_door.ipynb
    ├── 06_nlp.ipynb
    └── utils.py
```

### `Dockerfile`

Builds a JupyterLab environment based on `pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime`. It installs the Python packages needed by the notebooks, copies the contents of `tutorials/` into `/dli/tutorials`, exposes port `8888`, and starts JupyterLab.

The Docker image is intended for hosts with an NVIDIA GPU and `nvidia-container-toolkit` installed.

### `environment/`

Contains environment setup files:

- `requirements.txt`: Python dependencies for running the notebooks with `pip`.
- `entrypoint.sh`: JupyterLab startup script for environments that use a shell entrypoint.

### `tutorials/`

Contains the course notebooks:

- `00_jupyterlab.ipynb`: JupyterLab introduction and basic workflow.
- `01_mnist.ipynb`: Image classification with the MNIST handwritten digit dataset.
- `02_asl.ipynb`: Image classification with an American Sign Language dataset.
- `03_asl_cnn.ipynb`: Convolutional neural networks for image classification.
- `04a_asl_augmentation.ipynb`: Data augmentation to improve model generalization.
- `04b_asl_predictions.ipynb`: Using a trained model to make predictions.
- `05a_doggy_door.ipynb`: Using pre-trained models.
- `05b_corgi_door.ipynb`: Transfer learning with a pre-trained model.
- `06_nlp.ipynb`: Natural language processing with sequence data.
- `utils.py`: Shared helper code used by the notebooks.

## Run in Google Colab

**Only run the Setup for Google Colab cell if you are using Google Colab.**
In other environments, skip it and continue with the lesson.

Open a course notebook using a Colab link, select a GPU under **Runtime → Change
runtime type**, and run the **Setup for Google Colab** cell. The setup code is collapsed
in Colab and also runs when choosing **Run all**. It installs only missing
packages needed by that lab and downloads its support files. Continue when
the cell displays **Course ready**.

Run setup again after starting a new runtime. Re-running it in the same runtime
reuses installed packages and existing support files, and preserves files
created during the lesson.

| Lab | Support files downloaded from GitHub |
|---|---|
| 01 MNIST | None; torchvision downloads the dataset |
| 02 ASL | `data/data.py` |
| 03 CNN | `data/data.py` |
| 04a Augmentation | `utils.py`, `data/data.py` |
| 04b Predictions | `utils.py`, `images/A.jpg`, `images/B.jpg` |
| 05a Doggy Door | `data/imagenet_class_index.json` and the three images in `data/doggy_door_images/` |
| 05b Corgi Door | `utils.py`, `data/data.py` |
| 06 NLP | None; transformers downloads the models and tokenizer |

Markdown illustrations load directly from GitHub. Lab 4b also needs
`model.pth`: generate it in Lab 4a, download it, and upload it to Lab 4b's Colab
session as explained in that notebook. Setup does not download or overwrite it.

The setup cell does nothing outside Google Colab. Docker and local installations
continue to use `environment/requirements.txt`.

## Run with Docker

From this directory, build the image:

```bash
docker build -t fdl-course .
```

Run JupyterLab:

```bash
docker run --rm -it --gpus all -p 8888:8888 fdl-course
```

Then open:

```text
http://localhost:8888/lab
```

To keep notebook edits on your local machine, mount the `tutorials/` directory when running the container:

```bash
docker run --rm -it --gpus all -p 8888:8888 \
  -v "$PWD/tutorials:/dli/tutorials" \
  fdl-course
```

If port `8888` is already in use, map a different local port:

```bash
docker run --rm -it --gpus all -p 8890:8888 fdl-course
```

Then open `http://localhost:8890/lab`.

## Run Locally with `pip`

If you do not want to use Docker, create a Python virtual environment (Python 3.10+), install PyTorch 2.5 or newer, and then install the dependencies from `environment/requirements.txt`.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install torch==2.7.1
python -m pip install -r environment/requirements.txt
```

Start JupyterLab from the repository directory:

```bash
jupyter lab tutorials
```

or simply by running the script on `environment/entrypoint.sh`

```bash
sh environment/entrypoint.sh
```

JupyterLab will print a local URL in the terminal. Open that URL in your browser, then select a notebook from the file browser.

## Try Activity tracking locally on stage

This optional pilot requires NVIDIA VPN access to download the SDK wheel and
reach the stage API. Complete the local course setup above first. From
`course_content/`, install JupyterLab 4.6.2 and the SDK into the same active
Python environment. The SDK requires JupyterLab `>=4.6.2,<4.7`.

```bash
python -m pip install jupyterlab==4.6.2
python -m pip install --no-deps --require-hashes -r environment/requirements-activity-stage.txt
python -m jupyterlab tutorials --ServerApp.ip=localhost --ServerApp.port=8888 --ServerApp.port_retries=0
```

Open the token URL printed by JupyterLab, using `http://localhost:8888` as the
origin. Stage registers this exact origin. If port 8888 is occupied, stop the
other server before starting this one.

In JupyterLab, open **Settings → Settings Editor → DLI Activity** and set these
three fields. Use the JSON Settings Editor if needed.

```json
{
  "baseUrl": "https://activity-api.stage.learn.nvidia.com",
  "artifactId": "fundamentals-of-deep-learning",
  "artifactVersion": "main"
}
```

Save the settings and reload JupyterLab. Then open `01_mnist.ipynb` and run the lesson through the
training loop under **1.7.5 The Training Loop**. Successful execution of the cell
with the `dli:complete:01:mnist-trained` tag creates an anonymous stage session
and sends milestone `01:mnist-trained`.

This pilot has no progress panel, session persistence across page reloads, or
overall course completion. Keep these settings for stage use only.

## Notes

- Some notebooks may download datasets or pre-trained model files the first time they run.
- The Docker setup uses a CUDA-enabled PyTorch image. On machines without an NVIDIA GPU, the local `pip` setup is usually the simpler option.
- Stop JupyterLab with `Ctrl+C` in the terminal where it is running.
