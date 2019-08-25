import json
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from interface_main.forms.user import UserForm

from interface_main.utils.http_format import response_success
from interface_main.utils.log import default_log
from interface_main.exception.my_exception import MyException


# Create your views here.
class UsersView(View):
    def get(self, request, *args, **kwargs):
        """
        代表登录
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = UserForm(request.GET)
        result = form.is_valid()
        if not result:
            default_log.error(form.errors.as_json())
            raise MyException()

        user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        if user:
            login(request, user)  # 登录持久化， 生成session
            return response_success("登录成功")
        else:
            raise MyException(message="登录失败")

    def post(self, request, *args, **kwargs):
        """
        代表的是注册
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body  # 返回的是字符串
        data = json.loads(body)  # 把字符串进行解析为字典

        form = UserForm(data)
        result = form.is_valid()
        if not result:
            default_log.error(form.errors.as_json())
            raise MyException()

        if User.objects.filter(username=form.cleaned_data["username"]).exists():
            raise MyException(message="用户已存在")

        user = User.objects.create_user(username=form.cleaned_data["username"],
                                        password=form.cleaned_data["password"])
        if user:
            login(request, user)  # 登录持久化， 生成session
            return response_success("注册成功")
        else:
            raise MyException(message="注册失败")


    def delete(self, request, *args, **kwargs):
        """
        代表的是注销
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        logout(request)
        return response_success("注销成功")