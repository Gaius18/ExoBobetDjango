from django import forms
from .models import Candidat, Document, Concours

class CandidatForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = [
            'nom', 'prenoms', 'date_naissance', 'lieu_naissance', 
            'sexe', 'nationalite', 'email', 'telephone', 'adresse',
            'niveau_etudes', 'etablissement_origine', 'annee_obtention',
            'concours_souhaite'
        ]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenoms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénoms'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lieu_naissance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lieu de naissance'}),
            'sexe': forms.Select(attrs={'class': 'form-control'}),
            'nationalite': forms.TextInput(attrs={'class': 'form-control', 'value': 'Ivoirienne'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+225 XX XX XX XX XX'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adresse complète'}),
            'niveau_etudes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Bac Série D'}),
            'etablissement_origine': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'établissement'}),
            'annee_obtention': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2024'}),
            'concours_souhaite': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nom': 'Nom',
            'prenoms': 'Prénoms',
            'date_naissance': 'Date de naissance',
            'lieu_naissance': 'Lieu de naissance',
            'sexe': 'Sexe',
            'nationalite': 'Nationalité',
            'email': 'Email',
            'telephone': 'Téléphone',
            'adresse': 'Adresse',
            'niveau_etudes': 'Niveau d\'études',
            'etablissement_origine': 'Établissement d\'origine',
            'annee_obtention': 'Année d\'obtention',
            'concours_souhaite': 'Concours souhaité',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Candidat.objects.filter(email=email).exists():
            raise forms.ValidationError("Cette adresse email est déjà utilisée.")
        return email

    def clean_annee_obtention(self):
        annee = self.cleaned_data.get('annee_obtention')
        from datetime import date
        if annee and (annee < 1990 or annee > date.today().year):
            raise forms.ValidationError("Année d'obtention invalide.")
        return annee


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['type_document', 'fichier']
        widgets = {
            'type_document': forms.Select(attrs={'class': 'form-control'}),
            'fichier': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.jpg,.jpeg,.png'}),
        }
        labels = {
            'type_document': 'Type de document',
            'fichier': 'Fichier (PDF, JPG, PNG - max 5MB)',
        }

    def clean_fichier(self):
        fichier = self.cleaned_data.get('fichier')
        if fichier:
            # Vérifier la taille (5MB max)
            if fichier.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Le fichier ne doit pas dépasser 5MB.")
            
            # Vérifier l'extension
            import os
            ext = os.path.splitext(fichier.name)[1].lower()
            if ext not in ['.pdf', '.jpg', '.jpeg', '.png']:
                raise forms.ValidationError("Format non supporté. Utilisez PDF, JPG ou PNG.")
        
        return fichier