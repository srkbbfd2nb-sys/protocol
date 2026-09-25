# PADC-IA V.8 — Couche ARCHIVE (détail, hors contexte)

> Source de la couche active. Citations `module:ligne` sur `tj_v72/06_padc_ia` + `MOTEUR_T2_V8`. Passe fraîche.

---

## 1 · Les 4 contraintes épistémologiques C1-C4 (`06_padc_ia`)

- **C1 — Classification N sur chaque objection** : toute objection porte un niveau N1/N2/N3.
- **C2 — Signalisation de fragilité** : les points fragiles sont explicités, pas masqués.
- **C3 — Pas de contradiction artificielle** : ne pas fabriquer d'opposition là où il n'y en a pas (converge avec GDA : anti-leurre).
- **C4 — Cohérence de nature F/E/O/P** : les objections respectent la classification épistémique.

## 2 · Moteur GDA — étapes détaillées (`MOTEUR_T2_V8 §2-3`)

Voir `MOTEUR_T2_V8.md` pour la spec canonique. Points de scoring (sous-axe MECA, §6) :
`leurres = présentées − survivantes` ; effondrement (1 survivant) sans réfutation démontrée → pénalité forte (faux effondrement) ; amorce inappropriée (forks forcées sur du factuel) → pénalité. Score haut ⇔ 0 leurre ET (effondrement ⇒ réfutation montrée).

**Gate de présentation** (Fork A tranchée) : 1 survivant → chemin + réfutations montrées · 2-3 survivants → vraies forks (recommandation `[O]`, sert ②) · >3 → clustering + top distincts (sert #20/#33).

## 3 · PADC-EVAL — 6e axe longitudinal

Boucle d'autonomisation : mesure l'évolution de l'autonomie cognitive de l'utilisateur sur la session. Signale à F-04 (étape 7) si valeur cognitive basse malgré profil Expert. Alimente MECA (métrique de session, `06_padc_ia:171`).

## 4 · Risques & mitigations (`MOTEUR_T2_V8 §7`)

- **R-a Coût** (steelman = tokens) → profondeur calibrée aux enjeux (complet pour contesté/CCR-élevé ; léger pour routine). ≠ mode allégé de format (écarté).
- **R-b Faux effondrement** → réfutation démontrée obligatoire et montrée ; auditée par MECA §6.
- **R-c Sur-génération** (forcer la divergence sur du simple) → gate d'AMORCE sémantique.

## 5 · Couplages (réf. Graphe V.8, `06_padc_ia:170-171`)

REÇOIT : Noyau (analyse critique) · MEDA (Complet/Expert) · F-01 (INVARIANT A/B si SDA-I 6-8) · F-04 (étape 7) · EXT-01 Phase 1.5 (modèle système → base contradictoire). ENVOIE : MECA (robustesse A/B ×0,20 + PADC-EVAL + **authenticité alternatives**) · F-04 (PADC-EVAL) · EXT-02 (C-3 version B) · Utilisateur (PADC-ALERTE).

## 6 · Décisions de construction

- **Pôle ① + frontière ②** : PADC-IA authentifie (acte épistémique ①), mais le *comptage honnête* + *vraies forks* renforcent la souveraineté ② (frontière ②/③ du moteur T2). Rattaché ① avec note ②.
- **Refonte GDA** : le mécanisme legacy « 1 vraie option + N leurres » est remplacé par la Génération Divergente Authentifiée. Le nombre de chemins est *découvert*, jamais imposé (#22 résolu).
- **AMORCE→PROCESSUS→SORTIE** : AMORCE sémantique (multi-chemins défendables) ; PROCESSUS = GDA 5 étapes + C1-C4 ; SORTIE = 1-N alternatives authentifiées.
- **Coupe S4** : AMORCE + GDA 6 étapes + C1-C4 (noms) + couplage F-04/MECA → actif ; C1-C4 détail + PADC-EVAL + risques R-a/b/c → archive.

---

*Module behavioral ① (frontière ②) V.8 — porte le moteur GDA. Vague 2. Couplage cœur T2 : PADC-IA → F-04 → MECA.*
