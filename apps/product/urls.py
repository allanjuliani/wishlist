from django.urls import path

from apps.product.views import ProductView

app_name = 'product'

urlpatterns = [
    path('', ProductView.as_view(), name='product-views'),
    path('<int:product_id>/', ProductView.as_view(), name='product-views'),
]
