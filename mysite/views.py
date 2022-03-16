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
                queryset = queryset.filter('estatus'!='E')
            return queryset
