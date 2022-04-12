from django.test import TestCase

from apps.client.forms import ClientForm
from apps.client.models import Client


class TestClientForms(TestCase):
    form = ClientForm
    model = Client

    def test_client_forms(self):
        data = {
            'name': 'Client Name',
            'email': 'clientemail@example.com',
        }
        client_form = self.form(data=data)
        self.assertEqual(self.model.objects.all().count(), 0)

        if client_form.is_valid():
            client_form.save()
            dict_that_should_return = [
                {
                    'id': 1,
                    'name': 'Client Name',
                    'email': 'clientemail@example.com',
                }
            ]
            queryset = self.model.objects.values().all()
            dict_from_queryset = [entry for entry in queryset]
            dict_from_queryset[0].pop('created_at')
            dict_from_queryset[0].pop('updated_at')
            self.assertEqual(self.model.objects.all().count(), 1)
            self.assertEqual(dict_from_queryset, dict_that_should_return)
