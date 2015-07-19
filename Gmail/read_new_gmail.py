#!/usr/bin/env python

import os.path
import sys

if not os.path.exists('/home/greg/Git/PandoraProject/out/new_email.txt'):
    sys.exit(0)  # File does not exist

with open('/home/greg/Git/RaspberryPi/out/new_email.txt') as f:
    for line in f:
        if 'Youtube' in line:
            print line
