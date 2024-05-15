from abc import ABC, abstractmethod

class EmailService(ABC):
    """
    Abstract base class for email services. All email services should inherit from this class 
    and implement the send_email method.
    """
    @abstractmethod
    def send_email(self, sender: str, recipient: str, subject: str, body: str):
        pass
