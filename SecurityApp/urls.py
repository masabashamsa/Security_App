# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('vulnerable_query/', views.vulnerable_query, name='vulnerable_query'),
    path('vulnerable_change_password/', views.vulnerable_change_password, name='vulnerable_change_password'),   
]
