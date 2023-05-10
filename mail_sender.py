import os
import smtplib 

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('EMAIL_ADDRESS', 'EMAIL_PASS')
    subject = 'lets get party'
    body  = 'ok lets go and drink some water also'
    
    msg = f'subject {subject}\n\n{body}'
    smtp.sendmail('EMAIL_ADDRESS','karkirajan6543210@gmail.com', msg)