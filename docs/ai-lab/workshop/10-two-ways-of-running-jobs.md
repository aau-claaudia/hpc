# Two ways of running jobs

You can run compute tasks in two main ways on AI-LAB: **interactive (srun)** or **batch (sbatch)**.

---

## 1️⃣ Interactive Job – srun

Runs immediately in your terminal session.

```bash
srun -u echo "Hello from compute node"
```

Use for quick tests or debugging.

`-u` forces srun to print outputs immediately

---

## 2️⃣ Batch Job – sbatch

Submit a script to run in the background.

```bash title="run.sh"
#!/bin/bash
echo "Hello from compute node"
```

Submit it:

```bash
sbatch run.sh
```

---

**Next:** [Exercise 1 →](11-exercise-1.md)
