from Servicios.models import *

from rest_framework import serializers

class Garantias_Serial(serializers.HyperlinkedModelSerializer):
      class Meta:
        model = Garantias
        fields = '__all__'


class Devoluciones_Serial(serializers.HyperlinkedModelSerializer):
      class Meta:
        model = Devoluciones
        fields = '__all__'

class Entregas_Serial(serializers.HyperlinkedModelSerializer):
      class Meta:
        model = Entregas
        fields = '__all__'




