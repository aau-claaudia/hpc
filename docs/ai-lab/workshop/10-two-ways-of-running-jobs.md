# Two ways of running jobs

You can run compute tasks in two main ways on AI-LAB: **interactive (srun)** or **batch (sbatch)**.

---

## 1️⃣ Interactive Job – srun

Runs immediately in your terminal session.

```bash
srun --job-name=hello echo "Hello from compute node"
```

Use for quick tests or debugging.

---

## 2️⃣ Batch Job – sbatch

Submit a script to run in the background.

```bash title="run.sh"
#!/bin/bash
#SBATCH --job-name=hello
#SBATCH --output=hello.out
echo "Hello from compute node"
```

Submit it:

```bash
sbatch run.sh
```

---

**Next:** [Exercise 1 →](11-exercise-1.md)
