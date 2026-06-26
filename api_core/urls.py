from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SavantViewSet, CategorieViewSet, PrecheViewSet

# Le routeur de DRF génère automatiquement toutes les URLs standard (GET /api/preches/, GET /api/preches/id/, etc.)
router = DefaultRouter()
router.register(r'savants', SavantViewSet, basename='savant')
router.register(r'categories', CategorieViewSet, basename='categorie')
router.register(r'preches', PrecheViewSet, basename='preche')

urlpatterns = [
    path('', include(router.urls)),
]