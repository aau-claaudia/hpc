In this section we explain, how we can pull Docker containers from online repositories. 

Using the command `singularity pull`, we can download them and automatically convert them into Singularity containers.

## Find a container

#### Find a container on the **NVIDIA NGC Catalog:**

1. Visit [NGC Catalog](https://catalog.ngc.nvidia.com/){target=_blank}
2. Search for your framework (e.g., "TensorFlow", "PyTorch")
3. Click "Get Container" to get the URL
4. Copy the URL (e.g., `nvcr.io/nvidia/tensorflow:24.11-tf2-py3`)

![Screenshot of NGC](/assets/img/ai-lab/download-image-1.png)

#### Find a container on **Docker Hub:**

1. Visit [Docker Hub](https://hub.docker.com/){target=_blank}
2. Search for your container
3. Click on "Tags" to see available versions
4. Copy the URL (e.g., `tensorflow/tensorflow:nightly-jupyter`)

![Screenshot of Docker Hub](/assets/img/ai-lab/download-image-2.png)

## Downloading the container image

Now that we have found a container image, we can create the following batch script:

```bash title="pull-pytorch.sh"
#!/bin/bash

#SBATCH --job-name=build_basic
#SBATCH --cpus-per-task=32
#SBATCH --mem=60G
#SBATCH --time=02:00:00
#SBATCH --output=out.%x
#SBATCH --error=err.%x

export SINGULARITY_TMPDIR=$HOME/.singularity/tmp
export SINGULARITY_CACHEDIR=$HOME/.singularity/cache
mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR

# URI of container to pull
uri="nvcr.io/nvidia/pytorch:25.10-py3"

# Name of the resulting container
output_sif="pytorch_25.10.sif"

# Call the build instructions
singularity pull $output_sif docker://$uri
```

Some options we can set in the batch script.

* **The memory paramater:**

    From experience we know that the conversion between Docker and Singularity formats can be a memory consuming operation. If our build fails because of insufficient memory, we may need to adjust the memory parameter. In this example we have set it to 60 gb.


* **Environment variables:**

    Before pulling the container image, we need to set the `SINGULARITY_TMPDIR` and `SINGULARITY_CACHEDIR` environment variables. If these are not set, Singularity assumes that we have lots of space in `/tmp` on the host system - which is not the case. If they are set, Singularity will use this directory for storing temporary files and cached data during container operations. These are mandatory.

Launch the batch script to pull the container image:

```
sbatch pull-pytorch.sh
```

Note that this may take ~20-30 minutes to complete.
