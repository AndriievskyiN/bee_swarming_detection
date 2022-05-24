from script import cv2, datetime, os
from script import save_to_github
from script.take_pictures import take_pictures
from script.save_to_github import pushToGitHub

current_time = datetime.now()

if __name__ == "__main__":
    take_pictures(current_time)
    pushToGitHub(current_time)
