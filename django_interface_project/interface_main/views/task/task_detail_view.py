import json

from django.forms import model_to_dict
from django.views.generic import View

from interface_main.forms.task import TaskForm
from interface_main.models.task import Task
from interface_main.utils.http_format import response_success
from interface_main.exception.my_exception import MyException


# Create your views here.
class TaskDetailView(View):
    def get(self, request, task_id, *args, **kwargs):
        """
        代表获取单个task
        :param request:
        :param task_id: task的id
        :param args:
        :param kwargs:
        :return:
        """
        task = Task.objects.filter(id=task_id).first()
        if task is None:
            return response_success()
        else:
            return response_success(model_to_dict(task))

    def put(self, request, task_id, *args, **kwargs):
        """
        代表的是更新task
        :param request:
        :param task_id: 服务的id
        :param args:
        :param kwargs:
        :return:
        """
        task = Task.objects.filter(id=task_id).first()
        if task is None:
            return response_success()

        body = request.body
        if not body:
            return response_success()
        data = json.loads(body)
        form = TaskForm(data)
        if form.is_valid():
            # Service.objects.filter(id=service_id).update(name=form.cleaned_data["name"],
            #                                              description=form.cleaned_data["description"],
            #                                              parent=form.cleaned_data["parent"])
            Task.objects.filter(id=task_id).update(**form.cleaned_data)
            return response_success()
        else:
            raise MyException()

    def delete(self, request, task_id, *args, **kwargs):
        """
        代表的是删除task
        :param request:
        :param task_id: task的id
        :param args:
        :param kwargs:
        :return:
        """
        Task.objects.filter(id=task_id).delete()
        return response_success()
