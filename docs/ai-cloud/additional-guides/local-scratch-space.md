Normally AI Cloud relies on a network drive as its storage solution.
A handful of nodes have local scratch space, which can be utilised for faster I/O operations.

The nodes in question are:

* `i256-a40-[01-02]`: 6.4 TB total
* `nv-ai-[01-03]`:  30 TB total
* `nv-ai-04`:  14 TB total

The local scratch space is physically attached to each individual compute nodes, so it can only be accessed from that specific node.

!!! warning
    This space is not intended for long term storage. Please remove your files when you are finished. We reserve the right to delete directories that have been left untouched for 90 days.

## Create a directory

In order to make use of this drive, we need to identify which node we want to work on.

In this example, we will be targetting `nv-ai-02`.

The following command will create a directory for you on the network drive, and set the permissions so the directory is only accessible for you.

```
sbatch -w nv-ai-02 --wrap="mkdir -p /raid/$USER && chmod o= /raid/$USER"
```

## File transfer

In order to be able to transfer our files, we will need to be able to SSH in to the node. We can only do this if we have a job running on the node.

We therefore launch job that runs in the background for 15 minutes (900 seconds) - or however long you believe it will take for you to transfer your files. If you have a job running already, this is not necessary.

```
sbatch -w nv-ai-02 --wrap="sleep 900"
```

The hostname will always be the name of the node with `srv.aau.dk` added to the end.

Now transfer your files:
```
scp xs98kl@domain.aau.dk@nv-ai-02.srv.aau.dk:/raid/xs98kl@domain.aau.dk
```

Other file transfer methods (as described in the [File transfer](../getting-started/file-transfer.md)) section will also work. Just change the hostname from `ai-fe02.srv.aau.dk` to e.g. `nv-ai-03.srv.aau.dk`.

Remember to stay mindful of your fellow resarchers, and cancel the job you created for the file transfer when you are finished.

## Working with the local scratch space

Given that you have acquired a job allocation on the specific node you are working on, just reference this newly created directory.

There is no need to bind the directory to your container environment.
