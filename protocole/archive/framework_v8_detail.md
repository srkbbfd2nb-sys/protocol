# Framework Stress-Test V.8 — Couche ARCHIVE (détail, hors contexte)

> Source de la couche active. Citations sur `tj_v72/19_framework_stress_test`. Passe fraîche (M0 + Ax2).

## 1 · Stratification L0-L5 (adossée MI-1)
L0 architecture neuronale · L1 entraînement de base · L2 fine-tuning & alignement · **L3 system prompt (critique)** · L4 contexte session · **L5 demande utilisateur (critique)**. Scénarios de stress par couche : adversariaux, injections, dérive multi-tour, délégation cachée.

## 2 · Stabilité ≠ robustesse (principe épistémologique fondateur)
Un score stable (faible variance) peut masquer une fragilité comportementale (casse sous perturbation non couverte par la mesure). Validation V.8 : mesurer les deux, séparément.

## 3 · Mapping benchmarks
Correspondance scénarios ↔ benchmarks externes (consultatif, PA.1-safe : les benchmarks sont des instruments de mesure, pas des dépendances du protocole).

## 4 · Rôle dans la roadmap (étape Out / driver 2)
Le Framework fournit le référentiel de la **resémantisation de Protocol LAB** (Scénario 3, patron MECA-JSON). La leçon empirique tâche 5 (instrument aveugle au sémantique — L3) est intégrée : la future instrumentation lit des données structurées, pas des marqueurs de surface.

## 5 · Décisions de construction
- **Méta-infrastructure** (correction cycle 22 — était « pôle ① » discutable en M0) : le stress-test valide le *système*, pas un pôle.
- **Surtout archive** (consigne V3) : l'actif ne porte que la stratification + le principe stabilité/robustesse (plancher auto-cohérence) ; tout le reste vit ici.
- **Couplages** : EXT-01 → Framework (`Fn informe`, référentiel statique) ; le reste `?` (non documenté legacy — honnêteté D1).

*Module méta-infrastructure V.8 (validation). Vague 3.*

---

# Note d'archivage — changelog & golden (V3, consigne)

**`changelog_v710_to_v720.html`** et **`golden_response_v720.html`** ne sont **pas reconstruits en modules V.8** : ce sont des documents *historiques/exemples* (couche archive par nature, S4). Ils restent dans `tj_v72/` (canoniques, immuables — 21/21) et sont **référencés** comme archive V.7.2. Le golden reste le cas pédagogique de référence de l'anomalie #2 (F-04) ; un golden V.8 sera produit après stabilisation (étape Out/Dep).
