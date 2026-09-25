# EXT-02 V.8 — Couche ARCHIVE (détail, hors contexte)

> Source de la couche active. Citations `module:ligne` sur `tj_v72/14_ext02`. Passe fraîche.

## 1 · Les 5 composants C-1..C-5
- **C-1 Snapshot** : état du système cible (5 éléments), confiance mesurée (< 0.7 → signal F-01).
- **C-2 Périmètre** : limites explicites de l'action (application d'INV.6 permissions minimales).
- **C-3 Spécification** : décomposition en actions atomiques ; version B (contradictoire PADC-IA) optionnelle sur actions complexes.
- **C-4 Garde-fous** : patterns de sécurité + invariants déclarés (INV.3/4 : confirmation sur irréversible).
- **C-5 Vérification** : V-1..V-4 exécutées après action ; résultat → MECA Axe 3 ; échec → itération F-02.

## 2 · Domaines
code · infra · data · design · config · générique. Adaptation de C-1..C-5 par domaine.

## 3 · Couplages (`14_ext02:224-225`)
REÇOIT : MEDA (dim 8 ≥ 2 + ≥ Complet) · Lyra (P3-P4) · EXT-01 (modèle causal → C-1/C-2) · F-01 SDA-I · F-02 (position pipeline) · F-04 (profil ESP → verbosité) · I-05 (AI-WATCH D2) · Utilisateur (contexte cible). ENVOIE : agent technique (C-3) · MECA (C-5 → Axe 3) · F-01 (snapshot incomplet) · F-02 (itération) · Utilisateur (rapport pré/post).

## 4 · Décisions de construction
- **Pôle ③** : EXT-02 encadre la *production d'actions* — c'est l'habilitation technique du moteur, dans le spectre borné (clause ③).
- **Trim de sortie** (M0 P3 : legacy 823 l., le plus verbeux après Noyau/Graphe) : l'actif ne porte que seuil + C-1..C-5 (noms) + couplages ; tout le détail descend en archive.
- **Coupe S4** : cf. ci-dessus.

*Module behavioral ③ V.8. Vague 2.*
