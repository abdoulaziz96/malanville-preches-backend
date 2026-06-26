from django.contrib import admin
from .models import Savant, Categorie, Preche

# Personnalisation de l'affichage pour la table Savant
@admin.register(Savant)
class SavantAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'telephone', 'date_creation')
    search_fields = ('nom_complet', 'telephone')

# Personnalisation de l'affichage pour la table Catégorie
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)

# Personnalisation de l'affichage pour la table Prêche
@admin.register(Preche)
class PrecheAdmin(admin.ModelAdmin):
    list_display = ('titre', 'savant', 'categorie', 'langue', 'est_public', 'date_creation')
    list_filter = ('langue', 'est_public', 'categorie', 'savant')
    search_fields = ('titre', 'description')
    readonly_fields = ('telechargements_count', 'ecoutes_count') # Empêche la modification manuelle des compteurs