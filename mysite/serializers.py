from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ('id', 'descripcion', 'fechaFin', 'duracion', 'tiempoReg', 'estatus', 'usuario')
