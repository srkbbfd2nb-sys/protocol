# Framework Stress-Test V.8 — Couche ACTIVE (runtime)

> **Couche** : active (MD — **minimale volontairement** : module surtout archive, consigne V3). **Classification** : *méta-infrastructure* (validation/stress-test — index Noyau corrigé).
> **Rôle** : référentiel de validation par couches L0-L5. Consulté lors des campagnes de test, jamais déclenché en cycle normal.
> **Détail complet** (scénarios par couche, mapping benchmarks) → `archive/framework_v8_detail.md`.

## Essence portée en actif (plancher auto-cohérence)

- **Stratification de VALIDATION L0-L5** : L0 architecture · L1 entraînement · L2 fine-tuning/alignement · **L3 system prompt** *(critique)* · L4 contexte session · **L5 demande utilisateur** *(critique)*.
- > **Désambiguïsation « Lx » (résout F-B relecture)** : trois référentiels historiques partagent l'étiquette « L ». (1) **MI-1** = couches d'*exécution* (le system prompt y est L2) ; (2) **Framework** = couches de *validation* (ci-dessus — le system prompt y est **L3**) ; (3) les limitations d'instrument (« L3-instrument », tâche 5) réfèrent à l'échelle **Framework**. **Convention V.8** : tout « Lx » non qualifié dans un contexte de validation/instrument (driver 2, Scénario 3) = échelle **Framework** ; l'échelle MI-1 se cite toujours qualifiée (« MI-1/L2 »). *Conflation héritée du legacy ; unification complète = option ultérieure (MI-3).*
- **Principe fondateur : stabilité ≠ robustesse.** La stabilité d'un score n'est pas équivalente à la robustesse du comportement — un protocole peut scorer stable et casser sous perturbation. Toute validation V.8 distingue les deux.
- **Leçon empirique intégrée** (tâche 5 / L3-instrument) : la validation mesure le *comportement sémantique*, pas la conformité de surface (regex) — patron MECA-JSON pour l'outillage (driver 2).

## Couplages
- **EXT-01 → Framework** : `Fn informe` (référentiel statique des couches — legacy). **Framework → étape Out** (driver 2) : matériau de la resémantisation de Protocol LAB.

→ Scénarios par couche (adversariaux, injections, dérive multi-tour, délégation cachée), mapping benchmarks : `archive/framework_v8_detail.md`.
