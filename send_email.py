import smtplib
from email.mime.text import MIMEText
import os


def send_email():

    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    receiver = "jaybansod525@gmail.com"

    msg = MIMEText("Playwright Test Passed")

    msg["Subject"] = "Daily Test Result"
    msg["From"] = sender
    msg["To"] = receiver

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    print("EMAIL_USER:", sender)
    print("EMAIL_PASS exists:", password is not None)
    print("EMAIL_PASS length:", len(password) if password else 0)

    server.login(sender, password)



    server.send_message(msg)

    server.quit()


if __name__ == "__main__":
    send_email()