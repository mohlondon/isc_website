import django_filters
from .models import Material
from django import forms


class MaterialFilter(django_filters.FilterSet):
    component_name = django_filters.CharFilter(lookup_expr='icontains', label='', widget=forms.TextInput(attrs={
        "placeholder": "component Name",
        "class": "form-control col-2 m-2",
        'style': ''}))
    Category = django_filters.CharFilter(lookup_expr='icontains', label='', widget=forms.TextInput(attrs={
        "placeholder": "Category",
        "class": "form-control col-2 m-2",
        'style': ''}))
    reference = django_filters.CharFilter(label='',lookup_expr='icontains', widget=forms.TextInput(attrs={
        "placeholder": "Reference",
        "class": "form-control col-2 m-2",
        'style': ''}))

    class Meta:
        model = Material
        exclude = [ "Picture", "Quantity","Quantity_in_stock","note",
                   "purchased_at", "description", "is_available"]
