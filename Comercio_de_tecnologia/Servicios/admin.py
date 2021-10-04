from django.contrib import admin

# Register your models here.

from Servicios.models import *

admin.site.register(Garantias)
admin.site.register(Devoluciones)
admin.site.register(Entregas)

