from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext as _

from apps.client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    def products_link(self, obj):
        total = obj.products.all().count()
        if total:
            return format_html(
                '<a href="{url}?client__id__exact={id}">{total}</a>',
                url=reverse('admin:product_product_changelist'),
                id=obj.id,
                total=total,
            )

    products_link.short_description = _('Products')

    filter_horizontal = ('products',)
    list_display = ('id', 'name', 'email', 'products_link', 'created')
    list_display_links = list_display
    list_filter = ('created',)
    list_per_page = 20
    search_fields = ('email',)
