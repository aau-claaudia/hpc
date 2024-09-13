Sometimes, jobs may get stuck or encounter unforeseen issues, causing them to run indefinitely. Setting a time limit ensures that such jobs are automatically terminated after a certain duration, preventing them from consuming resources unnecessarily.

You can add a `--time` parameter to your Slurm command, e.g. `--time=08:00:00` to run a job for maximum 8 hours:

```console
srun --time=08:00:00 hostname
```
