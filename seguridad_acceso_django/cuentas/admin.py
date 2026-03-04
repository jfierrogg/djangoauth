from django.contrib import admin
from .models import ConsultaContacto

@admin.register(ConsultaContacto)
class ConsultaContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'fecha_envio')
    search_fields = ('nombre', 'correo')              
    readonly_fields = ('fecha_envio',)               