# Generated by Django 3.2.7 on 2021-09-14 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('id_cat', models.IntegerField(primary_key=True, serialize=False)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='marca',
            fields=[
                ('nombre', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='articulo',
            fields=[
                ('referencia', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('precio', models.FloatField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.marca')),
            ],
        ),
    ]
