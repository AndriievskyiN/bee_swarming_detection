# Importing libraries
import cv2

import os
from datetime import datetime

# Reading the image from the camera and saving it to our clear_sky folder if it's later than 5 AM, and not later than 9 PM
def take_pictures(current_time):
    if current_time.strftime("%H:%M") > "05:00":
        if current_time.strftime("%H:%M") < "21:00":

            # Initializing the camera
            cam = cv2.VideoCapture(0)

            s, img = cam.read()
            cv2.imwrite(f"images/clear_sky/{datetime.now()}.jpg", img)

            # Releasing the camera, so that we don't capture video all the time
            cam.release()