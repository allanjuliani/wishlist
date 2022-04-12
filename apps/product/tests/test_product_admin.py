from django.test import TestCase

from apps.client.models import Client
from apps.product.admin import ProductAdmin
from apps.product.models import Product


class TestProductAdmin(TestCase):
    model = Product

    def setUp(self):
        client = Client.objects.create(
            name='Product Name', email='clientemail@example.com'
        )
        self.product = Product.objects.create(
            title='Product Name',
            brand='Brand New',
            image='https://dummyimage.com/300',
            price='99.99',
            review_score='5',
        )

        client.products.add(self.product)

    def test_clients_link(self):
        self.assertEqual(
            ProductAdmin.clients_link(None, self.product),
            '<a href="/admin/client/client/?products__id__exact=1">1</a>',
        )

    def test_image_preview(self):
        self.assertEqual(
            ProductAdmin.image_preview(None, self.product),
            '<img width="100" src="https://dummyimage.com/300">',
        )

    def test_price_formatted(self):
        self.assertEqual(
            ProductAdmin.price_formatted(None, self.product), '$ 99.99'
        )
