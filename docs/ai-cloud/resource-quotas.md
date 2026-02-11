### Overview of access modes

| Name          | Max jobs  | Max GPU's    |  Access requirement    | Special notes          |
| ---           | ---       | ---          |  ---                   | ---                    | 
| Default       | 12        | 12           |  None                  |                        |
| Deadline      | 12        | 12           |  Approved applicants   | [Requires application](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=22a816638322be5053711d447daad379)   |
| Unprivileged  | Infinite  | Infinite     |  None                  | Jobs are preemptible   |
| AI Centre     | Infinite  | Infinite     |  AI Center affiliation |                        |

You should know that the quotas stack. This means that once you have submitted the maximum number of jobs that the default quota allows, you can launch additional jobs in *unprivileged mode*, or request access to additional capacity from the *deadline* resources.

### The default quota
We enforce a standard quota which allows each user to run 12 simultaneous jobs, with a maximum of 12 GPU's. An unlimited number of jobs can be queued.

### Deadline access
In case you are working under a deadline, it's possible to apply for deadline resources. This is effectively a doubling of the default quota, which grants you access to additional resources for a limited time - totalling to 24 jobs running simultaneously and 24 GPU's for up to 14 days. Once granted it is not possible to reapply for another 14 says.

This option is not meant to become a permanent solution for research projects with large resource needs - if this is the case with your research project, we encourage you to consider applying for a grant at an external HPC facility. Read more about that oppurtunity on our page for [External HPC](external-hpc/).

* Find the application form: [AI Cloud: Request access to deadline resources](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=22a816638322be5053711d447daad379).
* Learn more about [launching jobs in deadline mode](ai-cloud/additional-guides/run-jobs-beyond-the-default-qota).

### Unprivileged access
It's possible to run an unlimited number of jobs in *unprivileged mode*. You must however understand, that your jobs can be interrupted if a request is made for the same resources. Once they free up again, your job is automatically requeued.

* Learn more about [launching jobs in unprivileged mode](ai-cloud/additional-guides/run-jobs-beyond-the-default-qota).
* Learn more about [launching unprivileged jobs on proprietary nodes](http://localhost:8000/ai-cloud/additional-guides/run-jobs-on-proprietary-nodes/).

### Proprietary nodes

Resarchers with affiliation to the [Pioneer Centre for AI](https://www.aicentre.dk/) can be granted special access to the `aicentre` and `aicentre-a100` partitions. If you are affiliated with this group, speak to your group leader about this.

* Learn more about [launching privileged jobs on proprietary nodes](ai-cloud/additional-guides/run-jobs-on-proprietary-nodes/).
