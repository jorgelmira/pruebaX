from django.conf import settings
from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    
    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()
    def __str__(self):
        return self.titulo

class Pecera(models.Model):
    usuario=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    nombre = models.CharField(max_length=50)
    tipo_agua = models.CharField(max_length=10)
    capacidad_litros = models.IntegerField()
    peces = models.TextField()
    fecha_ultimo_mantenimiento = models.DateTimeField(blank=True, null=True)
    iluminacion_led = models.BooleanField(default=False)
    observaciones = models.TextField()

    def __str__(self):
        return self.nombre

