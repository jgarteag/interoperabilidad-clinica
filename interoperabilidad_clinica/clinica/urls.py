from django.contrib import admin
from django.urls import path
from .views import create_pacient, IndexView, edit_patient, PageNotFoundView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("pacient/", create_pacient, name="pacient"),
    path('patient/edit/<int:id>/', edit_patient, name='edit_patient'),
    path('not_found/', PageNotFoundView.as_view(), name='not_found'),
]