# Getting Containers for AI-LAB

Most applications on AI-LAB run inside **containers** - self-contained environments that include all the software and dependencies you need. AI-LAB uses [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html){target=_blank} to run containers.

## What is a Container?

A container is like a pre-packaged software environment that includes:

- The application (Python, PyTorch, TensorFlow, etc.)
- All required libraries and dependencies
- System tools and configurations
- Everything needed to run your code

Think of it as a complete, portable computer environment that works the same way every time.

## Three Ways to Get Containers

1. **[Use pre-downloaded containers](#1-pre-downloaded-containers)** - Quickest option
2. **[Download containers](#2-download-containers)** - For specific versions
3. **[Build your own container](#3-build-your-own-container)** - For custom environments

### Which Method Should You Choose?

| Method | When to Use | Time Required | Difficulty |
|--------|-------------|---------------|------------|
| Pre-downloaded | Getting started, common frameworks | Instant | Easy |
| Download | Need specific version, latest updates | 10-20 minutes | Easy |
| Build | Custom requirements, specific packages | 30+ minutes | Advanced |

<hr>

## 1. Pre-downloaded Containers

The easiest way to get started is using containers that are already available on AI-LAB. These are stored in `/ceph/container` and are regularly updated.

### Available Containers

Check what's available:

```bash
ls /ceph/container
```

Common containers include:

- **Python**: Basic Python environment
- **PyTorch**: Deep learning with PyTorch
- **TensorFlow**: Deep learning with TensorFlow
- **MATLAB**: MATLAB computational environment

### Using Pre-downloaded Containers

You can use these containers directly by referencing their full path:

```bash
# Example: Using PyTorch container
/ceph/container/pytorch/pytorch_24.09.sif
```

### Finding the Right Container

To see what's in each container directory:

```bash
ls /ceph/container/pytorch/    # See available PyTorch versions
ls /ceph/container/tensorflow/ # See available TensorFlow versions
```

<hr>

## 2. Download Containers

If you need a specific version or container not available in the pre-downloaded collection, you can download containers from online repositories.

### Popular Container Sources

- **[NVIDIA NGC Catalog](https://catalog.ngc.nvidia.com/){target=_blank}**: Optimized containers for AI/ML
- **[Docker Hub](https://hub.docker.com/){target=_blank}**: Large collection of community containers

#### Step 1: Find Your Container

**NVIDIA NGC Catalog:**

1. Visit [NGC Catalog](https://catalog.ngc.nvidia.com/){target=_blank}
2. Search for your framework (e.g., "TensorFlow", "PyTorch")
3. Click "Get Container" to get the URL
4. Copy the URL (e.g., `nvcr.io/nvidia/tensorflow:24.11-tf2-py3`)

![Screenshot of NGC](/assets/img/ai-lab/download-image-1.png)

**Docker Hub:**

1. Visit [Docker Hub](https://hub.docker.com/){target=_blank}
2. Search for your container
3. Click on "Tags" to see available versions
4. Copy the URL (e.g., `tensorflow/tensorflow:nightly-jupyter`)

![Screenshot of Docker Hub](/assets/img/ai-lab/download-image-2.png)

#### Step 2: Set Up Singularity Environment

Before downloading, configure Singularity for optimal performance:

```bash
# Set up directories for Singularity
export SINGULARITY_TMPDIR="$HOME/.singularity/tmp/"
export SINGULARITY_CACHEDIR="$HOME/.singularity/cache/"

# Create the directories
mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR
```

#### Step 3: Download the Container

Use `srun` to download the container (this may take 10-20 minutes):

```bash
# Example: Download TensorFlow container
srun --mem 40G singularity pull docker://nvcr.io/nvidia/tensorflow:24.03-tf2-py3
```

**Command explanation:**

- `srun --mem 40G`: Run on compute node with 40GB memory
- `singularity pull`: Download and convert container
- `docker://`: Indicates this is a Docker container URL

#### Step 4: Use Your Downloaded Container

After download completes, you'll find a `.sif` file in your current directory:

```bash
ls *.sif  # List downloaded containers
```

Use it just like pre-downloaded containers:

```bash
# Example usage
srun singularity exec --nv tensorflow_24.03-tf2-py3.sif python my_script.py
```


<hr>

## 3. Build Your Own Container (Advanced)

For specialized requirements or custom environments, you can build your own containers using Singularity definition files.


#### Step 1: Create a Definition File

Create a Singularity definition file (`.def`) that describes your container:

```bash
nano my_container.def
```

Here's a simple example for a Python container:

```bash title="my_container.def"
Bootstrap: docker
From: ubuntu:20.04

%post
    # Set temporary directory
    export TMPDIR=/tmp
    mkdir -p $TMPDIR

    # Update system
    apt-get update
    apt-get upgrade -y

    # Install Python and pip
    apt-get install -y python3 python3-pip

    # Upgrade pip
    pip install --no-cache-dir --upgrade pip

    # Install Python packages
    pip install --no-cache-dir numpy matplotlib torch

%test
    # Test that Python works
    python3 --version
    python3 -c "import numpy, matplotlib, torch; print('All packages imported successfully')"
```

**Definition file sections:**
- `Bootstrap: docker`: Use Docker as the base
- `From: ubuntu:20.04`: Base operating system
- `%post`: Commands to run during build
- `%test`: Commands to test the container

#### Step 2: Set Up Environment

Configure Singularity for building:

```bash
# Set up directories
export SINGULARITY_TMPDIR="$HOME/.singularity/tmp/"
export SINGULARITY_CACHEDIR="$HOME/.singularity/cache/"

# Create directories
mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR
```

#### Step 3: Build the Container

Build your container using `srun`:

```bash
srun singularity build --fakeroot my_container.sif my_container.def
```

This process may take 10-30 minutes depending on the complexity.

#### Step 4: Test Your Container

Test that your container works:

```bash
# Test basic functionality
srun singularity exec my_container.sif python3 --version

# Test package imports
srun singularity exec my_container.sif python3 -c "import torch; print('PyTorch version:', torch.__version__)"
```

#### Step 5: Use Your Container

Use your custom container just like any other:

```bash
srun singularity exec --nv my_container.sif python3 my_script.py
```

!!! info "Tips for Building Containers"

    - **Start simple**: Begin with basic containers and add complexity gradually
    - **Use `--no-cache-dir`**: Prevents pip from storing package files
    - **Test thoroughly**: Use the `%test` section to verify everything works
    - **Document your choices**: Add comments explaining why you chose specific versions

### Advanced Definition File Options

For more complex containers, you can use additional sections:

- `%environment`: Set environment variables
- `%runscript`: Define what happens when the container runs
- `%labels`: Add metadata to your container
- `%help`: Add help text

See the [Singularity documentation](https://docs.sylabs.io/guides/3.0/user-guide/definition_files.html){target=_blank} for complete details.

<hr>

You are now ready to proceed to learn about [**using containers to run jobs :octicons-arrow-right-24:**](using-containers.md)