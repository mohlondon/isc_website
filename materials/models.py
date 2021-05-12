from django.db import models
from django.urls import reverse
from Users.models import CustomUser


class Material(models.Model):
    component_name = models.CharField(max_length=120)
    Picture = models.FileField(null=True,default="defaultComponent.png")
    description = models.TextField(max_length=120)
    reference = models.CharField(max_length=120, unique=True)
    note = models.CharField(max_length=120,default="",null=True)
    purchased_at = models.DateField(auto_now_add=True)
    Quantity_in_stock = models.IntegerField(default=1)
    Quantity = models.IntegerField(default=1)
    Category = models.CharField(max_length =120 ,default="")
    objects = models.Manager()
    def get_detail_url(self):
        return reverse("materials:Detail_View", kwargs={"pk": self.pk})
    def get_update_url(self):
        return reverse("materials:update-material", kwargs={"pk": self.pk})
    def get_absolute_url(self):
        return reverse("materials:list-material")

    def __str__(self):
        return self.component_name


class Borrowing_order(models.Model):
    material = models.ManyToManyField(Material)
    requested_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    requested_at = models.DateField(auto_now_add=True)
    Reason = models.TextField()
    Quantity = models.IntegerField(default=1)
    return_at = models.DateField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.matirial.component_name
