
It is generally considered good practice to build your own Singularity containers, to contain the software environment for a project you wish to run on an HPC system. This is because containers represent a solution that allows robustness and reproducibility.


## Create a definition file

First we need to create a definition to build our container image from. We will provide a basic example, but it also be helpful to read the official documentation page on [building container images](https://docs.sylabs.io/guides/3.0/user-guide/definition_files.html).


```bash title="torch.def"
Bootstrap: docker
From: ubuntu:22.04

%post
    # This section is where you install software packages

    # Update the package manager (apt)
    apt update

    # install the latest Python and pip version
    apt install -y python3-pip python3-dev

    # use pip to install torch
    pip3 install torch torchvision torchaudio
```

## Create a batch script to build from

We can now create a batch script to launch our build:

```bash title="build_torch.sh"
#!/usr/bin/env bash

#SBATCH --job-name=build_torch
#SBATCH --output=build_torch.out
#SBATCH --error=build_torch.err
#SBATCH --cpus-per-task=32
#SBATCH --mem=80G

export SINGULARITY_TMPDIR=$HOME/.singularity/tmp
export SINGULARITY_CACHEDIR=$HOME/.singularity/cache
mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR

# The path to the definition file
input_def="torch.def"

# The resulting container image
output_sif="torch.sif"

singularity build --fakeroot $output_sif $input_def
```

We can now build the container by launching our batch script with: 

```bash
sbatch build_torch.sh
```

After our file has been built we can test it with:

```bash
srun --gres=gpu:1 singularity exec --nv torch.sif python3 -c "import torch ; print(torch.cuda.is_available())"
```

Which should output:

```bash
srun: job 767374 queued and waiting for resources
srun: job 767374 has been allocated resources
True
```

