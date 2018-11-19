from django import forms
from .models import Grado, Materia


class MateriaForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Materia
        fields = ('nombre', 'grados')


def __init__ (self, *args, **kwargs):
        super(MateriaForm, self).__init__(*args, **kwargs)
        self.fields["grados"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["grados"].help_text = "Ingrese los Grados de las Materias"
        self.fields["grados"].queryset = Grado.objects.all()
