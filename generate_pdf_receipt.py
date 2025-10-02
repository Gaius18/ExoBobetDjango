"""
Script pour générer un PDF du reçu d'inscription
Nécessite: pip install reportlab
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os
from datetime import datetime

def generate_receipt_pdf(candidat, documents, output_path):
    """
    Générer un PDF du reçu d'inscription
    """
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # Style personnalisé pour le titre
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0e5aa7')
    )
    
    # Style pour les sous-titres
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=20,
        textColor=colors.HexColor('#0e5aa7')
    )
    
    # En-tête avec logo (si disponible)
    logo_path = "inscriptions/static/inscriptions/img/esatic-logo.svg"
    if os.path.exists(logo_path):
        try:
            logo = Image(logo_path, width=2*inch, height=2*inch)
            logo.hAlign = 'CENTER'
            story.append(logo)
        except:
            pass  # Si le logo ne peut pas être chargé
    
    # Titre principal
    story.append(Paragraph("ESATIC", title_style))
    story.append(Paragraph("École Supérieure Africaine des Technologies de l'Information et de la Communication", styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Titre du reçu
    story.append(Paragraph("REÇU D'INSCRIPTION", title_style))
    story.append(Spacer(1, 20))
    
    # Numéro d'inscription en évidence
    numero_style = ParagraphStyle(
        'NumeroStyle',
        parent=styles['Normal'],
        fontSize=18,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0e5aa7'),
        borderWidth=2,
        borderColor=colors.HexColor('#0e5aa7'),
        borderPadding=10
    )
    story.append(Paragraph(f"<b>Numéro d'inscription: {candidat.numero_inscription}</b>", numero_style))
    story.append(Spacer(1, 30))
    
    # Informations du candidat
    story.append(Paragraph("Informations du candidat", subtitle_style))
    
    candidat_data = [
        ['Nom et Prénoms:', f"{candidat.nom} {candidat.prenoms}"],
        ['Email:', candidat.email],
        ['Téléphone:', candidat.telephone],
        ['Date de naissance:', candidat.date_naissance.strftime('%d/%m/%Y')],
        ['Lieu de naissance:', candidat.lieu_naissance],
        ['Nationalité:', candidat.nationalite],
    ]
    
    candidat_table = Table(candidat_data, colWidths=[2*inch, 4*inch])
    candidat_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f8fafc')),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#475569')),
        ('TEXTCOLOR', (1, 0), (1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    story.append(candidat_table)
    story.append(Spacer(1, 20))
    
    # Informations du concours
    story.append(Paragraph("Informations du concours", subtitle_style))
    
    concours_data = [
        ['Concours:', candidat.concours_souhaite.nom],
        ['Niveau requis:', candidat.concours_souhaite.get_niveau_requis_display()],
        ['Frais d\'inscription:', f"{candidat.concours_souhaite.frais_inscription:,.0f} FCFA"],
        ['Date limite:', candidat.concours_souhaite.date_limite.strftime('%d/%m/%Y')],
    ]
    
    concours_table = Table(concours_data, colWidths=[2*inch, 4*inch])
    concours_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f0f6ff')),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#0e5aa7')),
        ('TEXTCOLOR', (1, 0), (1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#0e5aa7')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    story.append(concours_table)
    story.append(Spacer(1, 20))
    
    # Documents fournis
    story.append(Paragraph("Documents fournis", subtitle_style))
    
    if documents:
        doc_data = [['Document', 'Date d\'upload']]
        for doc in documents:
            doc_data.append([
                doc.get_type_document_display(),
                doc.date_upload.strftime('%d/%m/%Y à %H:%M')
            ])
    else:
        doc_data = [['Aucun document fourni', '']]
    
    doc_table = Table(doc_data, colWidths=[3*inch, 2*inch])
    doc_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#22c55e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#22c55e')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    story.append(doc_table)
    story.append(Spacer(1, 30))
    
    # Statut et date
    status_style = ParagraphStyle(
        'StatusStyle',
        parent=styles['Normal'],
        fontSize=16,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#22c55e'),
        borderWidth=2,
        borderColor=colors.HexColor('#22c55e'),
        borderPadding=15
    )
    story.append(Paragraph("<b>✓ INSCRIPTION VALIDÉE</b>", status_style))
    story.append(Spacer(1, 20))
    
    # Informations de contact
    story.append(Spacer(1, 30))
    story.append(Paragraph("Informations de contact", subtitle_style))
    contact_text = """
    <b>Date d'inscription:</b> {}<br/>
    <b>Contact ESATIC:</b> info@esatic.edu.ci | +225 XX XX XX XX XX<br/>
    <b>Adresse:</b> Abidjan, Côte d'Ivoire<br/><br/>
    Ce reçu confirme votre inscription au concours. Conservez-le précieusement.
    """.format(candidat.date_inscription.strftime('%d/%m/%Y à %H:%M'))
    
    story.append(Paragraph(contact_text, styles['Normal']))
    
    # Générer le PDF
    doc.build(story)
    return output_path

# Exemple d'utilisation
if __name__ == "__main__":
    print("Script de génération PDF pour les reçus ESATIC")
    print("Usage: Intégrer dans les vues Django pour générer automatiquement les PDFs")