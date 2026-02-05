from fastapi.templating import Jinja2Templates
import smtplib
from email.message import EmailMessage

templates=Jinja2Templates(directory="templates")

def sent_mail_now(name,email,project_type,message):
    EMAIL_ADDRESS=""
    EMAIL_PASSWORD=""
    msg=EmailMessage()
    msg["Subject"]=f"New Portfolio Contact : {name}"
    msg["From"]=EMAIL_ADDRESS
    msg["To"]=EMAIL_ADDRESS
    msg.set_content(f"""
                        New messege from portfolio website 
                        Name:{name}
                        email:{email}
                        Project:{project_type}
                        Message:{message}
                    """)
    with smtplib.SMTP_SSL("smtp.gmail.com",465)as server:
        server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        server.send_message(msg)
