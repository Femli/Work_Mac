# Getting Started with Git and Github

Git and Github are very popular tools that are used by engineers, programmers and scientists in today's age. 

In a nutshell, *Git* is known as a "version control" software program. It basically allows you to keep track of all the changes made by you or teammates on projects. *Github* is a company that uses *Git* to create and manage online **repositories** -- think of Google Drive but for programmers and developers.

If you would like to know more about Git and Github, check out this [article](https://codeburst.io/git-and-github-in-a-nutshell-b0a3cc06458f) or this [video](https://www.youtube.com/watch?v=uUuTYDg9XoI)

## Github

If you don't have a Github account already, go ahead and create one by following this [guide](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners) (read step **0** and then skip to step **6** only).

## Git

*Git* already comes pre-installed with Macs, but if you are using Windows then feel free to follow this [link](https://git-scm.com/download/win) to download the Git program. Once downloaded, run the program (just leave all settings at default) and it should be straight forward from there.

Then, once again follow this [guide](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners) from **steps 1 - 8** (skip steps **5** and **6**)


## The Basics

There are two main processes for Git: 
- Pushing your local work to your online repository
- Pulling work from your online repository to your local files

To create a git repository in your local files, run the following commands in your terminal:

- Select the folder you want to start your repo in by doing `cd <enter file directory here>`. 
  - For example, if I want to save it in my documents I would type `cd documents`
- Then to create a repository in the file location, type `git init`

At this point you can push this local git repository into your online repository on GitHub.

#### Cloning
If you want to clone an online repository from GitHub, then do the following:
- Go into the root directory of a GitHub repository and then copy the URL.
  - For example, the URL to one of my own repositories is `https://github.com/Femli/Work_Mac`
- Now open the terminal, navigate into the folder you want to clone this repo to, and enter the following commands:
  - `git clone <repo URL here>`

#### Global Settings
Afterwards, configure your Git settings so that you can push your work. Do this by entering the following:
- `git config --global user.name "<your GitHub username here>"`
  - For example, for my GitHub I would say `git config --global user.name "Femli"`
- Then enter your email associated with your GitHub account with `git config --global user.email "<your GitHub email here>"`
  - For example, I would write `git config --global user.email "franco@digitalnest.org"`

Once your global settings are configured, you can begin saving your work online by pushing it.

#### Pushing

There are three steps to saving your work onto your GitHub repository.

**Step 0** - Verifying changes
Once you have saved the file changes you want to add to your online repo, verify that you actuall have changes to implement by opening the Terminal, navigate to your local repo, and then type `git status`. All files in red are unsaved changes to your online repository.

**Step 1** - Getting on the Bus to Hades
Once you confirm there are changes to be made, go ahead and add those changes by enter `git add <file name here>`. If you want to save all the changes you made to your repo, then simply type `git add .`

**Step 2** - Bus Travels to Hades
Once you added the changes to be made, you want to *stage* those changes by doing the following `git commit -m "<personal note here>"`.
- You usually want to give yourself a note about the changes you made since last time you worked on your file. For example, `git commit -m "added code that creates a hit box"`

**Step 3** - Get off the bus!
The final step is now to simply push all your commited changes to your online repo by entering `git push`. You should now see all the changes you made on your local repo be reflected on your GitHub repo.



