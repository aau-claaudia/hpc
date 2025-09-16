
<!-- !!! warning "Next Service window: 13th and 15th of May 2025" -->

Four times a year, all of our platforms are subject to *service windows* where changes and security upgrades are implemented.
During these, we reserve an entire day for maintainance of the systems.

It should be expected that the platforms are offline for the entire day from 00:01 until 23:59 - but they may come online by the end of the days, as the work is finished.

## Schedule

A service window will take place on the following dates:

<div class="grid" markdown>

<div markdown>

**AI Cloud, Strato, UCloud VM's & UCloud Kubernetes**

| 2025  | 2026  | 2027  | 2028  |
| ---   | ---   | ---   | ---   |
| <s>11/02</s> | 10/02 | 09/02 | 08/02 |
| <s>13/05</s> | 12/05 | 11/05 | 09/05 |
| <span style="background:#211a52; color:white; font-weight:bold; border:2px solid #211a52; border-radius:4px; padding:2px 8px; display:inline-block;">16/09</span> | 15/09 | 14/09 | 12/09 |
| 02/12 | 01/12 | 30/11 | 28/11 |

</div>

<div markdown>

**AI-LAB**

| 2025  | 2026  | 2027  | 2028  |
| ---   | ---   | ---   | ---   |
| <s>13/02</s> | 12/02 | 11/02 | 10/02 |
| <s>15/05</s> | 14/05 | 13/05 | 11/05 |
| <span style="background:#211a52; color:white; font-weight:bold; border:2px solid #211a52; border-radius:4px; padding:2px 8px; display:inline-block;">18/09</span> | 17/09 | 16/09 | 14/09 |
| 04/12 | 03/12 | 02/12 | 30/11 |

</div>

</div>

!!! info "Sign up for notifications on serviceinfo.dk"
    Click this link to go to serviceinfo.dk. Then select *Aalborg University*,
    and under the tab *Subscribe* (or *Abonnér*), select *CLAAUDIA*.
    Select *email*, *SMS* or *calendar*, according to your preferences:

     [:octicons-arrow-right-24: Go to ServiceInfo.dk](https://serviceinfo.dk/)

### Platform specific information

## Strato and UCloud virtual machines

**Be sure to save your work** no later than the end of the day before the service window begins, as all virtual machines will be automatically shut down during the service window and any unsaved data will be lost.

!!! warning "New Usage Management Process - Effective 16th September 2025"
    
    **1. Servers will NOT restart automatically after service windows**
        - All servers in the AAU availability zone will be shut down during service windows and will not restart automatically, unless they have been registered for automatic restart before the service window.
        - You can easily restart your servers manually after the service window.

    **2. Automatic server resizing after 48 hours of inactivity**
        - Servers that remain shut down for more than 48 hours will be automatically resized to the smallest CPU configuration.
        - You will receive a notification when your instance has been resized.

    **3. Automatic server deletion after 30 days of inactivity**
        - Servers that remain shut down for 30 days will be permanently deleted, but their volumes will be preserved.
        - You will be notified in advance about any affected instances.

    **4. Unused volume cleanup**
        - Volumes not attached to any server for 30 days will be deleted.
        - A notification will be sent before deletion.

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



## UCloud (AAU/K8s)

The UCloud (AAU/K8s) cluster will be unavailable for the entire duration of the service window and may become available again by the end of the day. While it may be technically possible to start jobs on the day of the service window, please note that any running jobs will be terminated as part of the scheduled maintenance activities performed by the administrators. We recommend planning your work accordingly to avoid interruptions.


