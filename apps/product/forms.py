from django import forms
from django.utils.text import slugify

from apps.product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'price', 'brand', 'image', 'review_score')
