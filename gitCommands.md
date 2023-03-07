># 1. add
* The git add command adds a change in the working directory to the staging area. 
* It tells Git that you want to include updates to a particular file in the next commit. However, git add doesn't really affect the repository in any significant way—changes are not actually recorded until you run git commit.

> git add (options)




># 2. checkout
* The git checkout command lets you navigate between the branches created by git branch . Checking out a branch updates the files in the working directory to match the version stored in that branch, and it tells Git to record all new commits on that branch.

> git checkout (options)



># 3. clone
* git clone is primarily used to point to an existing repo and make a clone or copy of that repo at in a new directory, at another location. The original repository can be located on the local filesystem or on remote machine accessible supported protocols. The git clone command copies an existing Git repository.

> git clone (Https link)
>
> ushabhat@ushabhat-Latitude-5531:~$ **git clone** https://github.com/UshaBhat/MyDevelop.git
> 
> Cloning into 'MyDevelop'...
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 9 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (9/9), 2.35 KiB | 2.35 MiB/s, done.
ushabhat@ushabhat-Latitude-5531:~$ ls
> 
> Desktop    Downloads  MyDevelop  Public           snap       Videos
Documents  Music      Pictures   PycharmProjects  Templates



># 4. commit
*  Commit a snapshot of all changes in the working directory. This only includes modifications to tracked files (those that have been added with git add at some point in their history). git commit -m "commit message" A shortcut command that immediately creates a commit with a passed commit message.

> git commit (options)



># 5. config
* Define the author name to be used for all commits by the current user.
* Define the author email to be used for all commits by the current user.

> git config --global user.email <email> 
> 
> git config --global
user.name <name> 





># 6. gitignore
* A gitignore file specifies intentionally untracked files that Git should ignore. Files already tracked by Git are not affected; see the NOTES below for details. Each line in a gitignore file specifies a pattern.

> .gitignore




># 7. log
* The git log command is used to view the history of committed changes within a Git repository. Each set of changes made by a developer is recorded as a commit in Git. The git log command shows a default output for quickly reviewing the commit history.
> git log 
> 
> ushabhat@ushabhat-Latitude-5531:~/MyDevelop$ git log
> 
> commit 4a4a3bc6180dbb2927b9f63df3af0f7e98ca0701 (HEAD -> main, origin/main, origin/HEAD)
Author: UshaBhat <ushabhatalagodu@gmail.com>
Date:   Mon Mar 6 10:59:12 2023 +0530
    Add files via upload
commit 4708a21d85fe58c1d1d2610782cad13fb8cf3d2f
Author: UshaBhat <ushabhatalagodu@gmail.com>
Date:   Fri Mar 3 11:07:53 2023 +0530
    Update README.md
commit a991ff4874fcb852f4e28db722f4494a96b5c0c7 (origin/readme-edits)
Author: UshaBhat <ushabhatalagodu@gmail.com>
Date:   Fri Mar 3 10:58:44 2023 +0530

    Initial commit



># 8. init
* Create empty Git repo in specified directory. Run with no
arguments to initialize the current directory as a git repository.

> git init (directory)
> 
> ushabhat@ushabhat-Latitude-5531:~/MyDevelop$ git init Desctop
Initialized empty Git repository in /home/ushabhat/MyDevelop/Desctop/.git/




># 9. merge
* Merge <branch> into the current branch.
> git merge branch
> 
> ushabhat@ushabhat-Latitude-5531:~/MyDevelop$ git merge origin/readme-edits
Already up to date.



># 10. gitk
* Gitk is invoked similarly to git log . Executing the gitk command will launch the Gitk UI which will look similar to the following: The upper left pane displays the commits to the repository, with the latest on top. The lower right displays the list of files impacted by the selected commit.

> gitk (options)
  


># 11. status
* The git status command displays the state of the working directory and the staging area. It lets you see which changes have been staged, which haven't, and which files aren't being tracked by Git. 
> git status
> 
> ushabhat@ushabhat-Latitude-5531:~/MyDevelop$ git status
> 
> On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean



># 12. push
* The git push command is used to upload local repository content to a remote repository. Pushing is how you transfer commits from your local repository to a remote repo.

> git push 


># 13. pull
* The git pull command is used to fetch and download content from a remote repository and immediately update the local repository to match that content. 
> git pull --rebase 
> 
> ushabhat@ushabhat-Latitude-5531:~/MyDevelop$ git pull --rebase
Current branch main is up to date.



># 14. remote
* The git remote command lets you create, view, and delete connections to other repositories. Remote connections are more like bookmarks rather than direct links into other repositories.


> git remote
> 
>ushabhat@ushabhat-Latitude-5531:~/MyDevelop$ git remote
origin


># 15. stash
* git stash temporarily shelves (or stashes) changes you've made to your working copy so you can work on something else, and then come back and re-apply them later on.
>git stash
> 
> ushabhat@ushabhat-Latitude-5531:~/MyDevelop$ git stash
No local changes to save
