from django.shortcuts import render
from django.views import View
from .models import Countries, Typesdocs, Occupations
from .forms import SexForm

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})

class PacientView(View):
    def get(self, request):
        countries = Countries.objects.all()
        typesdocs = Typesdocs.objects.all()
        occupations = Occupations.objects.all()
        form = SexForm()
        return render(request, 'pacient.html', {'countries': countries, 
                                                'typesdocs': typesdocs,
                                                'form': form,
                                                'occupations': occupations})