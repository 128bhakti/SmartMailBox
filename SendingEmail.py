import smtplib
import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(4,IO.IN)
while 1:
time.sleep(0.5)
if(IO.input(4)==False):
smtpUser = 'smartmailbox703@gmail.com'
smtpPass = 'smart@703'
toAdd='gandhirachana703@gmail.com'
fromAdd = smtpUser
subject= 'You have a new mail in your Postbox'
header = 'To: '+toAdd+'\n'+'From: '+fromAdd+'\n'+'Subject: '+subject
body='Message sent fom a Python script'
print header +'\n'+ body
s=smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(smtpUser,smtpPass)
s.sendmail(fromAdd,toAdd,header+'\n\n'+body)
s.quit()
