from django.shortcuts import render
from django.http import HttpResponse # Import nécessaire

# Fonction pour une première page
def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')
