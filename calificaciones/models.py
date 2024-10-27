from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from usuarios.models import Usuario
from actividades.models import Actividad

class CalificacionGenerica(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Usuario que califica
    puntuacion = models.IntegerField()  # Calificación dada por el usuario
    fecha = models.DateField(auto_now_add=True)  # Fecha de la calificación

    # Campos para GenericForeignKey
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Tipo de entidad
    object_id = models.PositiveIntegerField()  # ID de la entidad
    content_object = GenericForeignKey('content_type', 'object_id')  # Objeto calificado

class CalificacionActividad(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name='calificaciones_actividad_actividades')  # Cambiar related_name para evitar conflictos
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='calificaciones_actividad_usuarios')  # Cambiar related_name para evitar conflictos
    puntuacion = models.IntegerField()  # Calificación dada por el usuario
    fecha = models.DateField(auto_now_add=True)  # Fecha de la calificación