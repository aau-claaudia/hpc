When we run a job, a number of default parameters are passed to Slurm, and we are granted access to resources in accordance with the default configuration.
In some cases we may want to pass different values to some of these paramaters, eg. in order to launch a job on a node with access restrictions, or if we want to access the default resources on different terms.

On AI Cloud we use a variety of features to control access to resources. Nodes in the cluster can belong to one or more `partitions`, access to them may be restricted to certain `accounts`, and finally `quality of serivce` (abbreviated `QOS`) can determine the amount of resources that can be accessed at any given time. On this page, we will give you a demonstration of what is possible.

## The default quota

By default each user is allowed to have 12 jobs running simultaneously, with a maximum of 12 GPU's.

For reference, let's launch a job with the default settings:

```
srun bash -c 'env | grep SLURM'
```

This returns a long list of environment variables that describe the settings our jobs was run with. As we did not pass any arguments to the srun command, these are the defaults. Among these, we should be able to find `SLURM_JOB_PARTITION=prioritized`, `SLURM_JOB_ACCOUNT=aau` and `SLURM_JOB_QOS=normal` which can serve as an interesting comparison in this section.

## Unprivileged mode

An infinite number of jobs can be launched using the flag `--qos=unprivileged`. You will also have to specify your expected walltime (currently a maximum of 6 days - `6-00-00-00`)  This is available to all users.

```
srun --qos=unprivileged --time=2-00:00:00 bash -c 'env | grep SLURM'
```

It's important to be aware of the conditions for launching your jobs with the `unprivileged` QOS; if a request for the same resources is made, the job will be interrupted and placed in the queue, where it will remain until the resources become available again.

## Deadline mode


In the `deadline` account users are allowed to have an additional 12 simultaneous jobs with an additional 12 GPU's for a period of up to 14 days. Users can apply for these resources by submitting an application on the [Serviceportal](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=22a816638322be5053711d447daad379). These will be processed on the same day.


To run a job with deadline resources, we must specify `--account=deadline`.

```
srun --account=deadline bash -c 'env | grep SLURM'
```
This option is for researchers who are working towards a deadline, and is not intended to become a permanent solution for projects with large resource needs. Once granted it will not be possible to reapply for another 14 days. If your project requires a large amount of resources, you should consider applying for a grant for an [external HPC system](/external-hpc/).

