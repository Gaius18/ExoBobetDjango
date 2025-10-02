from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Concours, Candidat, Document
from .forms import CandidatForm, DocumentForm

def accueil(request):
    """Page d'accueil avec la liste des concours"""
    concours = Concours.objects.filter(actif=True)
    return render(request, 'inscriptions/accueil.html', {'concours': concours})


def inscription(request, concours_id=None):
    """Formulaire d'inscription du candidat"""
    concours_selectionne = None
    if concours_id:
        concours_selectionne = get_object_or_404(Concours, id=concours_id, actif=True)
    
    if request.method == 'POST':
        form = CandidatForm(request.POST)
        if form.is_valid():
            candidat = form.save()
            messages.success(request, f'Inscription créée avec succès ! Numéro: {candidat.numero_inscription}')
            return redirect('upload_documents', candidat_id=candidat.id)
    else:
        form = CandidatForm()
        if concours_selectionne:
            form.fields['concours_souhaite'].initial = concours_selectionne
    
    return render(request, 'inscriptions/inscription.html', {
        'form': form,
        'concours_selectionne': concours_selectionne
    })


def upload_documents(request, candidat_id):
    """Upload des documents scannés"""
    candidat = get_object_or_404(Candidat, id=candidat_id)
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.candidat = candidat
            document.save()
            messages.success(request, 'Document ajouté avec succès !')
            return redirect('upload_documents', candidat_id=candidat.id)
    else:
        form = DocumentForm()
    
    documents = Document.objects.filter(candidat=candidat)
    
    return render(request, 'inscriptions/upload_documents.html', {
        'form': form,
        'candidat': candidat,
        'documents': documents
    })


def confirmation(request, candidat_id):
    """Page de confirmation avec reçu"""
    candidat = get_object_or_404(Candidat, id=candidat_id)
    documents = Document.objects.filter(candidat=candidat)
    
    # Marquer l'inscription comme validée si elle ne l'est pas déjà
    if not candidat.valide:
        candidat.valide = True
        candidat.save()
        messages.success(request, 'Votre inscription a été validée avec succès !')
    
    return render(request, 'inscriptions/confirmation.html', {
        'candidat': candidat,
        'documents': documents
    })


def recherche_inscription(request):
    """Rechercher une inscription par numéro"""
    candidat = None
    numero = request.GET.get('numero', '').strip()
    
    if numero:
        try:
            candidat = Candidat.objects.get(numero_inscription=numero)
        except Candidat.DoesNotExist:
            messages.error(request, 'Aucune inscription trouvée avec ce numéro.')
    
    return render(request, 'inscriptions/recherche.html', {
        'candidat': candidat,
        'numero': numero
    })