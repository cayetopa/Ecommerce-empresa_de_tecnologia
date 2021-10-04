from .permissions import AccesoPersonal
from .models import *
from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import viewsets,views , authentication, permissions
from rest_framework.response import Response

class UsuarioAPI (viewsets.ModelViewSet):
    serializer_class =UsuarioSerial
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAdminUser, AccesoPersonal)
    queryset = get_user_model().objects.all()

class PerfilAPI (viewsets.ModelViewSet):
    serializer_class = PerfilSerial
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated, AccesoPersonal)    
    queryset = Perfil.objects.all()

class InfoAPI (viewsets.ModelViewSet):
    serializer_class = InfoSerial
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated, AccesoPersonal)
    queryset = Info_envio.objects.all()

#****************************************

class LoginAPI (views.APIView):
    def post(self, request):
        if 'username' in request.data and 'password' in request.data:
            usuario = get_object_or_404(get_user_model(), username = request.data['username'])
            if usuario.check_password(request.data['password']):
                login(request, usuario)
                return Response ("El usuario " + usuario.username + " ha hecho login")
            return Response ("Datos de usuario y/o contraseña incorrectos")
        return Response ("Datos Incorrectos")

class LogoutAPI (views.APIView):
    def get(self, request):
        logout(request)
        return Response ("Se ha hecho Logout con éxito")