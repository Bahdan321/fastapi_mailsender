from config import HOST, USERNAME, PASSWORD, PORT, MailBody
from ssl import create_default_context
from email.mime.text import MIMEText
from smtplib import SMTP

def send_email(data:dict|None=None):
    msg = MailBody(**data)
    message = MIMEText(msg.bodym, "html")
    message["From"] = USERNAME
    message["To"] = ",".join(msg.to)
    message["Subject"] = msg.Subject

    ctx = create_default_context()

    try:
        with SMTP(HOST,PORT) as server:
            server.ehlo()
            server.starttls(context=ctx)
            server.ehlo()
            server.login(USERNAME, PASSWORD)
            server.send_message(message)
            server.quit()
        return {
            "status": 200,
            "errors": None,
        }
    except Exception as err:
        return {
            "status": 500,
            "errors": err,
        }