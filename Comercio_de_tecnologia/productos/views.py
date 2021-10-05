from rest_framework import viewsets, views, authentication, permissions
from productos.models import *
from productos.serializers import *
from usuarios.permissions import *

class apicategoria (viewsets.ModelViewSet):
    serializer_class = categoria_serial
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, AccesoPersonal)
    queryset = categoria.objects.all()

class apimarca(viewsets.ModelViewSet):
    serializer_class = marca_serial
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, AccesoPersonal)
    queryset = marca.objects.all()

class apiarticulo (viewsets.ModelViewSet):
    serializer_class = articulo_serial
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,AccesoPersonal)
    queryset = articulo.objects.all()
