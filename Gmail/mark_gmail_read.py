#!/usr/bin/env python

import imaplib

PASSWORD = ""

with open ("~/Git/PandoraProject/Conf/Gmail_Password.txt", "r") as myfile:
    PASSWORD=myfile.read().replace('\n', '')

obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')
obj.login('GrehgPi', PASSWORD)
obj.select('Inbox') #  <--- it will select inbox
typ ,data = obj.search(None,'UnSeen')
obj.store(data[0].replace(' ',','),'+FLAGS','\Seen')
