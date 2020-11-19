# Setting up git

![](https://git-scm.com/images/logos/downloads/Git-Logo-Black.png)

!!! Note
    All information provided in this page comes from [here](https://git-scm.com/)

- **Windows**: [Gitbash](https://gitforwindows.org/) for windows users

- **Mac**: [command line](https://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line) and install from [here](https://git-scm.com/download/mac). You can use [`homebrew`](https://brew.sh/) as a package manager

- **Linux**: `sudo apt-get git`
 
## Make an account

!!! info "MDEF Only"

    - Make an account in [Gitlab.com](https://gitlab.com/) using the email you used in the program registration form

!!! danger "Format for the username"
    
    Make a username as such: `name_surname`

    For example if my name is...

    Andrés Casas Lee: `andres_casas`

    Or...

    Wongsathon Choonhavan: `wongsathon_choonhavan`

## Go local

- In your terminal, add your Git username and set your email

```
git config --global user.name "your_username"
```

- Configure you email address for uploading

```
git config --global user.email "your_email@mail.com"
```

## Generate SSH Keys

- Check if you have an SSH KEY already (If you see a long string starting with ssh-rsa, you can skip the ssh-keygen step)

```
cat ~/.ssh/id_rsa.pub
```

- Generate your SSH key

```
ssh-keygen -t rsa -C "your_email@mail.com"
```

- Now let´s see your keygen

```
cat ~/.ssh/id_rsa.pub
```

- Copy your key

**Windows**

```
clip < ~/.ssh/id_rsa.pub
```

**macOS**

```
pbcopy < ~/.ssh/id_rsa.pub
```

**linux**

```
xclip -sel clip < ~/.ssh/id_rsa.pub
```

## Go remote

- Finally add the copied key to GIT on the web version

<div style="text-align: center;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/54mxyLo3Mqk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Make a repository

There are several ways to have a repository:

- In the online git platform, create a repository and then clone it
- In your terminal initialising it from scratch
- Cloning an existing one (most likely)

### Online Git platform

If you are using and online web service for git ([Github](https://github.com/), [Gitlab](https://gitlab.com/), [bitbucket](https://bitbucket.org/)...), you can create a new project or repo by simply going to one of these below and then follow the instructions to _clone it_:

- [New github repo](https://github.com/new)
- [New gitlab repo](https://gitlab.com/projects/new)
- and so on...

### Terminal from scratch

!!! example "Step-by-step"
    - Navigate to the folder where you want to put or create your repo

    - In the terminal, type:

    ```
    git init
    ```

    - If you have a remote already, you can just do:

    ```
    git remote add origin git@gitlab.com:gitusername/repository.git
    ```

    - And then pull the remote:

    ```
    git pull
    ```

### Cloning an existing one

If you have a template or an online repository you want to reuse, you can navigate with your terminal to the desired destination folder and do:

!!! example "MDEF Students"

    - Navigate to the folder where you want to put or create your repo
        
        ```
        cd folder-for-your-project
        ```

    - Clone your student repository (ssh)

        ```
        git clone git@gitlab.com:MDEF/2020/documentation-template.git
        ```

        or http

        ```
        git clone https://gitlab.com/MDEF/2020/documentation-template.git
        ```

    - Create your own project in Gitlab - [Direct access](https://gitlab.com/projects/new) - Make sure that is **public!!**

    ![](../../material/extras/week01/assets/new-project.png)

    - Tell your local repository to push to the new project in Gitlab:

    ```
    git remote rename origin old-origin
    git remote add origin git@gitlab.com:username/your-repo-name.git
    ```

    - Do some edits and then add-commit-push (like this for the first commit):

    ```
    git add FILENAME
    git commit -m "My first commit"
    git push -u origin --all
    ```

    - For further changes, your workflow should be:

    ```
    git add FILENAME
    git commit -m "My other commit"
    git push
    ```

!!! danger "If you f****d up"

    Navigate to the project repository and under _Settings > General > Visibility_ and make it **Public** in the dropdown:

    ![](assets/visibility_gitlab.png)

!!! danger "About the commit message"
    This is a general point of failure for many many students (and instructors) that do not make a relevant commit message. 

    Write a **meaningful commit message**. This should answer the question: 
    > "If I apply this commit, I will... <commit message>". 
    
    For example: 
    > "uploading final project idea"
    
    This is not OK at all and will not help anyone to trace problems (and they will happen):

    ![](../../material/extras/week01/assets/bad-repo.png)

!!! Note "More guides"
    - [Fast guide to upload and update your repo to the GIT repo of Fab Academy by Eduardo Chamorro](http://fabacademy.org/2019/docs/FabAcademy-Tutorials/week01_principles_practices_project_management/git_simple.html)
    - [Full Guide Fab Academy](http://fabacademy.org/2019/docs/FabAcademy-Tutorials/week01_principles_practices_project_management/git_cheat_sheet.html)

<iframe width="560" height="315" src="https://www.youtube.com/embed/Y5cm-__K3sM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>