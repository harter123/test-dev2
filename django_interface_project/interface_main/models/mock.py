from django.db import models
from interface_main.models.fields.json_field import JsonField


# Create your models here.
class Mock(models.Model):
    name = models.CharField("mock的名称", default="", null=False, max_length=100)
    description = models.CharField("mock的描述", default="", null=False, max_length=2000)
    method = models.CharField("方法", default="get", null=False, max_length=20)
    response = JsonField("响应")

