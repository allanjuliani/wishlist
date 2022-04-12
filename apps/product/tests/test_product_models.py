from django.test import TestCase

from apps.client.models import Client
from apps.product.models import Favorite, Product


class TestProductModels(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            title='Product Name',
            brand='Brand New',
            image='https://dummyimage.com/300',
            price='99.99',
            review_score='5',
        )

        client = Client.objects.create(
            name='Client Name',
            email='clientemail@example.com',
        )

        self.favorite = Favorite.objects.create(
            product=self.product,
            client=client,
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Product Name - Brand New')

    def test_price_formatted(self):
        self.assertEqual(
            'R$ 99.99', Product.price_formatted.__get__(self.product)
        )

    def test_favorite_str(self):
        self.assertEqual(
            str(self.favorite),
            'Product Name - Brand New - Client Name - clientemail@example.com',
        )
