from django.urls import path
from . import views

urlpatterns = [
    path('', views.information_block),
    path('news', views.news)
]