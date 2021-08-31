from django.utils.translation import gettext as _
from rest_framework import serializers

from apps.client.forms import ClientForm
from apps.client.models import Client

# class LoadClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = ['id', 'name', 'email', 'created']


# class ClientSerializer(serializers.Serializer):
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'created']

    # def create(self, validated_data):
    #     # __import__('ipdb').set_trace()
    #     client_form = ClientForm(validated_data)
    #
    #     if client_form.is_valid():
    #         user = client_form.save()
    #         return {
    #             'success': True,
    #             'message': _('New client created'),
    #             'data': {'client_id': user.id},
    #         }
    #     else:
    #         raise serializers.ValidationError(client_form.errors.as_json())

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.created = validated_data.get('created', instance.created)
    #     return instance
