from django.db.models import fields
from rest_framework import serializers
from .models import *

class UsuarioSerial (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]
        extra_kwargs = {
            "password": {"write_only":True, "style": {'input_type':'password'}},
            "email": {"write_only":True}
        }

class PerfilSerial (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class InfoSerial (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Info_envio
        fields ='__all__'