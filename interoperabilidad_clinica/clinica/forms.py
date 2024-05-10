from django import forms
from .models import Person

class SexForm(forms.ModelForm):
    biologic_sex = forms.ChoiceField(choices=Person.SEX_BIO, label="Sexo Biológico")

    class Meta:
        model = Person
        fields = ['biologic_sex', 'gender_identity']