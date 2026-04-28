---
icon: lucide/server-cog
---

# UCloud datacenter migration

The migration deadline has now passed, and UCloud will remain offline until the new datacenter is established on **May 4, 2026**.

## Timeline

| Date | Status |
|------|--------|
| ~~**Before April 27, 2026 at 08:00**~~ *(surpassed)* | ~~Final deadline for moving data out of `AAU/K8` and `AAU/VM`.~~ |
| **April 27 to May 4, 2026** *(ongoing)* | Full UCloud downtime during the migration. |
| **May 4, 2026** | Expected reopening of UCloud in the new SDU datacenter. |


## What users should know

There is no action to take inside UCloud right now because the platform is offline.

When the new datacenter opens, all project data stored in `u1-cephfs` will be available as before. If you have not yet applied for the new compute resources `cpu-amd-zen5` and `gpu-nvidia-b200`, you must do so before you can use them. The application procedure is the same as usual as shown on the [How to access UCloud page](/ucloud/how-to-access/).

For technical details about the new hardware and machine types, see the [official SDU migration guide](https://docs.cloud.sdu.dk/intro/new_datacenter.html#sphx-glr-new-datacenter).

## AAU datacenters are now closed

The old AAU datacenters, `AAU/VM` and `AAU/K8`, are now closed. As a result, any data and services that were hosted in these environments are no longer accessible.


---
> ###  UCloud Service status
>
> Stay updated on UCloud's current status by visiting the [UCloud status page](https://status.cloud.sdu.dk/).
---