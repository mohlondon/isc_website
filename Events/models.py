from Users.models import CustomUser
from django.db import models
from django.urls import reverse
from materials.models import Material


class Event(models.Model):
    title = models.CharField(max_length=120)
    place = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    Date = models.DateField(null=True, blank=True)
    Coach = models.CharField(max_length=120, null=True)
    ParticipantFile = models.CharField(max_length=120, null=True)
    Email = models.EmailField(null=True)
    Picture = models.FileField(null=True)
    type = models.CharField(choices=(("E", "Event"), ("W", "WorkShop")),max_length=120,default='E')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now_add=True, null=True)
    status = models.IntegerField(default=0)
    material = models.ManyToManyField(Material)
    objects = models.Manager()

    def get_edit_url(self):
        return reverse("Edit View", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("Delete View", kwargs={"pk": self.pk})

    def get_detail_url(self):
        return reverse("Detail View", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        return reverse("events:Home-View")

    def __str__(self):
        return self.title


class Participant(models.Model):
    participant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Event = models.ForeignKey(Event, on_delete=models.DO_NOTHING, default='')
    group = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.participant.username


class Sessions(models.Model):
    name = models.CharField(max_length=120)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    group = models.IntegerField(default=0, null=True)
    date = models.DateField(auto_now_add=True)


class Attendance(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.DO_NOTHING)
    session = models.ForeignKey(Sessions, on_delete=models.DO_NOTHING,null=True)
    checked_in = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.participant.participant.username


class Commenters(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def get_absolute_url(self):
        return ""


class Likes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def get_absolute_url(self):
        return ""
