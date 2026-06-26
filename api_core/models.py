import uuid
from django.db import models

class Savant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom_complet = models.CharField(max_length=150, verbose_name="Nom complet")
    biographie = models.TextField(blank=True, null=True, verbose_name="Biographie")
    photo = models.ImageField(upload_to='photos_savants/', blank=True, null=True, verbose_name="Photo de profil")
    telephone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone")
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_complet

    class Meta:
        verbose_name = "Savant"
        verbose_name_plural = "Savants"

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True, verbose_name="Nom de la catégorie")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"


class Preche(models.Model):
    LANGUES_CHOICES = [
        ('Dendi', 'Dendi'),
        ('Bariba', 'Bariba'),
        ('Haoussa', 'Haoussa'),
        ('Français', 'Français'),
        ('Autre', 'Autre'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titre = models.CharField(max_length=255, verbose_name="Titre du prêche")
    description = models.TextField(blank=True, null=True, verbose_name="Description / Résumé")
    
    # Le fichier audio physique sera téléversé dans un dossier 'audios_preches/'
    audio_fichier = models.FileField(upload_to='audios_preches/', verbose_name="Fichier Audio (MP3)")
    
    duree_secondes = models.IntegerField(blank=True, null=True, verbose_name="Durée (en secondes)")
    taille_octets = models.BigIntegerField(blank=True, null=True, verbose_name="Taille (en octets)")
    langue = models.CharField(max_length=50, choices=LANGUES_CHOICES, default='Dendi', verbose_name="Langue du prêche")
    date_enregistrement = models.DateField(blank=True, null=True, verbose_name="Date de l'enregistrement")
    
    # Relations (Clés étrangères)
    savant = models.ForeignKey(Savant, on_delete=models.SET_NULL, null=True, related_name='preches', verbose_name="Savant")
    categorie = models.ForeignKey(Categorie, on_delete=models.RESTRICT, related_name='preches', verbose_name="Catégorie")
    
    est_public = models.BooleanField(default=True, verbose_name="Visible sur l'application")
    telechargements_count = models.IntegerField(default=0, verbose_name="Nombre de téléchargements")
    ecoutes_count = models.IntegerField(default=0, verbose_name="Nombre d'écoutes")
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "Prêche"
        verbose_name_plural = "Prêches"
        ordering = ['-date_creation'] # Les plus récents apparaissent en premier