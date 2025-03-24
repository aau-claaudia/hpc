To run applications such as `Python`, `PyTorch`, or `TensorFlow` etc. on AI-LAB, you need to use containers in most instances. On AI-LAB we use the container software, [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html){target=_blank}.

!!! info "What is a container?"
    A container is a static, portable file that contains all the components needed to run a piece of software, including the code, runtime, system tools, libraries, and settings.

In general, there are 3 ways to get containers:

1. [Pre-downloaded containers](/ai-lab/guides/getting-containers/#1-pre-downloaded-containers)
2. [Download containers](/ai-lab/guides/getting-containers/#2-download-containers)
3. [Build your own container](/ai-lab/guides/getting-containers/#3-build-your-own-container)

<hr>

## 1. Pre-downloaded containers
The most straightforward method to acquire containers on AI-LAB is by accessing pre-downloaded containers stored in the `/ceph/container` directory. We aim to consistently update these containers to the latest versions. Some of the containers includes `Python`, `PyTorch`, and `TensorFlow` containers.

You can check which containers exist in the `/ceph/container` directory on AI-LAB with `ls`:

```
ls /ceph/container
```

To use the containers, you can use them straight from the `/ceph/container` directory by referencing the absolute path, e.g.:

```
/ceph/container/pytorch/pytorch_24.09.sif
```

<hr>

## 2. Download containers
You can download a wide range of pre-built containers by visiting websites such as:

* [https://catalog.ngc.nvidia.com/](https://catalog.ngc.nvidia.com/){target=_blank}
* [https://hub.docker.com/](https://hub.docker.com/){target=_blank}

Check out the guide below for detailed instructions on how to download the containers.

??? news "Guide on how to download containers"

    ### NVIDIA NGC Catalog

    On [the NGC page](https://catalog.ngc.nvidia.com/){target=_blank}, search or browse for the container (e.g., TensorFlow), click on "Get Container" to get the container URL (e.g., `nvcr.io/nvidia/tensorflow:24.11-tf2-py3-igpu`). 

    ![Screenshot of NGC](/assets/img/ai-lab/download-image-1.png)

    ### Docker Hub

    On [Docker Hub](https://hub.docker.com/){target=_blank}, search or browse for the container (e.g., TensorFlow), click on the "Tags" to get the container URL (e.g., `tensorflow/tensorflow:nightly-jupyter`).

    ![Screenshot of Docker Hub](/assets/img/ai-lab/download-image-2.png)

    ### Setting up environment variables for Singularity

    Before downloading the container, set the following environment variables to optimize performance:

    ```
    export SINGULARITY_TMPDIR="$HOME/.singularity/tmp/"
    export SINGULARITY_CACHEDIR="$HOME/.singularity/cache/"
    ```

    Create the required directories if they don’t already exist:

    ```
    mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR
    ```

    ### Downloading the container

    Use the `srun` command to run Singularity via the Slurm queueing system and download the container. Replace the example URL below with the link you copied from one of the above pages. You will also need to add `docker://` before the URL:

    ```
    srun --mem 40G singularity pull docker://nvcr.io/nvidia/tensorflow:24.03-tf2-py3
    ```

    **The download may take up to 20 minutes.**

    ### Command breakdown

    * `srun`: Executes the command on a compute node via Slurm.
    * `--mem 40G`: Allocates 40GB of memory (adjust if necessary).
    * `singularity pull`: Downloads and converts the container to a Singularity-compatible format.
    * `docker://..`.: Specifies the Docker URL (copied from one of the suggested pages).

    After the download completes, you’ll find the container file (e.g., `tensorflow_24.03-tf2-py3.sif`) in your current directory.


<hr>

## 3. Build your own container
You also have the flexibility to create your own container tailored to your specific environment requirements. 

Check out the guide below for detailed instructions on building your own container:

??? news "Guide on how to build your own container"
    It is possible to define and build your own container with Singularity. Lets try creating a simple Singularity container with Python and pip installed. 

    First we need to create a [Singularity definition file](https://docs.sylabs.io/guides/3.0/user-guide/definition_files.html){target=_blank} (`.def`). This definition file is a blueprint for how Singularity should build the container. It includes information about the base OS to build, which software to install and several other options.

    Lets create an empty text file by using the `nano` command:

    ```
    nano
    ```

    Now we can enter the blueprint needed to install our application:

    ```
    Bootstrap: docker
    From: ubuntu:20.04

    %post
        # Set a custom temporary directory (adjust the path as needed)
        export TMPDIR=/scratch/ry90cd/tmp
        mkdir -p $TMPDIR

        apt-get update
        apt-get upgrade -y

        # Install Python and pip
        apt-get install -y python3 python3-pip

        # Upgrade pip using no-cache-dir
        pip install --no-cache-dir --upgrade pip

        # Install Python libraries without caching
        pip install --no-cache-dir numpy matplotlib torch torchtune

    %test
        # Test Python version1~# Test Python version
        python3 --version
    ```

    In the `%post` section, the `--no-cache-dir` flag ensures that pip does not store locally cached packages, which helps reduce disk usage and avoid running out of space.

    In this example we will use `docker` to pull `ubuntu:20.04` as the base OS of our container. 

    In the next section,`%post`, we can define commands that will be executed after the base OS has been installed. In this example, we will update the container and install `python3` and `pip` along with `numpy pandas scikit-learn matplotlib` packages. 

    After that we can define commands to run after the container is built in the `%test` section. Lets try with `python3 --version`.

    You can find more options to use in definition file in the [Singularity definition file documentation](https://docs.sylabs.io/guides/3.0/user-guide/definition_files.html){target=_blank}.

    To save the file press `CTRL + O` and enter a filename ending with `.def` and hit `ENTER`. In this example, lets call it `python3.def`.

    #### Setting environment variables
    Before building the container, we need to set the `SINGULARITY_TMPDIR` and `SINGULARITY_CACHEDIR` environment variables, to speed up repeated operations. We will use these variables to a temporary directory (`$HOME/.singularity/tmp/` and `$HOME/.singularity/cache/`) inside your home directory. Singularity will use this directory for storing temporary files and cached data during container operations.

    ```
    export SINGULARITY_TMPDIR="$HOME/.singularity/tmp/"
    export SINGULARITY_CACHEDIR="$HOME/.singularity/cache/"
    ```

    Then we need to create the directories defined by `SINGULARITY_CACHEDIR` and `SINGULARITY_TMPDIR`, if they don’t already exist. The -p flag ensures that the command does not return an error if the directories are already in place.

    ```
    mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR
    ```

    ### Building the container

    You can now build container from the `python3.def` file:

    ```
    srun singularity build --fakeroot python3.sif python3.def
    ```

    After some time you should see the `Python X.X.X` version be printed in the terminal, and you should now have a `python3.sif` container image ready to run.

    Lets for example print the matplotlib version:

    ```
    srun singularity exec python3.sif python3 -c "import matplotlib; print('Matplotlib version:', matplotlib.__version__)"
    ```

    You can find more information about building containers from Singularity definition files [here](https://docs.sylabs.io/guides/3.0/user-guide/definition_files.html){target=_blank}.

<hr>

You are now ready to proceed to learn about [**using containers to run jobs :octicons-arrow-right-24:**](using-containers.md)