# Multi-class-Classification
AUEB Project for Data and Web Mining

Average Log Loss of train_small:  3.07967394989

Hey,  
so to be able to use this repository so you can develop your solution of the code you have to follow this short tutorial:

1. #### Make a GitHub Account:  ####
Yeah since you are already on that page let's just start with that step. Register on this website.
https://github.com/join

2. #### Install Git:  ####
What is git? Git is a version-control and source-code-management system.
That means you can keep track of your changes to the source code and if you mess something up 
you can reset to a previous state.  
Git is much more powerful, especially if you work in teams on the same source code,
but since we will work in different 'branches' it's not so important to go into that.  
Mac users don't need to do that because they already have git installed on their machine.
Windowsusers however have to download and install git if it's not installed already.
Just download git from here and follow the instructions: http://git-scm.com/download/win

3. #### Install SourceTree:  #####
Now we have git and theoretically we could just start,
but every time we would want to commit, upload (push) or download (pull) code 
we would need to do that with a command in the Shell.  
SourceTree will provide us a graphical interface so we will not have to type in
long git commands manually but only have to press some buttons.
Just download and install it from here:
https://www.sourcetreeapp.com/download/

4. #### Setup SourceTree and our Repository:  ####
When you open SourceTree for the first time, it will ask you if you want to add an account.
Just select "GitHub" and enter your GitHub Credentials.  
Then press next till you see the Main Screen of Source Tree:
![alt tag](http://img.softmonk.com/sourcetree-1.8.1-1_960x484.png)  
Now we will try to clone this repository to our computer by clicking on "Clone/New" in the upper left corner.
In the new screen you have to enter the address of this repository (https://github.com/greece57/Multi-class-Classification)
and then select the folder on your computer where it should be saved.  
As last point you have to select your working branch. For that just open the "Advanced Options" and add your name
in the textbox next to "Checkout Branch" (Julia, Laura, Stefan, Beppe or Roman). In the end bevor you press "Clone" it should look like this:  
(Yeah Roman I know, it's in German. You will be able to understand what to do ;) )
![alt tag](http://s15.postimg.org/rs7mn8dij/Source_Tree_New_Project.png)

5. #### And now?  ####
Now the code should be on your machine. Just check the folder where you saved the repository,
there should be 3 python-files, 1 .cvs-file and one .git-folder.
You should now be able to simply add those 3 files to Spyder and run them. 

6. #### And why now git?/How to work with git:  ####
 1. *Clone*  
First what did we do till now? On the server there was our git repository where every information was stored (files, branches, ...).
We cloned (copied) all the information of the server on our machine. That means if the server now breaks we could theoretically just
upload our cloned repository and recreate exactly the same state (as long as we have the latest state).  
 2. *Commit*  
Now every time you make a bigger code change and have a working state you should commit your changes.
By committing your changes you create a point to which you can return whenever you want.  
For example if you mess up something and want to start clean again you can just reset your working copy 
and everything will be reset to your last commit. You can also theoretically rebase to an older commit 
but I don't think you'll need to do that. I never needed it.  
You can easily commit in SourceTree. Whenever you have changes you can change to the window "Filestatus" 
(on the bottom / for mac users switch the view as far as I know on the upper left). In that window you can see the files you changed.
The files you want to commit should be in the upper left window. Now just enter a commit-message (what did you change) and press commit
in the right corner under the commit-message textbox.
![alt tag](http://blog.sourcetreeapp.com/files/2014/08/Screen-Shot-2014-08-19-at-2.02.03-PM.png)  
 3. *Push*  
 After a commit it's always a good idea to also push your states (if you have an internet connection).
 By pushing you send your changes to the server and update the state of the server.
 If your machine would now break the current state of your work would still be on the server and you could clone it on a new device.  
 It's always a good idea to push at least at the end of the day.
 4. *Pull*  
 Pull is the opposite of push. Since we don't really work together on the same code you will not really need this function 
 because you will be the only one working on your branch. Pull pulls the latest code from the server and updates your data.  
 You will have to commit before pulling the latest state. 
 If the pulled code is different from this on your machine git will try to merge it automatically.
 If 2 people will work on the same file, it can lead to merge conflicts. 
 I will not explain how to solve them, because we won't have any ;)  
 5. *Branches*  
 I'm talking the whole time about branches without explaining them. Good job Niko.  
 So a branch is practically kind of your "sandbox". I made 1 branch for everybody so everybody can work separately.  
 Imagine it like a tree. The root is for us all the same (the 3 files we got) but then our work will go in different directions.
 1 branch for everybody and on this branch you can develop your work.  
 You can theoretically even make more branches if you want to,
 for example if you want to work on a new feature you could create a new "feature-branch" on which you work only on this new feature
 and after you finished the feature and its tested and working you could "merge" it back to your original branch.
 So you can work on more the 1 feature at the same time without having to have a working state 
 every time you finish your work on one feature.  
 But for us it's fine if just everybody will work on his branch and in the end we can merge the best solutions 
 together to the "master"-branch. For example if Julia made the best classify-method and Laura made the best work on the main.py document
 we will merge Julia's classify-file and Laura's main-file to the "master"-branch so we have in the end the best running state.
 
