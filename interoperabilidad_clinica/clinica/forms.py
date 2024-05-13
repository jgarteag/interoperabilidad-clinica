from django import forms
from .models import Person, ContactWithHealthService


class PacientForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'country_origin', 'doc_type', 'number_doc', 'last_name', 'surname', 'first_name',
            'middle_name', 'date_born', 'biologic_sex', 'gender_identity', 'occupation_care',
            'opossition_donation', 'antiquated_will_document', 'category_disability',
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

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactWithHealthService
        fields = [
            'cod_borr', 'modality_of_realization_it',  'it_groups', 'env_attention',
            'way_of_entry', 'cause_of_care', 'classification_triage', 'diagnosis_of_admission',
            'type_of_diagnosis'
        ]
        labels = {
            'cod_borr': 'Código del prestador ',
            'modality_of_realization_it': 'Modalidad de realización de la TI en salud',
            'it_groups': 'Grupos de servicios de TI en salud',
            'env_attention': 'Entorno de atención',
            'way_of_entry': 'Vía de ingreso',
            'cause_of_care': 'Causa de la atención',
            'classification_triage': 'Clasificación de triage',
            'diagnosis_of_admission': 'Diagnóstico de ingreso',
            'type_of_diagnosis': 'Tipo de diagnóstico'
        }
        widgets = {
            'cod_borr': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'modality_of_realization_it': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'it_groups': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'env_attention': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'way_of_entry': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'cause_of_care': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'classification_triage': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'diagnosis_of_admission': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'type_of_diagnosis': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }