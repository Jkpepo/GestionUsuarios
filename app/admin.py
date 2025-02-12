from django.contrib import admin
from .models import DatosUsuario,Empresa

# Register your models here.
admin.site.register(DatosUsuario)
# admin.site.register(Curso)
admin.site.register(Empresa)
