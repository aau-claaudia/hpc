# Creating an sbatch script

Batch scripts tell Slurm what to run and which resources to use.

---

## ✏️ Creating a script

Create your script using nano or your preferred editor:

```bash
micro run.sh
```

```bash title="run.sh"
#!/bin/bash
# This tells the system to run the script using the Bash shell
# It must be the first line of your script

# ============================================
# Slurm Arguments
# ============================================
# These lines tell Slurm how to run your job
# They start with #SBATCH and must come before your commands

#SBATCH --job-name=myjob           # Name of your job (useful for identifying it in the queue)
#SBATCH --time=0:10:00             # Time limit (hours:minutes:seconds). Job is killed if it exceeds this. Also default time is 1 hour so if you need more you need to use --time.
#SBATCH --output=myjob.log         # Where to save standard output and errors

# ============================================
# Commands to Run
# ============================================
# Everything below will execute on the compute node

echo "Hello from compute node"    # Print a message
sleep 60                          # Wait for 60 seconds
echo "Done sleeping"              # Print another message
```

Save and exit (`Ctrl+S`, Enter, `Ctrl+Q`).

---

## 🚀 Submit your script

Submit the batch script to Slurm:

```bash
sbatch run.sh
```

This command sends your script to the Slurm scheduler, which will run it when resources become available.

---

## 📄 Check the output

Once your job completes, check the output file:

```bash
cat myjob.log
```

---

**Next:** [Exercise 2 →](13-exercise-2.md)
