from django.db import models
from menus.models import MenuItem

class Promocion(models.Model):
    descripcion = models.CharField(max_length=100)
    menuitems = models.ManyToManyField(MenuItem)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)
