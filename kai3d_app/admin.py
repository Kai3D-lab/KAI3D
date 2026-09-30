# 06_Django_Architecture_y_Configuracion.ipnyb

from django.contrib import admin
from .models import Material, Impresion

# Registra los modelos

admin.site.register(Material)
admin.site.register(Impresion)


