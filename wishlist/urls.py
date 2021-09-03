from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', include('apps.client.urls')),
    path('product/', include('apps.product.urls')),
]
