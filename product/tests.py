from django.test import TestCase

from product.models import Product


class ProductTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('== Product Test Case ==')

        Product.objects.create(
            title='Generic Product That Allow Everything Be Tested',
            price='9.99',
            image='',
            brand=brand,
            review_score=Product.ReviewScore.FIFTH_SCORE
        )
