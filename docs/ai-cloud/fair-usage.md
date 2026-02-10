
The CLAAUDIA team is responsible for system administration and user support. We work closely with the infrastructure team in ITS.

It is a priority for us to help our users utilise the platform, and we are therefore happy to help you get started. If you are 

We are here to serve our users, and we are therefore always happy to receive any questions.

### Distribution of resources

* We enforce a standard quota which allows each user to run 12 simultaneous jobs, with a maximum of 12 GPU's. An unlimited number of jobs can be queued.

* It's possible to run an unlimited number of jobs in *unprivileged mode*. You must however understand, that your jobs can be interrupted if a request is made for the same resources. Once they free up again, your job is automatically requeued.

* In case you are working under a deadline, it's possible to apply for *deadline resources*. This doubles the default quota additional 12 jobs (an additional maximum of 12 GPU's), totalling to 24 simultaneous jobs and 24 GPU's. This option is valid for 14 days, and once granted you can not reapply for another 14 days. Find the application [AI Cloud: Request access to deadline resources](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=22a816638322be5053711d447daad379)

* Resarchers with affiliation to the [Pioneer Centre for AI](https://www.aicentre.dk/) can be granted special access to the `aicentre` and `aicentre-a100` partitions. If you are affiliated with this group, speak to your group leader about this.

### Responsible use of resources 

We do recognise that we are a learning institution, and that much of the work carried out on AI Cloud is *learning-by-doing*. Users are encouraged to experiment with features that they do not yet master, and we encourage them to reach out to us if they want our help with utilising the platform.

AI Cloud is intended for gpu-demanding workloads, that can be executed without the need for user interaction.

* Wraps their software in a Singularity container

* Runs a GPU-demanding workload as a batch job, that requires no interference from the user.

* Occupies GPU-resources for only as long as they are needed.

* A platform experience that is characterised by stability and predictability.


### What we expect from our users

We therefore want to ask our users to be mindful of their own resource consumption. AI Cloud is a multi-user system, where the stability of the platform and the supply of resources is a shared responsibility between you as an individual user, all other users and CLAAUDIA/ITS.

We also want ask our users, not to interfere with our system administration. It is entirely up to CLAAUDIA to make objections to our users and no individual user has the authority to do so. Should you have any concerns, you are very welcome to get in touch with us.

### Violations

If we find indications of violations of the rules and principles layed out on this page, CLAAUDIA will contact you to learn more about your situation.

As a general rule CLAAUDIA does not cancel jobs without the user's permission. That being said - we do reserve the right to do so, if the situation compromises the platform or service we are able to provide. We will always get in touch with the user.

### Responsible resource consumption


* **Take care with multi-gpu allocations** Responsible ressource consumption also involves taking care with multi-GPU allocations. We encourage our users to experiment with this, but they should take great care to test their applications in order to verify that they can indeed make use of the ressources allocated to their jobs.

* If possible, we recomend making good use of times with low consumption - ie. times outside of office hours; on weekends, during holidays, during the night, etc. The parameter `--begin` can be added to your Slurm command for this purpose.



!!! warning "VS Code"

    Increasingly we observ that users are connecting to the server with editors like VS Code (and forks thereof, eg. *Cursor* )


!!! warning "Low or "

    Once resources have been allocated to your job.. This is to ensure  availability.


!!! failure "Disallowed"

AI Cloud is designed for processing GPU-demanding batch jobs, that can be executed without the need for user interaction. To ensure that this 



!!! failure "Interactive development sessions"

    By *interactive development* we mean opening jobs, where you have a GPU available to you, but you only ocassinally run commands on the GPU. This results in a very ineffective utilisation of the GPU's, risks  and decreases overall availability. Examples of interactive development session, could be connecting a Jupyter Notebook, Spyder, VS Code to a compute node. 
    
    Launching interactive jobs directly in the console is not allowed either - this could be something like: `srun --pty -G 1 singularity --nv shell`. Going in to an interactive session on a compute node, before launching your job will not release the resources automatically, when they are finished.

    Interactive development is allowed on [UCloud](/ucloud/).

    
    It can be useful in certain situations, when we are debugging something


    It is not very good practice to start jobs from within interactive shell sessions (using `srun --pty` with `singularity shell` or `bash -l`).
    
    This will start a job that will run until it reaches the time limit, and therefore you will risk occupying resources for longer than needed, and consequently preventing others from putting these to good use.

!!! failure "Non-GPU demanding applications"

    If your application can not make use of the GPU's (or does not require one) - AI Cloud is not the correct platform for your job. We refer to UCloud or LUMI for these purposes.

    Have a look around this website, or [contact CLAAUDIA for guidance](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=34e8536083cfc21053711d447daad30a) on the alternatives.

!!! failure "Attempting to mount external drives"

    Don't.
