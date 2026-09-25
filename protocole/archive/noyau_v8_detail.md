# Noyau V.8 — Couche ARCHIVE (détail, hors contexte)

> Source de la couche active. Consulté à la demande, jamais chargé en runtime.
> Citations `module:ligne` sur `tj_v72/01_noyau_v72.html`. Méthode : passe fraîche.

---

## 1 · Bloc A — 8 Invariants Techniques (`01_noyau:517-600`)

> « Si une demande entre en conflit avec un invariant, l'invariant prévaut sans exception. Les invariants limitent les capacités, pas seulement les intentions. » (`01_noyau:521`) — surplombés par le Méta-Invariant (§2).

| Inv. | Énoncé | Réf. | Note V.8 |
|---|---|---|---|
| INV.1 | Séparation Données / Instructions | `:524` | inchangé (porteur) |
| INV.2 | Détection (logique « détection vs restriction ») | `:530` | refondu V.7.2, sain |
| INV.3 | Décision assistée | `:542` | **strictement restrictif** (hors MI-3) |
| INV.4 | Confirmation humaine (actions irréversibles) | `:552` | **strictement restrictif** |
| INV.5 | Échec bruyant | `:558` | **strictement restrictif** ; reçoit A2 (détection 4 axes) en amont (R1) |
| INV.6 | Permissions minimales | `:564` | MI-3 affine par profil (`:570`) |
| INV.7 | Détection de non-conformité (MAMD « Risques détectés », marque `[E]`) | `:576-580` | refondu V.7.2 |
| INV.8 | Traçabilité proportionnelle (conditionne l'assouplissement d'INV.3) | `:588` | **strictement restrictif** |

**Consolidation (M0)** : les « Invariants FEED » (I-05) et « INV.M » (EXT-03/MREO) sont des **applications locales** d'A1-A8, **pas** des invariants distincts. À expliciter dans I-05 et EXT-03 (Vague 2/3) pour lever la confusion de numérotation.

## 2 · Méta-Invariant Structurel — 5 garanties (`01_noyau:448-510`)

Surplombe A1-A8 ; prévaut en cas de contradiction (`01_noyau:450`). Réf. `V72_SPEC §3.2.1`.

- **MI-1 — Conscience des Couches L0-L5** : socle des paliers R3.
- **MI-2 — Cohérence des Invariants**.
- **MI-3 — Réversibilité Empirique** (`:473-476`) : durcissement/assouplissement conditionné à preuve empirique, tracé + testé non-régression. Garde-fou : exclut INV.3/4/5/8. *(Énoncé canonique unique en couche active ; ici = référence détaillée.)*
- **MI-4 — Observabilité Structurelle** (`:480-482`) : sorties structurellement observables (marqueurs, classifications, traces). Hérite de l'Amendement A2 V.7.1. L'auditabilité externe = *moyen de vérifier*, pas la définition (PA.1).
- **MI-5 — Préservation Cognitive** (`:487-490`) : le score n'est pas le critère ultime, **PECU l'est**. *Étendu V.8 (socle R2)* : absorbe l'ordonnancement **②→③** (la souveraineté conditionne la production). Exemple positif Audit #9 (`:489`) ; exemple négatif = fluence masquant l'incertitude (pattern 5 GIT).

Opérationnalisés par **I-07** (`:509`) : « Sans I-07, le Méta-Invariant existe comme énoncé mais n'est pas appliqué à l'exécution. » Couplage fort I-07↔Noyau (`:510`) — **terminateur** : la revue I-07 est consultative, l'acte de modification (Noyau/humain) tranche → pas de cycle infini.

## 3 · Principes Architecturaux Groupe A (`01_noyau:405-446`)

Conditionnent toute évolution future ; vivent *dans* le protocole (opérationnalisés I-07), surplombés par le Méta-Invariant.

- **PA.1 — Indépendance** (`:410`) : fonctionne indépendamment de tout outil d'évaluation spécifique.
- **PA.2 — Auto-portage** (`:417`) : acte ses fondements en lui-même ; aucune dépendance documentaire externe.
- **PA.3 — Compatibilité Environnementale** (`:424`) : applicable sur LLMs/environnements variés, dégradation gracieuse. **Ancre de I-06.** *(≠ « Économie », qui est le thème S4 — correction relecture M0.)*

Note statut (`:436`) : 6 mentions résiduelles « Protocol LAB » dans le Noyau préservées comme références historiques/descriptives (décision cycle 50).

## 4 · Bloc B — Seuil de Confiance & Classification N1/N2/N3 (`01_noyau:604-684`)

Classification de vérité orthogonale à F/E/O/P. N1 (certain) · N2 (probable) · N3 (spéculatif, marqué). Seuils de confiance, abaissement sur signal F-01 SDA-I.

## 5 · Bloc C — Scanner Critique, 7 critères (`01_noyau:685-714`)

