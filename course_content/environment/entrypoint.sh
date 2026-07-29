# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

jupyter labextension disable "@jupyterlab/apputils-extension:announcements"
jupyter lab \
        --ip 0.0.0.0                               `# Bind to all network interfaces` \
        --allow-root                               `# Allow running as the root user` \
        --no-browser                               `# Do not attempt to launch a browser` \
        --NotebookApp.base_url="/lab"              `# Set a base URL for the lab` \
        --NotebookApp.password=""                  `# Do not require password to access the course`
