### The user's home directory

Each time you log in to AI Cloud, you are landed in your user's home directory. This directory serves as the primary location for storing project files and data.

The path to this directory can always be referenced with the variable `$HOME`.

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

The user directory is private by default, and users can there not access your files. In case you need to make files accessible for other users, we recommend putting them in the [Shared project directory](#the-shared-project-directory)

!!! info "Storage quota expansions"
    When users log in to AI Cloud for the first time, a user directory is created for them. These directories are allocated 1 TB of storage by default. This should be plenty for most users, but should you need additional space, it is possible to apply for storage quota expansions for a limited time using our [Storage quota expansions form](https://forms.office.com/e/AjT0GccAPb).
    
### The shared project directory

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

### Local scratch space

A handful of nodes have local storage which can be utilised for faster I/O operations.

  * Learn more about [utilising local node storage](/ai-cloud/additional-guides/local-storage)
<hr>
