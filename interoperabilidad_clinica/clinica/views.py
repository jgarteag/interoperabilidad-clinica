from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import *

class IndexView(View):
    """
    Clase para renderizar la página de inicio
    """
    def get(self, request):
        return render(request, 'index.html', {})

def create_pacient(request):
    """
    Función para crear un paciente
    """
    if request.method == 'POST':
        pacient_form = PacientForm(request.POST)
        contact_form = ContactForm(request.POST)
        if pacient_form.is_valid():
            pacient = pacient_form.save()
            if contact_form.is_valid():
                contact = contact_form.save(commit=False)
                contact.id_contact = pacient
                contact.save()
                return redirect('pacient')
    else:
        pacient_form = PacientForm()
        contact_form = ContactForm()

    return render(request, 'pacient.html', {'pacient_form': pacient_form, 'contact_form': contact_form})

def edit_patient(request, id):
    """
    Función para editar un paciente
    """
    pacient = Person.objects.get(id_history=id)
    contact = ContactWithHealthService.objects.get(id_contact=id)
    if request.method == 'GET':
        pacient_form = PacientForm(instance=pacient)
        contact_form = ContactForm(instance=contact)
    else:
        pacient_form = PacientForm(request.POST, instance=pacient)
        contact_form = ContactForm(request.POST, instance=contact)
        if pacient_form.is_valid():
            pacient = pacient_form.save()
            if contact_form.is_valid():
                contact = contact_form.save(commit=False)
                contact.id_contact = pacient
                contact.save()
                return redirect('index')
    return render(request, 'pacient.html', {'pacient_form': pacient_form, 'contact_form': contact_form})