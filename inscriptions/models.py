from django.db import models

class Concours(models.Model):
    """Les différents types de concours disponibles"""
    NIVEAUX_CHOICES = [
        ('BAC', 'Bac'),
        ('BACHELIER', 'Bachelier'),
        ('BAC+2', 'Bac+2'),
        ('BAC+3', 'Licence/Bac+3'),
        ('MASTER', 'Master'),
    ]
    
    nom = models.CharField(max_length=200)
    niveau_requis = models.CharField(max_length=10, choices=NIVEAUX_CHOICES)
    description = models.TextField()
    frais_inscription = models.DecimalField(max_digits=10, decimal_places=2)
    date_limite = models.DateField()
    actif = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Concours"
    
    def __str__(self):
        return f"{self.nom} - {self.niveau_requis}"


class Candidat(models.Model):
    """Informations du candidat"""
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    
    # Informations personnelles
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=200)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    nationalite = models.CharField(max_length=50, default="Ivoirienne")
    
    # Contact
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()
    
    # Études
    niveau_etudes = models.CharField(max_length=100)
    etablissement_origine = models.CharField(max_length=200)
    annee_obtention = models.IntegerField()
    
    # Concours
    concours_souhaite = models.ForeignKey(Concours, on_delete=models.PROTECT)
    
    # Système
    numero_inscription = models.CharField(max_length=20, unique=True, blank=True)
    date_inscription = models.DateTimeField(auto_now_add=True)
    valide = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.nom} {self.prenoms} - {self.numero_inscription}"
    
    def save(self, *args, **kwargs):
        if not self.numero_inscription:
            # Génère un numéro unique : ESATIC-2025-XXXX
            import datetime
            annee = datetime.datetime.now().year
            dernier = Candidat.objects.count() + 1
            self.numero_inscription = f"ESATIC-{annee}-{dernier:04d}"
        super().save(*args, **kwargs)


class Document(models.Model):
    """Documents scannés du candidat"""
    TYPE_DOCUMENT_CHOICES = [
        ('EXTRAIT', 'Extrait de naissance'),
        ('CERTIFICAT', 'Certificat de scolarité'),
        ('DIPLOME', 'Diplôme'),
        ('LETTRE', 'Lettre de motivation'),
        ('PHOTO', 'Photo d\'identité'),
        ('AUTRE', 'Autre document'),
    ]
    
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE, related_name='documents')
    type_document = models.CharField(max_length=20, choices=TYPE_DOCUMENT_CHOICES)
    fichier = models.FileField(upload_to='documents/%Y/%m/')
    date_upload = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['candidat', 'type_document']
    
    def __str__(self):
        return f"{self.candidat.nom} - {self.get_type_document_display()}"