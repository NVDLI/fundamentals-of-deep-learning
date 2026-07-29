# Third-Party Notices

This file contains notices for third-party open source software packages
included in or used by this project, as required for distribution under the
project's open source license.

---

## Third-Party OSS Dependencies

The following packages are listed in `course_content/environment/requirements.txt`
and are installed inside the project container. They are not modified or
redistributed as source; they are used at runtime. License texts are available
from each project's official repository.

| Package | Version | License | Source |
|---------|---------|---------|--------|
| boto3 | 1.34.104 | Apache-2.0 | https://github.com/boto/boto3 |
| datasets | 5.0.0 | Apache-2.0 | https://github.com/huggingface/datasets |
| huggingface_hub | 1.21.0 | Apache-2.0 | https://github.com/huggingface/huggingface_hub |
| kagglehub | 1.0.2 | Apache-2.0 | https://github.com/Kaggle/kagglehub |
| matplotlib | 3.8.4 | PSF-based (matplotlib License) | https://github.com/matplotlib/matplotlib |
| opencv-python | 4.9.0.80 | MIT (PyPI wrapper), Apache-2.0 (bundled OpenCV) | https://github.com/opencv/opencv-python |
| pandas | 2.3.3 | BSD-3-Clause | https://github.com/pandas-dev/pandas |
| sentencepiece | 0.2.1 | Apache-2.0 | https://github.com/google/sentencepiece |
| sacremoses | 0.1.1 | MIT | https://github.com/alvations/sacremoses |
| tables | 3.9.2 | BSD-3-Clause | https://github.com/PyTables/PyTables |
| transformers | 5.12.1 | Apache-2.0 | https://github.com/huggingface/transformers |
| testbook | 0.4.2 | BSD-3-Clause | https://github.com/nteract/testbook |
| tqdm | 4.66.3 | MIT AND MPL-2.0 | https://github.com/tqdm/tqdm |
| requests | 2.32.2 | Apache-2.0 | https://github.com/psf/requests |
| regex | 2026.6.28 | Apache-2.0 | https://github.com/mrabarnett/mrab-regex |

> **Note:** The PyTorch base image (`pytorch/pytorch:2.4.1-cuda11.8-cudnn9-runtime`)
> is provided by the PyTorch project under the BSD-3-Clause license and by NVIDIA
> under the NVIDIA Deep Learning Container License. It is not redistributed by this
> project; users pull it directly from Docker Hub.

---

## Third-Party Media Notices

## Microsoft 365 Premium Creative Content

Some PDFs, presentations, documents, or source files in this project may include
Microsoft 365 stock images, icons, or other premium creative content.

These Microsoft assets are not licensed under this project’s open source license.
They are included only under Microsoft’s applicable Microsoft 365 premium
creative content terms:

https://support.microsoft.com/en-us/office/foundations-experiences/what-am-i-allowed-to-use-premium-creative-content-for

Recipients may not extract, reuse, sublicense, or redistribute those Microsoft
assets separately under the project’s open source license. Any use of those
assets outside the included Microsoft 365 document, exported PDF, presentation,
or similar file must be separately permitted by Microsoft.



## ASL-HG images

Files:

- `course_content/tutorials/images/A.jpg`
- `course_content/tutorials/images/B.jpg`

Source: ASL-HG: American Sign Language Hand Gesture Image Dataset

Creators: Md. Famidul Islam Pranto, Md. Rifatul Islam, Md. Ali Akbor,
Nabonita Ghosh, Md. Rahatun Alam, Sudipto Chaki, and Md Masudul Islam.

- Dataset copy: https://huggingface.co/datasets/juanjodurillo/asl-hg
- Canonical record: https://doi.org/10.17632/j4y5w2c8w9.1
- License: Creative Commons Attribution 4.0 International
- Modifications: Images were selected and prepared for course presentation.

## ASL alphabet

File: `course_content/tutorials/images/asl.png`

- Creator: Ds13 (Darren Stone)
- Source: https://commons.wikimedia.org/wiki/File:Asl_alphabet_gallaudet.png
- Status: Released into the public domain by the creator
- Modifications: Original file renamed to `asl.png`; image content was not modified


## Jack Russell Terrier photograph

File: `course_content/tutorials/data/doggy_door_images/happy_dog.jpg`

- Photographer: Plank
- Photographer profile: https://commons.wikimedia.org/wiki/User:Plank
- Source: https://commons.wikimedia.org/wiki/File:Jack_Russell_Terrier_1.jpg
- License: Creative Commons Attribution 3.0 Unported
- License URL: https://creativecommons.org/licenses/by/3.0/
- Modification: Resized for course use

## MNIST figure

File: `course_content/tutorials/images/mnist1.png`

`mnist1.png` is an NVIDIA-created selection and arrangement of samples
from the MNIST Database of Handwritten Digits.

- MNIST authors: Yann LeCun, Corinna Cortes, and Christopher J. C. Burges
- Dataset source: https://yann.lecun.org/exdb/mnist/
- Retrieval method: `torchvision.datasets.MNIST`
- Modification: NVIDIA selected and arranged samples into one educational figure.

CC BY 4.0 covers NVIDIA's selection, arrangement, and presentation.

## Penny and brown_bear within the Corgi dataset

Files:

- `course_content/tutorials/images/Penny.jpg`
- `course_content/tutorials/data/doggy_door_images/brown_bear.jpg`

- Creator/licensor: Danielle Detering 
- Source: https://www.kaggle.com/datasets/danielledetering/penny-the-corgi
- License: Creative Commons Attribution 4.0 International
- License: https://creativecommons.org/licenses/by/4.0/
- Modifications: Selected and incorporated into the course materials.

## Sleepy cat photograph

File:

- `course_content/tutorials/data/doggy_door_images/sleepy_cat.jpg`

- Creator/licensor: Vadim Kudlay (NVIDIA employee)
- Copyright: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
- Source: Original photograph taken by Vadim Kudlay and supplied with authorization for distribution under CC BY 4.0.
- License: Creative Commons Attribution 4.0 International
- License: https://creativecommons.org/licenses/by/4.0/
- Modifications: Incorporated into the course materials.