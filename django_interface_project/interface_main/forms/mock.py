from django import forms

from interface_main.forms.fields.json_field import JsonField


class MockForm(forms.Form):
    name = forms.CharField(max_length=200,
                           min_length=1,
                           required=True,
                           error_messages={'required': "name can not be empty"})
    description = forms.CharField(max_length=2000,
                                  min_length=1,
                                  required=True,
                                  error_messages={'required': "description can not be empty"})

    method = forms.CharField(max_length=20,
                             required=True,
                             error_messages={'required': "method can not be empty"})

    response = JsonField()
