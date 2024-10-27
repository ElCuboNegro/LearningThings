from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from actividades.models import Actividad
from calificaciones.models import CalificacionGenerica
from menus.models import Menu


# Create your models here.
class Venue(models.Model):
    nombre = models.CharField(max_length=100)
    actividades = models.ManyToManyField(Actividad, related_name="venues")
    tipo = models.CharField(max_length=100)  # Tipo de comercio (cultural venue)
    calificacion = models.FloatField(default=0.0)  # Promedio de calificaciones
    latitud = models.CharField(max_length=255)
    longitud = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)  # Permitir que sea nulo
    calificaciones = GenericRelation(CalificacionGenerica)  # Relación con calificaciones



class Promocion(models.Model):
    TIPO_PROMOCION = [
        ('rebaja', 'Rebaja'),
        ('combo', 'Combo'),
        ('rebaja_total', 'Rebaja a toda la carta'),
        ('happy_hour', 'Happy Hour'),
        # Otros tipos de promociones que desees agregar
    ]

    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_PROMOCION)
    elementos_menu = models.ManyToManyField(Menu, related_name='promociones')  # Elementos del menú en promoción
    descripcion = models.TextField()  # Descripción de la promoción
    fecha_inicio = models.DateField()  # Fecha de inicio de la promoción
    fecha_fin = models.DateField()  # Fecha de fin de la promoción
