from django.db import models
# El Modelo Tarea utiliza un campo nuevo, el de usuario, el cual almacena el correo del usuario que es el propietario de la tarea. 

# Create your models here.

class Tarea(models.Model):
    descripcion = models.TextField()
    fechaFin = models.DateTimeField()
    duracion = models.FloatField()
    tiempoReg = models.FloatField()
    estatus = models.CharField(max_length=1)
    usuario = models.TextField(default="")

    def _str_(self):
        return self.descripcion