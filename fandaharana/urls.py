from django.urls import path

from .views import home, month


urlpatterns = [
    path('', home, name='home'),
    path('volana/<int:month_num>-<int:year_num>', month, name='month'),
]
