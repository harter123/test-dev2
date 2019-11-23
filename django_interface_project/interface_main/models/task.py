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


# 任务的执行结果
class TaskResult(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    success = models.BooleanField('代表成功或者失败', default=False)
    create_time = models.DateTimeField('代表创建时间', auto_now_add=True)
    version = models.IntegerField('代表某一次的执行的版本', default=1)

    request = JsonField("参数")
    response = models.TextField("响应", default="")

