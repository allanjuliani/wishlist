from django.db import IntegrityError
from django.test import TestCase

from apps.product.models import Product


class ProductTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('\n== Product Test Case ==')

        Product.objects.create(
            title='Generic Product That Allow Everything Be Tested',
            price='9.99',
            brand='Some',
            image='https://placekitten.com/200/200',
            review_score=Product.ReviewScore.FIFTH_SCORE,
        )

    def test_title_unique_field(self):
        with self.assertRaises(Exception) as raised:
            Product.objects.create(
                title='Generic Product That Allow Everything Be Tested',
                price='9.99',
                brand='Some',
                image='https://placekitten.com/200/200',
                review_score=Product.ReviewScore.FIFTH_SCORE,
            )

        self.assertEqual(IntegrityError, type(raised.exception))
