Understanding the Linux command line environment will greatly help you succeed on AI Cloud.

On this page we will go straight to the point, and help you understand what is going on.

<hr>

## :octicons-file-directory-16: File paths 


The directory `/home/domain/user/subdirectory` can thus be broken up into: `/`, `home`, `domain`, `user`. 
Note that the first `/` is the root, and the following directories are subdirectories to each other.

### Referencing paths

We can reference file paths in two ways. Suppose we want to list the files in `/home/domain/user/subdirectory`

* **Relative paths:** If we are standing in `user`, we can call `ls -l subdirectory`
    
* **Absolute paths:** Regardless of where we are standing, we can `ls -l /home/domain/user/subdirectory`

<hr>

## :octicons-command-palette-16: Commands 

Commands can either be *shell builtins* or *programs*. For the most part it is not important to be able to distinguish between them, but it is important to understand that in most cases commands are programs, which we can execute because the system knows where to find them.

This is important to understand because operating an HPC system involves jumping between shell environments (nodes and software containers), whereby the software environment changes, and we may want to confirm that we are indeed calling the correct command or the correct path.

In Linux, programs can be made available in two ways:

**We can call them because they are located in one of the directories in the `$PATH` variable.**

Consider the following:

 * We can call `squeue`
 * `which squeue` will return `/usr/local/bin/squeue`
 * `echo $PATH` will verify that `/usr/local/bin` is indeed in `$PATH`

**We can call them by referencing their paths.**

If a program is not in `$PATH`, we can execute it by referencing it's path:

* Calling `/bin/ls` is equivalent to calling `ls`
* If we are standing in `/bin`, calling `./ls` is equivalent to calling `ls`.

This can be useful for calling a specific version of a program or for verifying that you are indeed calling the program, you intend to call.

!!! example "Use cases for this knowledge: Confirm which Python executable you are calling"

    When you are setting up a new software environment and you are unsure if you have loaded the correct python environment, you can use `which python3` to confirm which executable you are referencing. If this does not print the directory you expected, you may have found your problem. The easiest and most straight-forward solution to this, would be to reference the file path to the Python executable.

<hr>

## :fontawesome-solid-dollar-sign: Variables

A number of variables are loaded into the *session* when you log in to the system. Additional variables can be set by the user in order to set paths or options.

#### Print a list of all variables loaded into the session:

```bash
env
```

#### Assign a variable:
```bash
var="hello world"
```

#### Print the content of a variable:

```bash
❯ echo $var
hello world
```

Notice that after the variable has been assigned, we must reference it with a prepended `$`. When we make the assignment, we must not do this.

#### Exporting variables

Prepending `export` to the assignment makes the variable accessible to child processes (and nested sessions). Suppose we prepended `export` to the assignment of `$var` in a batch-script:

```bash
export var="hello world"
```

This makes `$var` accessible on the compute node. We can confirm this by calling `env` or in Python with: `ìmport os ; os.environ.items()`


!!! example "Use case for variables: Control a program"

    When we build Singularity containers, we can set the variables [`SINGULARITY_TMPDIR`](https://docs.sylabs.io/guides/3.0/user-guide/build_env.html#temporary-folders) and [`SINGULARITY_CACHEDIR`](https://docs.sylabs.io/guides/3.0/user-guide/build_env.html#cache-folders) to override the default directories for these. This serves as an example of a program, that reads settings from variables.

    [See these in action here](/ai-cloud/additional-guides/building-your-own-container-image/#downloading-the-container-image).


!!! example "Use case for variables: Increase script readability"

    Using variables to reference files and directories is good practice, because it increases readability and maintainability.

    ```
    # Project directory
    project_dir=/home/domain/user/project_1    

    # The container image we want to launch:
    container_image="$project_dir/pytorch_25.04.sif"

    # The file we want to process on the compute node:
    file="$project_dir/is-available.py"

    # Execute job
    srun singularity exec --nv $container_image python3 $file
    ```


!!! example "Use case for variables: gather information on the current session"

    Notice that calling `srun env` (printing all variables in a compute node job), shows a large number of `SLURM` variables. These variables convey information about the current session, and we can use them to gather details about our job.

<hr>

## :fontawesome-solid-window-restore: Sessions

When you log in to the system, you start in an *interactive shell session*. This means that you are *standing* inside the session and that you can either execute commands or (in case a script is running) view the printed command outputs.

Interactive shell sessions are kept alive, for as long as the user keeps it alive. You can exit a shell session with the command `exit` or with the keybinding ++ctrl+d++.


#### Nested sessions

Sessions can be nested, meaning that a session can be started inside a session, which is running inside a separate session, etc. 

!!! example "Use cases for this knowledge: Understand your environment"

    This is useful to understand because: When we start a job on a compute node with `srun`, we start a new session on the compute node. This session is nested inside the session on the front-end node.

    We must understand that nested session is dependent on another session - which is why [we prefer to launch jobs with `sbatch`](/ai-cloud/getting-started/run-jobs/#which-one-to-use-srun-vs-sbatch)

    This also has implications for the environment variables, we can access. If we want to access them, we must `export`. We must also recognise, that they may be changed when switching between environments (nodes or containers).

<hr>


## :fontawesome-regular-window-maximize: Processes

Each time a program is launched or a command is executed - a new process is launched. By identifying the process we can see how much memory and cpu is being used by the process. It should be noted however that processes will often launch one or more child (or sister) processes, and monitoring resource consumption is not always straight forward.

!!! example "Use cases for this knowledge: Monitor active processes and their resource consumtion"

    We can get a list of running processes with `top` or only our own processes with `top -u $USER`.

    Press ++m++ to sort by memory consumption, and ++p++ to sort by cpu consumption.

    This can be used to see if your job is doing anything.

    In `top` - the parameter `load average` will tell about how stressed the node currently is.

