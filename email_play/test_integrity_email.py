# coding=utf-8

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.header import Header

ascii_msg = MIMEText('hello')
utf8_msg = MIMEText('你好', _charset='utf8')
image_msg = MIMEImage('')
excel_msg = MIMEApplication('', 'vnd.ms-excel')

e = MIMEMultipart()
e.attach(ascii_msg)
e.attach(utf8_msg)
e.attach(image_msg)
e.attach(excel_msg)


e['to'] = 'xxx@yyy.com'
e['from'] = 'yyy@xxx.com'
e['subject'] = Header('主题', charset='utf8')
print e.as_string()