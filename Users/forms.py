from django import forms
from .models import CustomUser,Profile


class SignUpForm(forms.ModelForm):
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        "placeholder": "password",
        "class": "form-control ",
        'style': ''}))
    re_password = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        "placeholder": "repeate password",
        "class": "form-control ",
        'style': ''}))
    username = forms.CharField(label="", widget=forms.TextInput(attrs={
        "placeholder": "username",
        "class": "form-control ",
        'style': ''}))
    gender = forms.ChoiceField(required=False,choices=(("","-----"),("M","Male"),("F","Female")), widget=forms.Select(attrs={
        "class": "custom-file",
        "style": "width:47%;margin:10px;"
    }))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={
        "placeholder": "email",
        "class": "form-control ",
        'style': ''}))

    class Meta:
        model = CustomUser
        fields = ["username", "email","gender", "password", "re_password"]

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("re_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords Doesn't match Please Repeate Again"
            )


class EditCustom(forms.ModelForm):
    Picture = forms.FileField(required=False, widget=forms.FileInput(attrs={
        "placeholder": "Picture",
        "class": "custom-file",
        "style": "width:47%;margin:10px;"
    }))
    gender = forms.ChoiceField(required=False,choices=(("-----",""),("M","Male"),("F","Female")), widget=forms.Select(attrs={
        "class": "custom-file",
        "style": "width:47%;margin:10px;"
    }))
    class Meta:
        model = CustomUser
        fields = ["first_name","last_name","username","email","Picture","gender"]


class EditProfileForm(forms.ModelForm):
    username = forms.CharField( widget=forms.TextInput(attrs={
        "placeholder": "Username",
        "class": "form-control col-12 mb-3",
        'style': ''}))
    last_name = forms.CharField( widget=forms.TextInput(attrs={
        "placeholder": "Last Name",
        "class": "form-control col-12 mb-3",
        'style': ''}))
    first_name = forms.CharField( widget=forms.TextInput(attrs={
        "placeholder": "First Name",
        "class": "form-control col-12 mb-3",
        'style': ''}))
    discipline = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "placeholder": "Discipline",
        "class": "form-control col-12 mb-3",
        'style': ''}))
    Phone = forms.CharField(required=False , widget=forms.TextInput(attrs={
        "placeholder": "Phone Number",
        "class": "form-control col-12 mb-3",
        'style': ''}))
    Education = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "placeholder": "Education",
        "class": "form-control col-12 mb-3",
        'style': ''}))
    fb_account = forms.CharField(required=False , widget=forms.TextInput(attrs={
        "placeholder": "Facebook Account url",
        "class": "form-control col-12 mb-3",
        'style': ''}))
    skills = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "placeholder": "Skills",
        "class": "form-control col-12 mb-3",
        'style': ''}))
    Picture = forms.FileField(required=False, widget=forms.FileInput(attrs={
        "placeholder": "Picture",
        "class": "custom-file",
        "style": "width:47%;margin:10px;"
    }))
    email = forms.EmailField( widget=forms.EmailInput(attrs={
        "placeholder": "Email",
        "class": "form-control col-12 mb-3",
        'style': ''}))
    bio = forms.CharField(required=False,widget=forms.TextInput(attrs={
        "placeholder": "Bio",
        "class": "form-control col-12 mb-3",
        'style': ''}))
    YearOfStudy = forms.ChoiceField(required=False,choices=(
        (1,"L1"),
        (2,"L2"),
        (3,"L3"),
        (4,"M1"),
        (5,"M2")
    ), widget=forms.Select(attrs={
        "placeholder": "Bio",
        "class": "form-control col-6 mb-3",
        'style': ''}))
    gender = forms.ChoiceField(required=False,choices=(("-----",""),("M","Male"),("F","Female")), widget=forms.Select(attrs={
        "class": "form-control col-6 mb-3",
        "style": ""
    }))
    class Meta:
        model = Profile
        fields = ["first_name","last_name","username","email","YearOfStudy","gender","Picture" ,"Education","discipline","fb_account","Phone","skills","bio"]

