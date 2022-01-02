set /p choice= "Enter Message to be set on Commit : " 
git add .
git commit -m "%choice%"
git push origin main 
git log --oneline
git log -1 --stat
@ECHO OFF
ECHO files commited and pushed successfully to github main branch
ECHO Press Any key to exit
PAUSE