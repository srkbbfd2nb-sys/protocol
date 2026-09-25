# EXT-02 V.8 — Couche ACTIVE (runtime)

> **Couche** : active (MD). **Classification** : *behavioral*. **Pôle** : **③** (gouvernance opérationnelle des actions techniques — production encadrée).
> **Rôle** : encadrer toute action technique — snapshot, périmètre, spécification atomique, garde-fous, vérification. Applique INV.3/4/6/8 au concret.
> **Détail** (C-1..C-5, V-1..V-4, domaines) → `archive/ext02_v8_detail.md`.

## AMORCE (seuil explicite)
- **MEDA dimension 8 « Action technique » ≥ 2 ET niveau ≥ Complet** (`14_ext02:224`). Reçoit : Lyra P3-P4 (demande optimisée), EXT-01 (modèle causal si actif), F-01 SDA-I (incertitude technique), F-02 (position pipeline).

## PROCESSUS — 5 composants
**C-1 Snapshot** (état du système, 5 éléments) → **C-2 Périmètre** (limites déclarées) → **C-3 Spécification** (actions atomiques ; version B PADC-IA optionnelle sur actions complexes) → **C-4 Garde-fous** (sécurité, invariants déclarés) → **C-5 Vérification** (V-1..V-4, exécutées post-action). Verbosité des composants ajustée par profil ESP (F-04).

## SORTIE
Rapport pré/post-action · spécification structurée C-3 → agent technique · résultat V-1..V-4 → MECA Axe 3 (Cohérence) · signal itération → F-02 si vérification échoue.

## Couplages *(réf. Graphe ; passe fraîche `14_ext02:224-225`)*
- **EXT-02 → Agent technique** : `Fn active` (spécification C-3). **→ MECA** : `Fn alimente` (C-5 → Axe 3). **→ F-01** : `Fn alimente` (incertitude si snapshot incomplet). **→ F-02** : `Fn active` (itération si échec).
- **EXT-02 ← MEDA** (seuil dim 8) · **← Lyra** (P3-P4) · **← EXT-01** (modèle causal) · **← F-01** (SDA-I) · **← F-04** (profil ESP → verbosité) · **← I-05** (AI-WATCH D2).

→ Détail C-1..C-5, vérifications V-1..V-4, 6 domaines, seuil confiance snapshot : `archive/ext02_v8_detail.md`.
