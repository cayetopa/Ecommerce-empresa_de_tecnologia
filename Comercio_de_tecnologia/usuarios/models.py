from django.db import models
from django.contrib.auth import get_user_model
#from django.db.models.base import Model

class Perfil (models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)

    def __str__(self):
        return self.usuario.username

class Info_envio (models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    barrio = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.perfil.usuario.username + " - "+ self.direccion + " - " + self.ciudad + " - " + self.pais
