from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token


class TestProductViews(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='tester', is_superuser=True, is_staff=True
        )
        self.token = Token.objects.create(user=user)
        self.authorization_token = self.token.key

        response = self.client.post(
            reverse('product:product-views'),
            HTTP_AUTHORIZATION=self.authorization_token,
            data={
                'title': 'Product Name',
                'brand': 'Brand New',
                'image': 'https://dummyimage.com/300',
                'price': 99.99,
                'review_score': 5,
            },
        )
        self.new_product = response.json()
        self.new_product.pop('created_at')
        self.new_product.pop('updated_at')

        response = self.client.post(
            reverse('client:client-views'),
            HTTP_AUTHORIZATION=self.authorization_token,
            data={
                'name': 'Client Name',
                'email': 'clientemail@example.com',
            },
        )
        self.new_client = response.json()

        response = self.client.post(
            reverse('product:favorite-views'),
            HTTP_AUTHORIZATION=self.authorization_token,
            data={
                'client': self.new_client.get('id'),
                'product': self.new_product.get('id'),
            },
        )
        self.new_favorite = response.json()

    def test_product_add(self):
        self.assertEqual(
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
            response_data.pop('created_at')
            response_data.pop('updated_at')

        self.assertEqual(
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

        self.assertEqual(response.json(), {'message': 'Product not found'})

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
        response_data.pop('created_at')
        response_data.pop('updated_at')

        self.assertEqual(
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

        self.assertEqual(response.json(), {'message': 'Product not found'})

    def test_product_delete(self):
        response = self.client.delete(
            reverse('product:product-views', args=('1')),
            HTTP_AUTHORIZATION=self.authorization_token,
        )
        response_data = response.json()
        response_data.pop('created_at')
        response_data.pop('updated_at')

        self.assertEqual(
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

        self.assertEqual(response.json(), {'message': 'Product not found'})

    def test_favorite_delete(self):
        response = self.client.delete(
            reverse('product:favorite-views', args=('1')),
            HTTP_AUTHORIZATION=self.authorization_token,
        )
        response_data = response.json()
        response_data.pop('created_at')

        self.assertEqual(
            response_data,
            {
                'id': None,
                'client': 1,
                'product': 1,
            },
        )

    def test_favorite_delete_not_found(self):
        response = self.client.delete(
            reverse('product:favorite-views', args=('2')),
            HTTP_AUTHORIZATION=self.authorization_token,
        )

        self.assertEqual(response.json(), {'message': 'Favorite not found'})

    def test_favorite_view(self):
        response = self.client.get(
            reverse('product:favorite-views', args=('1')),
            HTTP_AUTHORIZATION=self.authorization_token,
        )
        responses_data = response.json()

        for response_data in responses_data:
            response_data.pop('created_at')

        self.assertEqual(
            responses_data,
            [
                {
                    'id': 1,
                    'client': 1,
                    'product': 1,
                }
            ],
        )

    def test_favorite_view_not_found(self):
        response = self.client.get(
            reverse('product:favorite-views', args=('2')),
            HTTP_AUTHORIZATION=self.authorization_token,
        )

        self.assertEqual(response.json(), {'message': 'Favorite not found'})