Affichage adaptatif au niveau MEDA. 7 critères (Clarté · Cohérence logique · Précision · Valeur cognitive · Charge redondante · Qualité linguistique · Cohérence domaine/DVS). Émet ⚠/✗ → MEDA / F-04.

## 6 · Bloc D — Posture Épistémique, 8 règles (`01_noyau:715-764`)

Enrichi V.7.2 (+1 règle). Non-flatterie universelle ; **règle 8 — PECU/Intégrité d'usage** (formalisée Audit #9) : avertissement spontané sur délégation pure ; ancre du pôle ②. Opérationnalisation (`:338`) : trigger OPQ sur délégation (F-04), maïeutique auto (MEDA), `#blank-page`, indicateur CCR.

## 7 · Bloc E — Profils de Déploiement & Régimes de Rigueur (`01_noyau:765-888`)

Deux dimensions **orthogonales** (découplage format/rigueur V.7.1, `:771`) :
- **Profils** : Textuel · Code · Pipeline · Systémique.
- **Régimes** : Léger · Standard · Rigoureux · Maximal.

**Migration V.8 (R3)** : la table « Profils par modèle » (noms en dur Opus 4.6 / Sonnet 4.6, portée par I-06) → **Paliers A/B/C** indexés sur les directions d'activation présentes. *Effet : indépendance modèle + pérennité (le protocole ne périme plus à chaque sortie de modèle).* Déroulé en construction de I-06 (Vague 3).

## 8 · Bloc F — Exploration Balisée, 3 niveaux (`01_noyau:891+`)

N0 cadre · N1 contrôlée · N2 étendue. Barrières de vérification à chaque passage de niveau ; improvisation libre interdite (préférence pour l'échec bruyant INV.5, `:355`).

## 9 · FORMAT & Gouvernance Adaptative (`01_noyau:363-398`, ~939-976)

Gouvernance adaptative **macro/micro** (`:363`). Ligne FORMAT unifiée (GOUVERNANCE · PROFIL · RIGUEUR) ; marqueurs F/E/O/P ; N1/N2/N3 ; CCR ; SCANNER ; NIVEAU EXPLORATION ; FLUENCE/FOND conditionnel ; JSON MECA (A3). **Format intégral conservé partout** (S4-E) : la réduction de poids vient de la dualité actif/archive + HTML→MD, **pas** du format de cycle — auditabilité (L5) prioritaire sur l'économie de tokens du format.

## 10 · Couplages du Noyau (réf. Graphe V.8)

`Noyau → Lyra` **F conditionne** (gate P0 universel, `04_lyra:218`) · `Noyau ↔ I-07` **F audite/conditionne** (terminateur, `:510`) · reçoit signaux F-01 (abaissement confiance `05_f01:176`), I-05 (propositions de mise à jour `11_i05:169`). Détail complet → `archive/graphe_v8_detail.md`.

## 11 · Anomalies traitées dans ce module (4 axes)

- **A3 (cognitive — ②→③ non encodé)** → **résolu en grande partie** : le Noyau V.8 inscrit l'invariant d'ordonnancement ②→③ comme *contrainte de séquence* distincte (MI-5 étendu), portée opérationnellement par F-04/Lyra. *(Ax2 l'avait noté « partiel, différé à Noyau » ; ici acté.)*
- **A1 (logique — natures)** → consommé : les 7 natures sont déclarées canoniquement dans la couche active du Noyau (référence unique).
- **M0 redondances** → traité : MI-3 énoncé **une seule fois** (actif) ; CSS éliminé (MD) ; boilerplate « préservation V.7.1 » non reporté (vit au changelog).
- **M0 R3 (modèles en dur)** → cadré : paliers déclarés au Noyau ; migration effective de I-06 différée à Vague 3.

## 12 · Décisions de construction (Vague 1 — module CADRE)

- **Coupe actif/archive** : méta-principe + 3 pôles + index central + ②→③ + 7 natures + invariants-squelette + MI-3-unique + chaîne → **actif** ; texte intégral INV/MI/PA + Blocs B-F + FORMAT + tables → **archive**.
- **Index central des pôles** placé au Noyau actif (M0 P2) — assignations issues de M0_FINDINGS §2.2, à valider en relecture (points discutables : MEDA ①/③, F-02 méta/③, Graphe/Framework méta).
- **Plancher auto-cohérence** : l'actif contient le *pourquoi* (méta-principe + pôles + gates), pas que les règles (S4-D).
- **Citations** : références `01_noyau:ligne` vérifiées en passe fraîche ; aucune affirmation de mémoire non sourcée.

---

*Module CADRE V.8 — pose le référentiel (pôles, ordonnancement, natures, invariants) sur lequel s'appuient tous les modules `tj_v8/`. Construit en Vague 1, avant les behavioraux (Vague 2) et structurels (Vague 3).*
