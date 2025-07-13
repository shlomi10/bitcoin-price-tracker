import smtplib
from business_logic.logger import logger

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

        logger.info(f"Attaching image from {attachment_path}")
        with open(attachment_path, 'rb') as f:
            img_data = f.read()
            msg.add_attachment(img_data, maintype='image', subtype='png', filename='btc_graph.png')

        logger.info(f"Connecting to SMTP server {smtp_host}:{smtp_port}")
        with smtplib.SMTP(smtp_host, smtp_port) as smtp:
            smtp.starttls()
            logger.info(f"Logged in as {sender_email}. Sending email to {recipient_email}")
            smtp.login(sender_email, password)
            smtp.send_message(msg)
            logger.info("Email sent successfully.")