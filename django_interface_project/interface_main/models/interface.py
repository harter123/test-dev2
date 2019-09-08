from django.db import models
from interface_main.models.service import Service
from interface_main.models.fields.json_field import JsonField


# Create your models here.
class Interface(models.Model):
    name = models.CharField("接口的名称", default="", null=False, max_length=100)
    description = models.CharField("描述", default="", null=False, max_length=2000)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    path = models.CharField("path", default="", null=False, max_length=500)
    method = models.CharField("方法", default="get", null=False, max_length=20)
    params_type = models.CharField("json还是form", default="json", null=False, max_length=20)

    asserts = JsonField("断言")
    headers = JsonField("头部")
    params = JsonField("参数")
    response = models.TextField("响应", default="")
