from productos.models import * 
from rest_framework import serializers

class categoria_serial(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ['id_cat','nombre','logo','num_articulos']

class marca_serial(serializers.ModelSerializer):
    class Meta:
        model = marca
        fields = ['nombre','logo','num_articulos']

class articulo_serial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = articulo
        fields = '__all__'