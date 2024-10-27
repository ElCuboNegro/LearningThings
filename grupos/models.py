from django.db import models
from django.utils import timezone
from usuarios.models import Usuario
from actividades.models import Actividad
from comercios.models import Venue

class Grupo(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    usuarios = models.ManyToManyField(Usuario, related_name="grupos")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateField(default=timezone.now)  # Usar default sin auto_now_add

# Create your models here.
class CalificacionGrupo(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)  # Usar cadena
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Usuario que califica
    puntuacion = models.IntegerField()  # Calificación dada por el usuario
    fecha_creacion = models.DateField(default=timezone.now)  # Usar default sin auto_now_add
