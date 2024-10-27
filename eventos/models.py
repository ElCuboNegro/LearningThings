from django.db import models
from comercios.models import Venue
from menus.models import Menu
import uuid

class Evento(models.Model): 
    # Un evento puede pasar en multiples comercios? por ejemplo, burgermaster o eventos similares que ocurren en multiples puntos?
    # SI, pero independientemente de esto, un comercio puede tener multiples eventos, pero cada evento tiene su propio menu para cada evento.
    # tal vez sea una buena idea refactorizar para que los eventos sean independientes de los comercios para respetar el principio de responsabilidad unica.
    evento_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    fecha = models.DateField(auto_now_add=True)  # El momento de creación de cada evento
    nombre = models.CharField(max_length=100)  # Nombre del evento

class EventoVenue(models.Model):
    evento_venue_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='eventos_venues')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)  # Relación con el modelo Venue
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)  # Menú específico para este evento