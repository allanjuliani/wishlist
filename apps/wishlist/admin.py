from django.contrib import admin
from django.utils.translation import gettext as _

admin.site.index_title = _('Home')
admin.site.site_header = _('Wishlist Administration')
admin.site.site_title = admin.site.site_header
