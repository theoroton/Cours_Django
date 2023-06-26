from django.shortcuts import render
from django.http import HttpResponse # Import nécessaire

from listings.models import Band # Modèle Band importé
from listings.models import Listing # Modèle Listing importé

from django.shortcuts import render # Render pour les fichiers templates html
from django.core.mail import send_mail # Librairie pour envoyer un mail

from listings.forms import ContactUsForm # Formulaire de contact
from listings.forms import BandForm # Formulaire pour ajouter un groupe
from listings.forms import ListingForm # Formulaire pour ajouter une annonce

from django.shortcuts import redirect # Redirection vers une autre page


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



# Fonction pour ajouter un groupe
def band_create(request):
    # Si c'est une requête GET
    if request.method == 'GET':
        form = BandForm() # Crée un nouveau formulaire

    # Si c'est une requête POST
    else:
        form = BandForm(request.POST) # Formulaire avec les données

        # Si le formulaire est valide
        if form.is_valid():
            band = form.save() # Récupère les informations du formulaire et crée un objet Band à partir

            # Va vers le détail du nouveau groupe à l'aide de l'id du groupe créé
            return redirect('band-detail', band.id)

    return render(request, 
                  'listings/add_band.html',
                  {'form': form})




# Fonction pour la page à propos
def about(request):
    return render(request, 'listings/about.html')



# Fonction pour le formulaire de contact
def contact(request):
    # Si c'est la méthode get
    if request.method == 'GET':
        form = ContactUsForm() # Initialisation du formulaire

    # Si c'est la méthode post
    else:
        # Crée une instance du formulaire et le remplit avec les données POST
        form = ContactUsForm(request.POST)
        
        # Si le formulaire est valide
        if form.is_valid():
            # Envoie un mail (sur le serveur fictif)
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us Form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['test@merchex.xyz'])
            
            # Redirige vers une autre page
            return redirect('email-sent')


    return render(request, 
        'listings/contact.html',
        {'form': form})



# Fonction pour le retour d'une formulaire de contact
def email(request):
    return render(request,
        'listings/email_sent.html')



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


# Fonction pour ajouter une annonce
def listing_create(request):
    # Si c'est une requête GET
    if request.method == 'GET':
        form = ListingForm() # Crée un nouveau formulaire

    # Si c'est une requête POST
    else:
        form = ListingForm(request.POST) # Formulaire avec les données

        # Si le formulaire est valide
        if form.is_valid():
            listing = form.save() # Récupère les informations du formulaire et crée un objet Listing à partir

            # Va vers le détail de la nouvelle annonce à l'aide de son id
            return redirect('listing-detail', listing.id)

    return render(request, 
                  'listings/add_listing.html',
                  {'form': form})