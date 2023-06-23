from django.contrib import admin

from listings.models import Band # Permet de gérer le modèle Band en étant super utilisateur
from listings.models import Listing # Permet de gérer le modèle Listing en étant super utilisateur

# Change l'affichage du modèle Band dans l'interface admin
class BandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year_formed', 'genre')


# Change l'affichage du modèle Listing dans l'interface admin
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sold', 'year', 'type', 'band')





admin.site.register(Band, BandAdmin) # Enregistre le modèle sur le site d'administration et associe l'affichage du modèle admin
admin.site.register(Listing, ListingAdmin) # Enregistre le modèle Listing