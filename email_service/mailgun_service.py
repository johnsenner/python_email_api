import requests
from .base import EmailService
from .config import MAILGUN_DOMAIN_NAME, MAILGUN_API_KEY

class MailgunService(EmailService):
    def __init__(self):
        self.domain_name = MAILGUN_DOMAIN_NAME
        self.api_key = MAILGUN_API_KEY
        self.base_url = f"https://api.mailgun.net/v3/{self.domain_name}/messages"

    def send_email(self, sender_email, recipient_emails, subject, text):
        response = requests.post(
            self.base_url,
            auth=("api", self.api_key),
            data={
                "from": sender_email,
                "to": recipient_emails,
                "subject": subject,
                "text": text
            }
        )
        response.raise_for_status()
        return response.json()
