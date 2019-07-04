from django.urls import path

from .views import home, month


urlpatterns = [
    path('', home, name='home'),
    path('volana/', month, name='month'),
]
