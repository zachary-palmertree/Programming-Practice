### set up a new GitHub repository from a local repository
1. Go to the directory where you want the local repository to be stored
2. Type `git init`
3. `git branch -M main` to set the name of the current branch to 'Main' if it's not already
4. `git remote add origin <GitHub url>` to set the GitHub repo as the remote repository. Other examples use <username> inbetween the origin and GitHub url. 
5. `git add <files>`
6. `git commit -m "<commit message>"`
7. `git push` to push your local repository to the remote repository