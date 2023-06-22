from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Création model/classe groupe
class Band(models.Model):

    # Classe imbriqué pour définir les genres possibles
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'



    name = models.fields.CharField(max_length=100) # Attibut name : Character Field -> champ qui stocke une chaine d'une longueur max de 100
    genre = models.fields.CharField(choices=Genre.choices, max_length=5) # Attribut genre : Character Field -> choix parmis les genres disponibles et longueur max de 5
    biography = models.fields.CharField(max_length=1000) # Attribut biographie : Character Field -> longueur max de 1000
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    ) # Attribut année de formation : Integer Field -> validators pour une valeur min et une valeur max
    active = models.fields.BooleanField(default=True) # Attribut groupe actif : Boolean Field -> valeur par défaut True
    official_homepage = models.fields.URLField(null=True, blank=True) # Attribut page internet : URL Field -> autorise les valeurs NULL et permet de recevoir un texte vide

    #like_new = models.fields.BooleanField(default=False) # Migration non désirée

    def __str__(self):
        return f'{self.name}'


# Création modèle Affiche
class Listing(models.Model):

    # Classe imbriqué pour les types d'article possibles
    class Type(models.TextChoices):
        Records = 'RE'
        Clothing = 'CL'
        Posters = 'PO'
        Miscellaneous = 'MI'



    title = models.fields.CharField(max_length=100) # Titre de l'annonce -> longueur max de 100
    description = models.fields.CharField(max_length=500) # Description de l'article vendu -> longueur max de 500
    sold = models.fields.BooleanField(default=False) # Indique si l'objet a était vendu ou non -> false par défaut
    year = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)],
        null=True
    ) # Année de l'article -> valeur min et max & peut être null
    type = models.fields.CharField(choices=Type.choices, max_length=2) # Type de l'article -> type défini dans le choix

    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL) # Mise en place clé étrangère avec modèle Band, null pour dire qu'une annonce peut être lié à aucun groupe, on_delete change l'état de la clé lorsque le groupe lié est supprimé


