from django.shortcuts import render, redirect
from django.views import View

from .forms import *

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})

def create_pacient(request):
    if request.method == 'POST':
        pacient_form = PacientForm(request.POST)
        contact_form = ContactForm(request.POST)
        if pacient_form.is_valid() and contact_form.is_valid():
            pacient_form.save()
            contact_form.save()
            return redirect('pacient')
    else:
        pacient_form = PacientForm()
        contact_form = ContactForm()

    return render(request, 'pacient.html', {'pacient_form': pacient_form, 'contact_form': contact_form})