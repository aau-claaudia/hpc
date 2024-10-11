You can launch a shell within a Singularity container, allowing you to interact with the container's environment. Use the `shell` command with the desired image as follows

```
srun --gres=gpu:1 --pty singularity shell --nv /ceph/container/pytorch/pytorch_24.09.sif
```


The `--pty` creates a virtual interactive terminal for a command to run within.

You now have shell access

```
Singularity>
```

Lets try checking the Python version:

```
python3 --version
```

You can exit the interactive session with:

```
exit
```