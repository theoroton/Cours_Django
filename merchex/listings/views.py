from django.shortcuts import render
from django.http import HttpResponse # Import nécessaire

from listings.models import Band # Modèle Band importé
from listings.models import Listing # Modèle Listing importé

from django.shortcuts import render # Render pour les fichiers templates html


# Fonction pour une première page
def band_list(request):
    bands = Band.objects.all() # Récupère les groupes

    return render(request, 
        'listings/band_list.html', 
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


# Fonction pour le détail d'un groupe
def band_detail(request, id):
    band = Band.objects.get(id=id)
    listings_for_band = Listing.objects.filter(band__id=band.id)
    print(listings_for_band.count())

    return render(request,
                  'listings/band_detail.html',
                  {'band': band, 'listings_for_band': listings_for_band})



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
    'listings/listing_list.html', 
    {'listings': listings})


# Fonction pour le détail d'une annonce
def listing_detail(request, id):
    listing = Listing.objects.get(id=id)

    return render(request,
                  'listings/listing_detail.html',
                  {'listing': listing})