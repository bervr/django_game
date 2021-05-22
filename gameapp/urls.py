from django.contrib import admin
from django.urls import path
import gameapp.views as gameapp

app_name = 'gameapp'

urlpatterns = [
    path('level/<int:pk>/', gameapp.game_level, name='level'),
    ]
