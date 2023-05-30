from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
smtplib.debuglevel = 1


sender = 'odooamawy@gmail.com'
recipients = ['ahmedelamawy06@gmail.com']
subject = 'Test Email'
body = 'This is a test email sent from the script.'


message = MIMEMultipart()
message['From'] = sender
message['To'] = ', '.join(recipients)
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))



smtp_host = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'odooamawy@gmail.com'
smtp_password = '@123456Amawy'

with smtplib.SMTP(smtp_host, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.send_message(message)

