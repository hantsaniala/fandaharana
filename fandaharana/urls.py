from django.urls import path

from .views import home, month, privacy, contact


urlpatterns = [
    path('', home, name='home'),
    path('volana/<int:month_num>-<int:year_num>', month, name='month'),

    path('fifanekena/tsiambaratelo', privacy, name='privacy'),
    path('fifandraisana', contact, name='contact'),
]
