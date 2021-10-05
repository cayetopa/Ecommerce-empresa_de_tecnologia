#permisos personalizados 
# editar informacion solo de su cuenta personal
from rest_framework import permissions
from rest_framework.permissions import BasePermission

class AccesoPersonal (BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True
        if request.user.is_staff:
            return True
        return obj.id == request.user.id