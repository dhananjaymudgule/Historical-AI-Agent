import random


import smtplib
from email.message import EmailMessage

from app.core.config import settings


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
    otp = f"{random.randint(100000, 999999)}"
    otp_storage[email] = otp
    message = EmailMessage()
    message["From"] = email_sender
    message["To"] = email
    message["Subject"] = "Your OTP Code"
    message.set_content(f"Your OTP code is {otp}")
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_sender, email_password)
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


