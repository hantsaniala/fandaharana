from django.shortcuts import render, redirect
from django.utils import translation

from .models import Public


def home(request):
    return redirect('month')


def month(request):
    translation.activate('mg-mg')
    publics = Public.objects.all()

    data = {
        'publics': publics, }

    return render(request, 'month.html', data)
