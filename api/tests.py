from django.contrib.auth.models import User
from django.core.cache import cache
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from client.models import Client
from product.models import Product


class ApiTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        print('\n== API Test Case ==')
        cache.clear()

    def setUp(self):
        # Create admin user
        user = User.objects.create(username='tester', is_superuser=True, is_staff=True)

        # Crate token for every test
        self.token, created = Token.objects.get_or_create(user=user)

        # Create client base for show, update and delete test
        data = {'name': 'Client Base', 'email': 'client.base@example.com'}
        self.client_base = Client.objects.create(**data)

        # Create product base for show, update and delete test
        data = {
            'title': 'Product Base',
            'brand': 'Some',
            'image': 'https://placekitten.com/200/200',
            'price': '59.99',
        }
        self.product_base = Product.objects.create(**data)

    def test_client_add(self):
        """
        POST /api/client/
        data {'name': 'Client Add', 'email': 'useradd@example.com'}
        response {'success': True, 'message': 'New client created', 'data': {'client_id': 2}}
        """
        url = reverse('client-add')
        data = {'name': 'Client Add', 'email': 'useradd@example.com'}
        response = self.client.post(
            url, data, HTTP_AUTHORIZATION=f'Token {self.token}', format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'success': True,
                'message': 'New client created',
                'data': {'client_id': 2},
            },
        )

    def test_client_load(self):
        """
        GET /api/client/1/
        response {'success': True, 'data': {'id': 1, 'name': 'Client Base', 'email': 'client.base@example.com'}}
        """
        url = reverse('client-management', args=(self.client_base.id,))
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Token {self.token}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'success': True,
                'data': {
                    'id': 1,
                    'name': 'Client Base',
                    'email': 'client.base@example.com',
                },
            },
        )

    def test_client_update(self):
        """
        PUT /api/client/1/
        data {'name': 'Client New Name', 'email': 'client.base@example.com'}
        response {'success': True, 'message': 'Client 1 updated', 'data': {
            'id': 1, 'name': 'Client New Name',
            'email': 'client.base@example.com'}}
        """
        url = reverse('client-management', args=(self.client_base.id,))
        data = {'name': 'Client New Name', 'email': 'client.base@example.com'}
        response = self.client.put(
            url, data, HTTP_AUTHORIZATION=f'Token {self.token}', format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'success': True,
                'message': 'Client 1 updated',
                'data': {
                    'id': 1,
                    'name': 'Client New Name',
                    'email': 'client.base@example.com',
                },
            },
        )

    def test_client_delete(self):
        """
        DELETE /api/client/1/
        response {'success': True, 'message': 'Client 1 deleted'}
        """
        url = reverse('client-management', args=(self.client_base.id,))
        response = self.client.delete(url, HTTP_AUTHORIZATION=f'Token {self.token}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(), {'success': True, 'message': 'Client 1 deleted'}
        )

    def test_product_add(self):
        """
        POST /api/product/
        data {
            'title': 'Generic Product',
            'brand': 'Some',
            'image': 'https://placekitten.com/200/200',
            'price': 59.99,
            'review_score': 5
        }
        response {'success': True, 'message': 'New client created', 'data': {'new_product_id': 2}}
        """
        url = reverse('product-add')
        data = {
            'title': 'Generic Product',
            'brand': 'Some',
            'image': 'https://placekitten.com/200/200',
            'price': 59.99,
            'review_score': 5,
        }
        response = self.client.post(
            url, data, HTTP_AUTHORIZATION=f'Token {self.token}', format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'success': True,
                'message': 'New product created',
                'data': {'product_id': 2},
            },
        )

    def test_product_load(self):
        """
        GET /api/product/1/
        response {'success': True, 'data': {
            'title': 'Product Base',
            'brand': 'Some',
            'image': 'https://placekitten.com/200/200',
            'price': '59.99',
            'review_score': None,
        }
        """
        url = reverse('product-management', args=(self.product_base.id,))
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Token {self.token}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'success': True,
                'data': {
                    'title': 'Product Base',
                    'brand': 'Some',
                    'image': 'https://placekitten.com/200/200',
                    'price': '59.99',
                    'review_score': None,
                },
            },
        )

    def test_product_update(self):
        """
        PUT /api/product/1/
        response {'success': True, 'message': 'Product 1 updated', 'data': {
            'title': 'Product Updated',
            'brand': 'Some',
            'image': 'https://placekitten.com/200/200',
            'price': '29.99',
        }
        response {'id': 1, 'name': 'Client New Name', 'email': 'product.base@example.com'}
        """
        url = reverse('product-management', args=(self.product_base.id,))
        data = {
            'title': 'Product Updated',
            'brand': 'Some',
            'image': 'https://placekitten.com/200/200',
            'price': '29.99',
        }
        response = self.client.put(
            url, data, HTTP_AUTHORIZATION=f'Token {self.token}', format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'success': True,
                'message': 'Product 1 updated',
                'data': {
                    'title': 'Product Updated',
                    'brand': 'Some',
                    'image': 'https://placekitten.com/200/200',
                    'price': '29.99',
                },
            },
        )

    def test_product_delete(self):
        """
        DELETE /api/product/1/
        response {{'success': True, 'message': 'Product 1 deleted'}
        """
        url = reverse('product-management', args=(self.product_base.id,))
        response = self.client.delete(url, HTTP_AUTHORIZATION=f'Token {self.token}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(), {'success': True, 'message': 'Product 1 deleted'}
        )

    def test_client_add_product(self):
        """
        POST /api/client/product/
        data {'name': 'Client Add', 'email': 'useradd@example.com'}
        response {'success': True, 'message': 'Product favored',  'data': {
            'client_id': 1,
            'product_id': 1}}
        """
        url = reverse('client-products-management')
        data = {'client_id': 1, 'product_id': 1}
        response = self.client.post(
            url, data, HTTP_AUTHORIZATION=f'Token {self.token}', format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'success': True,
                'message': 'Product favored',
                'data': {'client_id': 1, 'product_id': 1},
            },
        )

    def test_client_delete_product(self):
        """
        POST /api/client/product/
        data {'name': 'Client Add', 'email': 'useradd@example.com'}
        response  {'success': True, 'message': 'Product removed from favorite', 'data': {
            'client_id': 1,
            'product_id': 1}}
        """
        url = reverse('client-products-management')
        data = {'client_id': 1, 'product_id': 1}
        self.client.post(
            url, data, HTTP_AUTHORIZATION=f'Token {self.token}', format='json'
        )
        response = self.client.delete(
            url, data, HTTP_AUTHORIZATION=f'Token {self.token}', format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'success': True,
                'message': 'Product removed from favorites',
                'data': {'client_id': 1, 'product_id': 1},
            },
        )

    def test_client_products_load(self):
        """
        POST /api/client/1/product/
        """
        url = reverse('client-products-management')
        data = {'client_id': 1, 'product_id': 1}
        self.client.post(
            url, data, HTTP_AUTHORIZATION=f'Token {self.token}', format='json'
        )

        url = reverse('client-products', args=(self.client_base.id,))
        response = self.client.get(
            url, HTTP_AUTHORIZATION=f'Token {self.token}', format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'success': True,
                'data': [
                    {
                        'id': 1,
                        'title': 'Product Base',
                        'brand': 'Some',
                        'image': 'https://placekitten.com/200/200',
                        'price': '59.99',
                        'review_score': None,
                    }
                ],
                'next_page': None,
                'prev_page': None,
            },
        )
