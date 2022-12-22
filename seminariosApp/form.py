from django import forms
from seminariosApp.models import Registro, Institucion

class formRegistro(forms.ModelForm):
    class Meta:
        model = Registro 
        fields = ['nombre', 'telefono', 'fecha_inscripcion', 'institucion', 'hora_inscripcion', 'estado', 'observacion']
        widgets = {
            'fecha_inscripcion': forms.DateInput(attrs={'type': 'date'}),
        }
        exclude = ['hora_inscripcion']
