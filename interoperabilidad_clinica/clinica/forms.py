from django import forms
from .models import Person


class PacientForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'country_origin', 'doc_type', 'number_doc', 'last_name', 'surname', 'first_name',
            'middle_name', 'date_born', 'biologic_sex', 'gender_identity', 'occupation_care',
            'opossition_donation', 'antiquated_will_document', 'cod_borrower', 'category_disability',
            'habitual_residence', 'municipality_of_hab_res', 'ethnicity', 'territorial_zone', 'eps'
        ]
        labels = {
            'country_origin': 'País de origen',
            'doc_type': 'Tipo de documento',
            'number_doc': 'Número de documento',
            'last_name': 'Primer apellido',
            'surname': 'Segundo apellido',
            'first_name': 'Primer nombre',
            'middle_name': 'Segundo nombre',
            'date_born': 'Fecha de nacimiento',
            'biologic_sex': 'Sexo biologico',
            'gender_identity': 'Identidad de género',
            'occupation_care': 'Ocupación',
            'opossition_donation': '¿Oposición a donación?',
            'antiquated_will_document': '¿Documento de voluntad anticipada?',
            'cod_borrower': 'Código del prestador',
            'category_disability': 'Categoría de discapacidad',
            'habitual_residence': 'Residencia habitual',
            'municipality_of_hab_res': 'Municipio de residencia habitual',
            'ethnicity': 'Etnia',
            'territorial_zone': 'Zona territorial',
            'eps': 'EPS'
        }
        widgets = {
            'country_origin': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'doc_type' : forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'number_doc': forms.TextInput(
                attrs={
                    'id': 'identity',
                    'class': 'form-control',
                    'placeholder' : 'Número de documento',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Guerrero',
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Arteaga',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Juan',
                }
            ),
            'middle_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'date_born': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local',
                }
            ),
            'biologic_sex': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'gender_identity': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'occupation_care': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'opossition_donation': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'antiquated_will_document': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'cod_borrower': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'category_disability': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'habitual_residence': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'municipality_of_hab_res': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'ethnicity': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'territorial_zone': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'eps': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }

