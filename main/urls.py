"""This module manages urls"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.deck, name="deck"),
]
