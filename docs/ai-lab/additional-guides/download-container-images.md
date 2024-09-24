You can download a large range of container images by visiting [NVIDIA GPU Cloud (NGC)](https://catalog.ngc.nvidia.com/) and check whether NVIDIA provides a container image with the application you need.

![Screenshot of NGC website](/assets/img/ai-lab/ngc.png)

As an example, this could be TensorFlow. You can search on NGC and find [TensorFlow](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorflow). Here you can choose the desired version from the "Copy image path" dropdown menu:

![Screenshot of NGC TensorFlow page](/assets/img/ai-lab/ngc-tf-detail.png)

This copies a link to the container image which we will use in the following example.

#### Setting `SINGULARITY_TMPDIR` and `SINGULARITY_CACHEDIR`:
Before downloading the container image, we need to set the `SINGULARITY_TMPDIR` and `SINGULARITY_CACHEDIR` environment variables, to speed up repeated operations. We will use these variables to a temporary directory (`$HOME/.singularity/tmp/` and `$HOME/.singularity/cache/`) inside your home directory. Singularity will use this directory for storing temporary files and cached data during container operations.

```
export SINGULARITY_TMPDIR="$HOME/.singularity/tmp/"
export SINGULARITY_CACHEDIR="$HOME/.singularity/cache/"
```

Then we need to create the directories defined by `SINGULARITY_CACHEDIR` and `SINGULARITY_TMPDIR`, if they don’t already exist. The -p flag ensures that the command does not return an error if the directories are already in place.

```
mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR
```

## Downloading the container image

We need to use Singularity to download the container image and in order to run Singularity, we must run it through the Slurm queueing system using the command `srun`. 

To download the container image to your directory paste the url to the container image like so:

`srun --mem 40G singularity pull docker://nvcr.io/nvidia/tensorflow:24.03-tf2-py3`

NOTE: The container image could take ~20 minutes to download. 

The above example consists of the following parts:

- `srun`: the Slurm command which gets the following command executed on a compute node.
- `mem`: a Slurm command that allows you allocate memory to your process, in this case 40GB of memory. A higher amount of memory than the default is needed specifically for this TensorFlow container image.
- `singularity pull`: the Singularity command which downloads a specified container image.
- `docker://nvcr.io/nvidia/tensorflow:24.03-tf2-py3`: this part of the command itself consists of two parts. `docker://` tells Singularity that we are downloading a Docker container image and Singularity
automatically converts this to a Singularity container image upon download. `nvcr.io/nvidia/tensorflow:24.03-tf2-py3` is the container image label copied from the NGC webpage which identifies the particular container image and version that we want.

Once the `singularity pull` command has completed, you should have a file called `tensorflow_24.03-tf2-py3.sif` in your user directory (use the command `ls` to see the files in your current directory).