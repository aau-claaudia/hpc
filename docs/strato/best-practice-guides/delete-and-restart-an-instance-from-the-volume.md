This is essentially a 3 step process.

1. Rename the volume attached to your instance / server.
2. Delete your instance
3. Start a new instance and choose a volume rather than an image as the "Source".

## Method 1: How to Shut off, delete and reinstate an instance from a volume

### Preparation and deletion of an instance
1.	Browse to the `>Compute >>Instances` section, and on the relevant instance click the instance name.
	1.	Make a note of the volume number.
	2.	Copy and paste the volume number somewhere you can find it for future reference.
2.	Browse to the `>Volumes >>Volumes` section and rename the volume noted in 1.2 to a name you can identify later. (For example, RStudio server volume)
3.	Browse to the `>Compute >>Instances` section, and on the relevant instance click the dropdown-menu,
	1.	Select `Shut Off Instance`, to make sure that all operations are properly shut down before deleting.
4.	Browse to the `>Compute >>Instances` section, and on the relevant instance click the dropdown-menu,
	1.	Select Delete Instance. This will delete the instance.
5.	Browse to `>Volumes >>Volumes` and check that the volume is still there.


### Re-launching the instance:
6.	Browse to the `>Volumes >>Volumes` section.
	1.	Find the volume noted in point 3, and then click the dropdown menu button at Edit Volume:
7.	Select Launch as Instance.
8.	Choose the most relevant / appropriate flavour. You here have the option of changing flavours.
9.	NB when you select the `>Source >>Boot source`, you must select Volume. 
	1.	You will need to click the up arrow alongside the volume noted in point 3 to use it as the boot source.
	2.	Follow all other instance setup instructions as noted in the Quick guide for the network settings, keypairs etc., and launch the instance.
10.	Check that the instance has launched and note the new IP address.
11.	Access your volume via the terminal (ssh ubuntu@…. ), here you will need to use the new IP address.
12.	Your machine should run as before, but with the flavour most recently selected.

NOTE: Windows users may need to update PuTTy settings.



## Method 2: How to Shut off, delete and reinstate an instance where “Delete volume on Instance delete” is activated (set to yes).

*Warning: This method is experimental and includes a possible failsafe to prevent automatic deletion of volume, so proceed with caution: We have tested this to work, but we cannot guarantee that it will prevent the deletion of the volume.
At present, creating a snapshot of a volume prevents the automatic deletion of the volume when the instance is deleted. A snapshot is NOT a copy or image of a disk, and thus depends on the disk still existing. If you are in doubt about whether you have activated this setting, you should be able to use the following process to delete your instances safely:*

### Preparation and deletion of an instance
1.	Browse to the `>Compute >>Instances` section, and on the relevant instance click the instance name.
1.	Make a note of the volume number.
2.	Copy and paste the volume number somewhere you can find it for future reference.
2.	Browse to the `>Volumes >>Volumes` section and rename the instance noted in 1.2 to a name you can identify later. (For example RStudio server volume)
3.	Browse to the `>Compute >>Instances` section, and on the relevant instance click the dropdown-menu,
1.	Select Shut Off Instance, to make sure that all operations are properly shut down before deleting.
4.	Browse to `>Volumes >>Volumes`, and for the relevant volume:
1.	Click the dropdown-box and select Create snapshot.
2.	Choose an appropriate name. (For example Temporary snapshot of RStudio server volume), and create the snapshot
3.	Check that the snapshot is listed in the `>Volumes >>Snapshots` section.
5.	Browse to the `>Compute >>Instances` section, and on the relevant instance click the dropdown-menu,
1.	Select Delete Instance. This will delete the instance, you can now go ahead and delete the snapshot.
6.	Browse to `>Volumes >>Volumes` and check that the volume is still there.
7.	Browse to `>Volumes >>Snapshots` and click the dropdown box alongside the relevant snapshot, then click the Delete snapshot option to delete the snapshot.

### Re-launching the instance:
8.	Browse to the `>Volumes >>Volumes` section.
1.	Find the volume noted in point 3, and then click the dropdown menu button at Edit Volume:
9.	Select Launch as Instance.
10.	Choose the most relevant / appropriate flavour. You have the option of changing flavours.
11.	NB when you select the `>Source >>Boot` source, you must select Volume. 
1.	You will need to click the up arrow alongside the volume noted in point 3 to use it as the boot source.
2.	Follow all other instance setup instructions as noted in the Quick guide for the network settings, keypairs etc., and launch the instance.
12.	Check that the instance has launched and note the new IP address.
13.	Access your volume via the terminal (ssh ubuntu@…. ), here you will need to use the new IP address.
14.	Your machine should run as before, but with the flavour most recently selected.

NOTE: Windows users may need to update PuTTy settings.

## Additional Benefits:
*	This solves the current inability to resize an instance.
*	Every time you need to make changes to the installation on the volume, you can spin up a machine that is the perfect size for the task.
*	This mitigates the problems encountered when trying to shelve a GPU instance. (Launching a new instance from a volume does not require that the identical physical device is attached to the instance, as is the case when trying to shelve an instance).
*	You will get an idea of how many volumes you have allocated to your user and can clean up your storage.

## Note on volume sizes
Volumes can always be extended later (but not reduced in size) so any image or snapshot creation intended for sharing or as templates should be set to the minimum viable size.

