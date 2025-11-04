# Exercise 3: Running a GPU script with containers and resources

Let's try running a Python GPU script inside a PyTorch container with resources allocated.

---

1. Inside the workshop directory, you will also find a file called `run_container.sh`

2. Check the file content using `cat run_container.sh`

3. Submit the job using `sbatch`

    ??? info "Hint"
        ```bash
        sbatch run_container.sh
        ```

4. Check the job status using `squeue --me` and find the JOBID.

    ??? info "Hint: How to find the JOBID"
        Here, `162841` is the JOBID
        ```bash
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
            162841        l4    myjob ry90cd@i  R      10:25      1 ailab-l4-11
        ```

5. Check the GPU utilization be running the following command:

    ```
    ailab --gpu-util 162841
    ```
     
    Replace `162841` with your JOBID

    ??? info "Hint: Understanding GPU Metrics"
        
        Key metrics to watch:

        GPU-Util: Percentage of GPU being used (aim for 70-100% during training)
        Memory-Usage: How much GPU memory your job is using
        Temperature: GPU temperature (should stay below 80°C)
        Power: Power consumption (indicates workload intensity)

        ```
        +-----------------------------------------------------------------------------------------+
        | NVIDIA-SMI 555.42.02              Driver Version: 555.42.02      CUDA Version: 12.5     |
        |-----------------------------------------+------------------------+----------------------+
        | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
        | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
        |                                         |                        |               MIG M. |
        |=========================================+========================+======================|
        |   0  NVIDIA L4                      Off |   00000000:01:00.0 Off |                    0 |
        | N/A   44C    P0             36W /   72W |     245MiB /  23034MiB |     90%      Default |
        |                                         |                        |                  N/A |
        +-----------------------------------------+------------------------+----------------------+
        |   1  NVIDIA L4                      Off |   00000000:02:00.0 Off |                    0 |
        | N/A   38C    P8             16W /   72W |       4MiB /  23034MiB |      0%      Default |
        |                                         |                        |                  N/A |
        +-----------------------------------------+------------------------+----------------------+
        |   2  NVIDIA L4                      Off |   00000000:41:00.0 Off |                    0 |
        | N/A   41C    P8             16W /   72W |       1MiB /  23034MiB |      0%      Default |
        |                                         |                        |                  N/A |
        ...

        +------------------------------------------------------------------------------+
        |  GPU    PID     USER    GPU MEM  %CPU  %MEM      TIME  COMMAND               |
        |    0 232843   user@+     236MiB   100   0.1  01:00:20  /usr/bin/python3 tor  |
        +------------------------------------------------------------------------------+
        ```

        The most important parameter to notice here is the GPU-Util metric. Here, you can see that the first GPU is operating at 90% GPU utilization. This indicates excellent utilization of the GPU.

        You can locate which GPU(s) that belongs to your job, by finding your username below USER and the GPU number under GPU. In this case user@+ are utilizing GPU number 0 in the NVIDIA-SMI list.

        ```
        +------------------------------------------------------------------------------+
        |  GPU    PID     USER    GPU MEM  %CPU  %MEM      TIME  COMMAND               |
        |    0 232843   user@+     236MiB   100   0.1  01:00:20  /usr/bin/python3 tor  |
        +------------------------------------------------------------------------------+
        ```
        
6. Once completed, cancel all your jobs by using `scancel -u $USER`

---

**Next:** [Final pointers →](19-final-pointers.md)
