from django.shortcuts import render, redirect

from .models import Public


def home(request):
    return redirect('month')


def month(request):
    publics = Public.objects.all()

    data = {
        'publics': publics, }

    return render(request, 'month.html', data)
