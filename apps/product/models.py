from django.contrib.humanize.templatetags.humanize import intcomma
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _

# Initially I wanted to create the Brand as a foreign key, but, this would create a SQL inner join on every query.
# Was removed to the API be faster.
# class Brand(models.Model):
#     title = models.CharField(_('Title'), max_length=96, unique=True)
#     created = models.DateTimeField(_('Created'), auto_now_add=True)
#
#     def __str__(self):
#         return self.title


class Product(models.Model):
    # Choices in django 3.0 new style
    class ReviewScore(models.IntegerChoices):
        FIRST_SCORE = 1, _('★☆☆☆☆')
        SECOND_SCORE = 2, _('★★☆☆☆')
        THIRD_SCORE = 3, _('★★★☆☆')
        FOURTH_SCORE = 4, _('★★★★☆')
        FIFTH_SCORE = 5, _('★★★★★')

    title = models.CharField(_('Title'), max_length=255, unique=True)
    slug = models.SlugField(_('Slug'), max_length=255, unique=True)
    price = models.DecimalField(_('Price'), max_digits=8, decimal_places=2)
    image = models.URLField(_('Image'))
    brand = models.CharField(_('Brand'), max_length=96, db_index=True)
    review_score = models.SmallIntegerField(
        _('Review Score'), choices=ReviewScore.choices, null=True, blank=True
    )
    created = models.DateTimeField(_('Created'), auto_now_add=True)

    class Meta:
        db_table = 'product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def price_formatted(self):
        return 'R$ {price}'.format(price=intcomma(self.price))
