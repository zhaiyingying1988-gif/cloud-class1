from rest_framework.response import Response
from django.db import DatabaseError
from rest_framework.views import exception_handler
import logging

log = logging.getLogger('django')

#  在产生结果的地方记录日志

# log.info('')
# log.error('')
def custom_exception_handler(exc,context):
    response = exception_handler(exc ,context)
    if response is None and isinstance(exc ,DatabaseError):
        log.error('当前服务器错误%s'%exc)
        return Response({'message:':'服务器内容不存在'},status=500)