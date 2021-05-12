from django.shortcuts import render, get_object_or_404, redirect
from Users.models import CustomUser
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView)
from django.http import JsonResponse
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf.urls import url
from Events.decorators import allowed_users
from .models import Material, Borrowing_order
from .forms import MaterialForm
from .filters import MaterialFilter


@method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=["Logistics"]), name='dispatch')
class CreateMaterial(CreateView):
    template_name = "materials/create.html"
    form_class = MaterialForm

    def get_queryset(self):
        queryset = Material.objects.all()
        return queryset


@method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=["Logistics"]), name='dispatch')
class DeleteMaterial(DeleteView):
    template_name = "materials/delete.html"
    def get_success_url(self):
        return reverse("materials:list-material")
    def get_object(self):
        return get_object_or_404(Material,id=self.kwargs.get("pk"))


@method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=["Logistics"]), name='dispatch')
class UpdateMaterial(UpdateView):
    template_name = "materials/create.html"
    form_class = MaterialForm

    def get_queryset(self):
        queryset = Material.objects.all()
        return queryset


@method_decorator(login_required, name="dispatch")
class ListMaterial(ListView):
    template_name = "materials/list.html"
    form_class = MaterialForm
    def get_my_queryset(self):
        if "Logistics" in [group.name for group in self.request.user.groups.all()]:
            return Material.objects.all()
        return Material.objects.filter(Quantity_in_stock__gte=1)
    def get_formFilter(self):
        return MaterialFilter(self.request.GET, queryset=self.get_my_queryset()).qs

    def get_queryset(self):
        return self.get_formFilter()

    def get_context_data(self, **kwargs):
        context = super(ListMaterial, self).get_context_data(**kwargs)
        context['myform'] = MaterialFilter(
            self.request.GET, queryset=self.get_my_queryset())
        return context


@method_decorator(login_required, name="dispatch")
class DetailMaterial(DetailView):
    template_name = "materials/detail.html"
    form_class = MaterialForm

    def get_queryset(self):
        queryset = Material.objects.all()
        return queryset


@method_decorator(login_required, name='dispatch')
@method_decorator(allowed_users(allowed_roles=["Logistics"]), name='dispatch')
class AdminMaterialListView(ListView):
    template_name = "materials/approve.html"

    def get_queryset(self):
        if 'status' in self.request.GET.keys():
            if str(self.request.GET['status']) == "1" or str(self.request.GET['status']) == "2" or str(self.request.GET['status']) == "0":
                return Borrowing_list.objects.filter(status=self.request.GET['status'])
        return Borrowing_list.objects.all()
