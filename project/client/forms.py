from django.forms import ModelForm
from interface.models import Client

class Client(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'password']
