from django.utils.translation import gettext as _
from rest_framework import serializers

from apps.client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'created']
