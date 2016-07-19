# coding=utf-8

from email.mime.audio import MIMEAudio

audio_data = ''
audio_msg = MIMEAudio(audio_data)
print audio_msg.as_string()