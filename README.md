# SmartMailBox
 A Smart Mail Box as a part of Home Automation under Internet of Things, developed using R-pi and IR sensor.
 
Smart mail box will have an IR Sensor attached to the inside of the postbox. Whenever a post is dropped into the postbox, the user is notified that you have a new mail in your postbox through gmail.

![smartmailbox_Architectue](https://user-images.githubusercontent.com/36333782/56877972-4ac74c00-6a6f-11e9-8b2b-b12060bf3cb1.jpg)

## Technologies:
Python Script for IR Sensor and SMTP Mail Protocol into Raspberry Pi.
## Protocol:
SMTP- The Simple Mail Transfer Protocol (SMTP) is a communication protocol for electronic mail transmission. SMTP moves your email on and across networks. It works closely with something called the Mail Transfer Agent (MTA) to send your communication to the right computer and email inbox.

To access mail utility type command: Sudo apt-get install sssmtp mailutils

## SMTP configuration:
command: sudo nano etc/ssmtp/ssmtp.conf

hostname=raspberry pi

AuthUser=senders_email_id

AuthPass= senders_email_password

UseSTARTTLS=YES

UseTLS=YES
