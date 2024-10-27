from django.db import models
from django.utils import timezone

class Tag(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='actividades/', null=True, blank=True)
    fecha_creacion = models.DateField(default=timezone.now)  # Usar default sin auto_now_add
    fecha_modificacion = models.DateField(auto_now=True)
    fecha_eliminacion = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField('actividades.Tag', related_name='actividades')

