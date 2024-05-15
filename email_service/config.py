import os
from dotenv import load_dotenv

load_dotenv()

MAILGUN_DOMAIN_NAME = os.getenv('MAILGUN_DOMAIN_NAME')
MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')

BREVO_API_KEY = os.getenv('BREVO_API_KEY')

SMTP_CONFIG = {
    "host": os.getenv('SMTP_HOST'),
    "port": int(os.getenv('SMTP_PORT')),
    "username": os.getenv('SMTP_USERNAME'),
    "password": os.getenv('SMTP_PASSWORD')
}

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
