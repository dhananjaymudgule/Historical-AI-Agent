# app/services/email_service.py

import random
import smtplib
from email.message import EmailMessage

from app.core.config import settings
from app.utils.otp import generate_otp


smtp_server = settings.SMTP_SERVER
smtp_port = settings.SMTP_PORT
email_sender = settings.EMAIL_SENDER
email_password = settings.EMAIL_PASSWORD


otp_storage = {}



def send_otp(email: str):
    """
    Sends a One-Time Password (OTP) to the given email address.
    
    Args:
        email (str): The recipient's email address.
    
    Returns:
        None
    """
    otp = generate_otp()
    otp_storage[email] = otp
    message = EmailMessage()
    message["From"] = settings.EMAIL_SENDER
    message["To"] = email
    message["Subject"] = "Your OTP Code"
    message.set_content(f"Your OTP code is {otp}")
    try:
        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.EMAIL_SENDER, settings.EMAIL_PASSWORD)
            server.send_message(message)
        return "Thanks! I have sent a 6-digit code to your email. Please confirm by entering the code."

    except Exception as e:
        return f"Failed to send OTP: {e}"





def verify_otp(email: str, otp: str) -> str:
    """
    Verifies if the given OTP matches the stored OTP for the given email.

    Args:
        email (str): The email address to check the OTP for.
        otp (str): The OTP provided by the user.

    Returns:
        str: A message confirming OTP verification or failure.
    """
    if otp_storage.get(email) == otp:
        return "Great, thanks! I'll send you an email soon. Take care!"
    return "Invalid OTP. Please try again."


