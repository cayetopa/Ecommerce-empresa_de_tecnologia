# Generated by Django 3.2.7 on 2021-10-05 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0004_auto_20211004_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garantias',
            name='fecha_salida',
            field=models.DateField(blank=True, null=True),
        ),
    ]
