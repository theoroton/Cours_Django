from django.shortcuts import render
from django.http import HttpResponse # Import nécessaire

from listings.models import Band # Modèle Band importé
from listings.models import Listing # Modèle Listing importé


# Fonction pour une première page
def hello(request):
    bands = Band.objects.all()

    # Réponse HTTP à afficher retourné
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Groupes :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """)



# Fonction pour la page à propos
def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch !</p>')



# Fonction pour le formulaire de contact
def contact(request):
    return HttpResponse('<h1>Formulaire de contact</h1>')



# Fonction pour la page de listing
def listings(request):
    listings = Listing.objects.all()

    response = """<h1>Listings</h1>
                  <ul>
                """

    for listing in listings:
        response += f"<li>{listing.title}</li>"


    response += "<ul>"

    return HttpResponse(response)