from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    actividades_no_me_gustan = models.ManyToManyField("Actividad", related_name="usuarios_no_gustan")

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)

class Grupo(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    usuarios = models.ManyToManyField(Usuario, related_name="Grupos")

class CalificacionGrupo(models.Model):
    grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE)  # Relación con el modelo Grupo
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Usuario que califica
    puntuacion = models.IntegerField()  # Calificación dada por el usuario
    fecha = models.DateField(auto_now_add=True)  # Fecha de la calificación

class CalificacionActividad(models.Model):
    actividad = models.ForeignKey('Actividad', on_delete=models.CASCADE)  # Relación con el modelo Actividad
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Usuario que califica
    puntuacion = models.IntegerField()  # Calificación dada por el usuario
    fecha = models.DateField(auto_now_add=True)  # Fecha de la calificación

class UsuariosBloqueados(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Usuario que bloquea
    usuario_bloqueado = models.ForeignKey(Usuario, related_name='bloqueadores', on_delete=models.CASCADE)  # Usuario bloqueado
    fecha_bloqueo = models.DateField(auto_now_add=True)  # Fecha en que se bloqueó al usuario

class ActividadesRechazadas(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Usuario que rechaza la actividad
    actividad = models.ForeignKey('Actividad', on_delete=models.CASCADE)  # Actividad rechazada
    fecha_rechazo = models.DateField(auto_now_add=True)  # Fecha en que se rechazó la actividad

class ComprobacionesDeSeguridad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Usuario al que se le realiza la comprobación
    kyc_completado = models.BooleanField(default=False)  # Indica si el KYC está completado
    fecha_comprobacion = models.DateField(auto_now_add=True)  # Fecha de la comprobación
    # Otros campos necesarios para las comprobaciones de seguridad
