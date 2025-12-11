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
Alternatively, you can do this after using the longhand option

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
git add --all
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
This will change the origin from which you pull existing changes and push changes to, thus `git pull` will no longer result in an update of the branch from the `main`branch.

## Git fetch main branch and merge with local (remote) version

This step is optional and is only really necessary if there are multiple people editing the same file simultaneously, and potentially committing those changes to the `main`branch. Or there may be some other reason you want to pull and merge any changes made to the `main` branch to your remote new and modified branch.

```bash
# Check what branch you are working in
git branch

# Switch to the branch you want to update (if you are not already there)
git checkout newbranchname      # gets you "on branch newbranchname"

# Fetch the latest version of the branch you are on
git fetch origin        # gets you up to date with origin

# Merge in the latest 
git merge origin/main -m "write_a_good_commit_message_for_why_you_want_to_merge_the_new_main_branch"
```

Following this you will need to commit all of the modifications made to the main branch, into your new branch.

```bash
git status
git add --all
git commit -m "All files merged from main branch back into remote branch committed to new branch"
```

```bash
git merge origin/main -m "write_a_good_commit_message_for_why_you_want_to_merge_the_new_main_branch"
```

It is also recommended to switch back to your remote "main" branch (i.e. the one on your local machine) and update that with a `git pull`.

```bash
git checkout main
git pull
```
This will automatically fetch and merge all of the changes to the main branch to your local copy.


!!! info "There is a difference between `git pull` and `git fetch`"

    "The `git pull` command updates both the user’s local Git repository and the files in their working directory.
    That provides the developer with two benefits:

    - The local Git repo is now in sync with the remote repo.
    - The local filesystem has the latest, most up to date files.
    
    The `git pull` command has one prerequisite: the user cannot be actively editing any tracked files in their local workspace that conflict with what’s on the remote server.

    The benefit of the `git fetch` vs `git pull` is that a fetch enables you to continue editing files in your local working directory without having to merge your code with updates from the remote repo.

    With a `git fetch`, you can finish editing files locally, commit your files and then do a git merge to synchronize your updates with the fetched files. This brings you up to date with the updates the fetch pulled down from the remote machine.

    One of the other benefits of a `git fetch` is that it allows you to find out if the branch you are working on is ahead or behind the branch on the server.

    However, when we perform a `git fetch`, we are informed that we are actually three commits behind the master Git branch on the server.

    If you want to know how far ahead or behind your local branch is compared to what is on the server, the `git fetch` command, along with a `git status`, allows you to know that."

    *See for https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Git-pull-vs-fetch-Whats-the-difference for a full explanation*
    

# Github.com: Merging changes with the main branch

## Create, check and merge a pull request 
Log into Github and navigate to the [hpc page repo](https://github.com/aau-claaudia/hpc/).

Next there are ___ steps to complete the merge

1. Create a pull request
2. Check the changes in the pull request
3. Merge the pull request
4. Delete the branch on Github
5. Delete the branch locally
6. Prune remote links to deleted branches


### 1. Create a pull request
In the Github interface, inside the [hpc page repo](https://github.com/aau-claaudia/hpc/):

1. Click on the [pull request tab](https://github.com/aau-claaudia/hpc/pulls)
2. Click **New pull request**
3. Select the branch you want to merge into the main branch.

> The changes will be displayed in a code view at the bottom of the screen.

4. Click **Create pull request**

> Provide a title if you wish to change the title from the commit message, and notes about the changes.
Current internal processes are that pull requests do not require a review before merging for the hpc.aau.du site, but they must be reviewed for any code bases.


### 2. Check the changes in the pull request

1. Open the [pull request tab](https://github.com/aau-claaudia/hpc/pulls) again.
2. Open the pull request
3. Check the changes in the pull request
> If there was a review process it would happen here.

### 3. Merge the pull request

4. Click "Merge pull request"

### 4. Delete the branch on Github

Once the pull request has been merged, there is a button available to delete the branch.

*If you miss this opportunity, then you find and delete the branch from the repo.*

1. Return to the [hpc page repo](https://github.com/aau-claaudia/hpc/).
2. Click on the [branches](https://github.com/aau-claaudia/hpc/branches) button under the [Code tab](https://github.com/aau-claaudia/hpc).
3. Find the branch that you have just merged, and click the trashcan icon to the right.

### 5. Delete the branch locally

Once all changes have been merged, the branch can be deleted

**This should be done on github first, and then locally.**

```bash
git branch -d branch_name
```

### 6. Prune remote links to deleted branches

The prune command can then be used to remove any remote links to deleted branches. I.e. if you have a local branch that is set to track an online branch (i.e. upstream) then those links can be removed via pruning.

The following commands should all be run from another branch

```bash
git checkout main

git fetch --prune

git branch -d branchname
```

## Additional common commandline tools

### Rename a branch

```bash
git branch -m old_branch_name new_branch_name
```

### Force delete a branch locally
```bash
git branch -D branchname
```
