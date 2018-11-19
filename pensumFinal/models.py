from django.db import models
from django.contrib import admin

class Grado(models.Model):
    nombre  =   models.CharField(max_length=25)
    seccion = models.CharField(max_length=2)
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre    = models.CharField(max_length=60)
    grados   = models.ManyToManyField(Grado, through='Listado')
    def __str__(self):
        return self.nombre

class Listado(models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)


class ListadoInLine(admin.TabularInline):
    model = Listado
    extra = 1

class GradoAdmin(admin.ModelAdmin):
    inlines = (ListadoInLine,)

class MateriaAdmin (admin.ModelAdmin):
    inlines = (ListadoInLine,)
