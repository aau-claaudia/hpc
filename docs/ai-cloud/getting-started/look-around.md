In this section our goal is to provide you with a fundamental understanding of the platform, and to present you with a few of the fundamental commands used for interacting with the system..

## System overview

Find the diagram in the section [System overview](../system-overview.md) illustrating how the nodes in the cluster are structured.

Before going on, you should make sure that you understand the following:

 * **a front-end node** used for logging in, managing files and submitting your jobs to the queue.

 * **several compute nodes** which each contain several GPU devices.

 * all nodes are connected to a **network drive**

## Overview of compute nodes

GPU resources are in high demand, and it can be useful to get an overview of how busy the cluster is at the moment.

!!! example "Try running the following commands to see the traffic right now"

    
    * The command `nodesummary` will print each node, together with a bar chart indicating how much memory, how many CPU's and many GPU's on the node are available.

    * The command `squeue` will print all jobs in the queue.

    * The command `sinfo` will print a list of the partitions and the nodes in the cluster.

## Overview of directories

Become acquinted with the platform's directory structure. Head over to our section [Additional Guides > Directories overview](/ai-cloud/additional-guides/directories-overview/)

## Overview of the Linux CLI

Head over to our section [Additional Guides > Understanding the Linux CLI](/ai-cloud/additional-guides/understanding-linux-cli/) to learn more. Try a few of the commands for your self.


<br>

Now that you've become acquainted with the platform, head over to [** transfer files :octicons-arrow-right-24:**](ai-cloud/getting-started/file-management)
