# Running jobs on proprietary nodes

Research groups who have made use of the buy-in option (bought own hardware to be hosted in AI Cloud) will have privileged access to their nodes.

Other users can also make use of the resources with *unprivileged access*.

## Privileged access

### AI Centre

Researchers with affiliation to the [Pioneer Centre for AI](https://www.aicentre.dk/) can be added to the following privileged accounts:

* **`aicentre`**

    This account gives access to the partition of the same name `aicentre` containing the nodes `i256-a40-01` and `i256-a40-02`.

    To launch a privileged job on this node, the `--account=` and `--partition=` arguments must be added to your launch command:
    
    ```
    ❯ srun --partition=aicentre --account=aicentre hostname
    srun: job 793360 queued and waiting for resources
    srun: job 793360 has been allocated resources
    i256-a40-01.srv.aau.dk
    ```

* **`aicentre-a100`**

    This account gives access to the partition of the same name `aicentre-a100` containing the node `nv-ai-04`.
    
    To launch a privileged job on this node, the `--account=` and `--partition=` arguments must be added to your launch command:
    
    ```
    ❯ srun --partition=aicentre-a100 --account=aicentre-a100 hostname
    srun: job 793361 queued and waiting for resources
    srun: job 793361 has been allocated resources
    nv-ai-04.srv.aau.dk
    ```

## Unprivileged access

If you want wish to launch an unprivileged job on a proprietary node, you must specify the arguments; `--partition=`, `--qos=` and `--time` arguments:

```
❯ srun --qos=unprivileged --partition=aicentre --time=0-00:01:00 hostname
srun: job 793362 queued and waiting for resources
srun: job 793362 has been allocated resources
i256-a40-01.srv.aau.dk
```

Please note:

* The `--time=` parameter can be set to a maximum of `6-00:00:00` (6 days).

* Unprivileged jobs are preemtable. If a request is made for the same resources, the job will be interrupted until the resources free up again.


