from django.urls import path

from apps.api.views import ClientView, client_product_load, client_products_management, product_add, product_management

urlpatterns = [
    path('client/', ClientView.as_view(), name='client'),
    path('client/<int:client_id>/', ClientView.as_view(), name='client'),
    path(
        'client/product/', client_products_management, name='client-products-management'
    ),
    path(
        'client/<int:client_id>/products/', client_product_load, name='client-products'
    ),
    path('product/', product_add, name='product-add'),
    path('product/<int:product_id>/', product_management, name='product-management'),
]
