from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext as _

from product.models import Product


# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'created')
#     list_display_links = list_display
#     search_fields = ('title',)


# @admin.register(Favorite)
# class FavoriteAdmin(admin.ModelAdmin):
#     def user_link(self, obj):
#         return format_html('<a href="/admin/client/client/{id}">{full_name}</a>',
#                            id=obj.user.id, full_name=obj.user.full_name)
#     user_link.short_description = _('User')
#     user_link.admin_order_field = 'user__name'
#
#     def image_preview(self, obj):
#         if obj.product.image:
#             return format_html('<a href="/admin/product/product/{id}"><img width="100" src="{path}"></a>',
#                                id=obj.product.id, path=obj.product.image.url)
#     image_preview.short_description = _('Image')
#     image_preview.admin_order_field = 'image'
#
#     autocomplete_fields = ('client', 'product')
#     list_display = ('id', 'user_link', 'image_preview', 'created')
#     list_display_links = list_display
#     # Those filters client and product are here just for the test.
#     # In production with a lot of registers, they should be removed
#     list_filter = ('created', 'client', 'product')
#     search_fields = ('user__first_name', 'product__title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def clients_link(self, obj):
        total = obj.client_set.count()
        if total:
            return format_html(
                '<a href="{url}?products__id__exact={id}">{total}</a>',
                url=reverse('admin:client_client_changelist'),
                id=obj.id,
                total=total)
    clients_link.short_description = _('Clients')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img width="100" src="{path}">', path=obj.image)
        else:
            '-'
    image_preview.short_description = _('Image')
    image_preview.admin_order_field = 'image'

    def price_formatted(self, obj):
        return obj.price_formatted

    price_formatted.short_description = _('Price')
    price_formatted.admin_order_field = 'price'

    # autocomplete_fields = ('brand',)
    exclude = ('slug',)
    list_display = ('id', 'image_preview', 'title', 'price_formatted', 'brand', 'review_score', 'clients_link',
                    'created')
    list_display_links = list_display
    list_filter = ('created', 'review_score', 'brand')
    list_per_page = 20
    search_fields = ('title',)
