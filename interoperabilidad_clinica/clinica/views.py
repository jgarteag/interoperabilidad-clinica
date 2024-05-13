from django.shortcuts import render, redirect
from django.views import View
from .models import Countries, Typesdocs, Occupations, Disability, Municipalities, Ethnicity, Eps

from .forms import *

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})

def create_pacient(request):
    if request.method == 'POST':
        form = PacientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pacient')
    else:
        form = PacientForm()

    return render(request, 'pacient.html', {'form': form})