from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Rifa(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    encargado = models.CharField(max_length=100)
    fecha = models.DateField()
    caratula = models.ImageField(upload_to='caratulas/')
    total_posiciones = models.PositiveIntegerField()
    qr = models.ImageField(upload_to='qr/', blank=True, null=True)
    cuenta = models.CharField(max_length=100)
    numerocuenta = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Posicion(models.Model):
    rifa = models.ForeignKey(Rifa, related_name='posiciones', on_delete=models.CASCADE)
    numero = models.PositiveIntegerField()
    reservado = models.BooleanField(default=False)
    nombre_completo = models.CharField(max_length=200, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    comprobante = models.ImageField(upload_to='comprobantes/', blank=True, null=True)

    def __str__(self):
        return f"{self.rifa.nombre} - Posición {self.numero}"

# Señal para crear posiciones automáticamente
@receiver(post_save, sender=Rifa)
def crear_posiciones_automaticamente(sender, instance, created, **kwargs):
    if created and instance.posiciones.count() == 0:
        for i in range(1, instance.total_posiciones + 1):
            Posicion.objects.create(rifa=instance, numero=i)
