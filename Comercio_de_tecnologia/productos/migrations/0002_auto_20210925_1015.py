# Generated by Django 3.2.7 on 2021-09-25 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='articulo',
            name='nombre',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]