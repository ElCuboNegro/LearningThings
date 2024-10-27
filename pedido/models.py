from django.db import models
from usuarios.models import Usuario
from eventos.models import Evento
from comercios.models import Venue
from menus.models import MenuItem
from promociones.models import Promocion
import uuid

class Pedido(models.Model):
    pedido_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado'), ('cancelado', 'Cancelado')])
    items_pedido = models.ManyToManyField(MenuItem, blank=True)
    items_promocion = models.ManyToManyField(Promocion, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)
