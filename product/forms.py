from django import forms

from product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        widgets = {}
        fields = ('title', 'price', 'brand', 'image', 'review_score')
