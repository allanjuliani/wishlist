from django.utils.translation import gettext as _
from rest_framework import serializers

from apps.client.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'slug',
            'price',
            'image',
            'brand',
            'review_score',
            'created',
        ]
