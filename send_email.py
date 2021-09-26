import smtplib, ssl
import os
from email.mime.text import MIMEText
from structs import Job
from typing import List
from dotenv import load_dotenv

load_dotenv()

def send_email(jobs: List[Job]):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = os.getenv("SENDER_EMAIL")
    receiver_email = os.getenv("RECIEVER_EMAIL")
    password = os.getenv("EMAIL_PASS")
    
    msg_text = ""
    for job in jobs:
        msg_text += "\n"
        msg_text += f"Titel: {job['name']}\n"
        msg_text += f"Plats: {job['location']}\n"
        msg_text += f"Avdelning: {job['department']}\n"
        msg_text += f"Deadline: {job['deadline']}\n"
        msg_text += f"Länk: {job['link']}\n"

    text_type = "plain"
    msg = MIMEText(msg_text, text_type, "utf-8")
    msg["Subject"] = "Nya doktorandtjänster - KTH"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg)

        