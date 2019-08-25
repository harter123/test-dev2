from django.views.generic import View
from interface_main.utils.http_format import response_success
from interface_main.exception.my_exception import MyException


# Create your views here.
class UserInfoView(View):
    def get(self, request, *args, **kwargs):
        """
        代表获取用户的登录信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user = request.user
        if user.is_authenticated:  # 判断用户是否已经认证过了
            ret = {
                "username": user.username,
                "id": user.id,
            }
            return response_success(ret)
        else:
            raise MyException(message="用户没有登录")
