from django.urls import path

from api.views import (client_add, client_management, client_product_load,
                       client_products_management, product_add,
                       product_management)

urlpatterns = [
    path('client/', client_add, name='client-add'),
    path('client/<int:client_id>/', client_management, name='client-management'),
    path(
        'client/product/', client_products_management, name='client-products-management'
    ),
    path(
        'client/<int:client_id>/products/', client_product_load, name='client-products'
    ),
    path('product/', product_add, name='product-add'),
    path('product/<int:product_id>/', product_management, name='product-management'),
]
