from django.contrib import admin
from .models import Concours, Candidat, Document

@admin.register(Concours)
class ConcoursAdmin(admin.ModelAdmin):
    list_display = ['nom', 'niveau_requis', 'frais_inscription', 'date_limite', 'actif']
    list_filter = ['niveau_requis', 'actif']
    search_fields = ['nom', 'description']

@admin.register(Candidat)
class CandidatAdmin(admin.ModelAdmin):
    list_display = ['numero_inscription', 'nom', 'prenoms', 'email', 'concours_souhaite', 'valide', 'date_inscription']
    list_filter = ['concours_souhaite', 'valide', 'sexe']
    search_fields = ['nom', 'prenoms', 'email', 'numero_inscription']
    readonly_fields = ['numero_inscription', 'date_inscription']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['candidat', 'type_document', 'date_upload']
    list_filter = ['type_document', 'date_upload']
    search_fields = ['candidat__nom', 'candidat__prenoms']