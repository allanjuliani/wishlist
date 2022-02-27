from django.contrib.humanize.templatetags.humanize import intcomma
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _


class Product(models.Model):
    class ReviewScore(models.IntegerChoices):
        FIRST_SCORE = 1, _('⭐')
        SECOND_SCORE = 2, _('⭐⭐')
        THIRD_SCORE = 3, _('⭐⭐⭐')
        FOURTH_SCORE = 4, _('⭐⭐⭐⭐')
        FIFTH_SCORE = 5, _('⭐⭐⭐⭐⭐')

    title = models.CharField(_('Title'), max_length=255, unique=True)
    slug = models.SlugField(_('Slug'), max_length=255, unique=True, null=True)
    price = models.DecimalField(_('Price'), max_digits=8, decimal_places=2)
    image = models.URLField(_('Image'))
    brand = models.CharField(_('Brand'), max_length=96, db_index=True)
    review_score = models.SmallIntegerField(
        _('Review Score'), choices=ReviewScore.choices, null=True, blank=True
    )
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        db_table = 'product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return f'{self.title} - {self.brand}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def price_formatted(self):
        return _('R$ {price}').format(price=intcomma(self.price))


class Favorite(models.Model):
    client = models.ForeignKey(
        "client.Client", verbose_name=_("Client"), on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "product.Product", verbose_name=_("Product"), on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    class Meta:
        unique_together = (('client', 'product'),)
        verbose_name = _('Favorite')
        verbose_name_plural = _('Favorites')

    def __str__(self):
        return f'{self.product} - {self.client}'
