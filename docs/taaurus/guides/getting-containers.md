# Getting containers on TAAURUS

To run most applications on the TAAURUS GPU cluster you need to do it inside **containers** - self-contained environments that include all the software and dependencies you need. TAAURUS uses [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html){target=_blank} to run containers.

## What is a container?

A container is like a pre-packaged software environment that includes:

- The application (Python, PyTorch, TensorFlow, etc.)
- All required libraries and dependencies

Think of it as a complete, portable computer environment that works the same way every time.

## Methods to obtain containers

1. **Use pre-downloaded containers on TAAURUS** - Quickest option 
2. **Download containers locally or on AI Cloud** - For specific versions
3. **Build your own container locally or on AI Cloud** - For custom environments

<hr>

??? info "1. Pre-downloaded containers"

    The easiest way to get started is using containers that are already available on TAAURUS. These are stored in `/pack/Singularity` and are regularly updated.

    ### Available Containers

    Check what's available:

    ```bash
    ls /pack/Singularity
    ```

    ### Using pre-downloaded containers

    You can use these containers by first copying them to your projects work directory:

    ```bash
    # Example: Using PyTorch container
    cp /pack/Singularity/pytorch/pytorch_25.05.sif /media/test05/work
    ```

    Remember to replace `test05` with your projects name.


