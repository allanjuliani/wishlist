from django import forms

from apps.product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'price', 'brand', 'image', 'review_score')
