from django import forms
# from django.forms import CharField

from client.models import Client


class ClientForm(forms.ModelForm):
    # name = CharField(required=False)
    # email = CharField(required=False)

    class Meta:
        model = Client
        fields = ('name', 'email')
