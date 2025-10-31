# Using containers on AI-LAB

Let's run a simple Python script inside a Singularity container with GPU support.

---


## 🚀 Example: Running a container with srun

```bash
srun singularity exec --nv /ceph/container/pytorch/pytorch_25.04.sif python3 gpu_stress.py
```

---

## 📝 Example: Running a container with sbatch

In a batch script, add resource requests using `#SBATCH` directives:

```bash title="run.sh"
#!/bin/bash

singularity exec --nv /ceph/container/pytorch/pytorch_25.04.sif python3 gpu_stress.py
```

---

## 📖 Understanding the Singularity command

Let's break down what each part does:

* `singularity exec`: Tells Singularity to execute something inside the container.
* `--nv`: Tells Singularity to include NVIDIA libraries. **Always use this flag when running GPU-accelerated code** so your container can access the GPU.
* `/ceph/container/pytorch/pytorch_25.04.sif`: The path to your container file. This is a pre-downloaded PyTorch container stored on AI-LAB.
* `python3 gpu_stress.py`: The command to run inside the container. This executes your Python script using Python 3 from within the container environment.

---

**Next:** [Exercise 3 →](18-exercise-3.md)
