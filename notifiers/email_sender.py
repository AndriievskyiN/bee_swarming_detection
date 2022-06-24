import smtplib
from email.message import EmailMessage

import os
import imghdr

def send_email(img_path, email_address, email_password):
    msg = EmailMessage()
    msg["Subject"] = "Bee swarming has been classified"
    msg["From"] = email_address
    msg["To"] = "andriievskyiwork@gmail.com"
    msg.set_content("Bee swarming has bee classified from the attached image, take a look if it is true")

    with open(img_path, "rb") as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)

    msg.add_attachment(file_data, maintype="image", subtype=file_type)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
    except:
        print("Email could not be sent")