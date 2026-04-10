---
icon: lucide/info
hide:
    - toc
    - path
    - footer
---

# Strato

<div class="tag-container" markdown>

Researchers :lucide-check:
{ .hpc-tag title="Indicates if the platform is accessible for researchers (e.g., PhD students, postdocs, faculty) for research purposes." }

Students :lucide-ban:
{ .hpc-tag title="Indicates if the platform is accessible to students for educational purposes (e.g., coursework, projects, thesis)." }

Sensitive Data :lucide-ban:
{ .hpc-tag title="Whether the platform supports processing and storing sensitive or confidential data" }

CPU processing :lucide-check:
{ .hpc-tag title="Indicates if the platform supports computational tasks that only require CPU resources." }

GPU processing :lucide-check:
{ .hpc-tag title="Indicates if the platform supports computational tasks that require GPU resources for acceleration (e.g., deep learning)." }

Unlimited compute :lucide-ban:
{ .hpc-tag title="Whether the platform allows unrestricted compute usage, without limitations on the amount of usage time." }

Terminal interface :lucide-check:
{ .hpc-tag title="The method used to access the platform." }

Pre-installed apps :lucide-ban:
{ .hpc-tag title="Indicates if the platform comes with pre-installed applications or frameworks for convenience (e.g., Ansys, PyTorch, TensorFlow)." }

Collaboration friendly :lucide-check:
{ .hpc-tag title="Indicates if the platform supports collaborative work (e.g., sharing resources, co-editing, team projects)." }

Working interactively :lucide-check:
{ .hpc-tag title="Indicates if the platform supports interactive workflows where users can interact with running processes (e.g., Jupyter notebooks)." }

Possible to add GUI :lucide-check:
{ .hpc-tag title="Whether it is possible to run graphical user interfaces (GUIs) on the platform (e.g., remote desktops, JupyterLab)." }

Not for storage :lucide-ban:
{ .hpc-tag title="This platform is not designed for long term storage of research data." }

</div>

## Introduction

Strato is a cluster of hardware that is virtualised to create instances that essentially function as a regular computer environment. Strato Instances are virtual machines, that can be launched by the user when they need it. When the instance has been created, it can be accessed from a terminal application on the user's local computer. 

!!! info "Not for confidential data"
    With Strato you are only allowed to work with data that is **not confidential** according to [AAU’s data classification model](https://www.security.aau.dk/data-classification){target="_blank} (classified as level 1).

    If you would like to work with a higher data classification level (levels 2 and 3), then we support HPC platforms [UCloud](/ucloud/) and [TAAURUS](/taaurus).

[Get access to Strato](/strato/how-to-access){ .md-button .md-button--primary }

## Features

<div class="grid cards" markdown>

-   __Customizable virtual machines__

    Adjust CPU, RAM, and storage to match research needs across changing workloads and project phases.

    ---

    ![Customizable virtual machines](/assets/img/strato/strato-feature-1.png)

-   __Scalable computing power__

    Scale resources up or down for strong performance and cost-efficiency during intensive computational tasks.

    ---

    ![Scalable computing power](/assets/img/strato/strato-feature-2.png)

-   __CPU & GPU Support__

    Use powerful CPU and GPU resources for simulations, machine learning, and model training workflows.

    ---

    ![CPU & GPU Support](/assets/img/strato/strato-feature-3.png)

-   __Run your application in a web browser__

    Run applications on remote servers and access them through a web browser on your computer.

    ---

    ![Run your application in a web browser](/assets/img/strato/strato-feature-4.png)



</div>