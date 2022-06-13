import smtplib
from email.message import EmailMessage
import os

EMAIL_ADDRESS = os.environ.get("EMAIL_USER1")
EMAIL_PASSWORD = os.environ.get("PYTHON_PASS")

msg = EmailMessage()
msg["Subject"] = "Hello"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "andriievskyiwork@gmail.com"
msg.set_content("This is a test message")

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
except:
    print("Email could not be sent")