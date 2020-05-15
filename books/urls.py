from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:genre_name>/', views.genre, name='genre'),
]