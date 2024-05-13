from django.shortcuts import render, redirect
from django.views import View
from .models import Countries, Typesdocs, Occupations, Disability, Municipalities, Ethnicity, Eps
from .forms import PersonForm

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})

class PacientView(View):
    def get(self, request):
        countries = Countries.objects.all()
        typesdocs = Typesdocs.objects.all()
        occupations = Occupations.objects.all()
        category_disability = Disability.objects.all()
        municipality_of_hab_res = Municipalities.objects.all()
        ethnicity = Ethnicity.objects.all()
        eps = Eps.objects.all()
        person_form = PersonForm()
        return render(request, 'pacient.html', {'countries': countries, 
                                                'typesdocs': typesdocs,
                                                'person_form': person_form,
                                                'occupations': occupations,
                                                'category_disability': category_disability,
                                                'municipality_of_hab_res': municipality_of_hab_res,
                                                'ethnicity': ethnicity,
                                                'eps': eps})

    def post(self, request):
        person_form = PersonForm(request.POST)
        if person_form.is_valid():
            person_form.save()
            return redirect('pacient')
        else:
            countries = Countries.objects.all()
            typesdocs = Typesdocs.objects.all()
            occupations = Occupations.objects.all()
            category_disability = Disability.objects.all()
            municipality_of_hab_res = Municipalities.objects.all()
            ethnicity = Ethnicity.objects.all()
            eps = Eps.objects.all()
            return render(request, 'pacient.html', {'countries': countries, 
                                                    'typesdocs': typesdocs,
                                                    'person_form': person_form,
                                                    'occupations': occupations,
                                                    'category_disability': category_disability,
                                                    'municipality_of_hab_res': municipality_of_hab_res,
                                                    'ethnicity': ethnicity,
                                                    'eps': eps})