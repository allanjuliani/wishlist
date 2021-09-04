from django.test import TestCase

from apps.client.admin import ClientAdmin
from apps.client.models import Client
from apps.product.models import Product


class TestClientAdmin(TestCase):
    model = Client

    def setUp(self):
        self.client = self.model.objects.create(
            name='Client Name', email='clientemail@example.com'
        )
        product = Product.objects.create(
            title='Product Name',
            brand='Brand New',
            image='https://dummyimage.com/300',
            price='99.99',
            review_score='5',
        )

        self.client.products.add(product)

    def test_products_link(self):
        self.assertEqual(
            ClientAdmin.products_link(None, self.client),
            '<a href="/admin/product/product/?client__id__exact=1">1</a>',
        )
