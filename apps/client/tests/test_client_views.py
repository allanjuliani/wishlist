from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token

from apps.client.models import Client


class TestClientViews(TestCase):
    model = Client

    def setUp(self):
        user = User.objects.create(username='tester', is_superuser=True, is_staff=True)
        self.token = Token.objects.create(user=user)
        self.authorization_token = self.token.key
        data = {
            'name': 'Client Name',
            'email': 'clientemail@example.com',
        }
        response = self.client.post(
            reverse('client:client-views'),
            HTTP_AUTHORIZATION=self.authorization_token,
            data=data,
        )
        self.new_client = response.json()
        self.new_client.pop('created')

    def test_client_add(self):
        self.assertEquals(
            self.new_client,
            {
                'id': 1,
                'name': 'Client Name',
                'email': 'clientemail@example.com',
            },
        )

    def test_client_view(self):
        response = self.client.get(
            reverse('client:client-views', args=('1')),
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
                    'name': 'Client Name',
                    'email': 'clientemail@example.com',
                },
            ],
        )

    def test_client_view_not_found(self):
        response = self.client.get(
            reverse('client:client-views', args=('2')),
            HTTP_AUTHORIZATION=self.authorization_token,
        )

        self.assertEquals(response.json(), {'message': 'Client not found'})

    def test_client_update(self):
        data = {
            'name': 'Client Name',
            'email': 'new_email@example.com',
        }
        response = self.client.put(
            reverse('client:client-views', args=('1')),
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
                'name': 'Client Name',
                'email': 'new_email@example.com',
            },
        )

    def test_client_update_not_found(self):
        response = self.client.put(
            reverse('client:client-views', args=('2')),
            HTTP_AUTHORIZATION=self.authorization_token,
        )

        self.assertEquals(response.json(), {'message': 'Client not found'})

    def test_client_delete(self):
        response = self.client.delete(
            reverse('client:client-views', args=('1')),
            HTTP_AUTHORIZATION=self.authorization_token,
        )
        response_data = response.json()
        response_data.pop('created')

        self.assertEquals(
            response_data,
            {
                'id': None,
                'name': 'Client Name',
                'email': 'clientemail@example.com',
            },
        )

    def test_client_delete_not_found(self):
        response = self.client.delete(
            reverse('client:client-views', args=('2')),
            HTTP_AUTHORIZATION=self.authorization_token,
        )

        self.assertEquals(response.json(), {'message': 'Client not found'})
