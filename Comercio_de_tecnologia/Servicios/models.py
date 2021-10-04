from django.db import models
from checkout.models import producto, carrito


class Garantias(models.Model):
    producto=models.ForeignKey(producto, on_delete=models.CASCADE , null=True, blank = True)
    cantidad=models.IntegerField()
    descripcion=models.TextField()
    fecha_entrada=models.DateField(auto_now_add=True)
    fecha_salida=models.DateField(null=True, blank=True)
    reparado=models.BooleanField(default=False)

    def __str__(self):
        return self.producto.producto.nombre + " - " + self.producto.carrito.perfil.usuario.username + " - " + str(self.fecha_entrada)

class Devoluciones(models.Model):
    producto=models.ForeignKey(producto, on_delete=models.CASCADE, null=True, blank = True)
    cantidad=models.IntegerField()
    descripcion=models.TextField()
    fecha=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.cantidad) + " - " + self.producto.producto.nombre + " - " + self.producto.carrito.perfil.usuario.username + " - " + str(self.fecha)

class Entregas(models.Model):
    carrito=models.ForeignKey(carrito,on_delete=models.CASCADE , null=True, blank = True)
    enviado=models.BooleanField(default=False)
    fecha_envio=models.DateField(null=True, blank=True)
    entregado=models.BooleanField(default=False)
    fecha_entrega=models.DateField(null=True, blank=True)

    def __str__(self):
        return self.carrito.__str__() +"("+self.carrito.info_envio.__str__()