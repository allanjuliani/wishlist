from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext as _

from apps.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def clients_link(self, obj):
        total = obj.client_set.count()
        if total:
            return format_html(
                '<a href="{url}?products__id__exact={id}">{total}</a>',
                url=reverse('admin:client_client_changelist'),
                id=obj.id,
                total=total,
            )

    clients_link.short_description = _('Clients')  # type: ignore

    def image_preview(self, obj):
        return format_html('<img width="100" src="{path}">', path=obj.image)

    image_preview.short_description = _('Image')  # type: ignore
    image_preview.admin_order_field = 'image'  # type: ignore

    def price_formatted(self, obj):
        return obj.price_formatted

    price_formatted.short_description = _('Price')  # type: ignore
    price_formatted.admin_order_field = 'price'  # type: ignore

    exclude = ('slug',)
    list_display = (
        'id',
        'image_preview',
        'title',
        'price_formatted',
        'brand',
        'review_score',
        'clients_link',
        'created',
    )
    list_display_links = list_display
    list_filter = ('created', 'review_score', 'brand')
    list_per_page = 20
    search_fields = ('title',)
