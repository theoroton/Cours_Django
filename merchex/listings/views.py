from django.shortcuts import render
from django.http import HttpResponse # Import nécessaire

# Fonction pour une première page
def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')


# Fonction pour la page à propos
def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch !</p>')


# Fonction pour le formulaire de contact
def contact(request):
    return HttpResponse('<h1>Formulaire de contact</h1>')


# Fonction pour la page de listing
def listings(request):
    return HttpResponse('<h1>Listings</h1>')