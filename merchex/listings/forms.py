# Fichier pour le formulaire de l'application
from django import forms

# Classe contact
class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    message = forms.CharField(max_length=1000, required=True)