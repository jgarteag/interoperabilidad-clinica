from django.contrib import admin
from django.urls import path
from .views import IndexView, PacientView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("pacient/", PacientView.as_view(), name="pacient"),
]