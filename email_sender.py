import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'First_name Last_name'
email['to'] = 'akilovfs@gmail.com'
email['subject'] = 'Adding new car message!'
email.set_content(html.substitute({'name':'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('dummy.bummy777@gmail.com', 'samar_uzb_1234')
	for _ in range(3):
		smtp.send_message(email)
	print('All good boss!')