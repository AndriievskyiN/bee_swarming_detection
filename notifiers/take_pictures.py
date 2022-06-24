# Importing libraries
import cv2
import time
import os
from datetime import date, datetime

# Reading the image from the camera and saving it to our clear_sky folder if it's later than 5 AM, and not later than 9 PM
def take_pictures(current_time):
    if current_time.strftime("%H:%M") > "04:00":
        if current_time.strftime("%H:%M") < "22:00":
            # Initializing the camera
            cam = cv2.VideoCapture(0)
            s, img = cam.read()
            img_path = f"classified_images/{datetime.now()}.jpeg"
            cv2.imwrite(img_path, img)
            # Releasing the camera, so that we don't capture video all the time
            cam.release()
            return img_path
