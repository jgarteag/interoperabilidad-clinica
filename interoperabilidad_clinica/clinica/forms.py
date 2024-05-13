from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    biologic_sex = forms.ChoiceField(choices=Person.SEX_BIO, label="Sexo Biológico")
    gender_identity = forms.ChoiceField(choices=Person.GEN_ID, label="Identidad de Género")
    opossition_donation = forms.ChoiceField(choices=Person.OPOSSITION, label="¿Se opone a la oposición legal de donación?", widget=forms.Select(attrs={'id': 'opossition_donation'}))
    opossition_donation_date = forms.DateField(label="Fecha de oposición a la donación", widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'id': 'opossition_donation_date'}))
    antiquated_will_document = forms.ChoiceField(choices=Person.OPOSSITION, label="¿Tiene documento de voluntad anticipada?", widget=forms.Select(attrs={'id': 'antiquated_will_document'}))
    antiquated_will_document_date = forms.DateField(label="Fecha del documento de voluntad anticipada", widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'id': 'antiquated_will_document_date'}))
    territorial_zone = forms.ChoiceField(choices=Person.ZONE, label="Zona de residencia")

    class Meta:
        model = Person
        fields = ['biologic_sex', 'gender_identity', 'opossition_donation', 'opossition_donation_date', 'antiquated_will_document', 'antiquated_will_document_date', 'territorial_zone']