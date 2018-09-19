from django.contrib import admin
from .models import Secretaria,Unidad,Personal_secretaria,Personal_unidad

admin.site.register(Secretaria)
admin.site.register(Unidad)
admin.site.register(Personal_secretaria),
admin.site.register(Personal_unidad)