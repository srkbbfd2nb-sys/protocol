# MECA V.8 — Couche ACTIVE (runtime)

> **Couche** : active (MD). **Classification** : *behavioral*. **Pôle** : **①** (évaluation cognitive de la sortie — audite).
> **Rôle** : évaluation cognitive adaptative, 5 axes, **JSON structuré** en fin de cycle. Seul module à émettre du JSON — patron de la resémantisation instrument (driver 2).
> **Détail** (5 axes, seuils, JSON A3, sous-axes V.7.2, signal audit) → `archive/meca_v8_detail.md`.

## AMORCE
- **Automatique, en fin de cycle évalué** (tous modes/régimes ; contenu condensé en Léger, structure JSON obligatoire — A3). Reçoit : MEDA (profondeur), F-01 SDA-I (→ Axe 3), PADC-IA (robustesse A/B + authenticité), Lyra AED, F-03 inspection (→ Axe 5), F-02 (fin pipeline + OFI), EXT-01/EXT-02 (→ Axe 3) (`07_meca:177`).

## PROCESSUS — scoring 5 axes + audits V.8
Score : **clarté · valeur_cognitive · coherence · robustesse_ab · integrite** → `score_global` + seuil (Optimal/Acceptable/Insuffisant/Rejet).
Sous-axes : `nature_distinction` (F/E/O/P sur Clarté) · **`conformite_reflexive`** (PA.1/2/3, I-07 §F.3) · **`coherence_mamd`** (intention/nature/complexité/risques/contexte).

**Audits V.8 ajoutés** :
- **Audit ②→③** (gate de souveraineté) : vérifie qu'un cycle **n'a pas violé l'ordonnancement** — production (③) avant sécurisation de la souveraineté (②). Violation = signal (co-porté avec I-07). *(Inscrit ici sur consigne cycle 22 ; l'invariant lui-même vit au Noyau.)*
- **Sous-axe `authenticite_alternatives`** (T2 §6) — *déclaré* : présentées/survivantes/leurres/réfutation démontrée/effondrement (JSON sémantique). *Implémentation runtime différée driver 2 ; l'axe est posé.*

## SORTIE
**JSON MECA** brut (pas d'encapsulation markdown) : axes + score_global + seuil + nature_distinction + `mode_v72` + `conformite_reflexive` + `coherence_mamd` (+ `authenticite_alternatives` déclaré) + recommandations + `signal_audit`.

## Couplages *(réf. Graphe ; passe fraîche)*
- **MECA → F-04** : `Fn rétroagit` (si Clarté/Valeur cognitive < 0,70, `07_meca:178`). Inverse F-04→MECA `Fn alimente`.
- **MECA → F-03** : `Fn rétroagit` (si Intégrité < 0,70). **→ F-02** : `Fn rétroagit` (rejet/insuffisant → **OFI**, relance — ré-entrée).
- **MECA ← PADC-IA** (robustesse + authenticité), **← MAMD** (`coherence_mamd`), **← I-07** (`conformite_reflexive`) — `Fn audite`/`alimente`.
- **MECA + I-07** co-portent l'**audit ②→③**.

→ 5 axes détaillés, seuils, format JSON A3 complet, règles signal audit, EEO itératif, fail_safe : `archive/meca_v8_detail.md`.
