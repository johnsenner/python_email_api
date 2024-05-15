import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .base import EmailService
from .config import SMTP_CONFIG

class SMTPEmailService(EmailService):
    def __init__(self):
        self.smtp_config = SMTP_CONFIG

    def send_email(self, sender: str, recipient: str, subject: str, body: str):
        try:
            server = smtplib.SMTP(self.smtp_config["host"], self.smtp_config["port"])
            server.starttls()
            server.login(self.smtp_config["username"], self.smtp_config["password"])

            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server.sendmail(sender, recipient, msg.as_string())
            server.quit()
            return {"message": "Email sent successfully!"}
        except Exception as e:
            raise Exception(f"Failed to send email: {e}")
