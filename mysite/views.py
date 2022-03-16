from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TareaSerializer
from .models import Tarea

# Create your views here.


class TareaView(viewsets.ModelViewSet):
    serializer_class = TareaSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Tarea.objects.all()
            usuario = self.request.GET.get('q', None)
            if usuario is not None:
                queryset = queryset.filter(usuario=usuario)
            return queryset
        if self.request.method == 'DELETE':
            print("es delete")
            queryset = Tarea.objects.all()
            return queryset
        if self.request.method == 'PUT':
            print("es put!")
            queryset = Tarea.objects.all()
            return queryset
