LUMI is a supercomputer located in Kajaani, Finland and ranks among the world's Top 10 supercomputers according to the [Top 500 list](https://top500.org). The true power of the system lies in it's oppurtunity to scale jobs massively, but we also want to encourage our users to experiment with the system, and to think of it as an extension of the compute capacity available to them as researchers at AAU.


!!! abstract "Call open: Possible to apply for national resources"

    Call "H2-2026" is open from the 13th of January 2026, and will close 10th of March 2026.

    * Find more information on CLAAUDIA's page dedicated to this :octicons-arrow-right-16: [DeiC HPC resources](/external-hpc/deic-resources/).

    * Find the official call page :octicons-arrow-right-16: [DeiC "H2-2026"](https://www.deic.dk/en/grants/h2-2026-call-applications-access-national-e-resources).

## Access

The system is funded by [EuroHPC](https://www.lumi-supercomputer.eu/eurohpcju/) and the [LUMI consortium](https://www.lumi-supercomputer.eu/lumi-consortium/) which Denmark is a member of. For this reason CLAAUDIA can provide AAU-users with **direct access** to the system. 

### Recommendations for acquiring compute time on LUMI

Acquiring LUMI-resources should <u>always</u> be a two step proces:

  1. **<u>Acquire resources for testing out the system</u>:** 

    It is always good to do a test run on the system prior to reaching out for a larger grant. Being able to demonstrate that you are able to utilise the system effectivly, and that your project fits the system, will greatly help your chances of being awarded the resources.
    Further acquiring too large a resource, which is left unused, might make this resource unavailable to others who might have been able to put it to good use.

    Make use of one of the following:

      - **AAU's local resource pool:** Fill out [our application form](https://forms.office.com/e/4XC48iVu4S).

      - **EuroHPC:** Read more on [our page dedicated to this option](/external-hpc/eurohpc-resources/).

2. **<u>Acquire resources for actual project work</u>:** 

    When you have demonstrated that your applicaiton is fit for the system, you can reach out for a larger grant.

    Make use of one of the following:

      - **AAU's local resource pool**: Fill out [our application form](https://forms.office.com/e/4XC48iVu4S). Suitable for modest/large grants, depending on our budget.

      - **DeiC's national resource pool**: Read more on [our page dedicated to this option](/external-hpc/deic-resources/#applications-to-the-national-resource-pool).

      - **EuroHPC**: Read more on [our page dedicated to this option](/external-hpc/eurohpc-resources/).

!!! info "LUMI's resource cutter"

    In order to ensure consistency in the availability of resources, LUMI has imposed a *resource cutting* mechanism that affects projects that run for more than 6 months (ie. projects with a shorter lifespan are not affected). If 40 % of the allocated resources have not been consumed within 6 months, an amount up to 40 % is cut from the total allocation. To clarify:

    * If the project has consumed 39 % of the total allocation after 6 months, 1 % is cut.
    
    * If the project has consumed 45 % of the total allocation after 6 months, nothing is cut.

    * If the project's lifespan is 6 months or shorter, nothing is cut.


### User support

User support for the system is provided jointly by [CLAAUDIA](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad001310e) and the [LUMI User Support Team (LUST)](https://www.lumi-supercomputer.eu/user-support/).

With a EuroHPC grant it is possible to apply for in-depth, HPC-expert assistance from [the Epicure project](/external-hpc/eurohpc-resources/#epicure).

## Software

LUMI utilises two main software components:

- [Slurm queueing system](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/slurm-quickstart/) for distributing ressources.
- [Singularity container framework](https://docs.lumi-supercomputer.eu/software/containers/singularity/) for containerising software.

Users familiar with [AI Cloud](/ai-cloud) or [AI-LAB](/ai-lab) will find that operating the system a familiar experience.

## Hardware

#### Compute nodes
LUMI consists of multiple compute partitions. Two of the main ones are:

| Partition | Number of nodes | Purpose | Node configuration |
| ---       |       ---       |   ---   |   ---         |
| [LUMI-C](https://docs.lumi-supercomputer.eu/hardware/lumic/) | 2978 | Scaleable, demanding CPU operations | 128 cores AMD EPYC with different RAM capacities 256, 512 and 1024 GB| 
| [LUMI-G](https://docs.lumi-supercomputer.eu/hardware/lumig/) | 2048 | Scaleable, demanding GPU operations | 4 x AMD MI250x GPU's (128 GB GPU-RAM each)|

The table above is intended for the purpose of providing a rough overview of the hardware. 
A more complete overview can be found in [the official LUMI documentation](https://docs.lumi-supercomputer.eu/hardware/)

!!! info "A note on AMD GPU hardware"

    The AMD ROCM ecosystem has matured a lot in the recent years, and in most cases Nvidia-supported code can be ported to an AMD-system with only minor tweaks.

#### Network
All compute nodes are equipped with an high-speed interconnect which ensures high transfer speeds between compute nodes and storage partitions.

  - [Bandwidth measurements between storage and compute nodes](https://docs.lumi-supercomputer.eu/hardware/network/#inter-and-intra-partition-bandwidth)

#### Storage

LUMI also several different storage partitions serving different purposes. Users should note that these have different storage quotas, and different billing rates, ie. the allocated storage units `TB/hrs` are spent at different rates, depending on the storage partition is being used.

- [Recommendations on using the storage partitions](https://docs.lumi-supercomputer.eu/storage/)

## Using the system

### Before logging in

Assuming that you have decided to make use of AAU's local resource pool, follow the instructions in the letter of approval, sent out following your [resource application](/external-hpc/access). This involves completing AAU's identity verification procedure and [uploading an SSH key](https://docs.lumi-supercomputer.eu/firststeps/SSH-keys/) to the system.

### Log in to the system

Log in according to [official instructions](https://docs.lumi-supercomputer.eu/firststeps/loggingin/). Please know that after uploading your SSH-key, you may need to wait ~20 minutes for the server to synchronise.

### Looking around

Optionally `git clone` our [LUMI-starter-pack](https://github.com/aau-claaudia/lumi-starter-pack):
```
git clone https://github.com/aau-claaudia/lumi-starter-pack.git
```

LUMI's operating system CrayOS is a variant of Linux, and the system can thus be navigated using [regular GNU/Linux commands](https://linuxjourney.com/lesson/the-shell).

LUMI uses [Modules](https://modules.readthedocs.io/en/stable/module.html#description) to manage software environments. Loading modules essentially just alters the `$PATH` variable, allowing you to access additional software and/or versions. Learn about using modules [here](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/Lmod_modules/).

Each time the user logs in to the system, the [`lumi-tools`](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/l/lumi-tools/)-module is automatically loaded, giving you access to commands like `lumi-workspaces`, `lumi-allocations`, `lumi-check-quota`, which will allow you to inspect your project and it's resource consumption.

### Transfer your files

Transfer your files according to the [official instructions](https://docs.lumi-supercomputer.eu/firststeps/movingdata/). We recommend [Rsync](https://linuxjourney.com/lesson/rsync) for it's ability to continue a transfer if gets interrupted.

!!! warning "Storage units are spent continously"
    
    Please be mindful of the fact that storage units are spent continuously. There's no need to constantly move files around, but we ask you to be mindful of your storage quota, and to get in touch with us if you are nearing the limits of your quota. We will likely be able to help you find more resources.

### Prepare software environment

We recommend creating Singularity images using the tool [Cotainr](https://docs.lumi-supercomputer.eu/software/containers/singularity/#building-containers-using-the-cotainr-tool), which has been designed with LUMI in mind, eg. it has the flag `--system=lumi-g` to help you collect the correct modules.

You can also find pre-built container images in: `/appl/local/containers/sif-images`

### Run your first job

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
* Replace the paths to your `CONTAINER` and `SCRIPT`.

Finally run this batch-script with `sbatch torch_bm.sh` (or whatever you called the file).

### Monitor the job

Confirm that it is running with: 
```
squeue --me
```
If you are running a GPU-demanding job; find the `jobid` from the `squeue` command and run the following to monitor the GPU-activity:
```
srun --jobid=7100665 rocmi-smi
```
