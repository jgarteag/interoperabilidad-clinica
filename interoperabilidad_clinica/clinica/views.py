from django.shortcuts import render
from django.views import View
from .models import Countries, Typesdocs, Occupations
from .forms import SexForm, YesNoForm

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})

class PacientView(View):
    def get(self, request):
        countries = Countries.objects.all()
        typesdocs = Typesdocs.objects.all()
        occupations = Occupations.objects.all()
        sex_form = SexForm()
        yes_no_form = YesNoForm()
        return render(request, 'pacient.html', {'countries': countries, 
                                                'typesdocs': typesdocs,
                                                'sex_form': sex_form,
                                                'occupations': occupations,
                                                'yes_no_form': yes_no_form})