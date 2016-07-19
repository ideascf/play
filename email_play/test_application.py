# coding=utf-8
import xlwt
from io import BytesIO
from email.mime.application import MIMEApplication

excel = xlwt.Workbook('utf8')
bio = BytesIO()
excel.save(bio)

excel_data = bio.getvalue()

excel_msg = MIMEApplication(excel_data, _subtype='vnd.ms-excel')
excel_msg.add_header('Content-Disposition', 'attachment; filename="%s"' % 'test_filename')
print excel_msg.as_string()