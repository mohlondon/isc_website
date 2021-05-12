from django import forms
from .models import Event, Commenters
from materials.models import Material
from Users.models import CustomUser

class EventsForm(forms.ModelForm):
    # widgett = MultiWidget(widgets=[TextInput, TextInput])
    title = forms.CharField(label="", widget=forms.TextInput(attrs={
        "placeholder": "Title",
        "class": "form-control ",
        'style': 'width:47%;margin:10px;'}))
    place = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Place",
        "class": "form-control",
        'style': 'width:47%;margin:10px;'}))
    description = forms.CharField(label="", widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "description",
        "rows": "4",
        "style": "margin:10px;"
    }))
    Date = forms.DateField(label='', widget=forms.DateInput(attrs={
        "class": "form-control",
        "type": "date",
        "style": "width:47%;margin:10px;"
    }))
    Email = forms.EmailField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Email",
        "class": "form-control",
        "style": "margin:10px;width:47%;"
    }))

    Coach = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Coach",
        "class": "form-control",
        "style": "width:47%;margin:10px;"
    }))
    type = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Event Type",
        "class": "form-control",
        "style": "width:47%;margin:10px;"
    }))
    Picture = forms.FileField(label='', widget=forms.FileInput(attrs={
        "placeholder": "Picture",
        "class": "custom-file",
        "style": "width:47%;margin:10px;"
    }))
    material = forms.ModelMultipleChoiceField(required=False,queryset = Material.objects.filter(Quantity__gte=1))
    class Meta:
        model = Event
        fields = ["title", "place", "Date", "Coach",
                  "description", "Email", "Picture", "material","type"]


class CommenterForm(forms.ModelForm):
    comment = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Press Enter To Post Comment ",
        "class": "form-control form-control-sm",
        "style": "margin:10px;"
    }))

    class Meta:
        model = Commenters
        fields = ["comment"]
