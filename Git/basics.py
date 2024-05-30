# All important git commands

#1. git init
'''
This initialize git on a repository.
'''
#2. git add file_name
'''
it will add that file to the staging area.
'''
#3. git add .
'''
It will add every file present on present working directory to the staging area.
'''
#4. git status
'''
This command is used to check the status of git. i.e. it will check is there any changes made to files inside a git repository.
'''
#5. git commit -m "message"
'''
This command will save all the changes, means all those file those are in the staging area. it's just like saving a file. We can add desired message to staged files.
'''
#6. git commit -am "message"
'''
This will commit files without adding it to the staging area.
'''
#7. git rm --cached file_name
'''
This will remove file from the staged area.
'''
#8. git rm file_name
'''
This will remove file from working directory as well as from staging area.
'''
#9. git diff
'''
This will show us all the unstaged changes.
'''
#10. git diff --staged
'''
This will show us all the staged changes.
'''
#11. git log
'''
This will show us all history of changes made to files.
'''
#12. git log --reverse
'''
This will give us all commits made from oldest to newest.
'''
#13. git show HEAD
'''
This will only give the last commit made.
'''
#14. git restore
'''
This will discards all the local changes made (except untracked files)
'''
#15. git clean -fd
'''
This will remove all untracked files.
'''
#16. git checkout code
'''
This will check out the given commit.
'''
#17. git branch new_name
'''
Creates a new branch named new_name.
'''
#18. git checkout new_name
'''
Check out to new_name branch.
'''
#19. git clone url
'''
Clone everything from a git url to local.
'''
#20. git push origin main
'''
it will push all the changes made on branch origin to main branch.
'''
#21. git remote add origin github_url
'''
it will add out git directory with a github repo.
'''
#22. git pull main origin
'''
It will pull all the changes frommain to origin branch.
'''
#23. git reset
'''
It will reset everything made to the files.
'''
#24. git config --global user.name "your_name"
'''
This will set a global name so that other person can see who made the changes.
'''
#25. git config --global user.email "your_email"
'''
This will set a global email for user.name
'''