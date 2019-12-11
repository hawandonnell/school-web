from django.shortcuts import render
from .models import *


def main_page(request):
    return render(request, 'main_app/main.html', {
        "label": "Главная Страница"
    })

def news(request):
    new_S = New.objects.all()
    return render(request, 'main_app/news.html', {
        "label": "Школьные Новости",
        "news": new_S
    })