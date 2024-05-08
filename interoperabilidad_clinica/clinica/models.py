from django.db import models

# Create your models here.
class Typesdocs(models.Model):
    id_type = models.CharField(max_length=2, primary_key=True)
    doc_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'typesdocs'

    def __str__(self):
        return self.doc_type

class Occupations(models.Model):
    code_occ = models.CharField(max_length=4, primary_key=True)
    name_occ = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'occupations'

    def __str__(self):
        return self.name_occ

class Municipalities(models.Model):
    departament = models.CharField(max_length=200)
    code_dep = models.CharField(primary_key=True, max_length=5)
    name_dep = models.CharField(max_length=200)
    type_mnc = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'municipalities'

    def __str__(self):
        return self.name_dep

class Modality(models.Model):
    id_type = models.CharField(max_length=2, primary_key=True)
    description_modality = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'modality'

    def __str__(self):
        return self.description_modality
    
class Illness(models.Model):
    cod_4 = models.CharField(max_length=4, primary_key=True)
    des_illness = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'illness'

    def __str__(self):
        return self.des_illness

class Ethnicity(models.Model):
    id_et = models.CharField(max_length=2, primary_key=True)
    name_ethn = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ethnicity'

    def __str__(self):
        return self.name_ethn

class Eps(models.Model):
    code_eps = models.CharField(max_length=6, primary_key=True)
    name_eps = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'eps'

    def __str__(self):
        return self.name_eps

class Entrys(models.Model):
    id_type = models.AutoField(primary_key=True, max_length=2)
    entrys_names = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'entrys'

    def __str__(self):
        return self.name_entry

class Countries(models.Model):
    alfa_3 = models.CharField(max_length=3, primary_key=True)
    name_country = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'countries'

    def __str__(self):
        return self.name_country

class Causecare(models.Model):
    id_care = models.CharField(max_length=2, primary_key=True)
    type_care = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'causecare'

    def __str__(self):
        return self.type_care


class Disability(models.Model):
    id_dis = models.CharField(max_length=2, primary_key=True)
    name_dis = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'disability'

    def __str__(self):
        return self.name_dis


class Person(models.Model):
    SEX_BIO = [
        ('01', 'Hombre'),
        ('02', 'Mujer'),
        ('03', 'Indeterminado intersexual'),
    ]

    GEN_ID = [
        ('01', 'Masculino'),
        ('02', 'Femenino'),
        ('03', 'Transgenero'),
        ('04', 'Neutro'),
        ('05', 'No lo declara')
    ]

    OPOSSITION = [
        ('01', 'Si'),
        ('02', 'No')
    ]

    ZONE = [
        ('01', 'Urbana'),
        ('02', 'Rural')
    ]

    id_history = models.IntegerField(primary_key=True)
    country_origin = models.ForeignKey(Countries, on_delete=models.CASCADE, db_column='alfa_3')
    doc_type = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    number_doc = models.IntegerField(max_length=20, min_length=3, blank=False, null=False)
    last_name = models.CharField(max_length=60, min_length=2, blank=False, null=False)
    surname = models.CharField(max_length=60, min_length=2, blank=False, null=False)
    first_name = models.CharField(max_length=60, min_length=2, blank=False, null=False)
    middle_name = models.CharField(max_length=60, min_length=2, blank=False, null=False)
    date_born = models.DateField(max_length=16, min_length=10, blank=False, null=False)
    biologic_sex = models.CharField(max_length=2, min_length=2, blank=False, null=False, choices = SEX_BIO, default = '01')
    gender_identity = models.CharField(max_length=2, min_length=2, blank=False, null=False, choices = GEN_ID, default = '01')
    occupation_care = models.CharField(max_length=4, min_length=4, blank=False, null=False)
    opossition_donation = models.CharField(max_length=2, min_length=2, blank=False, null=False, choices = OPOSSITION, default = '01')
    date_opossition = models.DateField(max_length=10, min_length=10, blank=False, null=False)
    antiquated_will_document = models.CharField(max_length=2, min_length=2, blank=False, null=False, choices = OPOSSITION, default = '01')
    date_suscrip_ant_will_doc = models.DateField(max_length=10, min_length=10, blank=False, null=False)
    cod_borrower = models.CharField(max_length=12, min_length=12, blank=False, null=False)
    category_disability = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    habitual_residence = models.CharField(max_length=3, min_length=3, blank=False, null=False)
    municipality_of_hab_res = models.CharField(max_length=5, min_length=5, blank=False, null=False)
    ethnicity = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    territorial_zone = models.CharField(max_length=2, min_length=2, blank=False, null=False, choices = ZONE, default = '01')
    eps = models.CharField(max_length=6, min_length=6, blank=False, null=False)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.surname + " " + self.middle_name 
    
class ContactWithHealthService(models.Model):
    GRP_SERVICES = [
        ('01', 'Consulta Externa'),
        ('02', 'Apoyo Diagnostico y Complementacion Terapeutica'), 
        ('03', 'Internacion'),
        ('04', 'Quirurgico'),
        ('05', 'Atencion Inmediata'),
    ]

    ENV_ATT = [
        ('01', 'Hogar'),
        ('02', 'Comunitario'),
        ('03', 'Escolar'),
        ('04', 'Laboral'),
        ('05', 'Institucional'),
    ]

    TRIAGE = [
        ('01', 'TRIAGE I'),
        ('02', 'TRIAGE II'),
        ('03', 'TRIAGE III'),
        ('04', 'TRIAGE IV'),
        ('05', 'TRIAGE V'),
    ]

    TYPES = [
        ('01', 'Impresión Diagnóstica'),
        ('02', 'Confirmado Nuevo'),
        ('03', 'Confirmado Repetido')
    ]

    id_contact = models.IntegerField(primary_key=True)
    cod_eps = models.CharField(max_length=12, min_length=12, blank=False, null=False)
    date_start_attention = models.DateField(max_length=16, min_length=16, blank=False, null=False)
    modality_of_realization_it = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    it_groups = models.CharField(max_length=2, min_length=2, blank=False, null=False, choices = GRP_SERVICES, default = '01')
    env_attention = models.CharField(max_length=2, min_length=2, blank=False, null=False, choices = ENV_ATT, default = '01')
    way_of_entry = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    cause_of_care = models.CharField(max_length=2, min_length=2, blank=False, null=False)
    date_triage = models.DateField(max_length=16, min_length=16, blank=False, null=False)
    classification_triage = models.CharField(max_length=2, min_length=2, blank=False, null=False, choices = TRIAGE, default = '01')
    diagnosis_of_admission = models.CharField(max_length=4, min_length=4, blank=False, null=False)
    type_of_diagnosis = models.CharField(max_length=2, min_length=2, blank=False, null=False, choices = TYPES, default = '01')

    def __str__(self):
        return self.cod_eps + " " + self.date_start_attention + " " + self.diagnosis_of_admission
