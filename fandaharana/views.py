from django.shortcuts import render, redirect
from django.utils import translation

from datetime import datetime  #: 10, 11, 21, 23, 28

from .models import Public  #: 17


def home(request):
    now_month = datetime.now().month
    now_year = datetime.now().year
    return redirect('month', month_num=now_month, year_num=now_year)


def month(request, month_num, year_num):
    translation.activate('mg-mg')
    publics = Public.objects.filter(
        date__year=year_num).filter(
        date__month=month_num)

    dt = datetime(month=month_num, year=year_num, day=1)

    dt_prev = datetime(
        month=12 if month_num == 1 else month_num-1,
        year=year_num-1 if month_num == 1 else year_num,
        day=1, )

    dt_next = datetime(
        month=1 if month_num == 12 else month_num+1,
        year=year_num+1 if month_num == 12 else year_num,
        day=1, )

    data = {
        'publics': publics,
        'dt': dt,
        'dt_prev': dt_prev,
        'dt_next': dt_next, }

    return render(request, 'month.html', data)


def error_404(request, exception=None):
    data = {}
    return render(request, 'templates/404.html', data)


def error_500(request, exception=None):
    data = {}
    return render(request, 'templates/404.html', data)
