# Generated by Django 3.2.8 on 2024-05-15 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_auto_20240513_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='middle_name',
            field=models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Segundo nombre'),
        ),
    ]
