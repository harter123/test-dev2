import json

from django.forms import model_to_dict
from django.views.generic import View

from interface_main.forms.interface import InterfaceForm
from interface_main.models.interface import Interface
from interface_main.utils.http_format import response_success
from interface_main.exception.my_exception import MyException


# Create your views here.
class InterfaceDetailView(View):
    def get(self, request, interface_id, *args, **kwargs):
        """
        代表获取单个接口
        :param request:
        :param interface_id: 接口的id
        :param args:
        :param kwargs:
        :return:
        """
        service = Interface.objects.filter(id=interface_id).first()
        if service is None:
            return response_success()
        else:
            return response_success(model_to_dict(service))

    def put(self, request, interface_id, *args, **kwargs):
        """
        代表的是更新接口
        :param request:
        :param interface_id: 接口的id
        :param args:
        :param kwargs:
        :return:
        """
        interface = Interface.objects.filter(id=interface_id).first()
        if interface is None:
            return response_success()

        body = request.body
        if not body:
            return response_success()
        data = json.loads(body)
        form = InterfaceForm(data)
        if form.is_valid():
            Interface.objects.filter(id=interface_id).update(**form.cleaned_data)
            return response_success()
        else:
            raise MyException()

    def delete(self, request, interface_id, *args, **kwargs):
        """
        代表的是删除接口
        :param request:
        :param interface_id: 服务的id
        :param args:
        :param kwargs:
        :return:
        """
        Interface.objects.filter(id=interface_id).delete()
        return response_success()
