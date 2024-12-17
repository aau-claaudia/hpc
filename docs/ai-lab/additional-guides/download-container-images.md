You can find and download pre-built container images for various applications from pages such as:

* [https://catalog.ngc.nvidia.com/](https://catalog.ngc.nvidia.com/)
* [https://hub.docker.com/](https://hub.docker.com/)

### NVIDIA NGC Catalog

On [the NGC page](https://catalog.ngc.nvidia.com/), search or browse for the container image (e.g., TensorFlow), click on "Get Container" to get the container image URL (e.g., `nvcr.io/nvidia/tensorflow:24.11-tf2-py3-igpu`). 

![Screenshot of NGC](/assets/img/ai-lab/download-image-1.png)

### Docker Hub

On [Docker Hub](https://hub.docker.com/), search or browse for the container (e.g., TensorFlow), click on the "Tags" to get the container image URL (e.g., `tensorflow/tensorflow:nightly-jupyter`).

![Screenshot of Docker Hub](/assets/img/ai-lab/download-image-2.png)

## Setting up Environment Variables for Singularity

Before downloading the container image, set the following environment variables to optimize performance:

```
export SINGULARITY_TMPDIR="$HOME/.singularity/tmp/"
export SINGULARITY_CACHEDIR="$HOME/.singularity/cache/"
```

Create the required directories if they don’t already exist:

```
mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR
```

## Downloading the Container Image

Use the `srun` command to run Singularity via the Slurm queueing system and download the container image. Replace the example URL below with the link you copied from one of the above pages. You will also need to add `docker://` before the URL:

```
srun --mem 40G singularity pull docker://nvcr.io/nvidia/tensorflow:24.03-tf2-py3
```

**The download may take up to 20 minutes.**

### Command Breakdown

* `srun`: Executes the command on a compute node via Slurm.
* `--mem 40G`: Allocates 40GB of memory (adjust if necessary).
* `singularity pull`: Downloads and converts the container image to a Singularity-compatible format.
* `docker://..`.: Specifies the Docker image URL (copied from one of the suggested pages).

After the download completes, you’ll find the container image file (e.g., `tensorflow_24.03-tf2-py3.sif`) in your current directory.