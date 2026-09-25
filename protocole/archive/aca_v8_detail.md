# ACA V.8 — Couche ARCHIVE (détail, hors contexte)

> Source de la couche active. Citations `module:ligne` sur `tj_v72/17_aca`. Passe fraîche.

---

## 1 · Position structurelle (`17_aca:216`)

Module actif à **dominance opérationnelle (orchestrateur)**. S'exécute à chaque cycle, **post-MAMD pré-orchestration invariante**. Consomme la signature MAMD et décide quels modules orchestrés activer/désactiver. Se distingue de MEDA (`17_aca:223`) : MEDA route sur ses heuristiques propres, ACA décide selon la *signature multi-dimensionnelle MAMD*.

## 2 · Les 5 principes régulateurs (`17_aca:214`)

1. **Détection avant activation** — n'active qu'après lecture de la signature.
2. **Réversibilité explicite** — toute activation est annulable (MI-3).
3. **Priorité aux commandes manuelles** — l'utilisateur prime toujours sur l'auto-activation.
4. **Trace permanente** — chaque activation est tracée avec sa source MAMD (MI-4).
5. **Désactivation globale** — `#aca:off` / `#aca:off:session`.

## 3 · Règles d'activation (résumé — 8 règles)

Exemples clés : F-04 maïeutique forte (Champ 5 pure + Champ 8 confirmé, `17_aca:437-438`) · F-04 molle (partielle OU mixte) · Lyra clause éthique (Champ 6 risque éthique) · PADC-IA pondération renforcée (Champ 6 position contestée) · F-01 vigilance (Champ 3 mixte) · F-03 (Champ 6 surconfiance). *Détail complet des conditions → à porter en construction finale si besoin runtime.*

## 4 · Couplages (réf. Graphe V.8)

REÇOIT : MAMD (**F**, signature `17_aca:425`). ENVOIE (tous `active`) : F-04 (`:437`) · F-03 (`:443`) · Lyra (`:449`) · MEDA (`:431`, bidirectionnel partiel). Note : ACA *ajuste le déclenchement*, jamais le *contenu* du module cible.

## 5 · Portabilité des commandes (S3-B)

Textuel : honoré directement. Code (CC) : requiert protocole en contexte + instruction de les honorer. Pipeline (N8N) : aucune application auto sans injection par nœud. Systémique : dépend de l'orchestration.

## 6 · Fallback & garantie

`#aca:off` → F-04/modules retombent sur heuristiques V.7.1 (MI-3 réversibilité). En fallback, la résolution structurelle de l'anomalie #2 n'est plus garantie (documenté). À usage diagnostique, pas en exécution normale.

## 7 · Décisions de construction

- **Classification méta-infrastructure** : ACA orchestre, ne produit pas de contenu (`17_aca:223`) → aucun pôle ①/②/③ dominant. Cohérent index Noyau corrigé.
- **AMORCE→PROCESSUS→SORTIE** : AMORCE = auto post-MAMD + commandes ; PROCESSUS = 5 principes + évaluation règles ; SORTIE = bloc ACTIVATIONS ACA.
- **Coupe S4** : position + 5 principes (noms) + couplages + garantie fallback → actif ; détail des 8 règles + portabilité → archive.

---

*Module méta-infrastructure V.8. Active selon la signature MAMD. Vague 2.*
