import json

from django.forms import model_to_dict
from django.views.generic import View

from interface_main.forms.task import TaskForm
from interface_main.models.task import Task
from interface_main.utils.http_format import response_success
from interface_main.utils.log import default_log
from interface_main.exception.my_exception import MyException


class TaskListView(View):

    def get(self, request, *args, **kwargs):
        """
        代表获取task liebiao
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        tasks = Task.objects.all()
        data = [model_to_dict(i) for i in tasks]
        return response_success(data)

    def post(self, request, *args, **kwargs):
        """
        代表的是创建task
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        if not body:
            return response_success()
        data = json.loads(body)
        form = TaskForm(data)
        if form.is_valid():
            # Service.objects.create(name=form.cleaned_data["name"],
            #                                              description=form.cleaned_data["description"],
            #                                              parent=form.cleaned_data["parent"])
            Task.objects.create(**form.cleaned_data)
            return response_success()
        else:
            raise MyException()
