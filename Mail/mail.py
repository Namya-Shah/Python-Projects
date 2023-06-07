import smtplib
import creds
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = "" # Enter the subject
msg['From'] = creds.email # This gets email from your creds file
msg['To'] = ', '.join(creds.receiver) # This enters mail id to which you want to send the mail
msg.set_content("") # This sets content of the mail

files = [''] # Enter the files you want to send

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(creds.email, creds.password)

    smtp.send_message(msg)
    print("Success")
