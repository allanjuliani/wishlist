from django.core.validators import validate_email
from django.db import models
from django.utils.translation import gettext as _

from product.models import Product


class Client(models.Model):
    name = models.CharField(_('Name'), max_length=96)
    email = models.EmailField(_('E-mail'), max_length=96, unique=True)
    products = models.ManyToManyField(Product, verbose_name=_('Product'), blank=True)
    created = models.DateTimeField(_('Created'), auto_now_add=True)

    class Meta:
        db_table = 'client'
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        validate_email(self.email)
        self.email = self.email.lower()
        super().save(*args, **kwargs)

    # @property
    # def full_name(self):
    #     return f'{self.first_name} {self.last_name}'
