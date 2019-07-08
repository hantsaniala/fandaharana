from django.urls import path
from django.conf.urls import handler404, handler500

from .views import home, month, error_404, error_500


urlpatterns = [
    path('', home, name='home'),
    path('volana/<int:month_num>-<int:year_num>', month, name='month'),
]


handler404 = error_404
handler500 = error_500
