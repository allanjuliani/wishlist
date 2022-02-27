from rest_framework import serializers

from apps.client.models import Product
from apps.product.models import Favorite


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


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = [
            'id',
            'client',
            'product',
            'created_at',
            'updated_at',
        ]
