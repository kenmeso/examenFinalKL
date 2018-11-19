from django.contrib import admin
from pensumFinal.models import Grado, GradoAdmin, Materia, MateriaAdmin
# Register your models here.
admin.site.register(Grado, GradoAdmin)
admin.site.register(Materia, MateriaAdmin)
