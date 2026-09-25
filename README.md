# Protocole LAB — V.8

**Une discipline de cognition appliquée à l'interaction avec un modèle de langage.**
Pas un style de réponse, pas un *system prompt* de confort : un cadre qui gouverne comment
l'échange est structuré, exposé et **audité** — et qui déclare ce qu'il ne fait pas.

Le protocole s'installe comme **Agent Skill** (dossier [`skill/`](skill/)) et fonctionne dans
n'importe quel hôte capable de charger un fichier d'instructions.

---

## Ce qu'il fait

Il pose trois pôles et un ordre entre eux, qui est l'essentiel du dispositif :

| Pôle | Rôle |
|---|---|
| **① Épistémique** | classer, vérifier, marquer la nature d'une affirmation, résister à la fluence |
| **② Souveraineté cognitive** | amplifier la pensée de l'utilisateur, jamais s'y substituer |
| **③ Production** | optimiser l'extraction et la direction de la capacité productive |

**② conditionne ③.** Une production ne s'enclenche qu'après sécurisation de l'engagement cognitif
de la personne. L'inversion — produire d'abord, réfléchir ensuite — est le contournement que ce
protocole existe pour empêcher.

Autour de cet axe : **8 invariants**, **5 méta-invariants**, **3 principes architecturaux**,
**20 modules** couplés en un graphe typé, et un **bloc d'audit JSON** émis en fin de cycle, dont
plusieurs cohérences sont vérifiables **hors du modèle** — par exemple `leurres = présentées −
survivantes`, ou `maïeutique forte ⇒ engagement = délégation pure`.

## Ce qu'il n'est pas

Un oracle de qualité · une garantie de justesse · un substitut au jugement humain · un
neutralisateur des valeurs du modèle sous-jacent.

Il ne *crée* ni la qualité ni l'efficience — elles viennent du modèle, qui est un plafond
structurel. Il gouverne **à quelle distance de ce plafond** l'interaction opère.

Et une limite qu'il énonce lui-même : **une métrique dérivée de la structure qu'elle évalue est un
majorant, jamais une validation.** Un auditeur logé dans le même contexte que le producteur mesure
sa propre cohérence, pas sa justesse.

---

## Installation

**Agent de code** (Claude Code, Cursor, Codex…) — copier [`skill/`](skill/) dans le répertoire de
skills de l'outil, sous le nom du protocole. Le chargement est **progressif** : `SKILL.md` porte la
couche active, `references/` et `archive/` ne se chargent qu'à la demande.

**Application conversationnelle** — coller le contenu de [`skill/SKILL.md`](skill/SKILL.md) comme
instructions personnalisées ou en tête de conversation.

**Lecture directe** — [`protocole/actif/`](protocole/actif/) contient les 20 modules et le template
d'émission ; [`protocole/archive/`](protocole/archive/) leur détail.

## Structure

```
protocole/actif/     20 modules + le template d'émission — la couche runtime
protocole/archive/   20 fiches de détail — chargées à la demande
skill/               le même contenu, empaqueté en Agent Skill installable
```

La **dualité des couches** est le mécanisme de compacité : le format intégral est conservé partout,
la légèreté vient de la divulgation progressive, jamais d'une amputation.

## Langue

**Le français est la langue source.** Une traduction anglaise est prévue ; en cas de divergence
future, le français fait foi jusqu'à arbitrage explicite et daté.

Les citations internes de la forme `01_noyau:363-398` sont des **marqueurs de provenance** : elles
renvoient aux documents de construction des versions antérieures, conservés hors de ce dépôt. Elles
sont opaques pour un lecteur extérieur, et c'est assumé — elles attestent qu'une affirmation a une
source, sans prétendre la fournir.

---

## Contribuer

Ce protocole est **intrinsèquement collaboratif**. Une incohérence relevée vaut mieux qu'une
fonctionnalité ajoutée : un contre-exemple, une erreur, un défaut de portabilité, un cas où
l'instrument se trompe — tout cela fait avancer le travail plus sûrement qu'un ajout.

Une règle encadre les évolutions : **aucun durcissement ni assouplissement sans donnée empirique**.
Une proposition appuyée sur une mesure a un chemin ; une intuition seule n'en a pas.
Voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

[MIT](LICENSE) — aucune restriction d'utilisation, de réutilisation ou de modification.
La seule obligation est l'attribution. `Copyright (c) 2026 Lazerr`.
