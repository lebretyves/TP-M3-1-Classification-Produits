# TP M3-1 - Classification des produits

**Bien-être ou dispositif médical ?**

Module 3 - Epitech MBA Santé, IA & IoT - 16 octobre 2026.

**Équipe 2** : [lebretyves](https://github.com/lebretyves), [Faucourt](https://github.com/Faucourt) et [aglnix](https://github.com/aglnix).

Le PDF de réponse porte uniquement sur le **cas G : souris ergonomique avec batterie unique de 1 500 mAh et logiciel**. La grille Excel contient les huit produits du modèle et le cas G.

## Documents du TP

- [Énoncé étudiant](documents/TP_M3_1_Classification_produits_etudiant.pdf)
- [Grille de classification vierge](documents/TP_M3_1_Grille_classification.xlsx)

## Réponses

- [PDF du cas G](analyses/m3/TP_M3_1_corrige_cas_G.pdf) : finalité proposée, classement argumenté, rôle de l’organisme notifié et points à valider.
- [Grille complétée : huit produits et cas G](analyses/m3/grille_classification_cas_G.xlsx)

Le PDF a été réécrit le 16 octobre 2026. La classe IIa du logiciel reste une proposition pour l’usage médical envisagé, et non une certification du prototype. L’énoncé et la grille vierge restent inchangés.

La grille précise l’exemple étudié pour chaque produit. L’application de sommeil, la détection de chute et les rappels du pilulier sont retenus hors dispositif médical pour les usages étudiés : les colonnes classe et règle indiquent explicitement « Non applicable ». Pour IM009, la classe I indiquée est celle déclarée sous l’ancienne directive, pas une classe MDR confirmée. Les sources et les limites figurent dans les notes et les justifications.

## Source du PDF

- [Données du cas G et références](analyses/m3/cas_g.json)
- [Script de génération](scripts/generer_pdf_cas_g.py), utilisant ReportLab, PyMuPDF et les polices Arial de Windows.
