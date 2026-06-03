# Creating an sbatch script

Batch scripts tell Slurm what to run and which resources to use.



<div class="workshop-internal-break" role="separator"></div>


## ✏️ Creating a script

Create your script using micro or your preferred editor:

```bash
micro run.sh
```

```bash title="run.sh"
#!/bin/bash

#SBATCH --job-name=myjob       
#SBATCH --time=0:10:00 
#SBATCH --output=myjob.log

echo "Hello from compute node"
sleep 60
echo "Done sleeping"
```

Save and exit (`Ctrl+S`, Enter, `Ctrl+Q`).



<div class="workshop-internal-break" role="separator"></div>


## 🚀 Submit your script

Submit the batch script to Slurm:

```bash
sbatch run.sh
```

This command sends your script to the Slurm scheduler, which will run it when resources become available.



<div class="workshop-internal-break" role="separator"></div>


## 📄 Check the output

Once your job completes, check the output file:

```bash
cat myjob.log
```



<div class="workshop-internal-break" role="separator"></div>


**Next:** [Exercise 2 →](13-exercise-2.md)
