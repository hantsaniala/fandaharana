from django.shortcuts import render, redirect


def home(request):
    return redirect('month')


def month(request):
    return render(request, 'month.html')
