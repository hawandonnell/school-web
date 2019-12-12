from django.shortcuts import render
from .models import *


def main_page(request):
    new_s = New.objects.first()
    return render(request, 'main_app/main.html', {
        "label": "Главная Страница",
        "news": new_s
    })

def news(request):
    new_S = New.objects.all()
    return render(request, 'main_app/news.html', {
        "label": "Школьные Новости",
        "news": new_S
    })

def history(request):
    return render(request, 'main_app/history.html', {
        "label": "История Школы"
    })