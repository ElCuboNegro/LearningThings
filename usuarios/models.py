from django.db import models
from django.contrib.auth.models import User
from actividades.models import Actividad


# Create your models here.
class Usuario(models.Model):
    GENERO_USUARIO = [
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('no_binario', 'No binario'),
        ('otro', 'Otro'),
        ('prefiero_no_decirlo', 'Prefiero no decirlo'),
        # Otros tipos de promociones que desees agregar
    ]

    ESTADO_CIVIL = [
        ('soltero', 'Soltero'),
        ('casado', 'Casado'),
        ('es_complicado', 'Es complicado'),
        ('en_relacion_abierta', 'En relación abierta'),
    ]

    TIPO_16_PERSONALIDADES_A = [
        ('introvertido', 'Introvertido'),
        ('extrovertido', 'Extrovertido'),
    ]

    TIPO_16_PERSONALIDADES_B = [        
        ('sensorial', 'Sensorial'),
        ('intuitivo', 'Intuitivo'),
    ]

    TIPO_16_PERSONALIDADES_C = [
        ('pensamiento', 'pensamiento'),
        ('emocional', 'emocional'),
    ]

    TIPO_16_PERSONALIDADES_D = [
        ('calificador', 'calificador'),
        ('perceptivo', 'Perceptivo'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True, blank=True)  # Nombre de usuario único, inicialmente vacío
    foto_perfil = models.ImageField(upload_to='usuarios/', null=True, blank=True)  # Foto de perfil del usuario
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    fecha_eliminacion = models.DateField(null=True, blank=True)

    genero = models.CharField(max_length=20, choices=GENERO_USUARIO, null=True, blank=True)
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL, null=True, blank=True)
#    universidad = models.CharField(max_length=200, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    tipo_16personalidades_A = models.CharField(max_length=20, choices=TIPO_16_PERSONALIDADES_A, null=True, blank=True)
    tipo_16personalidades_B = models.CharField(max_length=20, choices=TIPO_16_PERSONALIDADES_B, null=True, blank=True)
    tipo_16personalidades_C = models.CharField(max_length=20, choices=TIPO_16_PERSONALIDADES_C, null=True, blank=True)
    tipo_16personalidades_D = models.CharField(max_length=20, choices=TIPO_16_PERSONALIDADES_D, null=True, blank=True)

    fecha_ultimo_evento = models.DateField(null=True, blank=True) #  fecha del último evento que el usuario ha participado y asistido

    spontime_activo = models.BooleanField(default=False) # indica si el usuario está activo en el momento
    actividades_spontime_activo = models.ManyToManyField(Actividad, related_name="actividades_activas_usuario") # actividades en las que el usuario está activo en el momento
    reputacion = models.FloatField(default=0) # reputación del usuario
    gustos_actividades = models.ManyToManyField(Actividad, through='GustoActividad', related_name='usuarios_gustos')

    def save(self, *args, **kwargs):
        # Asignar el username como el id del usuario si está vacío
        if not self.username:
            self.username = str(self.user.id)  # Convertir el id a string
        super().save(*args, **kwargs)  # Llamar al método save de la clase base

class Login(models.Model):
    TIPO_DISPOSITIVO = [
        ('movil', 'Movil'),
        ('web', 'Web'),
    ]
    
    fecha_login = models.DateField(auto_now_add=True)
    dispositivo = models.CharField(max_length=20, choices=TIPO_DISPOSITIVO)

class CalificacionActividad(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name='calificaciones_usuario')  # Agregar related_name
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='calificaciones_usuario_usuarios')  # Cambiar related_name para evitar conflictos
    puntuacion = models.IntegerField()  # Calificación dada por el usuario
    fecha = models.DateField(auto_now_add=True)  # Fecha de la calificación

class UsuariosBloqueados(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Usuario que bloquea
    usuario_bloqueado = models.ForeignKey(Usuario, related_name='bloqueadores', on_delete=models.CASCADE)  # Usuario bloqueado
    fecha_bloqueo = models.DateField(auto_now_add=True)  # Fecha en que se bloqueó al usuario
    fecha_desbloqueo = models.DateField(null=True, blank=True)  # Fecha en que se desbloqueó al usuario
    bloqueo_activo = models.BooleanField(default=True)  # Indica si el bloqueo está activo

class ComprobacionesDeSeguridad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Usuario al que se le realiza la comprobación
    kyc_completado = models.BooleanField(default=False)  # Indica si el KYC está completado
    fecha_comprobacion = models.DateField(auto_now_add=True)  # Fecha de la comprobación
    # Otros campos necesarios para las comprobaciones de seguridad

class GustoActividad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    nivel_gusto = models.IntegerField(default=0)  # Puedes usar un rango de 1 a 5, por ejemplo

    class Meta:
        unique_together = ('usuario', 'actividad')  # Asegura que un usuario no pueda tener múltiples entradas para la misma actividad

    def __str__(self):
        return f"{self.usuario.username} - {self.actividad.nombre}: {self.nivel_gusto}"
