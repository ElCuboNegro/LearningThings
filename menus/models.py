from django.db import models
from calificaciones.models import CalificacionGenerica
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.
class MenuItem(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del elemento
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del elemento
    foto = models.ImageField(upload_to='items/')  # Foto del elemento
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional del elemento
    calificaciones = GenericRelation(CalificacionGenerica)  # Relación con calificaciones

class Menu(models.Model):
    menu_items = models.ManyToManyField(MenuItem, related_name='menus')  # Agregado related_name