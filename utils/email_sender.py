import smtplib
from email.message import EmailMessage

"""
Sends an email with an image attachment using the specified SMTP server.
"""
def send_email(smtp_host, smtp_port, sender_email, password, recipient_email, subject, body, attachment_path):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content(body)

    with open(attachment_path, 'rb') as f:
        msg.add_attachment(f.read(), maintype='image', subtype='png', filename='btc_graph.png')

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)


