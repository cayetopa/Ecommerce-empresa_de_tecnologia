from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("usuarios", UsuarioAPI)
router.register("perfiles", PerfilAPI)
router.register("info", InfoAPI)

urlpatterns = [
    path('crud/', include(router.urls)),
    path('login/', LoginAPI.as_view()),
    path('logout/', LogoutAPI.as_view()),
]