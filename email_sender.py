import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Python Test'
email['to'] = 'name@gmail.com'
email['subject'] = 'python message!'
email.set_content('I am a python master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('name@gmail.com', 'password')
	for _ in range(3):
		smtp.send_message(email)
	print('All good boss!')