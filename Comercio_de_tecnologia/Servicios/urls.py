from django.urls import path, include
from rest_framework import urlpatterns
from Servicios.views import * 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('garantias',GarantiasAPI)
router.register('devoluciones',DevolucionesAPI)
router.register('entregas',EntregasAPI)

urlpatterns = [
    path('crud/',include(router.urls))
]
