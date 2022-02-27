from django.urls import path

from apps.product.views import FavoriteView, ProductView

app_name = 'product'

urlpatterns = [
    path('', ProductView.as_view(), name='product-views'),
    path('<int:product_id>/', ProductView.as_view(), name='product-views'),
    path('favorite/', FavoriteView.as_view(), name='favorite-views'),
    path(
        'favorite/<int:favorite_id>/',
        FavoriteView.as_view(),
        name='favorite-views',
    ),
]
