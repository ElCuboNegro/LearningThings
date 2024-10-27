from django.db import models
from django.utils import timezone
from usuarios.models import Usuario
from actividades.models import Actividad
import uuid
from comercios.models import Venue
from calificaciones.models import CalificacionGenerica

class Grupo(models.Model):
    grupo_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    usuarios = models.ManyToManyField(Usuario, related_name="grupos")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateField(default=timezone.now)  # Usar default sin auto_now_add

# Create your models here.
class CalificacionGrupo(CalificacionGenerica):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)  # Usar cadena