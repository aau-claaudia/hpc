## Checking GPU usage

When you have launched a job on a GPU, it is good practice to verify that it is indeed utilising the GPU.

We can do this by logging in to the compute node, and calling the `nvidia-smi` command.

Start by locating the node, that your job is running on. Then log in to the node:

```
ssh -l user@domain.aau.dk a256-t4-01.srv.aau.dk
```

And call:

```
nvidia-smi
```

Which prints a table:

```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.195.03             Driver Version: 570.195.03     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   4  NVIDIA L40S                    Off |   00000000:03:00.0 Off |                    0 |
| N/A   72C    P0            287W /  350W |   27963MiB /  46068MiB |     89%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
```

This table is a snapshot of the GPU devices (physical GPU's) allocated to your Slurm job. The values represent measures of a sampling period of 1 second.

the most important parameters to note:

* **Volatile GPU-Util**: How much of the sampling period the GPU was actively computing. As computations normally take place in batches, it is normal to see this value fluctuate.

* **Memory usage**: How much of the available GPU-ram is being consumed. Note that this is expressed in *mebibytes* (that's MiB not MB), which more accurately represents memory values (binary).

#### Bonus tips:

!!! tip "Continuous updates"

    Prepending the `watch` command, will execute the `nvidia-smi` command every 2 seconds - allowing us to get continuous updates to the GPU activity:

    ```
    watch nvidia-smi 
    ```

!!! tip "Print only the important bits"

    Instead of printing the whole table, we can print only select values:

    ```
    nvidia-smi --query-gpu=index,utilization.memory,utilization.gpu --format=csv
    ```

    The `watch` command can of course also be prepended in order to get continuous updates.

