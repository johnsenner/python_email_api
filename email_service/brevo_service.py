import requests
from .base import EmailService
from .config import BREVO_API_KEY

class BrevoService(EmailService):
    def __init__(self):
        self.api_key = BREVO_API_KEY
        self.base_url = "https://api.brevo.com/v3/smtp/email"
        self.bcc_address = "contact@helpfulbots.com"
        self.default_recipient = "user@helpfulbots.com"

    def send_email(self, sender_name: str, sender_email: str, recipient_email: str, subject: str, content: str):
        if not recipient_email:
            recipient_email = self.default_recipient

        html_content = f"<html><head></head><body><p>{content.replace('\\n', '<br>')}</p></body></html>"

        headers = {
            'Accept': 'application/json',
            'API-Key': self.api_key,
            'Content-Type': 'application/json'
        }

        payload = {
            "sender": {
                "name": sender_name,
                "email": sender_email
            },
            "to": [{"email": recipient_email}],
            "bcc": [{
                "name": "HelpfulBots Info",
                "email": self.bcc_address
            }],
            "replyTo": {
                "email": recipient_email
            },
            "subject": subject,
            "htmlContent": html_content
        }

        response = requests.post(self.base_url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
