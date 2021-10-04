# Generated by Django 3.2.7 on 2021-10-03 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('checkout', '0004_auto_20211002_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='info_envio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.info_envio'),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='perfil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.perfil'),
        ),
    ]
