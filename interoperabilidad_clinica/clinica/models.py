from django.db import models
from django.core.validators import RegexValidator
import uuid

# Create your models here.
class Typesdocs(models.Model):
    id_typedoc = models.CharField(verbose_name = 'Código del tipo de documento', max_length=2, primary_key=True)
    doc_type = models.CharField(verbose_name = 'Descripción', max_length=100, unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'typesdocs'

    def __str__(self):
        return f'{self.id_typedoc} - {self.doc_type}'

class Occupations(models.Model):
    code_occ = models.CharField(max_length=4, primary_key=True, verbose_name = 'Código de la ocupación')
    name_occ = models.CharField(max_length=200, verbose_name = 'Nombre de la ocupación', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'occupations'

    def __str__(self):
        return f'{self.code_occ} - {self.name_occ}'

class Municipalities(models.Model):
    departament = models.CharField(max_length=200, verbose_name='Departamento', null = False)
    code_dep = models.CharField(primary_key=True, max_length=5, verbose_name='Código del municipio', null = False)
    name_dep = models.CharField(max_length=200, verbose_name='Nombre del municipio', null = False)
    type_mnc = models.CharField(max_length=200, verbose_name='Tipo de municipio', null = False)

    class Meta:
        managed = False
        db_table = 'municipalities'

    def __str__(self):
        return f'{self.code_dep} - {self.name_dep}'

class Modality(models.Model):
    id_typemod = models.CharField(max_length=2, primary_key=True, verbose_name = 'Código de la modalidad')
    description_modality = models.CharField(max_length=100, verbose_name = 'Descripción de la modalidad', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'modality'

    def __str__(self):
        return f'{self.id_typemod} - {self.description_modality}'
    
class Illnesses(models.Model):
    cod_4 = models.CharField(max_length=4, primary_key=True, verbose_name = 'Código de la enfermedad')
    des_illness = models.CharField(max_length=400, verbose_name = 'Descripción de la enfermedad', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'illnesses'

    def __str__(self):
        return f'{self.cod_4} - {self.des_illness}'

class Ethnicity(models.Model):
    id_et = models.CharField(max_length=2, primary_key=True, verbose_name = 'Código de la etnia')
    name_ethn = models.CharField(max_length=200, verbose_name = 'Nombre de la etnia', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'ethnicity'

    def __str__(self):
        return f'{self.id_et} - {self.name_ethn}'

class Eps(models.Model):
    code_eps = models.CharField(max_length=6, primary_key=True, verbose_name = 'Código de la EPS')
    name_eps = models.CharField(max_length=200, verbose_name = 'Nombre de la EPS', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'eps'

    def __str__(self):
        return f'{self.code_eps} - {self.name_eps}'

class Entrys(models.Model):
    id_type_entrys = models.CharField(primary_key=True, max_length=2, verbose_name = 'Código de la entrada')
    entrys_names = models.CharField(max_length=200, verbose_name = 'Nombre de la entrada', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'entrys'

    def __str__(self):
        return f'{self.id_type_entrys} - {self.entrys_names}'

class Countries(models.Model):
    alfa_3 = models.CharField(max_length=3, primary_key=True, verbose_name = 'Código de tres letras del país')
    name_country = models.CharField(max_length=200, verbose_name = 'Nombre del país', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'countries'

    def __str__(self):
        return f'{self.alfa_3} - {self.name_country}'

class Causecare(models.Model):
    id_care = models.CharField(max_length=2, primary_key=True, verbose_name = 'Código de la causa de atención')
    type_care = models.CharField(max_length=50, verbose_name = 'Tipo de atención', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'causecare'

    def __str__(self):
        return f'{self.id_care} - {self.type_care}'


class Disability(models.Model):
    id_dis = models.CharField(max_length=2, primary_key=True, verbose_name = 'Código de la discapacidad')
    name_dis = models.CharField(max_length=50, verbose_name = 'Nombre de la discapacidad', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'disability'

    def __str__(self):
        return f'{self.id_dis} - {self.name_dis}'

class Borrows(models.Model):
    code_borrow = models.CharField(max_length=12, primary_key=True, verbose_name = 'Código prestadores')
    name_borrow = models.CharField(max_length=200, verbose_name = 'Nombre del prestador', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'borrows'

    def __str__(self):
        return f'{self.code_borrow} - {self.name_borrow}'


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

    id_history = models.AutoField(primary_key=True, verbose_name = 'Código de historia clínica')
    country_origin = models.ForeignKey(Countries, on_delete = models.PROTECT, verbose_name = 'País de origen', related_name='origin_country')
    doc_type = models.ForeignKey(Typesdocs, on_delete = models.PROTECT, verbose_name = 'Tipo de documento')
    number_doc = models.CharField(max_length=20, blank=False, null=False, validators=[RegexValidator(regex='^[0-9]*$', message='Solo se permiten números')], verbose_name = 'Número de documento persona')
    last_name = models.CharField(max_length=60, blank=False, null=False, verbose_name = 'Primer apellido')
    surname = models.CharField(max_length=60, blank=False, null=False, verbose_name = 'Segundo apellido')
    first_name = models.CharField(max_length=60, blank=False, null=False, verbose_name = 'Primer nombre')
    middle_name = models.CharField(max_length=60, null=True, blank=True, verbose_name = 'Segundo nombre', default = '')
    date_born = models.DateTimeField(blank=False, null=False, verbose_name = 'Fecha de nacimiento')
    biologic_sex = models.CharField(max_length=2, choices = SEX_BIO, default = '01', verbose_name = 'Sexo biológico')
    gender_identity = models.CharField(max_length=2, choices = GEN_ID, default = '01', verbose_name = 'Identidad de género')
    occupation_care = models.ForeignKey(Occupations, on_delete=models.PROTECT, verbose_name='Ocupación')
    opossition_donation = models.CharField(max_length=2, choices = OPOSSITION, default = '01', verbose_name = 'Oposición legal de donación')
    date_opossition = models.DateField(auto_now=True, verbose_name = 'Fecha de oposición a la donación') #automatico
    antiquated_will_document = models.CharField(max_length=2, blank=False, null=False, choices = OPOSSITION, default = '01')
    date_suscrip_ant_will_doc = models.DateField(auto_now=True, verbose_name='Fecha de suscripción del documento de voluntad anticipada') #automatico

    category_disability = models.ForeignKey(Disability, on_delete=models.PROTECT, verbose_name='Categoría de discapacidad')
    habitual_residence = models.ForeignKey(Countries, on_delete=models.PROTECT, verbose_name= 'País de residencia habitual', related_name='residence_country')
    municipality_of_hab_res = models.ForeignKey(Municipalities, on_delete=models.PROTECT, verbose_name='Municipio de residencia habitual')
    ethnicity = models.ForeignKey(Ethnicity, on_delete=models.PROTECT, verbose_name='Etnia')
    territorial_zone = models.CharField(max_length=2, choices = ZONE, default = '01', verbose_name='Zona de residencia')
    eps = models.ForeignKey(Eps, on_delete=models.PROTECT, verbose_name='EPS')

    class Meta:
        db_table = 'person'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        constraints = [
            models.UniqueConstraint(fields=['doc_type', 'number_doc'], name='UQ_DOCUMENT_TYPE_IDENTITY_CARD')
        ]

    def __str__(self):
        return f'{self.doc_type} - {self.number_doc}'.strip()
    
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

    id_contact = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True, related_name='id_contact')
    cod_borr = models.ForeignKey(Borrows, on_delete=models.PROTECT, verbose_name='Código del prestador')
    date_start_attention = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de inicio de atención') #automatico
    modality_of_realization_it = models.ForeignKey(Modality, on_delete=models.PROTECT, verbose_name='Modalidad de realización de la atención')
    it_groups = models.CharField('Grupo de servicios', max_length=2, choices = GRP_SERVICES, default = '01')
    env_attention = models.CharField('Entorno de atención', max_length=2, choices = ENV_ATT, default = '01')
    way_of_entry = models.ForeignKey(Entrys, on_delete=models.PROTECT, verbose_name='Vía de ingreso')
    cause_of_care = models.ForeignKey(Causecare, on_delete=models.PROTECT, verbose_name='Causa de atención')
    date_triage = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de triage') #automatico
    classification_triage = models.CharField('Clasificación de triage', max_length=2, choices = TRIAGE, default = '01')
    diagnosis_of_admission = models.ForeignKey(Illnesses, on_delete=models.PROTECT, verbose_name='Diagnóstico de ingreso')
    type_of_diagnosis = models.CharField('Tipo de diagnóstico', max_length=2, choices = TYPES, default = '01')

    class Meta:
        db_table = 'contact'
        verbose_name = 'Contacto con el servicio de salud'
        verbose_name_plural = 'Contacts'
        constraints = [
            models.UniqueConstraint(fields=['id_contact', 'date_start_attention'], name='UQ_ID_CONTACT_DATE_ATTENTION')
        ]

    def __str__(self):
        return f'{self.id_contact} - {self.date_start_attention}'.strip()
