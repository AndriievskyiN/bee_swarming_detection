import tensorflow as tf
import cv2

# Create a function to predict bee swarming based on the image using the model
def predict_bee_swarming(img_path, model):
    img = cv2.imread(img_path)
    # Resizing the image
    resized = tf.image.resize(img, (256,256))

    # Actually classifying the image
    yhat = model.predict(tf.expand_dims(resized/255, axis=0))
    if yhat < 0.5:
        return True
    else:
        return False
