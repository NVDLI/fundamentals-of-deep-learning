# Fundamentals of Deep Learning

[![Launch on Brev](https://img.shields.io/badge/Launch%20on-Brev-76B900)](https://brev.nvidia.com/) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue)](https://creativecommons.org/licenses/by/4.0/) [![License](https://img.shields.io/badge/License-Apache%202.0-blue)](LICENSE)

Fundamentals of Deep Learning is an open-source, hands-on course from the NVIDIA Deep Learning Institute (DLI) that introduces neural networks, convolutional architectures, and transfer learning through interactive Jupyter notebooks.

## Learning Outcomes

In these labs, learners will:

- Build and train neural networks using PyTorch on real image datasets
- Apply convolutional neural networks (CNNs) to image classification tasks
- Use data augmentation and transfer learning to improve accuracy on limited data
- Manage the bias-variance tradeoff and apply techniques to address overfitting
- Deploy a trained model to make predictions on new, unseen data

## Course Modules

| # | Module | Slide Deck | Notebooks |
|---|---|----------|--------|
| 01 | An Introduction to Deep Learning | [slides_01.pptx](./course_content/slides/slides_01.pptx) | [01_mnist.ipynb](./course_content/tutorials/01_mnist.ipynb) |
| 02 | How a Neural Network Trains | [slides_02.pptx](./course_content/slides/slides_02.pptx) | [02_asl.ipynb](./course_content/tutorials/02_asl.ipynb) |
| 03 | Convolutional Neural Networks | [slides_03.pptx](./course_content/slides/slides_03.pptx) | [03_asl_cnn.ipynb](./course_content/tutorials/03_asl_cnn.ipynb) |
| 04 | Data Augmentation and Deployment | [slides_04.pptx](./course_content/slides/slides_04.pptx) | [04a_asl_augmentation.ipynb](./course_content/tutorials/04a_asl_augmentation.ipynb) <br> [04b_asl_predictions.ipynb](./course_content/tutorials/04b_asl_predictions.ipynb) |
| 05 | Pre-Trained Models | [slides_05.pptx](./course_content/slides/slides_05.pptx) | [05a_doggy_door.ipynb](./course_content/tutorials/05a_doggy_door.ipynb) <br> [05b_corgi_door.ipynb](./course_content/tutorials/05b_corgi_door.ipynb) |
| 06 | Advanced Architectures | [slides_06.pptx](./course_content/slides/slides_06.pptx) | [06_nlp.ipynb](./course_content/tutorials/06_nlp.ipynb)  |

> Note: Slide decks are not included in this GitLab branch because of repository size limits.
> For review, the decks are available in Google Drive: [slide decks](https://drive.google.com/drive/folders/1ShCS0EOAG26cuLRkedbt5t_qPzmPoyHW?usp=sharing).
> They will be added to the public GitHub repository before release.

## Usage

### Getting Started

#### 1. Launch with Brev (Recommended)

🌟 [Launch this course on NVIDIA Brev](https://brev.nvidia.com/)

1. Click the **Launch on Brev** button above (or the badge at the top of this README).
2. Sign in or create a free NVIDIA Brev account.
3. Select a GPU instance — an NVIDIA T4 or L4 is sufficient for all five labs.
4. Click **Deploy**. The environment will be ready in ~2 minutes with CUDA,
   Python, and all dependencies pre-installed.
5. Open JupyterLab from the Brev console and navigate to the `course_content/tutorials/` directory.

#### 2. Clone and run locally

```bash
git clone https://github.com/NVDLI/fundamentals-of-deep-learning.git
cd course_content
```

**Prerequisites:** Python 3.9+, an NVIDIA GPU with CUDA 11.8+ (CPU-only works
but is slow for later notebooks), and conda or pip.

```bash
pip install -r environment/requirements.txt
jupyter lab
```

Then open <http://localhost:8888> in your browser and navigate to the
`tutorials/` directory.

#### 3. Run with Docker

To deploy the content with the provided `Dockerfile`, run:

```bash
docker build -t fdl-app . && docker run -d -p 8888:8888 --name fdl-container --gpus all fdl-app
```

Then open <http://localhost:8888> in your browser and navigate to the
`tutorials/` directory.

## Contributing

We welcome contributions from the community. To contribute:

1. Fork this repository and create a feature branch:
   ```bash
   git checkout -b feature/your-improvement
   ```
2. Make your changes. Ensure notebooks are cleared of all output before committing.
3. Open a Pull Request with a clear description of what changed and why.

For significant changes or new notebooks, please open an issue first to discuss.
Please do not commit datasets or large binary files — use download scripts instead.

See [CONTRIBUTING](CONTRIBUTING.md) for full guidelines.

## License

This repository uses a mixed licensing model:

- Source-code files and code cells in Jupyter notebooks:
  [Apache License 2.0](LICENSES/Apache-2.0.txt)
- Documentation, Markdown and raw notebook cells, and NVIDIA-created
  educational media:
  [Creative Commons Attribution 4.0 International](LICENSES/CC-BY-4.0.txt)
- Third-party material: its original license, as documented in
  [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)

Each complete Jupyter notebook is dual-licensed: code cells under Apache-2.0
and non-code cells under CC-BY-4.0. The combined dual-license terms are in
[LICENSES/CC-BY-4.0-Apache2_Dual_License.txt](LICENSES/CC-BY-4.0-Apache2_Dual_License.txt).

NVIDIA names, logos, and trademarks are not licensed for general reuse.
