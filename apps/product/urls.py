from django.urls import path

from apps.product.views import ProductView

urlpatterns = [
    path('', ProductView.as_view(), name='product'),
    path('<int:product_id>/', ProductView.as_view(), name='product'),
]
