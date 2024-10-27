from django.db import models
from grupos.models import Grupo
from usuarios.models import Usuario

class Mensaje(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='mensajes')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username}: {self.contenido[:20]}..."  # Muestra un resumen del mensaje