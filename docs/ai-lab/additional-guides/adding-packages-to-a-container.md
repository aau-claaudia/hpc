You may need to install additional packages if your existing container is missing software required for your work. The recommended practice is to create a copy of your container and modify this. This allows you to make the changes you want without affecting the original container.
## Step 1: Create a copy of the container
Navigate to the folder where your container is stored.
```
cd /ceph/container/
```
Choose the container you want to modify.  
Run the following command to create a copy of your selected container:
```
cp pytorch_26.04.sif ~/container/my_container.sif
```
###What does the command?
- `cp` – copies a file.
- `pytorch_26.04.sif` – the original container (source file).
- `~/container/my_container.sif` – the new copy, which is saved in the folder "container" in your home directory with the name "my_container.sif"

## Step 2: Check which packages are in the selected container
Before adding a new package, you can check which Python packages are already installed in the container.

Navigate to the folder where your container is stored.

```
cd ~/container/
```
To display a list of all Python packages installed in the container run the following command:
```
srun singularity exec my_container.sif pip list
```

- `srun` – asks Slurm to run the command as a job on a compute node.
- `singularity exec` – tells Singularity to run a command inside the container.
- `my_container.sif` – the name of the container you want to use.
- `pip list` – displays the Python packages installed in the container, along with their versions.

**A reccomendation is to make a list of the packages you are missing in the container you want to modify.**

## Step 3: Build a sandbox
A sandbox is a writable version of a container where you can make changes and install additional packages.

```
srun singularity build --sandbox /ceph/home/user/container/my_container/ /ceph/home/user/container/my_container.sif
```

- `srun` – asks Slurm to run the command as a job on a compute node.
- `singularity build` – is used to create a new container from an existing container.
- `--sandbox` – tells Singularity to create the new container as a writable sandbox directory instead of a .sif file.
- `/ceph/.../my_container/` – the location and name of the new sandbox.
- `/ceph/.../my_container.sif` – the existing .sif container that the sandbox is created from.

**Note:** Building the sandbox can take a couple of minutes. When the proces is complete, you will get the info message `INFO: Build complete: /ceph/.../my_container/`

## Step 4: Install packages in your sandbox
To be able to install additional packages, navigate to the folder where your sandbox is located and open a interactive session:
```
cd /ceph/home/user/container/
```
Followed by:
```
srun --pty singularity shell my_container/
```

- `srun` – asks Slurm to run the command as a job on a compute node.
- `singularity shell` – opens an interactive shell inside the container.
- `my_container/` – the sandbox directory you want to open.

You can now tell that you are inside your sandbox because the terminal prompt shows: `Singularity>`

Now you are free to install the additional packages you need! 
```
pip install package_name
```

To see all installed Python packages, run:
```
pip list
```
This displays a complete list of the packages installed in the sandbox.

If you want to check whether a specific package is installed, run:
```
pip show package_name
```
Replace `package_name` with the name of the package you want to check.

### Congrats you have now installed the additional packages in your sandbox!

When you are finished, exit the Singularity shell by running: `exit`


Did you exit your shell before you were done? Or have you closed the terminal and want to continue installing packages? Just navigate to the folder where you placed your sandbox and then run the following command:
```
srun singularity shell my_container/
```



## Run scripts in your sandbox
Once you have installed the required packages, you can use your modified sandbox to run your scripts without converting it to a `.sif` container first.
This is useful while you are still testing your environment or making changes to the installed packages.

### Run a script in the sandbox
Run your script directly from the sandbox with:
```
srun singularity exec my_container/ python my_script.py
```
**What does the command mean?**

- `srun` – asks Slurm to run the command as a job on a compute node.
- `singularity exec` – runs a command inside the sandbox.
- `my_container/` – the sandbox containing your installed packages.
- `python my_script.py` – runs your Python script inside the sandbox.

## When Should You Convert the Sandbox to a .sif Container?
A sandbox is ideal while you are installing packages, testing your environment, and making changes because it is writable.

Once you are finished modifying the container, it is recommended to convert the sandbox into a `.sif` container.

A `.sif` container is a better choice for long-term use because it:

- provides a fixed and reproducible environment,
- is easier to share with others,
- is more suitable for running production or batch jobs, and
- prevents accidental changes to the container.

## Convert the sandbox back into a `.sif` container
To convert your sandbox back into a `.sif` container, create a Slurm batch script and run it with `sbatch`.

Using a batch script is recommended because it:

- continues running even if you close your terminal,
- reduces the risk of the job stopping due to time limits or a frozen terminal, and
- allows you to choose the appropriate number of CPU cores and amount of memory to complete the conversion more efficiently.

Add the following content to your batch script:
```
#!/bin/bash
	#SBATCH --job-name=job_container_medium
	#SBATCH --gres=gpu:1
	#SBATCH --cpus-per-task=16
	#SBATCH –mem=64G
	#SBATCH –time=12:00:00
	#SBATCH –output=logs/%x_%j.out
	#SBATCH –error=logs/%x_%j.err
	mkdir -p logs
singularity build /ceph/home/its.aau.dk/vi40bx/training/container/my_container_updated.sif \
/ceph/home/its.aau.dk/vi40bx/training/container/my_container/
```

**Note:** that the job can take some time.

## Verify and test the new container
After the job has finished, check that a `.sif` container with the name you specified has been created by running this command:
```
ls -lh /ceph/home/user/container/*.sif
```
To verify that the packages you added have been installed successfully, follow these steps:

**Start the container by running:**
```
srun singularity shell \
/ceph/home/user/container/my_container_updated.sif
```
**Once you are inside the container, run this command:**
```
python -m pip list
```
This displays a list of the Python packages installed in the new container, allowing you to verify that the packages you added are present.

**Congrats, you can now run a job with your modified container and share your container with others!**
