from django.core.cache import cache
from django.core.validators import validate_email
from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext as _

from apps.product.models import Product


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
        return self.name or ''

    def save(self, *args, **kwargs):
        validate_email(self.email)
        self.email = self.email.lower()
        super().save(*args, **kwargs)


# Clear user get cache on add or remove product
@receiver(models.signals.m2m_changed)
def clean_user_cache(sender, instance, **kwargs):
    if kwargs.get('action') in ['post_add', 'post_remove']:
        for i in range(1, 999):
            if cache.get(f'client_get_{instance.id}_{i}'):
                cache.delete(f'client_get_{instance.id}_{i}')
            else:
                break
