from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TareaSerializer
from .models import Tarea

# Create your views here.

class TareaView(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()