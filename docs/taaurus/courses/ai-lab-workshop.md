---
author: Frederik Petri
date: MMMM dd, YYYY
paging: Slide %d / %d
---


```                                               
                        █████╗ ██╗      ██╗      █████╗ ██████╗                                                      
                        ██╔══██╗██║      ██║     ██╔══██╗██╔══██╗                                                     
                        ███████║██║█████╗██║     ███████║██████╔╝                                                     
                        ██╔══██║██║╚════╝██║     ██╔══██║██╔══██╗                                                     
                        ██║  ██║██║      ███████╗██║  ██║██████╔╝                                                     
                        ╚═╝  ╚═╝╚═╝      ╚══════╝╚═╝  ╚═╝╚═════╝                                                      
██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗███████╗██╗  ██╗ ██████╗ ██████╗      ███╗ ██████╗ ██╗  ██╗
██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██║  ██║██╔═══██╗██╔══██╗    ██╔██╗╚════██╗██║  ██║
██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ███████╗███████║██║   ██║██████╔╝    ╚═╝╚═╝ █████╔╝███████║
██║███╗██║██║   ██║██╔══██╗██╔═██╗ ╚════██║██╔══██║██║   ██║██╔═══╝           ██╔═══╝ ╚════██║
╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗███████║██║  ██║╚██████╔╝██║               ███████╗     ██║
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝               ╚══════╝     ╚═╝

###############    High-Performance Computing for AAU students and teachers   ###############

                                    by Frederik Petri
                                        CLAAUDIA

#############################################################################################

```

---

## Did you apply for access?

If not, please go to https://forms.office.com/e/caEhCRmqVN and fill out the form :)

---

## What is AI-LAB?

A GPU cluster available to students and teachers

### Hardware
* 2 login nodes
* 11 compute nodes each with 8 NVIDIA L4 GPUs
* Ceph file system

### Software
* Linux
* Containerization for applications
* Slurm queue system

---

## What can you use AI-LAB for?

* Access GPU resources for deep learning
* Enhance applied machine learning courses
* Collaborate on AI experiments and learning
* Semester project training and support

---

## Why use AI-LAB?

* Easy to access
* Unlimited GPU resources
* Store course-specific materials 
* Getting-started guides https://hpc.aau.dk/ai-lab/getting-started/
* CLAAUDIA support https://serviceportal.aau.dk/

---

## Other HPC options?

### UCloud

* Access through webbrowser
* Great for interactive work
* Large software selection
* Can handle sensitive data
* Read more: https://hpc.aau.dk/ucloud/

---

## Other HPC options?

### AI Cloud

* Large GPU cluster (AI-LABs big brother)
* Very limited access to students
* Need a strong justification
* Read more: https://hpc.aau.dk/ai-cloud/

---

## Terms of use

* Access is removed at August 1st
* 1 hour default, 12 hour maximum limit on jobs
* Must not be used for confidential or sensitive data

---

## Lets begin using AI-LAB!

1. Log in via your local terminal using: `ssh -l user@student.aau.dk ailab-fe01.srv.aau.dk`
2. Enter `yes` if you get the following message: `Are you sure you want to continue connecting (yes/no/[fingerprint])?`
3. Enter your AAU password (it will not be visible)

### Exercises
* Log in to AI-LAB

---


## File management

* Store files in your user directory `/ceph/home/student.aau.dk/user`
* Shared files in `/ceph/container` and `/ceph/course`
* Shared project directories in `/ceph/project`

---

## Nice file commands to know

* `ls [path]`: List files in directory
* `cd [path]`: Change directory
* `cp [source] [destination]`: Copy a file within AI-LAB
* `cp -r [source] [destination]`: Copy a folder within AI-LAB
* `mkdir [name]`: Make a directory
* `cat [filename]`: Print out file content in terminal

* `~`: Shortcut path to your directory, e.g. `mkdir ~/stuff` creates a folder called `stuff` in your directory.

### Exercises

