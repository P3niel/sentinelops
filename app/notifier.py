# app/notifier.py

import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# 🔐 Charge les variables du .env
load_dotenv()

FROM_EMAIL = os.environ.get("FROM_EMAIL")
TO_EMAIL = os.environ.get("TO_EMAIL")
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASS = os.environ.get("SMTP_PASS")
SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PASSWORD = os.environ.get("SMTP_PASS")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 2525))  # fallback en cas d'absence


def send_notification(data: dict):
    subject = f"🚨 Alerte SentinelOps : {data}"
    body = f"""
🚨 Alerte SentinelOps

🕒 Timestamp : {data.get('timestamp')}
🧠 Type : {data.get('type')}
💬 Message : {data.get('message')}

📍 Hôte : {data.get('hostname')}
🌐 IP : {data.get('ip')}
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
            print(f"📧 Alerte envoyée à {TO_EMAIL}")
    except Exception as e:
        print(f"❌ Échec envoi alerte : {e}")

