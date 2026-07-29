## Home directory

Each time you log in to AI Cloud, you are landed in your user's home directory. This directory serves as the primary location for storing project files and data. The path to this directory can always be referenced with the variable `$HOME`.

<div class="tree">
    <ul>
    <li><i class="fa fa-folder-open"></i> / <span>root</span>
        <ul>
        <li><i class="fa fa-folder-open"></i> home <span> home directories</span>
            <ul>
            <li><i class="fa fa-folder-open"></i> domain <span>e.g es.aau.dk</span>
                <ul>
                    <li><i class="fa fa-folder"></i> user <span>your user directory</span></li>
                </ul>
            </li>
            </ul>
        </li>
        </ul>
    </li>
    </ul>
</div>

The user directory is private by default, and users can there not access your files. In case you need to make files accessible for other users, we recommend putting them in a [Shared project directory](#the-shared-project-directory)

!!! info "Storage quota expansions"
    When users log in to AI Cloud for the first time, a user directory is created for them. These directories are allocated 1 TB of storage by default. This should be plenty for most users, but should you need additional space, it is possible to apply for storage quota expansions for a limited time using our [Storage quota expansions form](https://forms.office.com/e/AjT0GccAPb).
    
## Shared project directories

AI Cloud fosters collaborative work through shared project directories in `/home/project`:

<div class="tree">
    <ul>
    <li><i class="fa fa-folder-open"></i> /home <span>AI Cloud's file system</span>
        <ul>
        <li><i class="fa fa-folder-open"></i> project <span>shared project directories</span>
            <ul>
            <li><i class="fa fa-folder"></i> my_shared_project
            </li>
            </ul>
        </li>
        </ul>
    </li>
    </ul>
</div>

Users are welcome to create directories for their groups themselves, but they are encouraged to name the directories in a meaningful way (ie. after your group or project name).

Go in to the project directory
```
cd /home/project
```
Before going ahead and creating a directory for group project, please consider naming the directory in a meaningful manner (ie. after your group or research project). A project directory can be created in the following manner (swap out `<name>` for the actual name of your project).
```
mkdir <name> 
```
Please remember, that these directories should be deleted when your project is finished, and you no longer need them. They are not intended for long term data storage.

## Local storage

A handful of compute nodes have local scratch space (as opposed to network drives), which can be utilised for faster I/O operations. These storage volumes are physically attached to each individual compute nodes, and can only be accessed from that specific node.

The nodes in question are:

* `i256-a40-[01-02]`: 6.4 TB total
* `nv-ai-[02-03]`:  30 TB total
* `nv-ai-04`:  14 TB total

!!! warning
    This space is not intended for long term storage. Please remove your files when you are finished. We reserve the right to delete directories that have been left untouched for 90 days.

### Create a directory

In order to make use of this drive, we need to identify which node we want to work on.

In this example, we will be targetting `nv-ai-02`.

The following command will create a directory for you on the network drive, and set the permissions so the directory is only accessible for you.

```
sbatch -w nv-ai-02 --wrap="mkdir -p /raid/$USER && chmod o= /raid/$USER"
```

### File transfer

In order to be able to transfer our files, we will need to be able to SSH in to the node. We can only do this if we have a job running on the node.

We therefore launch job that runs in the background for 15 minutes (900 seconds) - or however long you believe it will take for you to transfer your files. If you have a job running already, this is not necessary.


```
sbatch -w nv-ai-02 --wrap="sleep 900"
```

The hostname will always be the name of the node with `srv.aau.dk` added to the end.

Now transfer your files:
```
scp xs98kl@domain.aau.dk@nv-ai-02.srv.aau.dk:/raid/xs98kl@domain.aau.dk
```

Other file transfer methods (as described in the [File transfer](../getting-started/file-transfer.md)) section will also work. Just change the hostname from `ai-fe02.srv.aau.dk` to e.g. `nv-ai-03.srv.aau.dk`.

Remember to stay mindful of your fellow resarchers, and cancel the job you created for the file transfer when you are finished.


### Working with the local scratch space

Given that you have acquired a job allocation on the specific node you are working on, just reference this newly created directory.

There is no need to bind the directory to your container environment.

## Remote storage

We do generally support mounting remote network drives on AI Cloud. Mounting remote drives and making them available on all compute nodes, requires a considerable effort from our infrastructure and network departments. In addition to that the read/write speeeds from remote drives would be bottlenecked by the network routing, which would impair GPU performance.

Instead we recomend transferring files between locations. In case your file transfer is very large, or if there are any special requirements - you are welcome to contact CLAAUDIA at [serviceportal.aau.dk](https://serviceportal.aau.dk).
