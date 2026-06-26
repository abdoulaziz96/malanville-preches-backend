from rest_framework import serializers
from .models import Savant, Categorie, Preche

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class SavantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savant
        fields = '__all__'


class PrecheSerializer(serializers.ModelSerializer):
    # Ces lignes permettent d'inclure les détails textuels du savant et de la catégorie au lieu d'afficher juste un ID unique (UUID)
    savant_nom = serializers.ReadOnlyField(source='savant.nom_complet')
    categorie_nom = serializers.ReadOnlyField(source='categorie.nom')

    class Meta:
        model = Preche
        fields = [
            'id', 'titre', 'description', 'audio_fichier', 
            'duree_secondes', 'taille_octets', 'langue', 
            'date_enregistrement', 'savant', 'savant_nom', 
            'categorie', 'categorie_nom', 'telechargements_count', 
            'ecoutes_count', 'date_creation'
        ]