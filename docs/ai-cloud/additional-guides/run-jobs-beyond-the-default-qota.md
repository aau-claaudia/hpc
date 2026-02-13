When we run a job, a number of default parameters are passed to Slurm, and we are granted access to resources in accordance with the default configuration.
In some cases we may want to pass different values to some of these paramaters, eg. in order to launch a job on a node with access restrictions, or if we want to access the default resources on different terms.

### Resource control features
On AI Cloud we use a variety of features to control access to resources:

* Nodes in the cluster can belong to one or more `partitions`
* Access to these partitions may be restricted to certain `accounts`
* The term `quality of serivce` (abbreviated `QOS`) can determine the amount of resources that can be accessed at any given time. On this page, we will give you a demonstration of what is possible.

## The default access mode

For reference, let's launch a job with the default settings:

```
srun hostname
```

This job is run with the parameters `--account=aau`, `--qos=normal` and `--partition=prioritized`. These parameters are the defaults, and do not have to be passed to your launch command.

!!! example "Excercise: Verify the Slurm parameters"

    If you want to view the values passed to the mentioned arguments, you can run the command:

    ```
    srun bash -c 'env | grep SLURM'
    ```

    This returns the Slurm *environment variables*. Among these we should be able to find `SLURM_JOB_PARTITION=prioritized`, `SLURM_JOB_ACCOUNT=aau` and `SLURM_JOB_QOS=normal` which can serve as an interesting comparison in this section. As we did not pass any arguments to the srun command, these are the defaults. 

## Unprivileged access

An infinite number of jobs can be launched using the flag `--qos=unprivileged`.

```
srun --qos=unprivileged --time=2-00:00:00 hostname
```
    
It's important to note that `unprivileged` jobs are preemptable. If a request for the same resources is made, the job will be interrupted and placed in the queue, where it will remain until the resources become available again.

## Deadline access

In the `deadline` account users are allowed to have an additional 12 simultaneous jobs with an additional 12 GPU's for a period of up to 14 days.
To run a job with deadline resources, we must specify `--account=deadline`.

```
srun --account=deadline hostname
```

In order to gain access to the deadline account, users must submit an application found on serviceportal.aau.dk → [AI Cloud: Request access to deadline resources](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=22a816638322be5053711d447daad379). We will try to process applications on the same day.


This option is for researchers who are working towards a deadline, and is not intended to become a permanent solution for projects with large resource needs. Once granted it will not be possible to reapply for another 14 days. If your project requires a large amount of resources, you should consider applying for a grant for an [external HPC system](/external-hpc/).

