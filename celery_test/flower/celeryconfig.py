# coding=utf-8

address = '0.0.0.0'
port = 6100

# 日志相关
log_file_max_size = 104857600  # 10M
log_file_num_backups = 3        # 保留3个日志文件
log_file_prefix='/home/qfpay/monitor/flower/log/flower'
logging = 'DEBUG'  # 日志等级

# 业务相关
BROKER_URL = 'redis://192.10.30.19:4600/1'  # broker的URL
CELERY_TIMEZONE = 'Asia/Shanghai'  # 设置flower显示task的时区

# 页面相关
url_prefix = 'flower'  # url的前缀
auto_refresh = True  # dashboard是否自动刷新
persistent = True  # 持久化存储task信息
