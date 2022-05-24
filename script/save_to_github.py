import os

from datetime import datetime as dt

# Pushing changes to github at the end of the day
def pushToGitHub(current_time):
    if current_time.strftime("%H:%M") > "09:00":
        os.system("git add .")
        os.system('git commit -m "new photos"')
        os.system("git push -u origin main")