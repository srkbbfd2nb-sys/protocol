# MAMD V.8 — Couche ARCHIVE (détail, hors contexte)

> Source de la couche active. Consulté à la demande. Citations `module:ligne` sur `tj_v72/16_mamd`. Passe fraîche.

---

## 1 · Les 8 champs — valeurs & sources de détection (`16_mamd:253-416`)

| # | Champ | Valeurs possibles | Sources de détection |
|---|---|---|---|
| 1 | Intention | production / analyse / clarification / décision… | lexique + structure de la demande |
| 2 | Domaine | domaine(s) du sujet | vocabulaire, entités |
| 3 | Nature épistémique | F / E / O / P (ou mixte) | type d'assertions attendues |
| 4 | Complexité cognitive | Faible / Modérée / Élevée | portée, arbitrages requis |
| 5 | **Engagement utilisateur** *(critique)* | Autonome · Collaboratif · **Délégation partielle** · **Délégation pure** (`16_mamd:351-352`) | cadrage personnel présent/absent, verbe |
| 6 | Risques détectés | liste (position contestée, risque éthique, surconfiance…) | **reçoit A2** (détection 4 axes) |
| 7 | Contexte session | premier échange / historique / pivot | état de la session |
| 8 | **Signaux de délégation** *(critique)* | multi-couches : lexical / syntaxique / intentionnel (`16_mamd:354,408`) | analyse des 3 couches |

## 2 · Champs 5 + 8 = résolution anomalie #2 (`16_mamd:360, 416, 437`)

Le Champ 5 **catégorise** l'engagement (synthétique) ; le Champ 8 **détaille** les signaux qui ont mené à la catégorisation (analytique). Dualité = réponse structurelle directe : le bypass délégation devient *détectable ET explicable* (`16_mamd:416`).

Alimentation F-04 (`16_mamd:437`) : Champ 5 = Délégation pure + Champ 8 confirmé multi-couches → **maïeutique forte** ; Champ 5 = partielle OU Champ 8 mixte → **maïeutique molle**.

## 3 · Format de sortie SIGNATURE MAMD — 10 lignes (`16_mamd:480-488`)

```
SIGNATURE MAMD
- Intention : [valeur]
- Domaine : [valeur]
- Nature épistémique : [valeur]
- Complexité cognitive : [valeur]
- Engagement utilisateur : [valeur]
- Risques détectés : [liste]
- Contexte session : [valeur]
- Signaux de délégation : lexical=[X], syntaxique=[Y], intentionnel=[Z]
```

Visible par défaut en régimes Standard/Rigoureux ; optionnellement masqué en Léger (sauf `#mamd:debug`, `16_mamd:474` — diagnostic, n'altère pas le comportement).

## 4 · Couplages (réf. Graphe V.8, passe fraîche)

REÇOIT : — (producteur, en tête de chaîne). ENVOIE : ACA (`16_mamd:204`+`17_aca:214`, inverse ACA→MAMD **F** `17_aca:425`) · MEDA (**F** pré-MEDA `16_mamd:430`) · F-04 (**F**, Champ 5 `16_mamd:360`) · MECA (sous-axe `coherence_mamd`). Ré-entrée : **F-04→MAMD** (re-signature post-maïeutique).

## 5 · Portabilité (S3-B) & principes architecturaux

`#mamd:debug` = standard portable, pas une dépendance d'environnement (PA.1, `16_mamd:527`). Applicable par tout LLM analysant une demande textuelle, dégradation gracieuse possible (Champ 8 réductible à lexical+syntaxique si couche intentionnelle trop coûteuse — Palier C, `16_mamd:529`).

## 6 · Décisions de construction

- **Classification méta-infrastructure** (pas un pôle ①/②/③) : MAMD *sert* tout le système en signant chaque demande ; il ne « produit » ni « souveraineté » ni « épistémique » — il alimente. Cohérent index Noyau corrigé (cycle 22) + principe d'intégrité Ax2-A2.
- **Schéma AMORCE→PROCESSUS→SORTIE** appliqué : AMORCE = automatique pré-MEDA (position invariante) ; PROCESSUS = signature 8 champs ; SORTIE = bloc 10 lignes.
- **Coupe S4** : rôle + 8 champs (noms) + Champs 5/8 critiques + couplages → actif ; valeurs/sources par champ + format + portabilité → archive.

---

*Module méta-infrastructure V.8 (tête de chaîne). Signe chaque cycle → alimente MEDA/F-04/MECA. Vague 2.*
