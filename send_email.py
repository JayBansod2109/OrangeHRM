import smtplib
from email.mime.text import MIMEText
import os

sender = os.getenv("EMAIL_USER")

password =os.getenv("EMAIL_PASS")

receiver = "jaybansod525@gmail.com"

msg = MIMEText("Playwright Test Passed")

msg["Subject"] = "Daily Test Result"

msg["From"] = sender

msg["To"] = receiver

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(sender, password)

print("Sender:", sender)
print("Password exists:", password is not None)
print("Password length:", len(password) if password else 0)

server.send_message(msg)

server.quit()