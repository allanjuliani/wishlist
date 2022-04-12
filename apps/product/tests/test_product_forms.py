from decimal import Decimal

from django.test import TestCase

from apps.product.forms import ProductForm
from apps.product.models import Product


class TestProductForms(TestCase):
    form = ProductForm
    model = Product

    def test_product_forms(self):
        data = {
            'title': 'Product Name',
            'brand': 'Brand New',
            'image': 'https://dummyimage.com/300',
            'price': 99.99,
            'review_score': 5,
        }
        product_form = self.form(data=data)
        self.assertEquals(self.model.objects.all().count(), 0)

        if product_form.is_valid():
            product_form.save()
            dict_that_should_return = [
                {
                    'id': 1,
                    'title': 'Product Name',
                    'slug': 'product-name',
                    'brand': 'Brand New',
                    'image': 'https://dummyimage.com/300',
                    'price': Decimal('99.99'),
                    'review_score': 5,
                }
            ]
            queryset = self.model.objects.values().all()
            dict_from_queryset = [entry for entry in queryset]
            dict_from_queryset[0].pop('created_at')
            dict_from_queryset[0].pop('updated_at')
            self.assertEquals(self.model.objects.all().count(), 1)
            self.assertEqual(dict_from_queryset, dict_that_should_return)
