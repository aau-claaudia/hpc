
LUMI ranks among the Top 10 supercomputer according to the [Top 500 list](https://top500.org), and is the largest HPC facility AAU holds [local resources](external-hpc/access/#hpc-facilities-accessible-with-local-and-national-resources) to.

The true power of LUMI thus lies in it's scaling oppurtunities, but we encourage users to experiment with the system and to think of it as an extension of the capacity that we provide at AAU.

!!! info "Accessing LUMI resources"

    There are three different resource pools:
    
    - **AAU's local resource pool**: This is recommended for first time users, and can usually be handled within 1 workday. When your application has been accepted, you will receive an email with step-by-step instructions on how to proceed.
    - **DeiC's national resource pool**: This is option is suitable for users who have some familiarity with the system and want to apply for larger grants.
    - **A EuroHPC access call**: This is suitable for when you want to apply for larger grants. With a EuroHPC grant, it is also possible to apply for in-depth HPC expertise support from [Epicure](https://epicure-hpc.eu/).

    Read more about this in our [How to access section](external-hpc/access/).

!!! info "User support"
    User support for the system is provided jointly by [CLAAUDIA](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad001310e) and the [LUMI User Support Team (LUST)](https://www.lumi-supercomputer.eu/user-support/).

## Software

LUMI utilises two main software components:

- [Slurm queueing system](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/slurm-quickstart/) for distributing ressources.
- [Singularity container framework](https://docs.lumi-supercomputer.eu/software/containers/singularity/) for containerising software.

Users familiar with [AI Cloud](/ai-cloud) or [AI-LAB](/ai-lab) will find that operating the system a familiar experience.

## Hardware

#### Compute nodes
LUMI consists of three different compute partitions:

| Partition | Number of nodes | Purpose | Node configuration |
| ---       |       ---       |   ---   |   ---         |
| [LUMI-C](https://docs.lumi-supercomputer.eu/hardware/lumic/) | 2978 | Scaleable, demanding CPU operations | 128 cores AMD EPYC with different RAM capacities 256, 512 and 1024 GB| 
| [LUMI-G](https://docs.lumi-supercomputer.eu/hardware/lumig/) | 2048 | Scaleable, demanding GPU operations | 4 x AMD MI250x GPU's (128 GB GPU-RAM each)|
| [LUMI-D](https://docs.lumi-supercomputer.eu/hardware/lumid/) | 8 | Interactive data visualisation | Nvidia A40 |

The table above is intended for the purpose of providing a rough overview of the hardware. 
A more complete overview can be found in [the official LUMI documentation](https://docs.lumi-supercomputer.eu/hardware/)

#### Network
All compute nodes are equipped with an high-speed interconnect which ensures high transfer speeds between compute nodes and storage partitions.

  - [Bandwidth measurements between storage and compute nodes](https://docs.lumi-supercomputer.eu/hardware/network/#inter-and-intra-partition-bandwidth)

### Storage

LUMI also several different storage partitions serving different purposes. Users should note that these have different storage quotas, and different billing rates, ie. the allocated storage units `TB/hrs` are spent at different rates, depending on the storage partition is being used.

- [Recommendations on using the storage partitions](https://docs.lumi-supercomputer.eu/storage/)

## Using the system

### Prior to logging in

Assuming that you have decided to make use of AAU's local resource pool, follow the instructions in the letter of approval, sent out following your [resource application](/external-hpc/access). This includes following AAU's identity verification procedure and uploading an SSH key to the system. After uploading your SSH-key, you may need to wait ~20 minutes for the server to synchronise.

### Log in to the system

Log in according to [official instructions](https://docs.lumi-supercomputer.eu/firststeps/loggingin/). 

If this is your first time logging in to the system, you may need to wait ~20 minutes for the system to synchronise after your SSH-key has been uploaded.

### Looking around

LUMI's operating system CrayOS is a variant of Linux, and the system can thus be navigated using regular GNU/Linux commands (find some of them [here](https://linuxjourney.com/lesson/the-shell)).

LUMI also uses [modules](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/Lmod_modules/) to manage software environments. Loading modules essentially just alters the `$PATH` variable, allowing you to access additional software and/or versions.

Each time the user logs in to the system, the [`lumi-tools`](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/l/lumi-tools/)-module is automatically loaded, giving you access to commands like `lumi-workspaces`, `lumi-allocations`, `lumi-check-quota`, which will allow you to inspect your project and it's resource consumption.

### Transfer your files

Transfer your files according to the [official instructions](https://docs.lumi-supercomputer.eu/firststeps/movingdata/). We recommend Rsync for it's ability to continue a transfer if gets interrupted.

Please be mindful of the fact that storage units are spent continuously. There's no need to constantly move files around, but we ask you to be mindful of your storage quota, and to get in touch with us if you are nearing the limits of your quota. We will likely be able to help you find more resources.

### Prepare software environment

We recommend creating Singularity images using the tool [Cotainr](https://docs.lumi-supercomputer.eu/software/containers/singularity/#building-containers-using-the-cotainr-tool), which has been designed with LUMI in mind, eg. it has the flag `--system=lumi-g` to help you collect the correct modules.

You can also find pre-built container images in: `/appl/local/containers/sif-images`

### Run your job

It is generally recommended to launch your jobs with batch-scripts. We provide the following example, which you can use as a basis for your own batch scripts.

    #!/bin/bash
    
    #SBATCH --job-name=torch_bm
    #SBATCH --account=project_415001489
    #SBATCH --partition=small-g
    #SBATCH --gpus=1
    #SBATCH --cpus-per-task=15
    #SBATCH --time=01:00:00
    #SBATCH --output=out.%x_%j
    #SBATCH --error=err.%x_%j
    
    # Directories
    PROJECT="/project/${SLURM_JOB_ACCOUNT}"
    SCRATCH="/scratch/${SLURM_JOB_ACCOUNT}"
    FLASH="/flash/${SLURM_JOB_ACCOUNT}"
    mkdir -p $PROJECT $SCRATCH $FLASH

    # Container
    lumi_images="/appl/local/containers/sif-images"
    lumi_pytorch_base="${lumi_images}/lumi-pytorch-rocm-6.2.3-python-3.12-pytorch-v2.5.1.sif"
    
    CONTAINER="$lumi_pytorch_base"
    
    # Script
    SCRIPT="${PROJECT_DIR}/torch_bm.py"
   
    # The command to execute on the node(s)
    srun --chdir="$PROJECT_DIR" singularity exec --bind="$PROJECT_DIR,$SCRATCH_DIR,$FLASH_DIR" $CONTAINER bash -c "\$WITH_CONDA; python3 $SCRIPT"

Consider making the following adjustments:

* Decide on a good naming convention for your runs. Pass this to `--job-name`.
* Find your project account number using the command `lumi-workspaces`. Pass this to the `--account` parameter.
* Decide on an appropriate compute partition to run on. 
    * View the partitions with the command: `sinfo -o "%25P %5D %l"`
    * Read about [the compute hardware](https://docs.lumi-supercomputer.eu/hardware/lumig/) in the official documentation.
* Replace the paths to your container image and your script.

