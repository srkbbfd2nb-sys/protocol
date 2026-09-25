# tj_v8/archive/ — Couche ARCHIVE (hors contexte)

> Décision **S4-C** (dualité actif/archive). Voir `FONDATIONS_V8.md` §S4.

**Rôle** : ce dossier contient la **documentation exhaustive hors contexte runtime**.
Consultée à la demande, **jamais chargée** dans le system prompt par défaut :
- documentation complète des modules · rationale · historique des décisions
- changelogs · benchmark / plan / update · notes de conception

**Format** : **HTML** (couche archive = HTML, réservée à la lecture humaine).

**Principe réconciliateur (S4-C)** : « ne rien réduire » ↔ « réduire le poids ».
On ne réduit *rien* (tout le détail vit ici, en archive) ; on réduit seulement ce que le
modèle *porte en contexte* (la couche `actif/`).

**Construction** : alimentée pendant **M0** au fil du repackaging actif/archive de chaque module.
Statut actuel : **EN CONSTRUCTION**.

**Référent stable immuable** : `prompts/tj_v72/` (21 documents HTML). Les artefacts V.7.2
restent la source de vérité tant que la couche V.8 n'est pas complète.
