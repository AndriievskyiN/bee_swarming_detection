import tensorflow as tf
import cv2

import os
import imghdr
from datetime import datetime

from predict import predict_bee_swarming
from email_sender import send_email
from take_pictures import take_pictures
from hidden import *

model = tf.keras.models.load_model("models/model2.h5")
current_time = datetime.now()

if __name__ == "__main__":
    # Take pictures
    img_path = take_pictures(current_time)
    # Predict bee swarming
    prediction = predict_bee_swarming(img_path, model)
    if prediction:
        #Send email
        send_email(img_path, EMAIL_USER1, PYTHON_PASS)
    else:
        pass
        # Delete the image
        #os.remove(img_path)

