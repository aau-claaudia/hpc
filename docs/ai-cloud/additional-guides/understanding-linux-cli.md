On this page our goal is to help you understand the most fundamental concepts of operating a Linux server. This page is not designed as a collection of useful commands, and neither is this a tutorial on operating a Linux server. Think of this page as a *concept glossary* that will help you understand how a Linux server works.

After having read this page you should be much better equipped to work on AI Cloud (and other HPC systems).

## :octicons-file-directory-16: Referencing file paths 

The directory `/home/domain/user/subdirectory` can thus be broken up into: `/`, `home`, `domain`, `user`. 
Note that the first `/` is the root, and the following directories are subdirectories to each other.

We can reference file paths in two ways. Suppose we want to list the files in `/home/domain/user/subdirectory`

* **Relative paths:** If we are standing in `/home/domain/user`, we can call `ls -l subdirectory`
    
* **Absolute paths:** If we are standing in a completely different location, we can always target its' absolute path `ls -l /home/domain/user/subdirectory`

## :octicons-command-palette-16: Executing commands and programs

Commands can either be *shell builtins* or *programs*. For the most part it is not important to be able to distinguish between them, but it is important to understand that in most cases commands are programs, which we can execute because the system knows where to find them. In other words: every command is an executable file with a valid filepath on the system (except for *shell builtins* - but don't worry about those).

**This is important to understand because operating an HPC system involves jumping between sessions/environments** (eg. nodes and software containers), whereby the software environment changes, and we may want to confirm that we are indeed calling the desired command (ie. from *the desired path*).

We could print the full path to the `python3` with:

```bash
❯ which python3
/usr/bin/python3
```

#### How the operating system determines the path to the command

When we call a command, the operating system will search for it in the directories in the `$PATH` variable. If there is not a matching executable in one of these directories we can not call the program. If there are multiple matches, the first one will be selected.

```bash
❯ type -a python3
python3 is /usr/bin/python3
python3 is /bin/python3
```

#### How do we target a specific executable?

There are two solutions:

* Referencing the absolute path to the executable. In the example above calling `python3` is equivalent to calling `/usr/bin/python3`. This is the most straight forward solution.

* Adding the directory with the executable to the environment variable `$PATH`, with: `export PATH="/path/to/dir:$PATH"`.

!!! note "Enviroment managing"

    In essence this is also how environment managers like `conda` or `venv` work. However our goal here is to demonstrate how Linux operating systems work - not to make recomendations for working with Python. If you want to activate a Python virtual environment or a Conda environment, please refer to more specific instructions.

## :fontawesome-regular-window-maximize: Processes

Whenever a program (or command) is executed it uses system resources (cpu, gpu, ram, disk) to deliver on the programs instructions. This is called a *proces*.

In Linux operating systems, we can get an overview of all running processes with a program called `top`, and we can view our own processes only with `top -u $USER`. The latter command is especially convenient on a multi user system.

We can use this view to get an indication of what the system is doing under the hood, and wether or not our program has actually started. 

!!! note  "Child processes"
    It should be noted, that is normal for programs to launch one or more child/sister processes, and therefore monitoring the exact resource consumption may not always be straight forward.

!!! note  "Monitoring GPU consumption"

    `top` does not monitor GPU activity. To learn how to do this, read our section [Checking GPU utilisation](/ai-cloud/additional-guides/checking-gpu-utilisation/).

## :fontawesome-solid-window-restore: Sessions

When you log in to the system, you start in an *interactive shell session*. This means that you are *standing* somewhere on a host system, and you can interact with the system by executing commands and viewing their outputs.

Interactive shell sessions are kept alive, for as long as the user keeps it alive. You can exit a shell session with the keybinding ++ctrl+d++ or with the command `exit`.

Sessions can be nested inside each other - meaning that a session can be started from within another session. This is useful to understand because: Whenever we start a job on a compute node with `srun`, we start a new session on the compute node. This session on the compute node is nested inside the session on the front-end node, meaning that it will only run for as long as the parent session is alive.

It's also useful to understand this, because sessions can differ from each other with regards to which variables are loaded or which commmands/programs can be executed. When we understand this, we can work with it - read the sections on Variables and Executing commands on this page.

## :fontawesome-solid-dollar-sign: Variables

A number of variables are loaded into the *session* when you log in to the system. Additional variables can be set by the user in order to set paths or options.

### Working with variables

```bash
env
```

Assign a variable:
```bash
var="hello world"
```

Print the content of a variable:
```bash
❯ echo $var
hello world
```

Notice that after the variable has been assigned, we must reference it with a prepended `$`. When we make the assignment, we must not do this.

Prepending `export` to the assignment makes the variable accessible to child processes (and nested sessions). Suppose we prepended `export` to the assignment of `$var` in a [batch-script](/ai-cloud/getting-started/run-jobs/#__code_5):

```bash
export var="hello world"
```

This makes `$var` accessible on the compute node. We can confirm this by calling `env` or in Python with: `ìmport os ; os.environ.items()`

### Example use cases for variables

* **<u>Control program settings</u>**:

    When we build Singularity containers, we can set the variables [`SINGULARITY_TMPDIR`](https://docs.sylabs.io/guides/3.0/user-guide/build_env.html#temporary-folders) and [`SINGULARITY_CACHEDIR`](https://docs.sylabs.io/guides/3.0/user-guide/build_env.html#cache-folders) to override the default directories for these. This serves as an example of a program, that reads settings from variables. [See these in action here](/ai-cloud/additional-guides/building-your-own-container-image/#downloading-the-container-image).

* **<u>Gather information on the current session</u>**:

    Notice that calling `srun env` (printing all variables in a compute node job), shows a large number of `SLURM` variables. These variables convey information about the current session, and we can use them to gather (or log) details about our job.

* **<u>Increase script readability</u>**:

    Using variables to reference files and directories is good practice, because it increases readability and maintainability:

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

<hr>

