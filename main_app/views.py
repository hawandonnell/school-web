from django.shortcuts import render

def information_block(request):
    return render(request, 'main_app/information.html', {
        "label": "Информационный Блок"
    })

def news(request):
    return render(request, 'main_app/news.html', {
        "label": "Школьные Новости"
    })