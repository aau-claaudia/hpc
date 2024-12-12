## System administration
The CLAAUDIA team is responsible for system administration and support. We work closely with the infrastructure team in ITS on maintainance of the system.

The overarching principle in our ressource administration is that we aim to strike a balance between high ressource utilisation, while still leaving the majority of users with the feeling that they can get their work done on the platform.

### Violations
If we find indications of violations of these principles, CLAAUDIA will contact you to learn more about your situation.

In exceptional cases, if we are unable to reach you, or if your jobs significantly disrupt the system (e.g., submitting an excessive number of jobs, monopolizing all cluster resources, or does not utilizing the cluster correctly), we may be forced to terminate the jobs to ensure fair usage for all users.

## Ressource consumption
The overall demand for GPU ressources fluctuates throughout the year, and we understand that demand is also dependent on the schedule of the individual student. We therefore prefer not to set a fixed limit on how many ressources an individual student can consume, as there may be times where they have a legitimate reason for high consumption. Instead we ask our users to be mindful of the overall supply, by making frequent asssesments of the queue.

Responsible ressource consumption also involves taking care with multi-GPU allocations. We encourage our users to experiment with this, but they should take great care to test their applications in order to verify that they can indeed make use of the ressources allocated to their jobs.

If possible, we recomend making good use of times with low consumption - ie. times outside of office hours; on weekends, during holidays, during the night, etc. The parameter `--begin` can be added to your Slurm command for this purpose.

## Not allowed
AI-LAB is designed for processing GPU-demanding batch jobs, that can be executed without the need for user interaction.

### Interactive development sessions
By *interactive development* we mean opening jobs, where you have a GPU available to you, but you only ocassinally run commands on the GPU. This results in a very ineffective utilisation of the GPU's, and decreases overall availability. Examples of interactive development session, could be connecting a Jupyter Notebook, Spyder, VS Code to a compute node.

Interactive development is allowed on [UCloud](../../ucloud/index.md).

### CPU demanding operations
If your application can not make use of the GPU's - or does not require one, AI-LAB is not the correct platform. Instead we recomend making use of one of our other computing platforms. Have a look around this website, or [contact CLAAUDIA for guidance](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=34e8536083cfc21053711d447daad30a) on more suitable alternatives.