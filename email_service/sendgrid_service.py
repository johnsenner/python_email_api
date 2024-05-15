from .base import EmailService
from .config import SENDGRID_API_KEY

class SendGridEmailService(EmailService):
    def __init__(self):
        self.sendgrid_api_key = SENDGRID_API_KEY

    def send_email(self, sender: str, recipient: str, subject: str, body: str):
        try:
            # Send email using SendGrid API or client
            return {"message": "Email sent successfully via SendGrid!"}
        except Exception as e:
            raise Exception(f"Failed to send email via SendGrid: {e}")
