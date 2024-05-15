from django.contrib import admin
from django.urls import path
from .views import create_pacient, IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("pacient/", create_pacient, name="pacient"),
]