from django.test import TestCase

from apps.product.models import Product


class TestProductModels(TestCase):
    model = Product

    def setUp(self):
        self.product = self.model.objects.create(
            title='Product Name',
            brand='Brand New',
            image='https://dummyimage.com/300',
            price='99.99',
            review_score='5',
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Product Name - Brand New')

    def test_price_formatted(self):
        self.assertEqual(
            'R$ 99.99', Product.price_formatted.__get__(self.product)
        )
