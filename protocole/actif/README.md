# Couche ACTIVE (runtime)

> Dualité actif / archive. C'est le mécanisme de compacité du protocole : on ne réduit *rien*,
> on réduit seulement ce que le modèle **porte en contexte**.

**Rôle** — ce dossier contient la couche **chargée en contexte** : ce qui est réellement présent
quand le modèle travaille. Porteur minimal, et rien de plus :

- la définition, le méta-principe *Conservation du Champ*, les 3 pôles et leur ordonnancement
- les invariants, les méta-invariants et les principes architecturaux
- le schéma d'activation **AMORCE → PROCESSUS → SORTIE** de chaque module
- la **logique-cœur** des modules — pas leur documentation exhaustive

**Format** : Markdown.

**Plancher anti-« oubli de soi »** — on conserve toujours ici le *pourquoi* compressé (méta-principe
et 3 pôles), pas seulement les règles. Un protocole réduit à ses règles perd la capacité de juger
un cas que ses règles n'avaient pas prévu.

**Contenu** : 20 modules + `emission_audit_v8.md`, le template du bloc d'audit émis en fin de
cycle. Le template n'est pas un module : il n'a pas de fiche de détail, et c'est normal.

**Le détail** vit dans [`../archive/`](../archive/) et ne se charge qu'à la demande.
