from django.db import models

# Create your models here.
class Person(models.Model):
    id_history = models.IntegerField(primary_key=True)
    country_origin = models.CharField(max_length=200, min_length=3,blank=False, null=False)
    doc_type = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    number_doc = models.IntegerField(max_length=20, min_length=3, blank=False, null=False)
    last_name = models.CharField(max_length=60, min_length=2, blank=False, null=False)
    surname = models.CharField(max_length=60, min_length=2, blank=False, null=False)
    first_name = models.CharField(max_length=60, min_length=2, blank=False, null=False)
    middle_name = models.CharField(max_length=60, min_length=2, blank=False, null=False)
    date_born = models.DateField(max_length=16, min_length=10, blank=False, null=False)
    biologic_sex = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    gender_identity = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    occupation_care = models.CharField(max_length=4, min_length=4, blank=False, null=False)
    opossition_donation = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    date_opossition = models.DateField(max_length=10, min_length=10, blank=False, null=False)
    antiquated_will_document = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    date_suscrip_ant_will_doc = models.DateField(max_length=10, min_length=10, blank=False, null=False)
    cod_borrower = models.CharField(max_length=12, min_length=12, blank=False, null=False)
    category_disability = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    habitual_residence = models.CharField(max_length=3, min_length=3, blank=False, null=False)
    municipality_of_hab_res = models.CharField(max_length=5, min_length=5, blank=False, null=False)
    ethnicity = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    territorial_zone = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    eps = models.CharField(max_length=6, min_length=6, blank=False, null=False)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.surname + " " + self.middle_name 
    
class ContactWithHealthService(models.Model):
    id_contact = models.IntegerField(primary_key=True)
    cod_eps = models.CharField(max_length=12, min_length=12, blank=False, null=False)
    date_start_attention = models.DateField(max_length=16, min_length=16, blank=False, null=False)
    modality_of_realization_it = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    it_groups = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    env_attention = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    way_of_entry = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    cause_of_care = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    classification_triage = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    diagnosis_of_admission = models.CharField(max_length=4, min_length=4, blank=False, null=False)
    type_of_diagnosis = models.CharField(max_length=2, min_length=2, blank=False, null=False)
