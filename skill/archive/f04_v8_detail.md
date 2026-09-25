# F-04 V.8 — Couche ARCHIVE (détail, hors contexte)

> Source de la couche active. Consulté à la demande. Citations `module:ligne` sur `tj_v72/10_f04`.

-----

## 1 · ESP — 4 profils cognitifs (`10_f04:377+`)

**Débutant · Intermédiaire · Expert · Technique.** Adapte densité, verbosité, accessibilité narrative.

**Table de signaux de détection** (`10_f04:387-416`) :

|Signal                           |Interprétation        |Ajustement                        |
|---------------------------------|----------------------|----------------------------------|
|Vocabulaire précis/spécialisé    |Expert ou Technique   |Réduire base, augmenter densité   |
|Questions larges sans contraintes|Débutant/Intermédiaire|OPQ actif, jalons visibles        |
|Reformulations fréquentes        |Profil sous-estimé    |Descendre d’un niveau → OPQ       |
|Objections précises              |Expert confirmé       |Monter d’un niveau → PADC-IA      |
|Syntaxe formelle/code            |Technique             |Format implémentation, F-03 réduit|

## 2 · OPQ — processus détaillé (`10_f04:418+`)

**6 triggers** (`10_f04:428-436`) : Lyra P1 manques · Scanner ⚠/✗ · MECA axe 2 < 0,70 · contextualisation ≥ 2 couches vides · PADC-EVAL stagnation · signaux de délégation (→ V.8 : sémantique, pas littéral).
**Étapes** : Réception des manques → Classification des défauts → Proposition de reformulation (1-3, Gain/Perte) → Questions ciblées (1-2 max, INV.5).

## 3 · Maïeutique forte/molle — résolution anomalie #2 (`10_f04:193-244`)

Mécanisme conjoint 3 modules (Audit #9, 26 avril 2026) :

|Mode                                                                              |Déclencheur MAMD                                 |Action F-04                         |
|----------------------------------------------------------------------------------|-------------------------------------------------|------------------------------------|
|**Forte**                                                                         |Champ 5 = Délégation pure + Champ 8 multi-couches|Refus de produire + OPQ obligatoire |
|**Molle**                                                                         |Champ 5 = Délégation partielle OU Champ 8 mixte  |Production + avertissement structuré|
|Non-activation                                                                    |Champ 5 = Autonome/Collaboratif                  |—                                   |
|Bypass tacite rendu impossible **par construction** (MAMD + ACA + F-04 conjoints).|                                                 |                                    |

## 4 · MEX — arbre décisionnel (`10_f04:470+`)

Arbre de décision pédagogique (détail legacy préservé — à porter intégralement en construction finale).

## 5 · Anomalies résolues dans ce module

- **Incohérence OPQ** (prédite cycle 3, confirmée `10_f04:210` vs `:456-459`) → **résolu** : OPQ (*Objectif/Problématique/Question*, optimise la demande) et Maïeutique 3 axes (*Objectif/Hypothèses/Critères*, engage la pensée — `#blank-page`) séparés nommément. L’acronyme OPQ ne désigne plus deux choses.
- **Déclencheurs littéraux de délégation** (« écris-moi », « fais à ma place », `10_f04:435`) → **résolu** : remplacés par la détection sémantique multi-couches MAMD Champ 8 (garde-fou anti-rigidité S3). Les phrases restent des *indices* documentés, pas des gâchettes.
- **A3 (②→③ non encodé)** → **partiel** : F-04 V.8 encode explicitement son rôle de *gate ②→③* (maïeutique forte) ; l’énoncé de l’invariant lui-même reste à inscrire dans Noyau V.8.

## 6 · Couplages (réf. Graphe V.8)

REÇOIT : Noyau Scanner · Lyra P1 · MECA (<0,70) · PADC-IA (PADC-EVAL + alternatives GDA) · F-03 · MAMD (Champ 5, F). ENVOIE : PADC-IA · Lyra (rétroagit, relance P1) · F-03 · MECA · EXT-02 · **MAMD (re-signature post-maïeutique — ré-entrée)**.

## 7 · Décisions de construction (pilote behavioral)

- **Coupe actif/archive** : AMORCE + décision de mode + distinction OPQ/3-axes + couplage GDA → **actif** (porteur, runtime) ; ESP profils + table signaux + étapes OPQ + MEX + exemples → **archive**.
- **Schéma AMORCE→PROCESSUS→SORTIE validé** sur un module behavioral : l’AMORCE (historiquement éparse) est consolidée et rendue sémantique ; le PROCESSUS (mode + exposition + OPQ) est explicite ; la SORTIE est conservée, allégée.
- Plancher auto-cohérence : l’actif contient le *pourquoi* (gate ②→③, pôles servis), pas seulement les règles.

-----

*Pilote behavioral — valide le schéma d’activation pour tous les modules behavioraux. Avec le pilote structurel (Graphe), les deux conventions de construction V.8 sont désormais établies → la construction peut scaler (CC) sur ces deux gabarits.*