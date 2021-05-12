from django import forms
from .models import Material


class MaterialForm(forms.ModelForm):
    component_name = forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder": "component Name",
        "class": "form-control ",
        'style': 'margin:10px;'}))
    description = forms.CharField(label='',required=False , widget=forms.TextInput(attrs={
        "placeholder": "Description",
        "class": "form-control ",
        'style': 'margin:10px;'}))
    reference = forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder": "Reference",
        "class": "form-control ",
        'style': 'margin:10px;'}))
    Category = forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder": "Category",
        "class": "form-control ",
        'style': 'margin:10px;'}))
    note = forms.CharField(label='',required=False,widget=forms.TextInput(attrs={
        "placeholder": "Note",
        "class": "form-control ",
        'style': 'margin:10px;'}))
    Quantity = forms.IntegerField(label='',initial=1,widget=forms.NumberInput(attrs={
        "placeholder": "Quantity",
        "class": "form-control ",
        'style': 'margin:10px;'}
    ))
    Picture = forms.FileField(label='',required=False ,widget=forms.FileInput(attrs={
        "placeholder": "Picture",
        "class": "",
        'style': 'margin:10px;'}
    ))

    class Meta:
        model = Material
        fields = ["component_name", "description",
                  "reference", 'Quantity', "Picture","note","Category"]
