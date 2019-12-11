from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('news', views.news)
]