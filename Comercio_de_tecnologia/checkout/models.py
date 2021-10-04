from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField, CharField, DateTimeField
from productos.models import articulo
from usuarios.models import Info_envio, Perfil

class carrito(models.Model):
    perfil=models.ForeignKey(Perfil, on_delete=models.SET_NULL, null = True)
    info_envio=models.ForeignKey(Info_envio, on_delete=models.SET_NULL, null=True)
    fecha=models.DateField(auto_now_add=True)
    pagado=models.BooleanField(default=False)

    def __str__(self):
        return self.perfil.usuario.username + " - " + str(self.fecha)

    @property
    def cant_art(self):
        cant = 0
        items = producto.objects.filter(carrito=self)
        for item in items:
            cant += item.cantidad
        return cant

    @property
    def total(self):
        total = 0
        items = producto.objects.filter(carrito=self)
        for item in items:
            total+= item.subtotal
        return total

class producto (models.Model):  
    carrito = models.ForeignKey(carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(articulo, on_delete=models.SET_NULL, null=True)        
    cantidad = models.IntegerField(default=0)
    
    def __str__(self):
        return self.carrito.__str__() + "(" + self.producto.nombre + ")" + "[" + str(self.cantidad)+ "]"
    
    @property
    def subtotal(self):
        return self.producto.precio*self.cantidad




