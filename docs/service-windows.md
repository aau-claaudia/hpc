On this page you will find information about the proposed upcoming service windows.

## Proposed schedule of service windows

**Next service window: 11/02/2025**


**2025** 11/02, 13/05, 16/09, 02/12

**2026** 10/02, 12/05, 15/09, 01/12

**2027** 09/02, 11/05, 14/09, 30/11

**2028** 08/02, 09/05, 12/09, 28/11


**We try to minimize the downtime of all systems**


**Time reservation for services: 00:00 to 23:59.**


!!! info "ServiceInfo: Sign up for progress notifications"
    Click this link to go to serviceinfo.dk, then select **Aalborg University**,
    and under the "Abonnér" / "Subscribe" tab you can select **CLAAUDIA**, and
    select *email*, *SMS* or *calendar*, according to your preferences:

     [:octicons-arrow-right-24: Go to ServiceInfo.dk](https://serviceinfo.dk/)


## OpenStack virtual machines
### (Strato and UCloud virtual machines)

**Remember to save your work on Strato and UCloud Virtual Machines
(VMs)**

**Strato: All hosts will be rebooted, and to do this all Strato virtual
machines will be shut off**

If you have active work on your virtual machines that has not been
saved, **please make sure you save your work** by the latest end of 
the day before the service window (Monday). All virtual machines will automatically undergo the
equivalent of shutting down your computer, so any unsaved data will be
lost.

We have reserved the entire day from 00:01 to 23:59, but the time
required to restart hosts once all instances have been shut down is only
a few minutes.

Virtual machines that are running at the start of the window will be
automatically restarted after the host has been rebooted. This includes
all virtual machines on the UCloud platform.

**Strato: All virtual machines should be removed when not in use**

The best practice, if you don't need your VM right away is to 1. Rename
your volume, 2. Delete your instance, and 3. When you need to run that
machine again, just launch a new VM from the volume. This also lets you
change the VM flavour or resize your disk if you need to. Basic rule:
keep your volumes, delete your unused VMs, and only run a VM with the
size you really need right now.

Link to Strato's
web-interface: [https://strato-new.claaudia.aau.dk](https://strato-new.claaudia.aau.dk/)

## AI Cloud

AI-Cloud will be unavailable throughout most of that day and will come
back online towards the end of the workday. 

**AI Cloud: Time limit will be imposed prior to service window**

In the days leading up to the [service
window](https://hpc.aau.dk/terms-and-conditions/),
a time limit will be imposed, which will  prevent you from launching
jobs with end dates that surpass the date of the service window. 

In this
period, you will only be able to launch new jobs, if you add
the `--time` parameter to your Slurm command. If the time parameter is
not set, Slurm assumes you ask for the default maximum time for the
partition. You will thus have to calculate how much time you have before
the service window, and then submit a job with this parameter added. To
submit a job that runs for 1 day and 8 hours, you can simply
add `--time=1-08:00:00` to your Slurm command. 

Additionally you can read
about our recommendations for
using [checkpointing](https://aicloud-docs.claaudia.aau.dk/slurm/#checkpointing) to
work with time limits.
