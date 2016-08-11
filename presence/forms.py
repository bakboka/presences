from django import forms
from .models import Student


class LogInForm(forms.Form):
    username = forms.CharField(label ="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)




