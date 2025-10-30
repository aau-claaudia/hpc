
## Sessions
Each time you log in to the system, you start an *interactive shell session*.
An interactive shell session is kept alive for as long as you keep it open.
You can exit the session with the command `exit` or by pressing ++ctrl+d++.

## File structure

The Linux file structure is structured in a tree-like fashion. Every file and directory on the system can be referenced absolutely or relatively to the current working directory.

### The file tree

The directory `/home/domain/user/subdirectory` can thus be broken up into: `/`, `home`, `domain`, `user`. 

Note that the first `/` is the root, and the following directories are subdirectories to each other.

### Referencing paths

We can reference file paths in two ways. Suppose we want to list the files in `/home/domain/user/subdirectory`

* **Relatively:** If we are standing in `user`, we can call `ls -l subdirectory`
    
* **Absolutely:** Regardless of where we are standing, we can `ls -l /home/domain/user/subdirectory`

## Commands

* `ls`: list files in the current directory
* `ls -al`: list all files in the current directory (including dotfiles).
* `pwd`: print the current working directory
* `cd`: change directory (if no input is given, go to `$HOME`)
* `cd mydir`: change directory to `mydir` (if no input is given, go to `$HOME`)
* `mkdir`: create (make) directory
* `rm`: remove file
* `rm -r`: remove directory
* `rmdir`: remove directory
* `cp`: copy file
* `cp -r`: copy file (or directory) *recursively* (including all it's subdirectories)
* `mv target-file target-location`: move file
* `mv old-filename new-filename`: rename file (think about this, as if you are editing the filepath)
* `touch filename`: create an empty file
* `cat filename`: print file content
* `head filename`: print the first 5 lines of a file
* `head -n 2 filename`: print the first 2 lines of a file
* `tail filename`: print the last 5 lines of a file
* `tail -n 2 filename`: print the last 2 lines of a file
* `tail -f filename`: print the last 5 lines of a file *continously* (follow newly written lines)

!!! tip "Tips and tricks"

    * Use tab completion as much as you can. This is both easier and decreases the risk of mistyping. 

    * Avoid using spaces when naming files and directories.

## Variables

Variables are attached to your *shell session* and are stored in memory.

Some variables are set, when you log into your session, eg. `$HOME`, `$USER`, `$PATH`. Others can be set by the user to interact with programs, or to be referenced in scripts.

Call the command `env` to see which variables are loaded into your current shell session.

Variable assignment can be done in the following manner:
```bash
var="hello world"
```

Variables can be printed with
```
❯ echo $var
hello world
```

Prepending `export` to the assignment makes the variable accessible to child processes. This can be useful if you are delegating a job to a compute node.

## Additional info on calling commands

Commands can either be *shell builtins* or *programs*. This can be checked with the command `type`:

```
❯ type echo
echo is a shell builtin
```
```
❯ type ls
ls is /bin/ls
```
For the most part it is not important to be able to distinguish between them, but it is important to understand that in most cases commands are programs, which we can execute because the system knows where to find them.

This is important to understand because operating an HPC system involves jumping between nodes and software containers, whereby the software environment changes, and we may want to confirm that we are indeed calling the correct command or the correct path.

In Linux, programs can be made available in two ways:

**1: We can call them because they are located in one of the directories in the `$PATH` variable.**

Consider the following:

 * We can call `squeue`
 * `which squeue` will return `/usr/local/bin/squeue`
 * `echo $PATH` will verify that `/usr/local/bin` is indeed in `$PATH`

**2: We can call them by referencing their paths.**

If a program is not in `$PATH`, we can execute it by referencing it's path:

* Calling `/bin/ls` is equivalent to calling `ls`
* If we are standing in `/bin`, calling `./ls` is equivalent to calling `ls`.

This can be useful for calling a specific version of a program or for verifying that you are indeed calling the program, you intend to call.
