from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Material


@receiver(post_save, sender=Material)
def create_Comment(sender, instance, created, **kwargs):
    if created:
        instance.Quantity_in_stock = instance.Quantity
        instance.save()
