from rest_framework import viewsets, filters
from .models import Savant, Categorie, Preche
from .serializers import SavantSerializer, CategorieSerializer, PrecheSerializer

class CategorieViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API pour lister et voir les catégories. (Lecture seule pour l'application mobile)
    """
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer


class SavantViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API pour lister et voir les savants.
    """
    queryset = Savant.objects.all()
    serializer_class = SavantSerializer


class PrecheViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API pour voir les prêches avec un système de recherche et filtrage.
    """
    queryset = Preche.objects.filter(est_public=True)
    serializer_class = PrecheSerializer
    
    # Intégration du système de recherche pour l'application mobile
    filter_backends = [filters.SearchFilter]
    search_fields = ['titre', 'description', 'savant__nom_complet', 'langue']