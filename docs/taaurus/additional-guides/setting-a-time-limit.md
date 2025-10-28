Sometimes, jobs may get stuck or encounter unforeseen issues, causing them to run indefinitely. Setting a time limit ensures that such jobs are automatically terminated after a certain duration, preventing them from consuming resources unnecessarily.

You can add a `--time` parameter to your Slurm command, e.g. `--time=08:00:00` to run a job for maximum 8 hours:

```console
srun --time=08:00:00 hostname
```
<br>

<h3>Default and Maximum Job Time Limits</h3>
<p>
Every job submitted to AI-LAB has a default time limit of 1 hour if no time is specified. This default has been set to encourage efficient resource usage and prevent jobs from running unnecessarily long. The 1-hour default helps ensure fair access to resources for all users and reduces the likelihood of jobs getting stuck or consuming resources without active monitoring. However, you can request up to 12 hours maximum for longer computations by explicitly specifying the time limit.
</p>

<h3>Jobs can run no longer than 12 hours</h3>
<p>
The maximum time limit for any job on AI-LAB is 12 hours. This limit is set to prevent a single user from monopolizing the entire cluster indefinitely. We are trying to ensure that all users receive an equal share of available resources.
</p>