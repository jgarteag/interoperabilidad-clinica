from django.shortcuts import render
from .models import Countries

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def pacient(request):
    return render(request, 'pacient.html', {})

def countries(request):
    countries = Countries.objects.all()
    return render(request, 'pacient.html', {'countries': countries})