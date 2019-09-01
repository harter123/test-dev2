from django import forms


class ServiceForm(forms.Form):
    name = forms.CharField(max_length=200,
                           min_length=1,
                           required=True,
                           error_messages={'required': "name can not be empty"})
    description = forms.CharField(max_length=2000,
                                  min_length=1,
                                  required=True,
                                  error_messages={'required': "description can not be empty"})

    parent = forms.IntegerField(required=False)
