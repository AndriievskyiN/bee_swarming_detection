# Importing libraries
import cv2
from datetime import datetime

# Initializing the camera
cam = cv2.VideoCapture(0)

# Reading the image from the camera and saving it to our clear_sky folder
s, img = cam.read()
cv2.imwrite(f"/home/nikita/bee_swarming/images/clear_sky/{datetime.now()}.jpg", img)

# Releasing the camera, so that we don't capture video all the time
cam.release()
