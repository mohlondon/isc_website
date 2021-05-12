from django.db.models.signals import post_save
from django.dispatch import receiver
from Users.models import CustomUser, Notifications
from .models import Commenters, Event, Likes


@receiver(post_save, sender=Commenters)
def create_Comment(sender, instance, created, **kwargs):
    if created and instance.event.user.id != instance.user.id:
        Notifications.objects.create(Member_id=instance.event.user.id,body=instance.user.username + ' Commented to your event ')
