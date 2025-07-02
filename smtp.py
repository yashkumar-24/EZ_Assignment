import smtplib
from email.mime.text import MIMEText
from app.config import settings

def send_verification_email(to_email: str, token: str):
    link = f"{settings.BASE_URL}/client/verify-email?token={token}"
    msg = MIMEText(f"Click to verify: {link}")
    msg["Subject"] = "Verify your email"
    msg["From"] = settings.SMTP_USER
    msg["To"] = to_email
    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.sendmail(settings.SMTP_USER, [to_email], msg.as_string()) 