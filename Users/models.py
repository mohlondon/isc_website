from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Group


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    Picture = models.FileField(max_length=120, default="default.png")
    gender = models.CharField(
        choices=(("M", "Male"), ("F", "Female")), max_length=255, null=True)

    def get_edit_url(self):
        return reverse("accounts:Edit View", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("accounts:Delete View", kwargs={"pk": self.pk})

    def get_detail_url(self):
        return reverse("accounts:Profile Page", kwargs={"pk": self.profile.pk})

    def get_absolute_url(self):
        return reverse("accounts:ListUsers Page")


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    Phone = models.CharField(max_length=120, null=True)
    skills = models.CharField(max_length=200, null=True)
    Education = models.CharField(max_length=200, null=True)
    YearOfStudy = models.IntegerField(choices=(
        (1,"L1"),
        (2,"L2"),
        (3,"L3"),
        (4,"M1"),
        (5,"M2")
    ), null=True)
    discipline = models.CharField(max_length=200, null=True)
    fb_account = models.CharField(max_length=120, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user_type_data = ((2, "Members"), (1, "Orgnizers"))
    user_type = models.CharField(
        default=2, choices=user_type_data, max_length=10)
    bio = models.TextField(null=True, default='')


class Notifications(models.Model):
    Privacy_choices = (
        (0, 'Owner'),
        (1, 'Group'),
        (2, 'Groups'),
        (3, 'Public'),
    )
    Member = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    notif_vis = models.IntegerField(choices=Privacy_choices, default=0)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Messages(models.Model):
    Privacy_choices = (
        (0, 'Owner'),
        (1, 'Group'),
        (2, 'Groups'),
    )
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    receiver_id = models.IntegerField()
    message = models.TextField()
    notif_vis = models.IntegerField(choices=Privacy_choices, default=0)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
