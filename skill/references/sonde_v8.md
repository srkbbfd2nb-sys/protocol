# SONDE V.8 — Couche ACTIVE (runtime)

> **Couche** : active (MD, portée en contexte). **Module MÉTA-INFRASTRUCTURE** — établit l'environnement avant que le cycle ne s'ouvre.
> **Pôle** : méta-infrastructure. *Rattachement justifié : la sonde sert ② (elle arme les garde-fous et refuse l'engagement nu) et ③ (elle ouvre l'accès aux capacités) sans qu'aucun des deux ne domine. Forcer un pôle serait une conflation — principe d'intégrité, `actif/noyau_v8.md` §index.*
> **Détail** (épreuves par nature, matrice de dégradation, format du bloc CAPACITES, cas limites) → `archive/sonde_v8_detail.md`.

## AMORCE

La sonde s'amorce dans trois cas, jamais autrement :

1. **Ouverture de cycle** — avant `MAMD signe` (`actif/noyau_v8.md` §chaîne canonique).
2. **Changement d'environnement détecté** — hôte différent, outil nouvellement déclaré, périmètre modifié.
3. **Défaillance en cours de cycle** — une capacité présumée disponible échoue → re-sonde (ré-entrée déclarée au Noyau).

*Elle ne s'amorce pas sur simple changement de sujet : l'environnement est stable tant que rien ne signale le contraire.*

## PROCESSUS

**P1 · Inventaire déclaré.** Relever ce que l'hôte annonce pouvoir faire. Cet inventaire est une **déclaration**, pas une preuve — il entre au statut `déclaré`.

**P2 · Épreuve minimale.** Éprouver chaque capacité par l'acte le plus petit, **non destructif et réversible**, qui la démontre. Une capacité qui passe l'épreuve devient `vérifié`. Une capacité qu'on ne peut éprouver sans effet de bord reste `déclaré` — **on ne la promeut jamais par confort**.

**P3 · Classement en trois états.** `vérifié` · `déclaré` (annoncé, non éprouvé) · `absent`. Aucun quatrième état, aucune valeur par défaut optimiste. L'inconnu se classe `absent`, pas `déclaré` — l'inverse fabriquerait une capacité.

**P4 · Routage en cascade.** Pour un besoin donné : voie primaire → secondaire → tertiaire. Le repli sur une voie inférieure est un **fait déclaré en sortie**, jamais une substitution silencieuse (INV.5, échec bruyant). Épuisement des voies → la capacité est `absente` et le besoin est **annoncé non couvert**, pas contourné.

**P5 · Armement des garde-fous.** Appliquer la table du Noyau (§Environnement) à toute capacité **engagée** : irréversible → INV.4 non délégable · sortante → fiche d'accès · ingérante → pré-ingestion + INV.1 · non vérifiée → information de précaution · dégradée → déclaration de repli. Aucune capacité ne s'engage sans garde-fou armé ou, à défaut, sans précaution portée en sortie.

**P6 · Application de la règle atteignable / engagé.** La carte recense tout l'**atteignable**. N'est **engagé** que ce que la demande requiert effectivement. Un écart entre atteignable et engagé n'est pas une perte : c'est la règle qui s'applique.

## SORTIE

Un **bloc CAPACITES** : par capacité, sa nature, son état (`vérifié` / `déclaré` / `absent`), la voie retenue si cascade, le garde-fou armé si engagée. Plus le **régime de dégradation** courant si une voie primaire est indisponible. *(Format intégral → archive ; le bloc ne se réduit pas — S4-E.)*

Le bloc alimente `MAMD` (contexte de session), borne `MEDA` (un régime ne peut router vers une capacité `absente`) et informe `F-04` (l'exposition doit dire ce qui n'a pas pu être fait).

## Couplages typés *(7 natures — `actif/noyau_v8.md` §natures)*

- `SONDE active MAMD` — **F** structurel. La signature ouvre le cycle *après* que l'environnement est établi (`actif/noyau_v8.md` §chaîne canonique).
- `SONDE alimente MEDA` — **F**. Le routage dépend des capacités réellement disponibles ; router vers une capacité `absente` est une erreur de type (`actif/meda_v8.md`).
- `SONDE borne EXT-02` — **F**. L'action technique ne peut engager qu'une capacité présente à la carte (`actif/ext02_v8.md`).
- `SONDE informe F-04` — **Fn** opérationnel. L'exposition porte les capacités non couvertes et les replis (`actif/f04_v8.md`).
- `SONDE alimente I-06` — **Fn**. Le palier estimé se lit aussi sur ce que l'environnement permet, pas seulement sur le modèle (`actif/i06_v8.md` §paliers R3).
- `MECA audite SONDE` — **Fn**. Un engagement sans garde-fou armé est une non-conformité mesurable (`actif/meca_v8.md` ; INV.7).
- `SONDE rétroagit Noyau` — **L** libre vérifié. Une capacité durablement absente sur tous les hôtes éprouvés est un signal d'évolution du cadre, pas une correction locale.

---

> **Statut** : module MÉTA-INFRASTRUCTURE V.8, **nouveau à Dep**. Rend opérationnelle la règle *atteignable / engagé* du Noyau et la découverte de capacités validée par Lazerr (2026-09-04). N'énumère aucun outil — il en découvre ; c'est ce qui rend le protocole portable sans devenir périmé (PA.3, compatibilité environnementale). *Mécanisme inspiré du diagnostic de backends et du repli en cascade — `TEC_SOURCES_GITHUB.md` §2-C.*
