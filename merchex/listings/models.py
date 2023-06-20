from django.db import models

# Création model/classe groupe
class Band(models.Model):
    name = models.fields.CharField(max_length=100) # Attibut name : Character Field -> champ qui stocke une chaine d'une longueur max de 100


# Création modèle Affiche
class Listing(models.Model):
    title = models.fields.CharField(max_length=100) # Attribut title