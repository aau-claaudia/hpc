# Git documentation process

This document provides a guide to editing our documentation using git locally, together with the hpc.aau.dk Github repo

## Clone the Github repo

Navigate to the location on your local machine where you want the repo to be stored.

```bash
cd /path_where_you_want_the_repo/
```

Then clone the hpc.aau.dk repo. 

```bash
git clone https://github.com/aau-claaudia/hpc/
```

### If returning to an older repo on your machine, check that you have the most up to date version of the main branch

```bash
git checkout main
git pull
```

- You should also check what branches you have locally and clean up or delete any unused branches.

## Create a new branch and switch over to it

```bash
git checkout -b newbranchname
```
or using the longhand option

```bash
git branch newbranchname
git checkout newbranchname
```


For now everything will exist on only on a local branch. 

### Check which branch you are on and what changes have been made

```bash
git branch
```
You can now edit the files that you wish to work on in the branch.

## Prepare to commit and commit the changes to the online branch.

Check the status of the branch you are in

```bash
git status
```

This should display all new files and all files that have been modified in the branch and not yet committed.

The files that you wish to include in your commit should then be added.

### Add the files that should be included in the commit

This can be done in bulk in 2 ways, for the current directory using
```bash
git add .
```

or, for the entire working directory using 

```bash
git add —all
```
Alternatively individual files can be added to the commit by specifying them as follows:

```bash
git add docs/guides/openstack_guides/delete_instance_launch_from_volume.md
git add mkdocs.yml
git add docs/index.md
```

### Commit the changes with a message to indicate the nature of changes

```bash
git commit -m "New guide for deleting instances and restarting from volume"
```


## Push the branch and changes

Once the branch has been created, remember to push it to the web and set the origin to the web based version.

This will allow you to see the branch on the web.

```bash
git push --set-upstream origin newbranchname
```

# Github.com: Merging changes with the main branch

## Create, check and merge a pull request 
Log into Github and navigate to the [hpc page repo](https://github.com/aau-claaudia/hpc/).

Next there are ___ steps to complete the merge

1. Create a pull request
2. Check the changes in the pull request
3. Merge the pull request
4. Delete the branch on Github
5. Delete the branch locally


### Create a pull request
In the Github interface, inside the [hpc page repo](https://github.com/aau-claaudia/hpc/):

1. Click on the [pull request tab](https://github.com/aau-claaudia/hpc/pulls)
2. Click **New pull request**
3. Select the branch you want to merge into the main branch.


### Check the changes in the pull request

### Merge the pull request

### Delete the branch on Github

### Delete the branch locally


Once all changes have been merged, the branch can be deleted
This should be done on github first, and then locally.

## Additional common commandline tools


### Rename a branch

```bash
git branch -m old_branch_name new_branch_name
```

### Prune remote links to deleted branches

The prune command can then be used to remove any remote links to deleted branches. I.e. if you have a local branch that is set to track an online branch (i.e. upstream) then those links can be removed via pruning.

The following commands should all be run from another branch

```bash
git checkout main

git fetch --prune

git branch -d branchname
```

Next, a pull request is needed to incorporate the changes into the main branch





If there are uncommitted changes, or commits that have not been merged, this will return an error.

Check git status one more time, and if you are certain you want to delete the branch, you can force the delete with the -D flag.

### Force delete a branch locally
```bash
git branch -D branchname
```
