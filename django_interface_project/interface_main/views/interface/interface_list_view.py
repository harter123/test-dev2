import json

from django.forms import model_to_dict
from django.views.generic import View

from interface_main.forms.interface import InterfaceForm
from interface_main.models.interface import Interface
from interface_main.utils.calc import CalcUtils

from interface_main.utils.http_format import response_success
from interface_main.utils.log import default_log
from interface_main.exception.my_exception import MyException


class InterfacesListView(View):

    def get(self, request, *args, **kwargs):
        """
        代表获取接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.GET
        service_id = data.get('service_id', None)
        size = int(data.get('size', 10))
        page = int(data.get('page', 1))

        if service_id is None:
            results = Interface.objects.all()
        else:
            results = Interface.objects.filter(service_id=service_id)

        ret = CalcUtils.page_data(results, page, size)
        ret['list'] = [model_to_dict(i) for i in ret['list']]
        return response_success(ret)

    def post(self, request, *args, **kwargs):
        """
        代表的是创建接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        if not body:
            return response_success()
        data = json.loads(body)
        form = InterfaceForm(data)
        if form.is_valid():
            Interface.objects.create(**form.cleaned_data)
            return response_success()
        else:
            print(form.errors.as_json())
            raise MyException()
