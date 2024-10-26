from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from usuarios.models import Usuario, Actividad  # Importa el modelo Usuario

class CalificacionGenerica(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)  # Usuario que califica
    puntuacion = models.IntegerField()  # Calificación dada por el usuario
    fecha = models.DateField(auto_now_add=True)  # Fecha de la calificación

    # Campos para GenericForeignKey
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Tipo de entidad
    object_id = models.PositiveIntegerField()  # ID de la entidad
    content_object = GenericForeignKey('content_type', 'object_id')  # Objeto calificado

# Create your models here.
class Venue(models.Model):
    nombre = models.CharField(max_length=100)
    actividades = models.ManyToManyField(Actividad, related_name="venues")
    tipo = models.CharField(max_length=100)  # Tipo de comercio (cultural venue)
    calificacion = models.FloatField(default=0.0)  # Promedio de calificaciones
    latitud = models.CharField(max_length=255)
    longitud = models.CharField(max_length=255)
    calificaciones = GenericRelation(CalificacionGenerica)  # Relación con calificaciones

class MenuItem(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del elemento
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del elemento
    foto = models.ImageField(upload_to='items/')  # Foto del elemento
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional del elemento
    calificaciones = GenericRelation(CalificacionGenerica)  # Relación con calificaciones

class Menu(models.Model):
    comercio = models.ForeignKey(Venue, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(MenuItem, related_name='menus')  # Agregado related_name

class Evento(models.Model):
    comercio = models.ForeignKey(Venue, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)  # El momento de creación de cada evento
    nombre = models.CharField(max_length=100)  # Nombre del evento
    invitados = models.ManyToManyField(Usuario, related_name='eventos_invitados')  # Cambiado a 'Usuario'
    asistentes = models.ManyToManyField(Usuario, related_name='eventos_asistentes')  # Cambiado a 'Usuario'
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
