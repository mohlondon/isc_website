from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notifications, Profile, CustomUser
from django.core.mail import EmailMessage

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # email = EmailMessage('Hello', 'Welcome aboard', to=['baba066h.s@gmail.com'])
        # email.send()
        Notifications.objects.create(
            Member=instance, body='Welcome to Our platform we hope you get the best experience we suggest you update your profile information')


# @receiver(post_save, sender=Profile)
# def update_profile(sender, instance, created, **kwargs):
#     if created == False:
#         # instance.save()
#         Notifications.objects.create(
#             Member=instance.user, body='profile updated Successfully Thank You for your attention')
