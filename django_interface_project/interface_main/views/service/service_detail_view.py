import json

from django.forms import model_to_dict
from django.views.generic import View

from interface_main.utils.http_format import response_success
from interface_main.exception.my_exception import MyException

from interface_main.models.service import Service
from interface_main.forms.service import ServiceForm


# Create your views here.
class ServiceDetailView(View):
    def get(self, request, service_id, *args, **kwargs):
        """
        代表获取单个服务
        :param request:
        :param service_id: 服务的id
        :param args:
        :param kwargs:
        :return:
        """
        service = Service.objects.filter(id=service_id).first()
        if service is None:
            return response_success()
        else:
            return response_success(model_to_dict(service))

    def put(self, request, service_id, *args, **kwargs):
        """
        代表的是更新服务
        :param request:
        :param service_id: 服务的id
        :param args:
        :param kwargs:
        :return:
        """
        service = Service.objects.filter(id=service_id).first()
        if service is None:
            return response_success()

        body = request.body
        if not body:
            return response_success()
        data = json.loads(body)
        form = ServiceForm(data)
        if form.is_valid():
            # Service.objects.filter(id=service_id).update(name=form.cleaned_data["name"],
            #                                              description=form.cleaned_data["description"],
            #                                              parent=form.cleaned_data["parent"])
            Service.objects.filter(id=service_id).update(**form.cleaned_data)
            return response_success()
        else:
            raise MyException()

    def delete(self, request, service_id, *args, **kwargs):
        """
        代表的是删除服务
        :param request:
        :param service_id: 服务的id
        :param args:
        :param kwargs:
        :return:
        """
        Service.objects.filter(id=service_id).delete()
        return response_success()
