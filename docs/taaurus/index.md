# TAAURUS HPC Platform Testing Guide

TAAURUS is a new HPC platform for testing SLURM job scheduling and Singularity container functionality.

## What is SLURM?

**SLURM** (Simple Linux Utility for Resource Management) is a job scheduler that:
- Manages compute resources (CPUs, memory, GPUs)
- Queues and runs your jobs when resources are available
- Handles job submission, monitoring, and cleanup

## What is Singularity?

**Singularity** is a container platform that:
- Packages applications with all dependencies
- Ensures reproducible environments
- Provides GPU access with `--nv` flag

## What is the PyTorch Container?

**pytorch_25.08.sif** is a pre-built Singularity container containing:
- PyTorch deep learning framework
- CUDA support for GPU acceleration
- Python and essential scientific libraries
- All dependencies needed to run GPU-accelerated code

## What does the Python Script do?

**gpu_test.py** performs a GPU stress test that:
- Creates large matrices (16,384 × 16,384) on the GPU
- Performs intensive matrix multiplications for 5 minutes
- Monitors GPU performance and memory usage
- Reports iteration times and status updates every 30 seconds
- Verifies CUDA drivers and GPU functionality are working

## Quick Test

The test files are already available on the server. Run this simple test:

### Option 1: Submit a batch job
```bash
sbatch run_gpu_test.sh
```

### Option 2: Run directly
```bash
srun --mem=50G --cpus-per-task=15 --gres=gpu:1 singularity exec --nv pytorch_25.08.sif python3 gpu_test.py
```

## Monitor Your Test

```bash
# Check job status
squeue -u $USER

# Watch output in real-time
tail -f gpu_test_*.log
```

## What to Expect

**Success indicators:**
- Job appears in `squeue` and runs (status: `R`)
- GPU detected: `Starting on GPU 0: <GPU_NAME>`
- Performance output: `Iteration 10, avg time: 0.1234s`
- Completion: `Finished after 300s, 1500 iterations`

**If it fails:**
- Check error logs: `cat gpu_test_*.err`
- Verify GPU availability: `nvidia-smi`
- Check resource availability: `sinfo`

## Test Results

The test runs for 5 minutes and performs GPU matrix multiplications. You should see:
- Regular status updates every 30 seconds
- Consistent iteration times (0.1-0.5 seconds typical)
- No CUDA or memory errors
- Successful completion message

That's it! This verifies both SLURM and Singularity are working correctly on TAAURUS.