??? info "2. Download or build containers locally"

    This guide will show you how to use an application called [Podman](https://podman.io/) on your local computer to build containers, transfer it to TAAURUS, and convert it into a Singularity image.

    !!! info "Why Use Podman to Build Containers Locally?"
        Building Singularity containers directly on TAAURUS requires an internet connection which is blocked on TAAURUS. To overcome this, you can use an application called [Podman](https://podman.io/) to build containers **locally** on your own machine. Podman is a container management tool similar to [Docker](https://www.docker.com/). Once created, the container can be transferred to TAAURUS and converted into a Singularity image.

    ### Install Podman on your local machine
    Before starting, you'll need to install [Podman](https://podman.io/) on your local machine to build containers. Podman is available for Windows, macOS, and Linux, and the installation process varies slightly depending on your operating system.

    ===+ "Windows"

        1. Begin by downloading the [Podman Windows installer](https://github.com/containers/podman/releases) (.exe). Make sure to choose version 4.1 or later for compatibility with the features discussed in this guide.

        2. Run the installer and follow the prompts to complete the installation. A system restart may be required.

        3. Once installed, open PowerShell and initialize your first Podman machine with the following command:

            ```
            podman machine init
            ```

        !!! info "Automatic WSL Installation"
            If [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) is not already installed, Podman will prompt you to install it automatically during the `podman machine init` process. Accepting this will install WSL and restart your system. After logging back in, the machine creation will continue. If you prefer, you can install WSL manually before running `podman machine init`.

        To start the Podman machine, run:

        ```
        podman machine start
        ```

        This starts a virtual machine where containers can be build.

    ===+ "macOS"
        4. You can either download the latest Podman installer from the [Podman GitHub releases](https://github.com/containers/podman/releases) or use Homebrew (recommended for macOS users) to install Podman:

            ```
            brew install podman
            ```

        5. Once installed, initialize your first machine:

            ```
            podman machine init
            ```

        6. Start the machine:

            ```
            podman machine start
            ```

            This starts a virtual machine where containers can be build.

    ===+ "Linux"
        On most Linux distributions, Podman is available through the package manager. Follow the instructions for your specific distribution below.

        7. Update your system: It's always good practice to update your system before installing new software.

            ```
            sudo apt update && sudo apt upgrade   # Debian-based distros (Ubuntu, etc.)
            sudo dnf update                       # Fedora-based distros
            ```

        8. Install Podman:

            * Debian-based distributions (Ubuntu, Debian, etc.):

                ```
                sudo apt install podman -y
                ```

            * Fedora-based distributions (Fedora, CentOS, RHEL): Podman may already be installed on Fedora. If not:

                ```
                sudo dnf install podman -y
                ```

            * Arch Linux:

                ```
                sudo pacman -S podman
                ```

            * Other distributions: Refer to the [official Podman installation guide](https://podman.io/docs/installation#installing-on-linux) for installation instructions for other Linux distributions.

        9. After installation, verify that Podman is installed correctly by checking the version:

            ```
            podman --version
            ```
                  
            You should see the installed version of Podman. If successful, you are ready to proceed.

    ### Download or build a container with Podman

    ===+ "Option A: Downloading a Container with Podman"

        If you don’t need to build your own container, Podman can also download (“pull”) existing containers from public registries such as [Docker Hub](https://hub.docker.com/) or [NVIDIA NGC](https://catalog.ngc.nvidia.com/).

        **Example: Download a container from Docker Hub**

        To download an official Python container:
            
        ```
        podman pull docker.io/library/python:3.10-slim
        ```

        You can list the downloaded containers with:
        ```
        podman images
        ```

        **Save the downloaded image as a TAR file:**
            
        Regardless of whether the image came from Docker Hub or NGC, export it for transfer to TAAURUS:
            
        ```
        podman save -o python-slim.tar docker.io/library/python:3.10-slim
        ```

        This will create a file named python-slim.tar.

    ===+ "Option B: Building a Container with Podman"
        To create a container, you first need to define what the container will look like and how it will behave. This is done using a special text file called a [Dockerfile](https://docs.docker.com/reference/dockerfile/). A Dockerfile is essentially a set of instructions that tell Podman how to create the container, such as what software to include and what commands to run when the container starts.

        When creating a Dockerfile, it's important that the file has no extension (like `.txt` or `.doc`). The file should simply be named *Dockerfile*. This is because tools like Podman specifically look for a file named `Dockerfile` to understand how to build the container.

        Here’s an example of a simple Dockerfile for a Python-based container:

        ``` title="Dockerfile"
        # Use an official Python image as the base
        FROM python:3.9-slim

        # Install necessary Python libraries
        RUN pip install --no-cache-dir numpy scipy

        # Set the command to run when the container starts
        CMD ["python3"]
        ```

        **What does this Dockerfile do?**
        `FROM python:3.9-slim`: This tells Podman to start from an existing container image, in this case, a lightweight version of Python 3.9. It provides a base to build your custom container.

        `RUN pip install --no-cache-dir numpy scipy`: This command installs the Python libraries `numpy` and `scipy` inside the container.
            
        `CMD ["python3"]`: This sets the default action when the container runs—in this case, it starts the Python interpreter.


        Next, save the Dockerfile in an **empty** folder on your computer. It's important to create an empty folder to save the Dockerfile in because when you build a container with Podman, it includes all the files from the current directory in the container image by default.

        In the directory where your Dockerfile is located, run:

        ```
        podman build -t my-python-app .
        ```

        !!! info "INFO: It may require a lot of space"
            Building the container may take up a lot of space on your local computer. A simple PyTorch container can take up approx. 20GB of space.

            Replace `my-python-app` with the name you want for your container image.

        ### Saving and Exporting the Container
        Once your container is built, export it as a TAR file so that it can be transferred to the Slurm cluster:

        ```
        podman save -o my-python-app.tar my-python-app
        ```

        This will create a file named `my-python-app.tar`.


    ### Transferring the Container to TAAURUS

    Follow our [import guide](/taaurus/guides/import-export-of-data/) to transfer the container to TAAURUS.

    ### Converting the Container to Singularity

    On TAAURUS, we need to set the `SINGULARITY_TMPDIR` and `SINGULARITY_CACHEDIR` environment variables, to speed up repeated operations. We will use these variables to a temporary directory (`/media/project/work/.singularity/tmp/` and `/media/project/work/.singularity/cache/`). 
      
    Remember to replace `project` with your projects name.

    ```
    export SINGULARITY_TMPDIR="/media/project/work/.singularity/tmp/"
    export SINGULARITY_CACHEDIR="/media/project/work/.singularity/cache/"
    mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR
    ```

    Now, convert the Podman image into a Singularity image:

    ```
    srun singularity build my-python-app.sif docker-archive://my-python-app.tar
    ```

    This will convert the container into a Singularity Image File (.sif) that can be used in the cluster.


    ### Test running the Singularity Container (optional)
    Submit a job to Slurm using the newly converted Singularity image:

    ```
    srun --gres=gpu:1 singularity exec my-python-app.sif python3 --version
    ```

??? info "3. Download or build containers (via AI Cloud)"

    Network access from TAAURUS compute nodes is restricted, so you cannot pull or build containers directly on TAAURUS. The easiest way to get specific or custom containers is to use AAU’s HPC platform [AI Cloud](/ai-cloud/), which has a similar setup (Slurm + Singularity) and allows internet access for pulling/building images. AI Cloud also provides the same GPU type (NVIDIA L40S), making it an ideal testing environment before running the container on TAAURUS.

    ### Workflow

    1. Get access to AI Cloud: see [How to access AI Cloud](/ai-cloud/how-to-access/)
    2. Log in to AI Cloud: see [Log in guide](/ai-cloud/getting-started/login/)
    3. Get the container by either:
        1. Pull container images on AI Cloud: see [Pulling container images from the internet](/ai-cloud/additional-guides/download-container-images/)
        2. Build your own container image on AI Cloud: see [Building your own container image](/ai-cloud/additional-guides/building-your-own-container-image/)
    4. Export the resulting `.sif` from AI Cloud: see [Transfer files between a server and a local computer](/ai-cloud/getting-started/file-management/)
    5. Import it into TAAURUS: see [Import & export of data](/taaurus/guides/import-export-of-data/)


You are now ready to proceed to learn about [**using containers to run jobs :octicons-arrow-right-24:**](using-containers.md)