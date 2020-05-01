import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import time
import datetime as dt

html = Template(Path('index.html').read_text())
def send_email():
	email = EmailMessage()
	email['from'] = 'First_name Last_name'
	email['to'] = 'example@gmail.com'
	email['subject'] = 'Adding new car message!'
	email.set_content(html.substitute({'name':'TinTin'}), 'html')
	with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login('from_example_email@gmail.com', 'password')
		smtp.send_message(email)
def send_email_at(send_time):
	time.sleep(send_time.timestamp()-time.time())
	send_email()
	print('email sent')

first_email_time = dt.datetime(2020, 5, 1, 12, 9, 59)
interval = dt.timedelta(seconds=15)
send_time = first_email_time
while True:
	send_email_at(send_time)
	send_time = send_time+interval
