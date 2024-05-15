# python_email_api

Helpfulbots Email API Module

A simple, extensible email service package for startups, supporting multiple email providers like SMTP, Mailgun, Brevo, and SendGrid.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/email-service.git
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your configuration settings:
    ```env
    MAILGUN_DOMAIN_NAME=your_mailgun_domain_name
    MAILGUN_API_KEY=your_mailgun_api_key

    BREVO_API_KEY=your_brevo_api_key

    SMTP_HOST=smtp.your-email-provider.com
    SMTP_PORT=587
    SMTP_USERNAME=your_smtp_username
    SMTP_PASSWORD=your_smtp_password

    SENDGRID_API_KEY=your_sendgrid_api_key
    ```

## Usage

There are a lot of great email APIs out there, any of which might meet your needs.

### Example Code

```python
from email_service.smtp_service import SMTPEmailService
from email_service.mailgun_service import MailgunService
from email_service.brevo_service import BrevoService
from email_service.sendgrid_service import SendGridEmailService

# Choose the email service to use (SMTP, Mailgun, Brevo, or SendGrid)
email_service = SMTPEmailService()
# email_service = MailgunService()
# email_service = BrevoService()
# email_service = SendGridEmailService()

sender = "your_email@example.com"
recipient = "recipient@example.com"
subject = 'Update on Your Request'
body = "This is the email body."

email_service.send_email(sender, recipient, subject, body)
```

## Adding New Services

To add a new email service, follow these steps:

1. **Create a New Service Class**:
    - Create a new file in the `email_service` directory, e.g., `new_service.py`.
    - Define a new class that inherits from the `EmailService` abstract base class.

    ```python
    from .base import EmailService

    class NewService(EmailService):
        def __init__(self, api_key):
            self.api_key = api_key
            self.base_url = "https://api.newservice.com/v1/send"

        def send_email(self, sender: str, recipient: str, subject: str, body: str):
            # Implement the logic to send an email using the new service's API
            response = requests.post(
                self.base_url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={
                    "from": sender,
                    "to": recipient,
                    "subject": subject,
                    "body": body
                }
            )
            response.raise_for_status()
            return response.json()
    ```

2. **Update Configuration**:
    - Add any necessary configuration settings to the `.env` file.

    ```plaintext
    NEW_SERVICE_API_KEY=your_new_service_api_key
    ```

    - Update the `email_service/config.py` file to include the new configuration settings.

    ```python
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
    NEW_SERVICE_API_KEY = os.getenv('NEW_SERVICE_API_KEY')
    ```

