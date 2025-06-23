
<!-- !!! warning "Next Service window: 13th and 15th of May 2025" -->

Four times a year, all of our platforms are subject to *service windows* where changes and security upgrades are implemented.
During these, we reserve an entire day for maintainance of the systems.

It should be expected that the platforms are offline for the entire day from 00:01 until 23:59 - but they may come online by the end of the days, as the work is finished.

## Schedule

A service window for **AI Cloud, Strato, UCloud VM's** and **UCloud Kubernetes** will take place on the following dates:

| 2025  | 2026  | 2027  | 2028  |
| ---   | ---   | ---   | ---   |
| 11/02 | 10/02 | 09/02 | 08/02 |
| 13/05 | 12/05 | 11/05 | 09/05 |
| 16/09 | 15/09 | 14/09 | 12/09 |
| 02/12 | 01/12 | 30/11 | 28/11 |

A service window for **AI-LAB** will take place on the following dates:

| 2025  | 2026  | 2027  | 2028  |
| ---   | ---   | ---   | ---   |
| 13/02 | 12/02 | 11/02 | 10/02 |
| 15/05 | 14/05 | 13/05 | 11/05 |
| 18/09 | 17/09 | 16/09 | 14/09 |
| 04/12 | 03/12 | 02/12 | 30/11 |

!!! info "Sign up for notifications on serviceinfo.dk"
    Click this link to go to serviceinfo.dk. Then select *Aalborg University*,
    and under the tab *Subscribe* (or *Abonnér*), select *CLAAUDIA*.
    Select *email*, *SMS* or *calendar*, according to your preferences:

     [:octicons-arrow-right-24: Go to ServiceInfo.dk](https://serviceinfo.dk/)

### Platform specific information

## Strato and UCloud virtual machines

**Remember to save your work on Strato and UCloud Virtual Machines (VMs).**  All hosts will be rebooted, and to do this all Strato virtual machines will be shut off
If you have active work on your virtual machines that has not been saved. 

**Please make sure you save your work** by the latest end of 
the day before the service window. All virtual machines will automatically undergo the
equivalent of shutting down your computer, so any unsaved data will be
lost.

Virtual machines that are running at the start of the window will be
automatically restarted after the host has been rebooted. This includes
all virtual machines on the UCloud platform.

**All virtual machines should be removed when not in use.** 
Basic rule: keep your volumes, delete your unused VMs, and only run a VM with the size you really need right now.
Please consult the page ['Delete and restart an instance from the volume'](strato/best-practice-guides/delete-and-restart-an-instance-from-the-volume/)
for instructions on how to do this.

Link to Strato's
web-interface: [strato-new.claaudia.aau.dk](https://strato-new.claaudia.aau.dk/)



## AI Cloud

In the days leading up to the service window, a reservation will be put in place for the entire cluster. The entirety of the cluster will therefore be unavailable for that day, but may come back online by the end of the day.

**You can still submit jobs in the days leading up to the service window.**
Since the `batch` and `prioritized` partitions have time limits of 12 hours and 6 days respectively, you will only be able to launch new jobs if you add the `--time` parameter to your Slurm command. If you do not set this parameter, and there are 5 days until the day of the service window, your job will not start until after the service window. You will thus need to calculate how much time there is left, and then submit the job with this parameter added. 

To submit a job that runs for 1 day and 8 hours, you can simply add `--time=1-08:00:00` to your Slurm command. 

Additionally you can read about our recommendations for using [checkpointing](ai-lab/additional-guides/requeuing-and-checkpointing/) to work with time limits.


## AI-LAB

In the days leading up to the service window, a time limit will be imposed, which will prevent you from launching jobs with end dates that surpass the date of the service window. 

In this period, you will only be able to launch new jobs, if you add the `--time` parameter to your Slurm command. If the time parameter is not included, Slurm assumes you ask for the default maximum time for the partition. You will thus have to calculate how much time you have before the service window, and then submit a job with this parameter added. 

To submit a job that runs for 12 hours, you should add: `--time=12:00:00`. Not setting the `--time` parameter will place your job in the queue, where it will wait until the service window has been completed.

**IMPORTANT:** You can still run jobs in the days leading up to the service window

If you have any questions, please open a case with us on [serviceportal.aau.dk](https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad001310e)