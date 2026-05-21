# Batch LLM Inference on TAAURUS

This guide explains how to run large-scale batch inference using **vLLM** on TAAURUS.

Typical use case:

> Processing 1,000–1,000,000 documents (e.g. clinical notes, journals, research text) using an LLM.

---

# System Overview

You will use:

* Slurm (job scheduling)
* Singularity (.sif containers)
* vLLM (high-performance LLM inference engine)
* NVIDIA L40 GPUs (`sp-l40-01`, `sp-l40-02`)

---

# 1. Shared components (read-only)

**These are shared resources** means every TAAURUS project can use the **same** container images and model weights from a central path. You do **not** need to copy the `.sif` files or model folders into each project directory. The containers and base models is only ever **read** at runtime. Your **inputs, job scripts, logs, and inference outputs** stay under your own project path (see [Project-specific storage](#project-specific-storage-strict-isolation) below)—that is where isolation matters.

```bash
/shared/containers/
    vllm-llm.sif
    llama3-8b.sif
    mistral-7b.sif

/shared/models/
    llama3-8b/
    mistral-7b/
```

In Slurm/Singularity jobs, reference these paths directly (for example `singularity exec /shared/containers/vllm-llm.sif …` and model weights under `/shared/models/…`). Many users may run jobs against the same files at the same time; that is expected and supported.

### ✔ Why this is safe

* **`.sif` containers are immutable** — Singularity runs them as read-only images; your job cannot alter the shared `.sif` for other users.
* **Models are read-only** — weights are loaded for inference only, not written back into `/shared/models/`.
* **No project secrets in shared paths** — prompts, documents, and results live in `/media/<your-project>/`, not in `/shared/`.
* **No cross-project data mixing from shared assets** — sharing a container or model does not give other projects access to your `data/` or `outputs/`; those directories remain separate.

---

## 📁 Project-specific storage (strict isolation) {#project-specific-storage-strict-isolation}

Each project has its own sandbox:

```bash
/media/projectA/
    data/
    jobs/
    outputs/
```

```bash
/media/projectB/
    data/
    jobs/
    outputs/
```

### ❌ Rule

Projects must **never access each other’s directories**

---

# ⚙️ 2. Prerequisites

Before starting, ensure:

✔ You have access to Slurm
✔ You have a GPU node allocation (L40)
✔ Input data is prepared in JSONL format
✔ vLLM container exists in `/shared/containers/`
✔ Model is downloaded in `/shared/models/`

---

# 📄 3. Prepare Your Input Data

Your input must be in **JSONL format**:

```json
{"id": 1, "text": "Patient presents with chest pain..."}
{"id": 2, "text": "Follow-up shows improvement..."}
```

Save it here:

```bash
/media/projectA/data/input.jsonl
```

---

# ✂️ 4. Split Data into Batch Chunks

Since Slurm runs parallel jobs, split your dataset:

```bash
python scripts/preprocess.py \
  --input /media/projectA/data/input.jsonl \
  --output /media/projectA/data/chunks/ \
  --num_chunks 100
```

### Result:

```bash
chunks/
  chunk_000.jsonl
  chunk_001.jsonl
  ...
```

---

# 🧠 5. Select Your Model

Available models:

```bash
/shared/models/llama3-8b/
/shared/models/mistral-7b/
/shared/models/mixtral-8x7b/
```

## Recommended for L40 GPUs:

✔ Llama 3 8B (fast + stable)
✔ Mistral 7B (lightweight + efficient)

---

# 📦 6. Verify vLLM Container

Ensure this exists:

```bash
/shared/containers/vllm-llm.sif
```

This container must include:

* vLLM
* PyTorch (CUDA enabled)
* Transformers (offline mode enabled)
* Python runtime

---

# 🧪 7. Test Single Chunk (Recommended First Step)

Before running full batch:

```bash
singularity exec --nv \
  /shared/containers/vllm-llm.sif \
  python /app/vllm_batch.py \
  --model /shared/models/llama3-8b \
  --input /media/projectA/data/chunks/chunk_000.jsonl \
  --output /media/projectA/outputs/test.jsonl
```

✔ Confirm output file is created
✔ Check no errors in logs

---

# 🧾 8. Create Slurm Job Script

Create file:

```bash
/media/projectA/jobs/vllm_batch.sbatch
```

---

## 🖥️ Slurm Batch Script

```bash
#!/bin/bash
#SBATCH --job-name=vllm-batch
#SBATCH --partition=gpu
#SBATCH --gres=gpu:l40:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=80G
#SBATCH --time=04:00:00
#SBATCH --array=0-99
#SBATCH --output=logs/%x_%A_%a.out
```

---

## 🔧 Load environment

```bash
module load singularity
```

---

## 🔐 Enable offline mode (IMPORTANT)

```bash
export TRANSFORMERS_OFFLINE=1
export HF_DATASETS_OFFLINE=1
export VLLM_NO_USAGE_STATS=1
```

---

## 📂 Define paths

```bash
CONTAINER=/shared/containers/vllm-llm.sif
MODEL=/shared/models/llama3-8b

INPUT_DIR=/media/projectA/data/chunks
OUTPUT_DIR=/media/projectA/outputs
```

---

## 📌 Assign chunk per job

```bash
INPUT_FILE=${INPUT_DIR}/chunk_${SLURM_ARRAY_TASK_ID}.jsonl
OUTPUT_FILE=${OUTPUT_DIR}/output_${SLURM_ARRAY_TASK_ID}.jsonl
```

---

## 🚀 Run vLLM job

```bash
singularity exec --nv \
  $CONTAINER \
  python /app/vllm_batch.py \
  --model $MODEL \
  --input $INPUT_FILE \
  --output $OUTPUT_FILE
```

---

# 🚀 9. Submit Your Job

Run:

```bash
sbatch /media/projectA/jobs/vllm_batch.sbatch
```

---

# 📊 10. Monitor Progress

## Check running jobs

```bash
squeue -u $USER
```

## View logs

```bash
tail -f logs/vllm-batch_*.out
```

---

# 📦 11. Collect Output Results

Each job produces:

```bash
/media/projectA/outputs/output_000.jsonl
/media/projectA/outputs/output_001.jsonl
...
```

---

## Merge results

```bash
cat /media/projectA/outputs/*.jsonl > final_results.jsonl
```

---

# 📄 12. Output Format

Each result looks like:

```json
{
  "id": 42,
  "result": "Patient shows improved symptoms with no complications."
}
```

---

# ⚡ 13. Performance Best Practices (L40 GPUs)

## ✔ Use batching

Process multiple prompts at once

## ✔ Keep chunk sizes balanced

Recommended:

* 500–2000 documents per chunk

## ✔ Use smaller models when possible

* 7B–8B models are optimal

## ✔ Avoid repeated model loading

Model loads once per Slurm job

---

# 🧠 14. Why vLLM is faster

vLLM improves performance using:

* Continuous batching
* KV-cache reuse
* PagedAttention memory system
* High GPU utilization

### Expected performance on L40:

| System                | Relative Speed |
| --------------------- | -------------- |
| Transformers baseline | 1x             |
| vLLM                  | 3–10x faster   |

---

# 🔁 15. Fault Recovery

If a job fails:

### Re-run only that chunk:

```bash
sbatch --array=42 /media/projectA/jobs/vllm_batch.sbatch
```

✔ No need to rerun full dataset
✔ Outputs are independent per chunk

---

# 🔒 16. Security Rules (Mandatory)

## ✔ Allowed

* Read-only access to `/shared/models/`
* Read-only access to `/shared/containers/`
* Write access only to `/media/projectX/`

## ❌ Not allowed

* Network access inside container
* Cross-project file access
* Writing into shared directories
* External API calls

---

# 🧾 17. Summary

You now have a fully working system for:

✔ Offline LLM inference
✔ High-performance vLLM execution
✔ Slurm-based distributed processing
✔ Secure multi-project isolation
✔ Scalable processing of 100k+ documents

---

# 🚀 Optional Next Step (recommended)

If you want, I can extend this with:

### 🔧 Production upgrades

* Auto-retry failed Slurm chunks
* Checkpointing inside vLLM jobs
* GPU memory optimization tuning for L40

### 🧠 Advanced scaling

* Multi-node L40 inference (tensor parallel vLLM)
* Hybrid Slurm + queue scheduler

### 🖥️ User experience layer

* Web GUI for launching batch jobs safely
* Job templates for researchers (1-click pipelines)

Just tell me 👍
