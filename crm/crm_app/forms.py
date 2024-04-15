from django.forms import ModelForm
from .models import Client, Service

class ClientForm(ModelForm):

    class Meta:
        model = Client
        fields = '__all__'

class ServiceForm(ModelForm):

    class Meta:
        model = Service
        fields = '__all__'

