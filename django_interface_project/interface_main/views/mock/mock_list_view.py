import json

from django.forms import model_to_dict
from django.views.generic import View

from interface_main.forms.mock import MockForm
from interface_main.models.mock import Mock
from interface_main.utils.calc import CalcUtils

from interface_main.utils.http_format import response_success
from interface_main.utils.log import default_log
from interface_main.exception.my_exception import MyException


class MockListView(View):

    def get(self, request, *args, **kwargs):
        """
        代表获取mock列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.GET
        size = int(data.get('size', 10))
        page = int(data.get('page', 1))
        results = Mock.objects.all()
        ret = CalcUtils.page_data(results, page, size)
        ret['list'] = [model_to_dict(i) for i in ret['list']]
        return response_success(ret)

    def post(self, request, *args, **kwargs):
        """
        代表的是创建mock
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        if not body:
            return response_success()
        data = json.loads(body)
        form = MockForm(data)
        if form.is_valid():
            Mock.objects.create(**form.cleaned_data)
            return response_success()
        else:
            print(form.errors.as_json())
            raise MyException()
