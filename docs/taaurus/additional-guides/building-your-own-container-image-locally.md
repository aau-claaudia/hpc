!!! info "This guide is currently in testing phase"
    If you encounter any errors or issues, please provide us with your feedback through the [AAU Service Portal](https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad001310e). Your input is invaluable in helping us improve this resource. Thank you for your understanding!

# Building your own container image locally

##### This guide will show you how to use an application called [Podman](https://podman.io/) on your local computer to build containers, transfer it to AI-LAB, and convert it into a Singularity image.

!!! info "Why Use Podman to Build Containers Locally?"
    Building Singularity containers directly on AI-LAB requires root privileges, which users don’t have. To overcome this, we can use an application called [Podman](https://podman.io/) to build containers **locally** on your own machine. Podman is a container management tool similar to [Docker](https://www.docker.com/), but it doesn't require root privileges to run. Once created, the container can be transferred to AI-LAB and converted into a Singularity image for use on AI-lAB.


## Step 1: Install Podman on your local machine
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
    1. You can either download the latest Podman installer from the [Podman GitHub releases](https://github.com/containers/podman/releases) or use Homebrew (recommended for macOS users) to install Podman:

        ```
        brew install podman
        ```

    2. Once installed, initialize your first machine:

        ```
        podman machine init
        ```

    3. Start the machine:

        ```
        podman machine start
        ```

        This starts a virtual machine where containers can be build.

===+ "Linux"
    On most Linux distributions, Podman is available through the package manager. Follow the instructions for your specific distribution below.

    1. Update your system: It's always good practice to update your system before installing new software.

        ```
        sudo apt update && sudo apt upgrade   # Debian-based distros (Ubuntu, etc.)
        sudo dnf update                       # Fedora-based distros
        ```

    2. Install Podman:

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

    3. After installation, verify that Podman is installed correctly by checking the version:

        ```
        podman --version
        ```
        
        You should see the installed version of Podman. If successful, you are ready to proceed.


## Step 2: Building a Container Locally with Podman
To create a container, you first need to define what the container will look like and how it will behave. This is done using a special text file called a [Dockerfile](https://docs.docker.com/reference/dockerfile/). A Dockerfile is essentially a set of instructions that tell Podman how to create the container, such as what software to include and what commands to run when the container starts.

!!! info "Creating the Dockerfile"
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

!!! info "What does this Dockerfile do?"
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

## Step 3: Saving and Exporting the Container
Once your container is built, export it as a TAR file so that it can be transferred to the Slurm cluster:

```
podman save -o my-python-app.tar my-python-app
```

This will create a file named `my-python-app.tar`.

## Step 4: Transferring the Container to AI-LAB
Use scp or a similar file transfer method ([view examples here](/ai-lab/getting-started/file-management/)) to transfer the TAR file to AI-LAB:

```
scp my-python-app.tar user@student.aau.dk@ailab-fe01.srv.aau.dk:~/some-dir
```

Replace `user@student.aau.dk` with your AAU email address.

Here, `~` represents your user directory on AI-LAB and `/some-dir` a folder in your directory.

## Step 5: Converting the Container to Singularity
[Login](/ai-lab/getting-started/login/) to AI-LAB. Once on the server, we need to set the `SINGULARITY_TMPDIR` and `SINGULARITY_CACHEDIR` environment variables, to speed up repeated operations. We will use these variables to a temporary directory (`$HOME/.singularity/tmp/` and `$HOME/.singularity/cache/`) inside your home directory.
```
export SINGULARITY_TMPDIR="$HOME/.singularity/tmp/"
```

```
export SINGULARITY_CACHEDIR="$HOME/.singularity/cache/"
```

Then we need to create the directories defined by `SINGULARITY_CACHEDIR` and `SINGULARITY_TMPDIR`, if they don’t already exist. The `-p` flag ensures that the command does not return an error if the directories are already in place.

```
mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR
```

Now, convert the Podman image into a Singularity image:

```
srun singularity build my-python-app.sif docker-archive://my-python-app.tar
```

This will convert the container into a Singularity Image File (.sif) that can be used in the cluster.


## Step 6: Test running the Singularity Container (optional)
Submit a job to Slurm using the newly converted Singularity image:

```
srun --gres=gpu:1 singularity exec my-python-app.sif python3 --version
```