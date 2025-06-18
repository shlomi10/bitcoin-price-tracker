import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

"""
This class sends an email with an image attachment using the specified SMTP server.
"""


from email.message import EmailMessage

class EmailSender:
    def send(self, smtp_host, smtp_port, sender_email, password, recipient_email, subject, body, attachment_path):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg.set_content(body)

        with open(attachment_path, 'rb') as f:
            img_data = f.read()
            msg.add_attachment(img_data, maintype='image', subtype='png', filename='btc_graph.png')

        with smtplib.SMTP(smtp_host, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(sender_email, password)
            smtp.send_message(msg)



