"""Génère le compte rendu consacré au cas G (ReportLab + PyMuPDF)."""
from pathlib import Path
import json
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pymupdf

ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'analyses/m3/cas_g.json').read_text(encoding='utf-8'))
for name,file in [('Arial','arial.ttf'),('Arial-Bold','arialbd.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'C:/Windows/Fonts/'+file))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold')
W,H=A4; M=43; WIDTH=W-2*M
INK=colors.HexColor('#253247'); BLUE=colors.HexColor('#244E76')
body=ParagraphStyle('body',fontName='Arial',fontSize=10.4,leading=14.4,textColor=INK,spaceAfter=7)
small=ParagraphStyle('small',parent=body,fontSize=8.6,leading=11.5)
heading=ParagraphStyle('heading',parent=body,fontName='Arial-Bold',fontSize=12,leading=16,spaceAfter=6)
OUT=ROOT/'analyses/m3/TP_M3_1_corrige_cas_G.pdf'
c=canvas.Canvas(str(OUT),pagesize=A4)
c.setTitle('TP M3-1 - Cas G : classification de la souris ergonomique et de son logiciel')
c.setAuthor('Équipe projet - Cas G')
def para(text,y,style=body):
    p=Paragraph(text,style);_,height=p.wrap(WIDTH,H)
    p.drawOn(c,M,y-height)
    return y-height-style.spaceAfter
def start(page,title):
    c.setFillColor(BLUE);c.setFont('Arial-Bold',9)
    c.drawString(M,H-32,'TP M3-1  /  CAS G  /  16 OCTOBRE 2026')
    c.setFillColor(INK);c.setFont('Arial-Bold',19)
    c.drawString(M,H-61,title)
    c.setStrokeColor(colors.HexColor('#C8D2DC'));c.line(M,36,W-M,36)
    c.setFont('Arial',8);c.drawString(M,23,'Epitech - MBA Santé, IA & IoT')
    c.drawRightString(W-M,23,f'{page} / 2')
    return H-80
def h(text,y): return para(text,y,heading)
def link(title,url): return '<link href="'+escape(url,{'"':'&quot;'})+'" color="#244E76"><u>'+escape(title)+'</u></link>'

y=start(1,'Notre souris est-elle un dispositif médical ?')
y=para('Nous étudions la souris ergonomique avec une batterie unique de 1 500 mAh et le logiciel qui doit exploiter ses données. Pour ce TP, nous conservons le projet d’une <b>aide à la prise en charge des troubles musculosquelettiques (TMS)</b>. Cette fonction médicale reste à développer et à valider.',y)
y=h('Le projet étudié',y)
y=para('La souris conserve son usage informatique. Les capteurs prévus recueillent des mouvements et des signaux au contact de la main : pouls, conductivité de la peau et température. Les deux contacts GSR sont intégrés à la coque. La batterie unique doit alimenter la souris et ses capteurs. Son intégration complète reste à finaliser. [4]',y)
y=para('Ces mesures ne prouvent pas, à elles seules, la présence d’un TMS. En particulier, mesurer le mouvement de la souris ne donne pas directement l’angle anatomique du poignet. Il faudra montrer quelles informations sont réellement utiles au professionnel de santé.',y)
y=h('(a) Bien-être ou dispositif médical ?',y)
y=para('Pour la finalité retenue, nous classons <b>le logiciel prévu comme dispositif médical</b>. Son résultat doit servir à adapter une prise en charge médicale. La forme ergonomique, la présence de capteurs et la capacité de la batterie ne suffisent pas à décider de ce statut. [1, 2]',y)
y=h('(b) Quelle phrase justifie ce choix ?',y)
y=para('Nous proposons la formulation suivante pour le projet :',y)
y=para('<b>« '+escape(DATA['finalite'])+' »</b>',y)
y=para('La partie décisive est « recommandations personnalisées de prise en charge des troubles musculosquelettiques ». C’est une finalité rédigée pour le TP, pas une citation de fabricant ni une performance déjà démontrée.',y)
y=h('(c) Quelle classe et quelle règle ?',y)
y=para('Nous proposons la <b>classe IIa selon la règle 11</b>, car les informations du logiciel doivent aider à une décision thérapeutique. Cette proposition suppose un usage non critique. Elle devra être revue à partir des conséquences possibles d’une recommandation erronée. [2]',y)
y=h('(d) Faut-il un organisme notifié ?',y)
y=para('<b>Oui, pour une mise sur le marché en classe IIa.</b> L’organisme notifié intervient dans l’évaluation de conformité. À ce stade, le projet n’a pas de certification médicale. Remplir la grille du TP ne vaut pas validation du dispositif. [1]',y)
assert y>46,('page 1',y)
c.showPage()

y=start(2,'Ce qu’il faut encore justifier')
y=h('Pourquoi la classe IIa reste une proposition',y)
y=para('Pour notre analyse, nous envisageons un suivi de personnes utilisant un ordinateur, avec des résultats examinés par un professionnel de santé. Ce scénario exclut l’urgence et une décision de traitement prise automatiquement. Il faut encore préciser les personnes concernées, les TMS visés et le contenu exact des recommandations.',y)
y=para('Une mauvaise recommandation pourrait rassurer à tort une personne, retarder une consultation ou proposer un geste inadapté. Il faut évaluer la gravité de ces situations. La présence d’un professionnel ne supprime pas ce risque.',y)
y=para('Selon la règle 11, une décision pouvant causer une détérioration grave ou nécessiter une intervention chirurgicale relève de <b>IIb</b>. Si elle peut causer un décès ou une détérioration irréversible, la classe est <b>III</b>. L’absence d’usage d’urgence ne suffit donc pas à garantir IIa. [2]',y)
y=h('La souris et le logiciel doivent être examinés ensemble',y)
y=para('La classe proposée ici concerne la fonction d’interprétation médicale du logiciel. Le rôle réglementaire de la souris reste à préciser : partie du dispositif, accessoire dédié ou produit séparé. Les capteurs, les contacts cutanés, la transmission et l’alimentation devront être évalués avec le logiciel, car une mesure fausse ou perdue peut fausser son résultat. [3]',y)
y=h('Les vérifications nécessaires pour notre projet',y)
for text in [
    '<b>Préciser l’usage :</b> qui utilise la souris, pour quel trouble, et quelle décision le professionnel peut prendre avec le résultat.',
    '<b>Vérifier les mesures :</b> qualité du contact, mouvements parasites, répétabilité et comparaison avec une méthode de référence adaptée.',
    '<b>Évaluer les recommandations :</b> utilité clinique, faux résultats et conséquences d’une erreur. Ces preuves ne sont pas fournies dans le dossier actuel.',
    '<b>Tester l’ensemble :</b> prototype assemblé, batterie et recharge, perte de liaison, sécurité des contacts et protection des données personnelles.'
]: y=para(text,y,small)
y=h('Ce qui ferait rester le projet dans le bien-être',y)
y=para('Une promesse limitée à « Aide à mieux organiser ses pauses et à améliorer le confort d’utilisation de l’ordinateur » pourrait relever du bien-être. Ce serait un autre usage, sans recommandation médicale personnalisée. Il faudrait que les fonctions réelles et toute la communication correspondent à cette promesse. [1, 2]',y)
y=h('Sources',y)
for src in DATA['sources']:
    y=para('['+src['id']+'] '+link(src['titre'],src['url']),y,small)
y=para('Références consultées le 16 octobre 2026. Les guides MDCG expliquent le règlement ; ils ne certifient pas le projet. Réponse correspondant à la question 5 et à la ligne 9 de la grille.',y,small)
assert y>46,('page 2',y)
c.save()
doc=pymupdf.open(OUT)
assert len(doc)==2
tmp=ROOT/'tmp/revision_cas_g';tmp.mkdir(parents=True,exist_ok=True)
for i,page in enumerate(doc):
    page.get_pixmap(matrix=pymupdf.Matrix(1.4,1.4)).save(tmp/f'cas_g_{i+1}.png')
    assert all(b[1]>15 and b[3]<H-12 for b in page.get_text('blocks'))
print({'pdf':str(OUT),'pages':len(doc),'bas_page_2':y,'liens':sum(len(p.get_links()) for p in doc)})
