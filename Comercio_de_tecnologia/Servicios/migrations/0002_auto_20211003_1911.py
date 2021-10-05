# Generated by Django 3.2.7 on 2021-10-04 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20211003_1839'),
        ('Servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devoluciones',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.producto'),
        ),
        migrations.AddField(
            model_name='entregas',
            name='carrito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.carrito'),
        ),
        migrations.AddField(
            model_name='garantias',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.producto'),
        ),
    ]