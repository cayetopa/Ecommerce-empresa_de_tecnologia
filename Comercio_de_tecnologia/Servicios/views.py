
from rest_framework import viewsets
from Servicios.models import *
from Servicios.serializers import *

class GarantiasAPI (viewsets.ModelViewSet):
    serializer_class = Garantias_Serial
    queryset = Garantias.objects.all()

class DevolucionesAPI(viewsets.ModelViewSet):
    serializer_class = Devoluciones_Serial
    queryset = Devoluciones.objects.all()

class EntregasAPI(viewsets.ModelViewSet):
    serializer_class = Entregas_Serial
    queryset = Entregas.objects.all()
