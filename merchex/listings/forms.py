# Fichier pour le formulaire de l'application
from django import forms

from listings.models import Band # Import du modèle band pour le lier au formulaire
from listings.models import Listing # Import du modèle listing pour le lier au formulaire

# Formulaire pour la page de contact
class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    message = forms.CharField(max_length=1000, required=True)


# Formulaire pour ajouter un groupe basé sur le modèle de groupe
class BandForm(forms.ModelForm):
    
    # Classe meta qui spécifie le modèle pour lequel ce formulaire sera utilisé
    class Meta:
        model = Band # Modèle associé
        # fields = '__all__' # Champs à prendre en compte (ici tous les champs du modèle)
        exclude = ('active', 'official_homepage') # Champs à ne pas prendre en compte dans le formulaire


# Formulaire pour ajouter une annonce basé sur le modèle d'annonce
class ListingForm(forms.ModelForm):
    # Classe meta qui spécifie le modèle pour lequel ce formulaire sera utilisé
    class Meta:
        model = Listing # Modèle associé
        fields = '__all__' # Champs à prendre en compte


