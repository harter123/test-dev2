import traceback

from django.db import DatabaseError
from django.utils.deprecation import MiddlewareMixin
from interface_main.utils.http_format import response_success, response_failed
from interface_main.exception.my_exception import MyException, ErrorCode


class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):  # 会捕捉所有的请求
        # print('请求进来了')
        pass

    def process_response(self, request, response): # 会捕捉所有的响应
        # print('响应来了')
        return response

    def process_exception(self, request, exception): # 会捕捉所有的异常
        # print('捕捉到异常了')
        print(traceback.print_exc())
        if isinstance(exception, MyException):
            print('这是我的错误')
            code = exception.code
            message = exception.message
            return response_failed(code, message)

        elif isinstance(exception, DatabaseError):
            print('数据库错误')
            return response_failed(ErrorCode.DB, '数据库错误')
        else:
            print('未知错误')
            return response_failed(ErrorCode.UNKNOWN, '未知错误')