* Create a directory called `workshop` in your home directory using the `mkdir` command
* Copy the file `/ceph/course/claaudia/docs/torch_bm.py` to the `workshop` folder using `cp` command
* Change directory to the `workshop` folder using `cd` command

---

## Create or edit files

* `nano [filename]`: Open or create a file
* Use the arrow keys to move around (don't click with your mouse!)
* Save the file: Press `Ctrl + O`, rename the file if you want, then hit `Enter`
* Exit Nano: Press `Ctrl + X`

### Exercises

* Create a new file in the `workshop` folder called `run.sh` (job script) using `nano`
* Enter this:

```
#!/bin/bash
echo "Hello from AI-LAB!"
```

* Save it, and exit the file.

---

## The queue system!

* Slurm for job scheduling and resource allocation.
* Jobs are queued and executed when resources are available.

### Nice commands to know

* `sinfo`: Current status of the compute nodes.
* `nodesummary`: Overview of allocated GPUs, CPUs, memory
* `squeue`: Overview of the current job queue
* `squeue --me`: Overview of your current job queue

---

## How to submit a job?

* `srun [one line command]`: Runs a command interactively, taking over your terminal until the job finishes, e.g: `srun echo "Hello from AI-LAB!"`
* `sbatch [script]`: Runs a sequence of commands in the background (best for long term jobs)

### Exercises

* Run the job script `run.sh` using the `sbatch` command
* Use `ls` to list the files in the `workhop` folder
* There should be an output file called something like `slurm-1234.out` in the folder
* Print out the content of the output file using the `cat` command

---

## Containers

* Containers bundle application code, libraries, and dependencies
* Easy to install and manage complex applications
* AI-LAB uses Singularity for container management
* Singularity container files (also called images), has `.sif` as extension

---

## Getting containers

### Downloading containers
* https://catalog.ngc.nvidia.com/
* https://hub.docker.com/
* https://cloud.sylabs.io/library/

### Pre-downloaded containers

* `ls /ceph/container`

### Customizing containers

* Add python packages via a virtual environment
* Build your own container image on your local computer

---

## Using containers

* `singularity exec [path/to/container] [action]`: tells Singularity to start a container and execute an action in that container instance, e.g:
    * `srun singularity exec /ceph/container/pytorch/pytorch_24.07.sif python3 torch_bm.py`

<br>

* You need to add `--nv` and `--gres=gpu:1` to enable NVIDIA libraries and allocate a GPU to the job:
    * srun --gres=gpu:1 singularity exec --nv /ceph/container/pytorch/pytorch_24.07.sif python3 torch_bm.py


---

## Lets put is all together in a job script
/ceph/course/claaudia/docs/run.sh:
```bash
#!/bin/bash
#SBATCH --job-name=torch_benchmark      # Name of the job
#SBATCH --output=output_%j.log          # Output file name (%j will be replaced with the job ID)
#SBATCH --error=error_%j.log            # Error file name (%j will be replaced with the job ID)
#SBATCH --gres=gpu:1                    # Request 1 GPU
#SBATCH --mem=16G                       # Request 16G Memory
#SBATCH --cpus-per-task=15              # Request 15 CPUs

# Run the command
singularity exec --nv /ceph/container/pytorch/pytorch_24.07.sif python3 torch_bm.py
```

## The final exercises!

Lets run the `torch_bm.py` script using a pre-made job script.

* Copy the job script `/ceph/course/claaudia/docs/run.sh` to the `workshop` folder using `cp /ceph/course/claaudia/docs/run.sh ~/workshop`
* Use `cat run.sh` to check the content
* Run the job script using `sbatch run.sh`
* Use `squeue --me` to check if your job is running, defined by the `R` below `ST`
* Locate the `JOBID` and cancel your job using `scancel [JOBID]`

---

```
################################################################################

             ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗███████╗
             ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝██╔════╝
                ██║   ███████║███████║██╔██╗ ██║█████╔╝ ███████╗
                ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║
                ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████║
                ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝

################### If you need any help, please visit: #######################
                    
https://serviceportal.aau.dk -> IT -> CLAAUDIA -> Support for CLAAUDIA services

################################################################################
```

