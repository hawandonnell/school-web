from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def main_page(request):
    new_s = New.objects.order_by('-pubdate').first()
    return render(request, 'main_app/main.html', {
        "label": "Главная Страница",
        "news": new_s
    })

def news(request):
    new_S = New.objects.order_by('-pubdate')
    return render(request, 'main_app/news.html', {
        "label": "Школьные Новости",
        "news": new_S
    })

def history(request):
    return render(request, 'main_app/history.html', {
        "label": "История Школы"
    })

def slujba(request):
    return render(request, 'main_app/slujba.html', {
        "label": "Учебно-Методическая Служба"
    })

