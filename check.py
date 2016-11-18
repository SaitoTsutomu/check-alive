import os, datetime, urllib.request
from time import sleep
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate

def send_mail(to, sub, body):
    charset = 'ISO-2022-JP'
    msg = MIMEText(body, 'plain', charset)
    msg['Subject'] = Header(sub, charset)
    msg['From'] = fr = os.environ.get('MAIL_USER')
    msg['To'] = to
    msg['Date'] = formatdate()
    with SMTP_SSL(os.environ.get('SMTP_HOST', 'smtp.gmail.com')) as smtp:
        smtp.login(fr, os.environ.get('MAIL_PASSWD'))
        smtp.sendmail(fr, [to], msg.as_string())

url = 'http://' + os.environ.get('TARGET', '127.0.0.1')
itv = int(os.environ.get('INTERVAL', '60'))
tmo = int(os.environ.get('TIME_OUT', '60'))
isdwn = False
while True:
    try:
        response = urllib.request.urlopen(url, timeout=tmo)
        html = response.read(1)
        isdwn = False
    except Exception as e:
        if not isdwn:
            isdwn = True
            send_mail(os.environ.get('MAIL_TO'), 'Site down',
                      'Down %s @%s\n%s'%(url, datetime.datetime.now(), e))
    sleep(itv)

