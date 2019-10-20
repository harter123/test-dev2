import json

from django.forms import model_to_dict
from django.views.generic import View

from interface_main.forms.mock import MockForm
from interface_main.models.mock import Mock
from interface_main.utils.http_format import response_success
from interface_main.exception.my_exception import MyException


# Create your views here.
class MockDetailView(View):
    def get(self, request, mock_id, *args, **kwargs):
        """
        代表获取单个mock
        :param request:
        :param mock_id: mock的id
        :param args:
        :param kwargs:
        :return:
        """
        mock = Mock.objects.filter(id=mock_id).first()
        if mock is None:
            return response_success()
        else:
            return response_success(model_to_dict(mock))

    def put(self, request, mock_id, *args, **kwargs):
        """
        代表的是更新mock
        :param request:
        :param mock_id: mock的id
        :param args:
        :param kwargs:
        :return:
        """
        mock = Mock.objects.filter(id=mock_id).first()
        if mock is None:
            return response_success()

        body = request.body
        if not body:
            return response_success()
        data = json.loads(body)
        form = MockForm(data)
        if form.is_valid():
            Mock.objects.filter(id=mock_id).update(**form.cleaned_data)
            return response_success()
        else:
            raise MyException()

    def delete(self, request, mock_id, *args, **kwargs):
        """
        代表的是删除mock
        :param request:
        :param mock_id: mock的id
        :param args:
        :param kwargs:
        :return:
        """
        Mock.objects.filter(id=mock_id).delete()
        return response_success()
