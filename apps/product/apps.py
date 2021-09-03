from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'apps.product'
    verbose_name = _('Product')
