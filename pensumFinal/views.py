from django.shortcuts import render
from django.contrib import messages
from .forms import MateriaForm
from pensumFinal.models import Materia, Listado

def materia_nueva(request):
    if request.method == "POST":
        formulario = MateriaForm(request.POST)
        if formulario.is_valid():
            materia = Materia.objects.create(nombre=formulario.cleaned_data['nombre'], grados = formulario.cleaned_data['grados'])
            for grado_id in request.POST.getlist('grados'):
                listado = Listado(grado_id=grado_id, materia_id = materia.id)
                listado.save()
                messages.add_message(request, messages.SUCCESS, 'Materia Guardada Exitosamente')
    else:
        formulario = MateriaForm()
    return render(request, 'pensumFinal/materia_editar.html', {'formulario': formulario})
