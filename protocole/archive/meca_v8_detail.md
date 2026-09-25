# MECA V.8 — Couche ARCHIVE (détail, hors contexte)

> Source de la couche active. Citations `module:ligne` sur `tj_v72/07_meca` + `MOTEUR_T2_V8`. Passe fraîche.

---

## 1 · Les 5 axes & seuils

Axes : clarté · valeur_cognitive · coherence · robustesse_ab · integrite. `score_global` = somme pondérée.
Seuils : Optimal [0.85-1.00] · Acceptable [0.70-0.84] · Insuffisant [0.50-0.69] · Rejet [0.00-0.49].
Verdicts d'action : EXECUTE ≥ 0.70 · PARTIEL ≥ 0.40 · SIMULE < 0.40.

## 2 · Sous-axes (V.7.1 + V.7.2)

- **nature_distinction** (V.7.1) : F/E/O/P sur l'axe Clarté ; pénalité si absent hors régime Léger.
- **conformite_reflexive** (V.7.2, I-07 §F.3) : `{pa1, pa2, pa3}` ∈ ok/alerte/echec.
- **coherence_mamd** (V.7.2) : `{intention, nature_feop, complexite, risques, contexte}` ∈ ok/derive.
- **mode_v72** : informe / partiel / fallback (selon disponibilité I-07/MAMD).

## 3 · Audits V.8 ajoutés (consigne cycle 22)

- **Audit ②→③** : MECA (+ I-07) vérifient que le cycle n'a pas produit (③) avant sécurisation de la souveraineté (②). C'est l'audit du **gate de souveraineté** (MI-5 étendu). L'énoncé de l'invariant vit au Noyau ; ici = sa *vérification*.
- **`authenticite_alternatives`** (T2 §6, Fork B) — déclaré : `{presentees, survivantes_steelman_distinction, leurres, effondrement, refutation_demontree, amorce_appropriee, score}`. Mesure sémantique (JSON, pas regex — sortie de la fragilité L3). **Runtime différé driver 2** ; l'axe est posé pour anti-régression.

## 4 · Format JSON A3 (obligatoire tous modes/régimes)

JSON brut, sans encapsulation markdown (commence par `{`, finit par `}`). Contenu condensé en Léger, structure toujours présente. Absence de JSON → plafond score 0.30 (fail-safe A3). Signal audit émis si ≥ 2 axes à valeur défaut (0.50) OU score_global < 0.70 (OU inclusif).

## 5 · Insight instrument (M0 / driver 2)

MECA est le **seul module à émettre du JSON structuré** → **patron de la resémantisation de Protocol LAB** : sortir de la fragilité regex (L3, finding empirique tâche 5) en faisant lire aux auditeurs des données structurées plutôt que des marqueurs de prose.

## 6 · Couplages (réf. Graphe V.8, `07_meca:177-178`)

REÇOIT : MEDA · F-01 SDA-I (→ Axe 3) · PADC-IA (A/B ×0,20 + PADC-EVAL + authenticité) · Lyra AED · F-02 (fin pipeline + OFI) · F-03 GIT (→ Axe 5) · EXT-01/EXT-02 (→ Axe 3) · Noyau Bloc C. ENVOIE : F-04 (< 0,70) · F-03 (Intégrité < 0,70) · F-02 (rejet → **OFI**) · Utilisateur (JSON + recommandations). Ré-entrée : **MECA→OFI→production**.

## 7 · Décisions de construction

- **Pôle ① (audite)** : MECA mesure la qualité de la sortie — acte épistémique pur.
- **Audit ②→③ inscrit** (consigne cycle 22) : co-porté MECA/I-07. Ferme le volet « rendre ②→③ auditable » de la Vague 1.
- **AMORCE→PROCESSUS→SORTIE** : AMORCE = fin de cycle auto ; PROCESSUS = 5 axes + sous-axes + audits V.8 ; SORTIE = JSON brut.
- **Coupe S4** : 5 axes (noms) + sous-axes V.7.2 + audits V.8 + couplages → actif ; seuils détaillés + format JSON complet + règles signal audit + EEO/fail-safe → archive.

---

*Module behavioral ① (audite) V.8. Clôt la chaîne (audit) + porte l'audit ②→③ + patron driver 2. Vague 2.*
