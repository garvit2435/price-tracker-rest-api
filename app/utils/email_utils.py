from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from typing import List

class EmailConfig:
    MAIL_USERNAME = "samplemail2435@gmail.com"
    MAIL_PASSWORD = "Garvit99284"
    MAIL_FROM = "samplemail2435@gmail.com"
    MAIL_PORT = 587
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_TLS = True
    MAIL_SSL = False
    USE_CREDENTIALS = True

conf = ConnectionConfig(
    MAIL_USERNAME = EmailConfig.MAIL_USERNAME,
    MAIL_PASSWORD = EmailConfig.MAIL_PASSWORD,
    MAIL_FROM = EmailConfig.MAIL_FROM,
    MAIL_PORT = EmailConfig.MAIL_PORT,
    MAIL_SERVER = EmailConfig.MAIL_SERVER,
    MAIL_TLS = EmailConfig.MAIL_TLS,
    MAIL_SSL = EmailConfig.MAIL_SSL,
    USE_CREDENTIALS = EmailConfig.USE_CREDENTIALS,
)

async def send_email(subject: str, recipients: List[str], body: str):
    message = MessageSchema(
        subject=subject,
        recipients=recipients,
        body=body,
        subtype="html"
    )
    
    fm = FastMail(conf)
    await fm.send_message(message)
