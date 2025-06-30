LUMI is a supercomputer located in Kajaani, Finland and ranks among the world's Top 10 supercomputers according to the [Top 500 list](https://top500.org). The true power of the system lies in it's oppurtunity to scale jobs massively, but we also want to encourage our users to experiment with the system, and to think of it as an extension of the compute capacity available to them as researchers at AAU.


## Access
The system is funded by EuroHPC and the [LUMI consortium](https://www.lumi-supercomputer.eu/lumi-consortium/) which Denmark is a member of, and for this reason AAU holds local ressources, which we can use to provide our researchers with **direct access** to the system.

!!! info "Recommendations for acquiring compute time on LUMI"

    1. Find a resource for testing out and gaining familiarity with the system. Make use of either:
        * **AAU's local resource pool**: Fill out [our application form](https://forms.office.com/e/4XC48iVu4S). We have meticulously crafted the application form, so that it guides you every step of the way. Upon approval you will receive an email with step-by-step instructions on how to log in to the system.
        * **EuroHPC**: Apply for either [*benchmark*](https://eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-benchmark-access_en) or [*development*](https://eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-development-access_en) access from EuroHPC. Consider the oppurtunity of applying for in-depth HPC-expert-assistance from [Epicure](/external-hpc/access/#epicure).
        
    2. If you would need additional resources for the system, you have the following options depending on how much your project requires:
        * **AAU's local resource pool**: We hand out resources for actual (non-testing) project work on a continuous basis. The amount we can allocate depends on our budget, but we encourage users to fill out [our application form](https://forms.office.com/e/4XC48iVu4S). If the applied amount is not within our budget, we will reach out to you and help you find the resources you need.
        * **DeiC's national resource pool**: This is a biannual call, suitable for both modest and very large project needs.
        * **EuroHPC**: Apply for on of the access modes; [*regular*](https://eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-regular-access-mode_en), [*extreme*](https://eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-extreme-scale-access-mode_en) or [*AI for Science and Collaborative EU Projects*](https://eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-ai-science-and-collaborative-eu-projects_en). Consider the oppurtunity of applying for in-depth HPC-expert-assistance from [Epicure](/external-hpc/access/#epicure).

    Generally we always recommend making use of AAU's resources first, as CLAAUDIA can provide you with the best onboarding oppurtunities, and guide you further along the way as your project grows.

!!! info "User support"
    User support for the system is provided jointly by [CLAAUDIA](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad001310e) and the [LUMI User Support Team (LUST)](https://www.lumi-supercomputer.eu/user-support/).

## System overview
### Software

LUMI utilises two main software components:

- [Slurm queueing system](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/slurm-quickstart/) for distributing ressources.
- [Singularity container framework](https://docs.lumi-supercomputer.eu/software/containers/singularity/) for containerising software.

Users familiar with [AI Cloud](/ai-cloud) or [AI-LAB](/ai-lab) will find that operating the system a familiar experience.

### Hardware

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

#### Storage

LUMI also several different storage partitions serving different purposes. Users should note that these have different storage quotas, and different billing rates, ie. the allocated storage units `TB/hrs` are spent at different rates, depending on the storage partition is being used.

- [Recommendations on using the storage partitions](https://docs.lumi-supercomputer.eu/storage/)

## Using the system

### Before logging in

Assuming that you have decided to make use of AAU's local resource pool, follow the instructions in the letter of approval, sent out following your [resource application](/external-hpc/access). This involves completing AAU's identity verification procedure and uploading an SSH key to the system.

### Log in to the system

Log in according to [official instructions](https://docs.lumi-supercomputer.eu/firststeps/loggingin/). Please know that after uploading your SSH-key, you may need to wait ~20 minutes for the server to synchronise.

### Looking around

LUMI's operating system CrayOS is a variant of Linux, and the system can thus be navigated using [regular GNU/Linux commands](https://linuxjourney.com/lesson/the-shell).

LUMI uses [Modules](https://modules.readthedocs.io/en/stable/module.html#description) to manage software environments. Loading modules essentially just alters the `$PATH` variable, allowing you to access additional software and/or versions. Learn about using modules [here](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/Lmod_modules/).

Each time the user logs in to the system, the [`lumi-tools`](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/l/lumi-tools/)-module is automatically loaded, giving you access to commands like `lumi-workspaces`, `lumi-allocations`, `lumi-check-quota`, which will allow you to inspect your project and it's resource consumption.

Optionally `git clone` our LUMI-starter-pack:
```
git clone https://github.com/aau-claaudia/lumi-starter-pack.git
```
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
    PROJECT="/project/$SLURM_JOB_ACCOUNT"
    SCRATCH="/scratch/$SLURM_JOB_ACCOUNT"
    FLASH="/flash/$SLURM_JOB_ACCOUNT"
    mkdir -p $PROJECT $SCRATCH $FLASH

    # Container image (here we are targetting one that comes preinstalled on the system)
    lumi_images="/appl/local/containers/sif-images"
    lumi_pytorch_base="$lumi_images/lumi-pytorch-rocm-6.2.3-python-3.12-pytorch-v2.5.1.sif"
    
    CONTAINER="$lumi_pytorch_base"
    
    # Script
    SCRIPT="$PROJECT_DIR/torch_bm.py"
   
    # The command to execute on the node(s)
    srun --chdir="$PROJECT_DIR" singularity exec --bind="$PROJECT_DIR,$SCRATCH_DIR,$FLASH_DIR" $CONTAINER bash -c "\$WITH_CONDA; python3 $SCRIPT"

Consider making the following adjustments:

* Decide on a good naming convention for your runs. Pass this to `--job-name`.
* Find your project account number using the command `lumi-workspaces`. Pass this to the `--account` parameter.
* Run the job on an appropriate compute partition:
    * View the partitions with the command: `sinfo -o "%25P %5D %l"`
    * Read about [the compute hardware](https://docs.lumi-supercomputer.eu/hardware/lumig/) in the official documentation.
* Replace the paths to your container image and your script.

