# Allocating resources

When running jobs, you can request specific resources like memory, CPUs, and GPUs.

---

### 💾 System memory

```
--mem=40G
```

### ⚙️ CPUs

```
--cpus-per-task=15
```

### 🎮 GPUs

```
--gres=gpu:1
```

---

## 🚀 Example: Allocating resources with srun

```bash
srun --cpus-per-task=4 --mem=8G --gres=gpu:1 python3 my_script.py
```

---

## 📝 Example: Allocating resources with sbatch

In a batch script, add resource requests using `#SBATCH` directives:

```bash title="run.sh"
#!/bin/bash
#SBATCH --gres=gpu:1          # Request 1 GPU
#SBATCH --cpus-per-task=4    # Request 4 CPUs
#SBATCH --mem=8G             # Request 8 GB memory

python3 my_script.py
```

---

**Next:** [Containers →](15-containers.md)
