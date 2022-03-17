from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TareaSerializer
from .models import Tarea

# Create your views here.


class TareaView(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    # Método que "sobreescribe" el método utilizado cuando se recibe una llamada GET. 
    # Al recibir una llamada GET, valida si hay algún parámetro en el query. 
    # De ser así, retorna las tareas almacenadas con el valor del parámetro.
    
    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Tarea.objects.all()
            usuario = self.request.GET.get('q', None)
            if usuario is not None:
                queryset = queryset.filter(usuario=usuario)
            return queryset
        # Adicionalmente se añaden listados de los elementos al recibir llamadas DELETE y PUT. 
        # Esto último porque, por alguna razón, el API bloqueaba llamadas de estos tipos cuando estas líneas no estaban presentes.
        if self.request.method == 'DELETE':
            print("es delete")
            queryset = Tarea.objects.all()
            return queryset
        if self.request.method == 'PUT':
            print("es put!")
            queryset = Tarea.objects.all()
            return queryset
