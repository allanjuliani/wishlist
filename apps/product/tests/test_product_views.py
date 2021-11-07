from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token

from apps.product.models import Product


class TestProductViews(TestCase):
    model = Product

    def setUp(self):
        user = User.objects.create(
            username='tester', is_superuser=True, is_staff=True
        )
        self.token = Token.objects.create(user=user)
        self.authorization_token = self.token.key
        data = {
            'title': 'Product Name',
            'brand': 'Brand New',
            'image': 'https://dummyimage.com/300',
            'price': 99.99,
            'review_score': 5,
        }
        response = self.client.post(
            reverse('product:product-views'),
            HTTP_AUTHORIZATION=self.authorization_token,
            data=data,
        )
        self.new_product = response.json()
        self.new_product.pop('created')

    def test_product_add(self):
        self.assertEquals(
            self.new_product,
            {
                'id': 1,
                'title': 'Product Name',
                'slug': 'product-name',
                'brand': 'Brand New',
                'image': 'https://dummyimage.com/300',
                'price': '99.99',
                'review_score': 5,
            },
        )

    def test_product_view(self):
        response = self.client.get(
            reverse('product:product-views', args=('1')),
            HTTP_AUTHORIZATION=self.authorization_token,
        )
        responses_data = response.json()

        for response_data in responses_data:
            response_data.pop('created')

        self.assertEquals(
            responses_data,
            [
                {
                    'id': 1,
                    'title': 'Product Name',
                    'slug': 'product-name',
                    'brand': 'Brand New',
                    'image': 'https://dummyimage.com/300',
                    'price': '99.99',
                    'review_score': 5,
                }
            ],
        )

    def test_product_view_not_found(self):
        response = self.client.get(
            reverse('product:product-views', args=('2')),
            HTTP_AUTHORIZATION=self.authorization_token,
        )

        self.assertEquals(response.json(), {'message': 'Product not found'})

    def test_product_update(self):
        data = {
            'title': 'Product New Name',
            'brand': 'Brand New',
            'image': 'https://dummyimage.com/300',
            'price': '199.99',
            'review_score': 5,
        }
        response = self.client.put(
            reverse('product:product-views', args=('1')),
            HTTP_AUTHORIZATION=self.authorization_token,
            data=data,
            content_type='application/json',
        )
        response_data = response.json()
        response_data.pop('created')

        self.assertEquals(
            response_data,
            {
                'id': 1,
                'title': 'Product New Name',
                'slug': 'product-new-name',
                'brand': 'Brand New',
                'image': 'https://dummyimage.com/300',
                'price': '199.99',
                'review_score': 5,
            },
        )

    def test_product_update_not_found(self):
        response = self.client.put(
            reverse('product:product-views', args=('2')),
            HTTP_AUTHORIZATION=self.authorization_token,
        )

        self.assertEquals(response.json(), {'message': 'Product not found'})

    def test_product_delete(self):
        response = self.client.delete(
            reverse('product:product-views', args=('1')),
            HTTP_AUTHORIZATION=self.authorization_token,
        )
        response_data = response.json()
        response_data.pop('created')

        self.assertEquals(
            response_data,
            {
                'id': None,
                'title': 'Product Name',
                'slug': 'product-name',
                'brand': 'Brand New',
                'image': 'https://dummyimage.com/300',
                'price': '99.99',
                'review_score': 5,
            },
        )

    def test_product_delete_not_found(self):
        response = self.client.delete(
            reverse('product:product-views', args=('2')),
            HTTP_AUTHORIZATION=self.authorization_token,
        )

        self.assertEquals(response.json(), {'message': 'Product not found'})
