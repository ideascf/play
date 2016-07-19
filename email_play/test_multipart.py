# coding=utf-8
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio

m = MIMEMultipart()

text = MIMEText('hello')
audio = MIMEAudio('')

m.attach(text)
m.attach(audio)
print m.as_string()