from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from client.models import Client


class ClientModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('\n== Client Model Test Case ==')

        Client.objects.create(name='Allan', email='allan.s.juliani@gmail.com')

    def test_email_unique_field(self):
        with self.assertRaises(Exception) as raised:
            Client.objects.create(name='Allan', email='allan.s.juliani@gmail.com')

        self.assertEqual(IntegrityError, type(raised.exception))

    def test_invalid_email(self):
        with self.assertRaises(Exception) as raised:
            Client.objects.create(name='Allan', email='allan.s.juliani@gmail')

        self.assertEqual(ValidationError, type(raised.exception))

    def test_not_null_name(self):
        with self.assertRaises(Exception) as raised:
            Client.objects.create(name=None, email='allan.s.juliani@gmail.com')

        self.assertEqual(IntegrityError, type(raised.exception))
