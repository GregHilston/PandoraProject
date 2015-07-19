#!/usr/bin/env python

# Script dependent on: https://github.com/rg3/youtube-dl

import imaplib
import email
from subprocess import call

youtube_urls = []

# Used to easily get a substring
def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def extract_body(payload):
    if isinstance(payload, str):
        return payload
    else:
        return '\n'.join([extract_body(part.get_payload()) for part in payload])


conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
PASSWORD = "";

with open ("/home/pi/Git/PandoraProject/Conf/Gmail_Password.conf", "r") as myfile:
    PASSWORD=myfile.read().replace('\n', '')

conn.login("GrehgPi@gmail.com", PASSWORD)
conn.select()
typ, data = conn.search(None, 'UNSEEN')
try:
    for num in data[0].split():
        typ, msg_data = conn.fetch(num, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1])
                subject = msg['subject']
                # print('Subject: ' + str(subject))
                payload = msg.get_payload()
                body = extract_body(payload)
                # print('Body: ' + str(body))

                if 'Youtube' in subject:
                    youtube_urls.append(find_between(body, 'href="', '"')) # Parses the Youtube URL

        typ, response = conn.store(num, '+FLAGS', r'(\Seen)')
finally:
    try:
        conn.close()
    except:
        pass
    conn.logout()

for url in youtube_urls:
    call(["/usr/local/bin/youtube-dl", url, "-x", "--audio-format", "mp3", "-o", '~/Music/%(title)s.mp3'])
