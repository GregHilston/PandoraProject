#!/usr/bin/env python

# See: http://mitchtech.net/connect-raspberry-pi-to-gmail-facebook-twitter-more/ for dependencies 

import feedparser

USERNAME = "GrehgPi@gmail.com"
PASSWORD = ""

with open ("~/Git/PandoraProject/Conf/Gmail_Password.txt", "r") as myfile:
    PASSWORD=myfile.read().replace('\n', '')

response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")
unread_count = int(response["feed"]["fullcount"])

f = open('/home/greg/Git/RaspberryPi/Logs/new_email.txt', 'w')

for i in range(0, unread_count):
    f.write("(" + str((i + 1)) + "/" + str(unread_count) + ") " + response['items'][i].title + "\n")

f.close()
