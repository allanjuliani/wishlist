from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ClientConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'apps.client'
    verbose_name = _('Client')
