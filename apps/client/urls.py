from django.urls import path

from apps.client.views import ClientView

app_name = 'client'

urlpatterns = [
    path('', ClientView.as_view(), name='client-views'),
    path('<int:client_id>/', ClientView.as_view(), name='client-views'),
]
