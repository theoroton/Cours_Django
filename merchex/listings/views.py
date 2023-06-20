from django.shortcuts import render
from django.http import HttpResponse # Import nécessaire

from listings.models import Band # Modèle Band importé
from listings.models import Listing # Modèle Listing importé

from django.shortcuts import render # Render pour les fichiers templates html


# Fonction pour une première page
def hello(request):
    bands = Band.objects.all() # Récupère les groupes

    return render(request, 
    'listings/hello.html', 
    {'bands': bands}) # Récupération du template (render crée un objet HttpResponse)


    ''' ANCIEN CODE
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
    '''



# Fonction pour la page à propos
def about(request):
    return render(request, 'listings/about.html')



# Fonction pour le formulaire de contact
def contact(request):
    return render(request, 'listings/contact.html')



# Fonction pour la page de listing
def listings(request):
    listings = Listing.objects.all() # Récupère les affiches

    return render(request, 
    'listings/listings.html', 
    {'listings': listings})