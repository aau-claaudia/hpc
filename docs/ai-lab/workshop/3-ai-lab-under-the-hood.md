# AI-LAB under the hood

AI-LAB combines specialized hardware and software to deliver high-performance computing for AI workloads.



<div class="workshop-internal-break" role="separator"></div>


``` mermaid
flowchart LR
  subgraph id1[<p style="font-family: Barlow, sans-serif; font-weight: 800; font-size: 12px; text-transform: uppercase; color: #221a52; letter-spacing: 1px; margin: 5px;">Compute nodes</p>]
  direction TB
  A["<span><img src="/assets/img/server.svg"  width='25' height='25' >ailab-l4-[01-11]</span>"]
  end

  subgraph id2[<p style="font-family: Barlow, sans-serif; font-weight: 800; font-size: 16px; text-transform: uppercase; color: #221a52; letter-spacing: 1px; margin: 10px;">AI-LAB</p>]
  direction TB
  subgraph id3[<p style="font-family: Barlow, sans-serif; font-weight: 800; font-size: 12px; text-transform: uppercase; color: #221a52; letter-spacing: 1px; margin: 5px;">Front-end nodes</p>]
    direction TB
    G["<span><img src="/assets/img/server.svg" width='25' height='25'>ailab-fe[01-02]</span>"]
    end
  id3 --> id1 

  subgraph id4[<p style="font-family: Barlow, sans-serif; font-weight: 800; font-size: 12px; text-transform: uppercase; color: #221a52; letter-spacing: 1px; margin: 5px;">File storage</p>]
    direction TB
    E["<span><img src="/assets/img/server.svg" width='25' height='25'>Ceph</span>"]
    end

  id1 & id3 <--> id4
  end

  F[<span><img src="/assets/img/person.svg" width='25' height='25'>User</span>]-- SSH --> id3

```



<div class="workshop-internal-break" role="separator"></div>


## 🖥️ Hardware Overview

| Component         | Description                                    |
| ----------------- | ---------------------------------------------- |
| **Login Nodes**   | 2 nodes for connecting and submitting jobs     |
| **Compute Nodes** | 11 powerful machines with GPUs                 |
| **GPUs**          | NVIDIA L4 GPUs (8 per node, 24 GB memory each) |
| **Storage**       | Central networked storage via Ceph             |

![](../images/ailab-architecture.png)



<div class="workshop-internal-break" role="separator"></div>


## ⚙️ Software Stack

| Layer      | Tool            | Purpose                                |
| ---------- | --------------- | -------------------------------------- |
| Scheduler  | **Slurm**       | Manages compute resources and queues   |
| Containers | **Singularity** | Isolates applications and dependencies |



<div class="workshop-internal-break" role="separator"></div>


**Next:** [The AI-LAB Workflow →](4-the-ai-lab-workflow.md)
