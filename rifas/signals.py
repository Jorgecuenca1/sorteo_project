from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rifa, Posicion

@receiver(post_save, sender=Rifa)
def crear_posiciones_automaticamente(sender, instance, created, **kwargs):
    if created and instance.posiciones.count() == 0:
        for i in range(1, instance.total_posiciones + 1):
            Posicion.objects.create(rifa=instance, numero=i)
