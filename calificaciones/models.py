from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from usuarios.models import Usuario
from actividades.models import Actividad
import uuid
class CalificacionGenerica(models.Model):
    calificacion_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Usuario que califica
    puntuacion = models.IntegerField()  # Calificación dada por el usuario
    fecha = models.DateField(auto_now_add=True)  # Fecha de la calificación

class CalificacionActividad(CalificacionGenerica):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name='calificaciones_actividad_actividades')  # Cambiar related_name para evitar conflictos
