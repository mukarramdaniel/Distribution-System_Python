import os
from email.message import EmailMessage
import smtplib
email_sender = "rasheedrayan514@gmail.com"
email_password = 'zpzsrqeasritevbu'
email_receiver = "hasannawaz2486@gmail.com"

subject = "Kiya haal h boss"
body = '''
Insan ki zindigi ko bamaqsad hona chahye
'''
for i in range(100):
    em = EmailMessage()
    em['from'] = email_sender
    em['to'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    #context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com' , 465 ) as smtp:
        smtp.login(email_sender , email_password)
        smtp.sendmail(email_sender , email_receiver , em.as_string())