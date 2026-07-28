import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv

import os


load_dotenv()


EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")


import smtplib
import os

from dotenv import load_dotenv

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")


def send_email(name, email, subject, message):

    msg = MIMEMultipart()

    msg["From"] = EMAIL
    msg["To"] = EMAIL
    msg["Subject"] = f"New Portfolio Contact - {subject}"

    body = f"""
New Portfolio Contact

Name: {name}

Email: {email}

Subject: {subject}

Message:

{message}
"""

    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(EMAIL, APP_PASSWORD)

    server.send_message(msg)

    server.quit()


def send_auto_reply(user_email, user_name):

    msg = MIMEMultipart()

    msg["From"] = EMAIL
    msg["To"] = user_email
    msg["Subject"] = "Thank you for contacting me"

    body = f"""
Hello {user_name},

Thank you for contacting me.

I have successfully received your message.

I usually reply within 24 hours.

Best Regards,

Siyam Ahmed
Python Automation Developer
"""

    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(EMAIL, APP_PASSWORD)

    server.send_message(msg)

    server.quit()