#! /usr/bin/env python
import sys
import smtplib
import time
from email.message import EmailMessage
import constants
def write_stdout(s):
    # only eventlistener protocol messages may be sent to stdout
    sys.stdout.write(s)
    sys.stdout.flush()

def write_stderr(s):
    sys.stderr.write(s)
    sys.stderr.flush()

def send_email(crash_report):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(constants.EMAIL_TO_SEND_FROM, constants.EMAIL_TO_SEND_FROM_PASS)
    msg = EmailMessage()
    msg.set_content(constants.ALERT_MESSAGE.format(crash_report))
    msg['From'] = constants.EMAIL_TO_SEND_FROM
    msg['To'] = ", ".join(constants.ALERT_RECIPIENTS)
    msg['Subject'] = "ALERT: KUMM Outage at {}".format(time.strftime("%Y-%m-%d %I:%M-%p"))
    server.send_message(msg)
    server.quit()

def main():
    while 1:
        # transition from ACKNOWLEDGED to READY
        write_stdout('READY\n')

        # read header line and print it to stderr
        line = sys.stdin.readline()
        write_stderr(line+"\n")

        # read event payload and print it to stderr
        headers = dict([ x.split(':') for x in line.split() ])
        data = sys.stdin.read(int(headers['len']))
        send_email(data)
        write_stderr(data+"\n")

        # transition from READY to ACKNOWLEDGED
        write_stdout('RESULT 2\nOK')

if __name__ == '__main__':
    main()
