from django.shortcuts import render
from django.views import View
from .models import Countries

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})

class PacientView(View):
    def get(self, request):
        countries = Countries.objects.all()
        return render(request, 'pacient.html', {'countries': countries})