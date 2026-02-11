The CLAAUDIA team is responsible for system administration and user support. We work closely with the infrastructure team in ITS, which takes care of hardware and system maintainance.

It is a priority for us to help our users utilise the platform, and we are therefore happy to help you get started. Don't hesistate to reach out to us if you have any questions (find the "Get Support" button in the top right corner of this page).


## Enforcement of rules

If we find indications of violations of the rules and principles layed out on this page, CLAAUDIA will contact you to learn more about your situation.

As a general rule CLAAUDIA does not cancel jobs without the user's permission. That being said - we do reserve the right to do so, if the situation compromises the platform or service we are able to provide. We will always get in touch with the user.

We also want ask our users not to interfere with our system administration. It is entirely up to CLAAUDIA to make objections to our users and no individual user has the authority to do so. Should you have any concerns, you are very welcome to get in touch with us.


## Distribution of resources

* We enforce a standard quota which allows each user to run 12 simultaneous jobs, with a maximum of 12 GPU's. An unlimited number of jobs can be queued.

* It's possible to run an unlimited number of jobs in *unprivileged mode*. You must however understand, that your jobs can be interrupted if a request is made for the same resources. Once they free up again, your job is automatically requeued. Learn more about this [here](ai-cloud/additional-guides/run-jobs-beyond-the-default-qota).

* In case you are working under a deadline, it's possible to apply for *deadline resources*. This doubles the default quota additional 12 jobs (an additional maximum of 12 GPU's), totalling to 24 simultaneous jobs and 24 GPU's. This option is valid for 14 days, and once granted you can not reapply for another 14 days. Find the application [AI Cloud: Request access to deadline resources](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=22a816638322be5053711d447daad379) and check out [our guide on launching jobs in deadline mode](ai-cloud/additional-guides/run-jobs-beyond-the-default-qota).

* Resarchers with affiliation to the [Pioneer Centre for AI](https://www.aicentre.dk/) can be granted special access to the `aicentre` and `aicentre-a100` partitions. If you are affiliated with this group, speak to your group leader about this. Check out [our guide on utilising these nodes](ai-cloud/additional-guides/run-jobs-on-special-access-nodes/) to learn more.

## Responsible use of the platform

In addition to the default resource limitations that are in place on the platform, we encourage you to use the resources responsibly. We want our users to make not of the following recomendations:

* Always launch your jobs as batch-jobs that require no interference from the user.

* Ensure that your jobs occupy resources only as long as they are needed.

* Do not allocate GPU's do your job, if it does not need them. Run on the CPU partition if possible.

* If you intend to allocate multiple GPU's to your job, it is your responsibility to ensure that your project is able to make use of the increased number of GPU-devices in a meaningful way.

* If possible, we recomend making good use of the scheduler features in Slurm. Launch jobs in periods with low demand - ie. times outside of office hours; on weekends, during holidays, during the night, etc. The parameter `--begin` can be added to your Slurm command for this purpose.

* Keep in mind that AI Cloud is a multi-user system, and that it is entirely possible for one user to destabilize the front-end node by launching resource-intensive operations. Ensuring that we have a stable platform is a shared responsibility.

It should also be noted, that we do recognise that we are a learning institution, and that much of the work carried out on AI Cloud is *learning-by-doing*. We welcome this. Users are encouraged to experiment with features that they do not yet master, and we encourage them to reach out to us if they want our help with utilising the platform.

## Disencouraged use of the platform

### Interactive development sessions

AI Cloud is designed for launching unattended batch jobs, and we thus discourage interactive development sessions. We understand that this can sometimes be necessary for very specific troubleshooting cases, but even this is in most cases preferable to do from within an unattended batch job (launched with `sbatch`). The reason for this is that interactive development sessions have very ineffective utilisation of resources, which inhibits the overall availability of the system.

Interactive development is allowed on [UCloud](/ucloud/).

#### Launching jobs from within interactive session

It is considered bad practice to launch unattended jobs from within interactive shell sessions. This would be opening a job with `srun --pty`, loading the container with `singularity exec image.sif` and then `python3 main.py`. Read our guide [Getting started > Run Jobs](ai-cloud/getting-started/run-jobs/) to learn what to do instead.

#### Interactive development sessions on compute nodes

We do not allow interactive development sessions. By *interactive development* we mean opening an interactive shell session with something like `srun --pty -G 1 singularity --nv <shell/exec> image.sif`, and only occassionally execute commands be that directly from the console or from an IDE like Jupyter Notebook, Spyder or VS Code. This does not guarantee that resources are released automatically, when they are no longer needed, and thus resources are occupied for longer than needed.
