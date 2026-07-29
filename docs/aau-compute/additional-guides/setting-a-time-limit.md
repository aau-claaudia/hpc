Sometimes, jobs may get stuck or encounter unforeseen issues, causing them to run indefinitely. Setting a time limit ensures that such jobs are automatically terminated after a certain duration, preventing them from consuming resources unnecessarily.

You can add a `--time` parameter to your Slurm command, e.g. `--time=0-08:00:00` to run a job for maximum 8 hours:

```console
srun --time=08:00:00 hostname
```

## Time limits before service windows
Setting a time limit is particularly important when a [service window](/ai-cloud/terms-and-conditions/#7-service-windows) is approaching. On the day of the service window, the entire cluster will be reserved for maintainance. As you may remember, jobs can be run in the `prioritized` partition for 6 consecutive days. If there are fewer than 6 days until the service window, and you do not specify the `--time` parameter, your job will only start *after* the service window has been completed. To run jobs in the days leading up to the service window, you will need to calculate how much time is left, and add this value to the `--time` argument to your Slurm command.
