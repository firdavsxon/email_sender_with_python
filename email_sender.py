import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Firdavs Akilov'
email['to'] = 'akilovfs@gmail.com'
email['subject'] = 'You won 1 000 000 dollars!'
email.set_content('I am a python master')

with smtplib.SMTP(host='gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('dummy.bummy777@gmail.com', 'apartment104')
	smtp.send_message(email)
	print('All good boss!')