# coding=utf-8

from email.mime.text import MIMEText

ascii_msg = MIMEText('hello world')
print ascii_msg.as_string()

# specify charset
utf8_msg = MIMEText('你好世界', _charset='utf8')
print utf8_msg.as_string()

# maybe can't be parsed, on some EMAIL client.
utf8_msg_err = MIMEText('你好世界')
print utf8_msg_err.as_string()