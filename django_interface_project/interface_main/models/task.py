from django.db import models
from interface_main.models.fields.json_field import JsonField

# Create your models here.
from interface_main.models.interface import Interface


class Task(models.Model):
    name = models.CharField("mock的名称", default="", null=False, max_length=100)
    description = models.CharField("mock的描述", default="", null=False, max_length=2000)


# 任务和接口的关联表
class TaskInterfaceRelation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    interface = models.ForeignKey(Interface, on_delete=models.SET_NULL, null=True)
