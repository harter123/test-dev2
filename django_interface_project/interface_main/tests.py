from django.test import TestCase

# Create your tests here.
from interface_main.utils.http_format import response_failed, response_success


def task_test1_get(request):

    method = request.method

    if "get" == method or "GET" == method:
        return response_success({'mytest': "test1"})
    else:
        return response_failed()


def task_test2_post(request):

    method = request.method
    if "post" == method or "POST" == method:
        return response_success({'mytest': "test2"})
    else:
        return response_failed()