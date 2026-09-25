# Graphe V.8 — Couche ACTIVE (runtime)

> **Couche** : active (MD, portée en contexte). **Module pilote V.8** — fixe les conventions.
> **Détail complet** (matrice, couplages Fn, citations, anomalies) → `archive/graphe_v8_detail.md`.
> **Natures (7)** : `conditionne` (gate) · `alimente` (donnée dont l’aval dépend) · `informe` (visibilité, sans dépendance) · `active` (amorce) · `borne` (contrainte) · `audite` (mesure) · `rétroagit` (retour).
> **Intensités** : `F` structurel · `Fn` opérationnel · `L` libre vérifié · `?` non documenté.

## Chaîne canonique d’un cycle (vue dynamique — le cœur runtime)

`SONDE établit → MAMD signe → ACA active → [ Lyra gate P0 · MEDA route · modules opèrent · PADC-IA/GDA authentifie → F-04 expose ] → MECA audite → I-07 réfléchit → rétroactions`

## Points de ré-entrée (« revenir, repartir »)

- **F-04 → MAMD** : re-signature post-maïeutique → nouveau sous-cycle.
- **MECA < seuil → OFI** : relance de la production.
- **A2 (détection 4 axes) → INV.5** : arrêt bruyant, mobilisable à tout moment.
- **③ → ①** : angles morts révélés par la production → réexamen épistémique.
- **capacité défaillante en cours de cycle → SONDE** : re-sonde de l'environnement.

## Couplages structurels (F) — le squelette

|Couplage    |Int.|Nature              |Note                                                                                                                  |
|------------|----|--------------------|----------------------------------------------------------------------------------------------------------------------|
|SONDE → MAMD|F   |active              |l'environnement est établi *avant* la signature — ouverture de cycle                                                  |
|SONDE → MEDA|F   |alimente            |router vers une capacité `absente` est une erreur de type                                                             |
|SONDE → EXT-02|F |borne               |une action technique ne peut engager qu'une capacité présente à la carte                                              |
|ACA ← MAMD  |F   |alimente            |ACA consomme la signature (pattern canonique D4)                                                                      |
|I-07 ↔ Noyau|F   |audite / conditionne|**Terminateur** : la revue I-07 est consultative ; l’acte de modification (Noyau/humain) tranche → pas de cycle infini|
|MAMD → MEDA |F   |alimente            |pré-MEDA, prérequis du routage                                                                                        |
|MAMD → F-04 |F   |alimente            |Champ 5 → maïeutique                                                                                                  |
|Noyau → Lyra|F   |conditionne         |gate P0 universel                                                                                                     |

## Invariant d’ordonnancement (≠ couplage modulaire)

**②→③** : la souveraineté conditionne la production (MI-5 étendu). C’est une **contrainte de séquence**, notée à part pour ne pas la conflater avec un couplage de données (résolution du challenge relecture cycle 17).

## Relations inter-pôles

`① borne ③` · `② conditionne ③` · `① informe ② ` · `③ rétroagit ①`