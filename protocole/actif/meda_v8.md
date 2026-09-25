# MEDA V.8 — Couche ACTIVE (runtime)

> **Couche** : active (MD). **Classification** : *behavioral*. **Pôle** : **①** (évaluation de la demande ; *sert ③ via le routage, sans être ③* — index Noyau).
> **Rôle** : routing cognitif — évalue la demande sur 8 dimensions, en déduit le niveau (Light/Complet/Expert) et route les modules. Informé par la signature MAMD (V.8).
> **Détail** (8 dimensions, plages, signaux EEO/MREO/Phase 1.5, contextualisation 5 couches) → `archive/meda_v8_detail.md`.

## AMORCE
- **Automatique, chaque cycle**, **post-MAMD** (consomme la signature 8 champs pour router en *informé* ; sans MAMD, route sur ses heuristiques propres). Reçoit aussi : Lyra P1 (complexité), EXT-01 (signal système réel), Noyau Bloc C (⚠/✗), commandes utilisateur (`02_meda:509`).

## PROCESSUS — routing 8 dimensions
Score la demande sur 8 dimensions (plage 8-24) → **niveau** :
`Light` (8-13) · `Complet` (14-19) · `Expert` (20-24).
Dimensions : Nature · Domaine · Sources requises · Longueur estimée · Risque d'erreur · Modules nécessaires · Système réel · Action technique.
Signaux dérivés : Phase 1.5 (système réel ≥ 2) · EXT-02 (action technique ≥ 2) · EEO (production) · MREO (artefact analysable) · contextualisation 5 couches · **maïeutique auto sur délégation** (→ F-04 ; V.8 : signal de délégation = sémantique via MAMD Champ 8, pas motif littéral — garde-fou S3).

## SORTIE
Ligne **MEDA — Niveau : [X] — Score : [n]/24** + dimensions + signaux d'activation. Détermine la profondeur de tous les modules aval.

## Couplages *(réf. Graphe ; passe fraîche)*
- **MEDA ← MAMD** : `F alimente` (pré-MEDA, `16_mamd:430`). Inverse `?`.
- **MEDA ← Lyra** (complexité), **← EXT-01** (système réel), **← Noyau Bloc C** (`02_meda:509`).
- **MEDA →** modules aval (profondeur de scoring), **→ F-04** (maïeutique si délégation), **→ MECA** (profondeur d'évaluation `07_meca:177`), **→ EXT-01/EXT-02/F-02** (signaux). *(détail ENVOIE `02_meda:510` → archive.)*
- **ACA ↔ MEDA** : `Fn active` (`17_aca:431`).

→ Plages détaillées, patterns de contextualisation, signaux EEO/MREO/dégradation Pipeline : `archive/meda_v8_detail.md`.
