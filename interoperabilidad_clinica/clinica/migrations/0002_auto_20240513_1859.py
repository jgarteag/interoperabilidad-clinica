# Generated by Django 3.2.8 on 2024-05-13 23:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id_history', models.AutoField(primary_key=True, serialize=False, verbose_name='Código de historia clínica')),
                ('number_doc', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Solo se permiten números', regex='^[0-9]*$')], verbose_name='Número de documento persona')),
                ('last_name', models.CharField(max_length=60, verbose_name='Primer apellido')),
                ('surname', models.CharField(max_length=60, verbose_name='Segundo apellido')),
                ('first_name', models.CharField(max_length=60, verbose_name='Primer nombre')),
                ('middle_name', models.CharField(default='', max_length=60, verbose_name='Segundo nombre')),
                ('date_born', models.DateTimeField(verbose_name='Fecha de nacimiento')),
                ('biologic_sex', models.CharField(choices=[('01', 'Hombre'), ('02', 'Mujer'), ('03', 'Indeterminado intersexual')], default='01', max_length=2, verbose_name='Sexo biológico')),
                ('gender_identity', models.CharField(choices=[('01', 'Masculino'), ('02', 'Femenino'), ('03', 'Transgenero'), ('04', 'Neutro'), ('05', 'No lo declara')], default='01', max_length=2, verbose_name='Identidad de género')),
                ('opossition_donation', models.CharField(choices=[('01', 'Si'), ('02', 'No')], default='01', max_length=2, verbose_name='Oposición legal de donación')),
                ('date_opossition', models.DateField(auto_now=True, verbose_name='Fecha de oposición a la donación')),
                ('antiquated_will_document', models.CharField(choices=[('01', 'Si'), ('02', 'No')], default='01', max_length=2)),
                ('date_suscrip_ant_will_doc', models.DateField(auto_now=True, verbose_name='Fecha de suscripción del documento de voluntad anticipada')),
                ('territorial_zone', models.CharField(choices=[('01', 'Urbana'), ('02', 'Rural')], default='01', max_length=2, verbose_name='Zona de residencia')),
                ('category_disability', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.disability', verbose_name='Categoría de discapacidad')),
                ('country_origin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='origin_country', to='clinica.countries', verbose_name='País de origen')),
                ('doc_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.typesdocs', verbose_name='Tipo de documento')),
                ('eps', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.eps', verbose_name='EPS')),
                ('ethnicity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.ethnicity', verbose_name='Etnia')),
                ('habitual_residence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='residence_country', to='clinica.countries', verbose_name='País de residencia habitual')),
                ('municipality_of_hab_res', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.municipalities', verbose_name='Municipio de residencia habitual')),
                ('occupation_care', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.occupations', verbose_name='Ocupación')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='ContactWithHealthService',
            fields=[
                ('id_contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='id_contact', serialize=False, to='clinica.person')),
                ('date_start_attention', models.DateTimeField(auto_now=True, verbose_name='Fecha de inicio de atención')),
                ('it_groups', models.CharField(choices=[('01', 'Consulta Externa'), ('02', 'Apoyo Diagnostico y Complementacion Terapeutica'), ('03', 'Internacion'), ('04', 'Quirurgico'), ('05', 'Atencion Inmediata')], default='01', max_length=2, verbose_name='Grupo de servicios')),
                ('env_attention', models.CharField(choices=[('01', 'Hogar'), ('02', 'Comunitario'), ('03', 'Escolar'), ('04', 'Laboral'), ('05', 'Institucional')], default='01', max_length=2, verbose_name='Entorno de atención')),
                ('date_triage', models.DateTimeField(auto_now=True, verbose_name='Fecha de triage')),
                ('classification_triage', models.CharField(choices=[('01', 'TRIAGE I'), ('02', 'TRIAGE II'), ('03', 'TRIAGE III'), ('04', 'TRIAGE IV'), ('05', 'TRIAGE V')], default='01', max_length=2, verbose_name='Clasificación de triage')),
                ('type_of_diagnosis', models.CharField(choices=[('01', 'Impresión Diagnóstica'), ('02', 'Confirmado Nuevo'), ('03', 'Confirmado Repetido')], default='01', max_length=2, verbose_name='Tipo de diagnóstico')),
            ],
            options={
                'verbose_name': 'Contacto con el servicio de salud',
                'verbose_name_plural': 'Contacts',
                'db_table': 'contact',
            },
        ),
        migrations.AddConstraint(
            model_name='person',
            constraint=models.UniqueConstraint(fields=('doc_type', 'number_doc'), name='UQ_DOCUMENT_TYPE_IDENTITY_CARD'),
        ),
        migrations.AddField(
            model_name='contactwithhealthservice',
            name='cause_of_care',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.causecare', verbose_name='Causa de atención'),
        ),
        migrations.AddField(
            model_name='contactwithhealthservice',
            name='cod_borr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.borrows', verbose_name='Código del prestador'),
        ),
        migrations.AddField(
            model_name='contactwithhealthservice',
            name='diagnosis_of_admission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.illnesses', verbose_name='Diagnóstico de ingreso'),
        ),
        migrations.AddField(
            model_name='contactwithhealthservice',
            name='modality_of_realization_it',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.modality', verbose_name='Modalidad de realización de la atención'),
        ),
        migrations.AddField(
            model_name='contactwithhealthservice',
            name='way_of_entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.entrys', verbose_name='Vía de ingreso'),
        ),
        migrations.AddConstraint(
            model_name='contactwithhealthservice',
            constraint=models.UniqueConstraint(fields=('id_contact', 'date_start_attention'), name='UQ_ID_CONTACT_DATE_ATTENTION'),
        ),
    ]
