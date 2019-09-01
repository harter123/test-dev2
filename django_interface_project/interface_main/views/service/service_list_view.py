import json

from django.forms import model_to_dict
from django.views.generic import View
from interface_main.utils.http_format import response_success
from interface_main.utils.log import default_log
from interface_main.exception.my_exception import MyException
from interface_main.models.service import Service, ROOT_ID
from interface_main.forms.service import ServiceForm


class ServicesListView(View):
    @classmethod
    def get_service_tree_recursion(cls, parent):
        res = []
        children_nodes = Service.objects.filter(parent=parent)
        if children_nodes.count() == 0:
            return res

        if ROOT_ID == parent:
            parent_name = ""
        else:
            obj = Service.objects.filter(id=parent).first()
            if obj is None:
                parent_name = ""
            else:
                parent_name = obj.name

        for child in children_nodes:
            tmp = model_to_dict(child)
            tmp['children'] = cls.get_service_tree_recursion(child.id)
            tmp['parent_name'] = parent_name
            res.append(tmp)
        return res

    def get(self, request, *args, **kwargs):
        """
        代表获取服务的树形结构
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = self.get_service_tree_recursion(ROOT_ID)
        return response_success(data)

    def post(self, request, *args, **kwargs):
        """
        代表的是创建服务
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        if not body:
            return response_success()
        data = json.loads(body)
        form = ServiceForm(data)
        if form.is_valid():
            # Service.objects.create(name=form.cleaned_data["name"],
            #                                              description=form.cleaned_data["description"],
            #                                              parent=form.cleaned_data["parent"])
            Service.objects.create(**form.cleaned_data)
            return response_success()
        else:
            raise MyException()
