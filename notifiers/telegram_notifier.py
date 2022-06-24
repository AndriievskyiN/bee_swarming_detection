import requests

def telegram_notify(time, img_path):
    photo = {"photo": open(img_path, "rb")}
    message = f"This image was classified as bee swarming on {time}"
    requests.post(f"https://api.telegram.org/bot5346782906:AAGuSoPx1rBt1xDSjI7LQVeVDvzo0ewWY84/sendPhoto?chat_id=579467950&caption={message}", files=photo)