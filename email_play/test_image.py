# coding=utf-8

from email.mime.image import MIMEImage

image_data = ''
image_msg = MIMEImage(image_data)
print image_msg.as_string()