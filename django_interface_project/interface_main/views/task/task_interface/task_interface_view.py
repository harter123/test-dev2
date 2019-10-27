import json

from django.forms import model_to_dict
from interface_main.models.interface import Interface
from interface_main.models.task import Task, TaskInterfaceRelation
from interface_main.utils.http_format import response_success
from interface_main.utils.log import default_log


def task_add_interface(request, task_id, interface_id):
    task = Task.objects.filter(id=task_id).first()
    if task is None:
        return response_success()

    interface = Interface.objects.filter(id=interface_id).first()
    if interface is None:
        return response_success()

    TaskInterfaceRelation.objects.create(task=task, interface=interface)
    return response_success()


def task_remove_interface(request, task_interface_id):
    TaskInterfaceRelation.objects.filter(id=task_interface_id).delete()
    return response_success()


def task_get_interfaces(request, task_id):
    task = Task.objects.filter(id=task_id).first()
    if task is None:
        return response_success([])
    tis = TaskInterfaceRelation.objects.filter(task=task)
    ret = []
    for i in tis:
        interface = i.interface
        data = model_to_dict(interface)
        data["task_interface_id"] = i.id
        ret.append(data)
    return response_success(ret)
