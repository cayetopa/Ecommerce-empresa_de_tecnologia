from django.db import models

class categoria (models.Model):
    nombre = models.CharField(max_length= 100, null=False)
    id_cat = models.IntegerField( primary_key=True, null=False)
    logo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    @property
    def num_articulos(self):
        return  len(articulo.objects.filter(categoria=self))

class marca (models.Model):
    nombre = models.CharField(primary_key = True, max_length=20,null=False)
    logo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    @property
    def num_articulos(self):
        return  len(articulo.objects.filter(marca=self))

class articulo (models.Model):
    nombre= models.CharField(max_length=200,null=False )
    referencia= models.CharField(max_length=100,primary_key=True,null=False)
    marca=models.ForeignKey(marca, on_delete=models.CASCADE,null=False)
    categoria=models.ForeignKey(categoria, on_delete=models.CASCADE,null=False)
    imagen = models.ImageField(null=True, blank=True)
    precio = models.FloatField(null=False)
    color = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.nombre +" - "+ self.referencia
