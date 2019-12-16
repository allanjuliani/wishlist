from django import forms

from product.models import Product


# class FavoriteForm(forms.ModelForm):
#     class Meta:
#         model = Favorite
#         widgets = {}
#         fields = ('user', 'product')


# class BrandForm(forms.ModelForm):
#     class Meta:
#         model = Brand
#         widgets = {}
#         fields = ('title',)


class ProductForm(forms.ModelForm):
    # your_name = forms.CharField(label='Your name', max_length=100)
    class Meta:
        model = Product
        widgets = {}
        fields = ('title', 'price', 'brand', 'image', 'review_score')

    # def clean(self):
    #     import ipdb;ipdb.set_trace()
    #     cleaned_data = super().clean()
    #     # brand = cleaned_data.get('brand')
    #
    #     # brand_new = Brand.objects.get_or_create(title=brand)
