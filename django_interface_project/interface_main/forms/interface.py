from django import forms


class InterfaceForm(forms.Form):
    name = forms.CharField(max_length=200,
                           min_length=1,
                           required=True,
                           error_messages={'required': "name can not be empty"})
    description = forms.CharField(max_length=2000,
                                  min_length=1,
                                  required=True,
                                  error_messages={'required': "description can not be empty"})
    service_id = forms.IntegerField(required=True, min_value=1)
    path = forms.CharField(max_length=500,
                           required=True,
                           error_messages={'required': "path can not be empty"})
    method = forms.CharField(max_length=20,
                             required=True,
                             error_messages={'required': "method can not be empty"})
    params_type = forms.CharField(max_length=20,
                                  required=True,
                                  error_messages={'required': "params_type can not be empty"})
    response = forms.CharField(required=False, max_length=5000)
