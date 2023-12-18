# Getting started with git

>>> Install git
>>> check the version
<git --version>

>>>Open your account on github.com

>>> Create new repositor(from github.com)
>>> go to your root directory of your project in cmd

<git init> 
#this will create the ".git" file on the root dir(it may be hidden if you want to check then show the hidden files)

<git add --all>
#this will add our all of the files which was present at root dir

<git commit -m "message">
#used to send all the local added changes to github


>>>Here, If you got an error for setup git to your local machine
>Follow the commands
<git config --global user.email satyam12@gmail.com>  #gmail from which you created github account
<git config --global user.name satyamverve>  #this is the name of your github acoount

>>>Now set the branch
<git branch -M main> 
here main is the local branch name you can give it any name


## Difference between Remote, Master, Origin and Main

1. MASTER: This is the default branch named in git repository
2. MAIN: Both Master and Main branch are same, the only difference is previous(means the repos which we created 
         earlier) default git repository is called MASTER and the current git repository where we are working is 
         called MAIN.
3. ORIGIN: When we clone someones repository to our github as local repositories then by 
           default that repository is called ORIGIN(you can make the name of ORIGIN anything)
4. REMOTE: It is a reference to the local repositories(called ORIGIN),which allowing to fetch, and push changes 
           between repositories(someones repository and our local repository called Origin).


## Make a remote and fetch your repo
(here remote name is origin bydefault and remote is used to add changes)

<git remote add origin repository_url>
<git remote add origin https://github.com/satyamverve/fastapi_project.git> 
#add .git at the end of your url


## git push
>>> after all changes push your all changes to git
<git push -u origin main>
The -u flag creates a tracking reference for every branch that you successfully push onto the remote repository.


# about some common commands
<git status>
used to see all the changes

<git fetch>
set to the current origin or remote

<git push>
push all changes

<git remote>
see what is your current remote

<git branch>
see all branches


## after git add --all
If you got an error below:

! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/satyamverve/fastapi.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

<It means local copy of a repository is behind the upstream repository, you need to fetch the changes from the upstream repository before you can push your local changes.
Here are the steps to do this:>

<git fetch origin>
<git merge origin/main>  #this command is optional
<git rebase origin/main >
<git rebase --continue>
<git merge --continue>

## Now push the changes
<git push origin main>


## Commands to clone my own repo to local and start pushing and commiting
>create a new directory
>go to that directory in terminal
>add your files here (which you want to push to your repo)
<git init>
<git remote add origin repo_url.git>
<git fetch origin>
<git branch -m main>
<git pull origin main>
<git config core.filemode false>
<git add --all>
<git commit -m "message">
<git push origin main>


# how to work on a global repository by cloning them to your git
>> Follow the commands:
>create a new directory

>go to that directory in terminal
<git init>

>> go to github and fork the global repo to your repositories
>> after fork copy the forked_repository url
<git clone forked_repository_url.git>

>> navigate to that cloned repo filename
<cd <cloned_repository_directory>

<git fetch origin>    #This command fetches changes from the remote repository but does not merge them into your local branch
>>Edit the file(s) you want to change.

>> Add specific changes to git:
<git add <filename1> <filename2> ...>

>> add all changes to git
<git add .> or <git add -all>

>> commit changes:
<git commit -m "Your commit message here">

>> Pull changes from Remote Repo,i.e, This fetches changes from the remote repository and merges them into your local branch.
<git pull origin <branch_name>   # here my branch_name is "main"

>> Resolve Merge Conflicts (if any):
If there are conflicting changes, Git will prompt you to resolve them.
Open the conflicted files, resolve the conflicts, and then add and commit the changes.

>> Push Changes to Remote Repository:
<git push origin <branch_name>> # default branch_name is "main"
<NOTE: Make sure you've pushed the changes to your forked repository on GitHub.>

>> After that you may get popup for authorization then do the authorization using your git account id where you forked this repo

<NOTE: After commit changes are stored in local
But after push changes are stored in both local and the remote repo>

<NOTE: Keep in mind that "git_fetch" and "git_pull" help you synchronize your local repository with the remote, preventing conflicts that might arise if someone else has pushed changes in the meantime. If there are changes on the remote, it's a good practice to fetch them before making your own changes and pushing them.>

>> After pushing you have to create a pull request from your git:

>> go to your github
>> Navigate to your fork on github
i.e, https://github.com/your-username/repository.
>> switch the branch where you pushed the changes (default "main")

>> on the top of the left side you see a button called "Pull requests"
>>> click on that
>>Click on the "New Pull Request" button

>>> Now choose the branches carefully:
i.e,
<In the "base repository" dropdown, select the repository of the owner (the original repository).
In the "base" dropdown, select the branch you want to merge into (usually main or master).
In the "head repository" dropdown, select your forked repository.
In the "compare" dropdown, select the branch you pushed changes to (feature-branch).
>

>>> Review changes
>>> Add a Title and Description
>>> Click on the "Create pull request" button.
>>> Your pull request will be created, and the owner of the original repository will be notified.
>>> They will review your changes and either merge them, request modifications, or close the pull request.

<IMPORTANT NOTES:
1. Make sure you are pushing changes to a new branch in your forked repository.
2. Be clear and descriptive in your pull request description, explaining what the changes are and why they are necessary.
3. If there are changes requested by the repository owner, make the modifications locally, commit, and push the changes. The pull request will be automatically updated.>


# How to clone repo from SSH
<git init>
<ssh-keygen -t ed25519 -C "abcd@gmail.com">
<cat ~/.ssh/id_ed25519.pub> <!-- This will generate a SSH key -->
>> got to your github account github.com
>> click on your profile(right side upper corner)
>> settings > SSH and GPG keys > New SSH key
>> give any name in in title > copy-paste your generated SSH key
>> click Add SSH key
>> go to terminal
<git clone git@github.com:username/repo.git>  <!-- cloning from the SSH from github.com -->
or,
<git remote add origin ssh_url>
>> navigate to your repo in terminal
<git fetch origin>
