import cv2

import datetime
import os

from take_pictures import take_pictures
from save_to_github import pushToGitHub

current_time = datetime.now()

if __name__ == "__main__":
    take_pictures(current_time)
    pushToGitHub(current_time)
