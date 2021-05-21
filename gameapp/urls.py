from django.contrib import admin
from django.urls import path
import gameapp.views as gameapp

app_name = 'gameapp'

urlpatterns = [
    path('level/<int:pk>/', gameapp.GameLevelView.as_view(), name='level'),
    ]
