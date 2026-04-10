---
icon: lucide/info
hide:
    - toc
    - path
    - footer
---


# AI Cloud

<div class="tag-container" markdown>

Researchers :lucide-check:
{ .hpc-tag title="Indicates if the platform is accessible for researchers (e.g., PhD students, postdocs, faculty) for research purposes." }

Students :lucide-ban:
{ .hpc-tag title="Indicates if the platform is accessible to students for educational purposes (e.g., coursework, projects, thesis)." }

Sensitive Data :lucide-ban:
{ .hpc-tag title="Whether the platform supports processing and storing sensitive or confidential data" }

CPU processing :lucide-ban:
{ .hpc-tag title="Indicates if the platform supports computational tasks that only require CPU resources." }

GPU processing :lucide-check:
{ .hpc-tag title="Indicates if the platform supports computational tasks that require GPU resources for acceleration (e.g., deep learning)." }

Unlimited compute :lucide-check:
{ .hpc-tag title="Whether the platform allows unrestricted compute usage, without limitations on the amount of usage time." }

Terminal interface :lucide-check:
{ .hpc-tag title="The method used to access the platform." }

Pre-installed apps :lucide-check:
{ .hpc-tag title="Indicates if the platform comes with pre-installed applications or frameworks for convenience (e.g., Ansys, PyTorch, TensorFlow)." }

Collaboration friendly :lucide-check:
{ .hpc-tag title="Indicates if the platform supports collaborative work (e.g., sharing resources, co-editing, team projects)." }

Working interactively :lucide-ban:
{ .hpc-tag title="Indicates if the platform supports interactive workflows where users can interact with running processes (e.g., Jupyter notebooks)." }

Possible to add GUI :lucide-ban:
{ .hpc-tag title="Whether it is possible to run graphical user interfaces (GUIs) on the platform (e.g., remote desktops, JupyterLab)." }

Not for storage :lucide-ban:
{ .hpc-tag title="This platform is not designed for long term storage of research data." }

</div>

## Introduction

AI Cloud is a GPU cluster made up of a collecton of NVIDIA GPU's, designed for processing GPU-demanding machine learning workloads. The platform is accessed through a terminal application on the user's local machine. From here the user logs in to a front end node, where files management and job submission to the compute nodes takes place.

!!! info "Not for confidential data"
    With AI Cloud you are only allowed to work with data that is **not confidential** according to [AAU’s data classification model](https://www.security.aau.dk/data-classification){target="_blank} (classified as level 1).

    If you would like to work with a higher data classification level (levels 2 and 3), then we support HPC platforms [UCloud](/ucloud/) and [TAAURUS](/taaurus).

[Get access to AI Cloud](/ai-cloud/how-to-access){ .md-button .md-button--primary }

## Features

<div class="grid cards" markdown>

-   __High-Performance GPU Cluster__

    Harness powerful NVIDIA GPUs to process large datasets and complex models quickly and efficiently.

    ---

    ![High-Performance GPU Cluster](/assets/img/ai-cloud/ai-cloud-feature-1.png)

-   __Containerization for Flexibility__

    Keep software environments consistent across nodes, supporting flexible workflows and reproducible experiments.

    ---

    ![Containerization for Flexibility](/assets/img/ai-cloud/ai-cloud-feature-2.png)

-   __Efficient Batch Processing__

    Use Slurm for reliable scheduling, streamlined batch execution, and efficient management of large workloads.

    ---

    ![Efficient Batch Processing](/assets/img/ai-cloud/ai-cloud-feature-3.png)

-   __Quota and job control__

    Manage large workloads with clear quotas, partitions, and scheduling controls for predictable platform usage.

    ---

    ![Quota and job control](/assets/img/ai-cloud/ai-cloud-feature-4.png)

</div>
