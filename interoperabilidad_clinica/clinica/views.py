from django.shortcuts import render
from django.views import View
from .models import Countries, Typesdocs, Occupations, Disability, Municipalities, Ethnicity, Eps
from .forms import SexForm, YesNoForm, TerritorialZone

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
        sex_form = SexForm()
        yes_no_form = YesNoForm()
        territorial_zone = TerritorialZone()
        return render(request, 'pacient.html', {'countries': countries, 
                                                'typesdocs': typesdocs,
                                                'sex_form': sex_form,
                                                'occupations': occupations,
                                                'yes_no_form': yes_no_form,
                                                'category_disability': category_disability,
                                                'municipality_of_hab_res': municipality_of_hab_res,
                                                'ethnicity': ethnicity,
                                                'territorial_zone': territorial_zone,
                                                'eps': eps})