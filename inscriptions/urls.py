from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('inscription/', views.inscription, name='inscription'),
    path('inscription/<int:concours_id>/', views.inscription, name='inscription_prefilled'),
    path('upload/<int:candidat_id>/', views.upload_documents, name='upload_documents'),
    path('confirmation/<int:candidat_id>/', views.confirmation, name='confirmation'),
    path('recherche/', views.recherche_inscription, name='recherche_inscription'),
]