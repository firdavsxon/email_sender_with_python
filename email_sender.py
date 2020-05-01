import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'First_name Last_name'
email['to'] = 'example@gmail.com'
email['subject'] = 'Adding new car message!'
email.set_content(html.substitute({'name':'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('example@gmail.com', 'password')
	for _ in range(3):
		smtp.send_message(email)
	print('All good boss!')