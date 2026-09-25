# Protocole LAB — V.8

**Une discipline de cognition appliquée à l'interaction avec un modèle de langage.**
Pas un style de réponse, pas un *system prompt* de confort : un cadre qui gouverne comment
l'échange est structuré, exposé et **audité** — et qui déclare ce qu'il ne fait pas.

Le dépôt porte les deux moitiés : **le protocole**, qui affirme, et **l'instrument**, qui vérifie.

```bash
python lab/audit_v8.py --input-file reponse.txt
```

Colle simplement entre "..." une réponse produite sous protocole dans un fichier, lance cette commande, obtiens un
verdict. Pas de clé, pas de compte, pas de serveur, aucune dépendance. C'est ce qui sépare un
document d'un objet vérifiable.

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
**20 modules** couplés en un graphe typé, et un **bloc d'audit JSON** émis en fin de cycle.

## À quoi ça ressemble

Chaque réponse sous protocole se termine par un bloc de ce genre — c'est la surface observable, et
c'est l'entrée de l'instrument :

```
===== LAB AUDIT JSON =====
{
  "signature_mamd": {
    "intention": "décider entre deux architectures de stockage",
    "engagement": "collaboratif",
    "risques": ["choix difficilement réversible", "données de charge absentes"]
  },
  "gates": {
    "lyra_p0": "passe", "f04_mode": "aucun",
    "ordre_2_3": { "securise": true, "viole": false }
  },
  "meca": {
    "axes": { "clarte": 0.91, "valeur_cognitive": 0.88, "coherence": 0.93,
              "robustesse_ab": 0.85, "integrite": 0.94 },
    "score_global": 0.90,
    "authenticite_alternatives": { "presentees": 3, "survivantes": 2, "leurres": 1 }
  }
}
===== FIN LAB AUDIT JSON =====
```

L'instrument y contrôle des cohérences qui ne demandent pas de relire le texte :
`leurres = présentées − survivantes` · `effondrement ⇒ réfutation démontrée` ·
`maïeutique forte ⇒ engagement = délégation pure` · `ordre ②→③ non violé`.
Il sort en `0`, `1` ou `2` — donc il se branche sur une chaîne d'intégration.

> **Ce que cela prouve, et ce que cela ne prouve pas.** Ces contrôles portent sur des champs que le
> modèle a lui-même émis : ils attrapent une incohérence de déclaration, **pas un mensonge
> cohérent**. Vérifier que `1 = 3 − 2` prouve que le compte se tient, pas que trois alternatives ont
> réellement été explorées. C'est un plancher d'honnêteté mécanique, et c'est la limite de fond du
> projet — voir [lab/README.md](lab/README.md).

## Ce qu'il n'est pas

Un oracle de qualité · une garantie de justesse · un substitut au jugement humain · un
neutralisateur des valeurs du modèle sous-jacent.

Il ne *crée* ni la qualité ni l'efficience — elles viennent du modèle, qui est un plafond
structurel. Il gouverne **à quelle distance de ce plafond** l'interaction opère.

Et une limite qu'il énonce lui-même : **une métrique dérivée de la structure qu'elle évalue est un
majorant, jamais une validation.** C'est aussi pourquoi l'instrument est *hors* de la boucle de
génération : un vérificateur intercalé partagerait le contexte du producteur, donc son biais.

## Ce qui a été mesuré

Une seule chose, et elle est publiée avec ses limites : le **gate ②→③ contourné**.
Même demande, deux exécutions — gate appliqué, gate contourné.

| | clarté | valeur cognitive | cohérence | robustesse | intégrité | global |
|---|--:|--:|--:|--:|--:|--:|
| gate appliqué | 0,92 | 0,95 | 0,94 | 0,88 | 0,95 | **0,93** |
| gate contourné | 0,90 | 0,82 | 0,88 | 0,75 | 0,85 | **0,84** |

Le contournement ne dégrade presque pas la **surface** (clarté −0,02) ; il dégrade le **fond**
(valeur cognitive et robustesse, −0,13 chacune). C'est un cas, n = 1, avec des scores auto-déclarés.
Méthode, lecture et limites : [mesures/](mesures/).

---

## Installation

**Agent de code** (Claude Code, Cursor, Codex…) — copier le dossier [skill/](skill/) dans le
répertoire de skills de l'outil **en le renommant `protocol-lab`**. Le nom du dossier doit
correspondre au champ `name` du frontmatter de [skill/SKILL.md](skill/SKILL.md), sans quoi la
skill ne se déclenche pas. Le chargement est ensuite **progressif** : `SKILL.md` porte la couche
active, `references/` et `archive/` ne se chargent qu'à la demande.

**Application conversationnelle** — coller le contenu de [skill/SKILL.md](skill/SKILL.md) comme
instructions personnalisées ou en tête de conversation.

**Lecture directe** — [protocole/actif/](protocole/actif/) contient les 20 modules et le template
d'émission ; [protocole/archive/](protocole/archive/) leur détail.

## Structure

```
protocole/actif/     20 modules + le template d'émission — la couche runtime
protocole/archive/   20 fiches de détail — chargées à la demande
skill/               le même contenu, empaqueté en Agent Skill installable
lab/                 l'instrument : extracteur, vérificateur, fixtures, 11 tests
mesures/             ce qui a été mesuré, et ce que ça ne prouve pas
GLOSSAIRE.md         les sigles, leur développement et ce qu'ils désignent
```

La **dualité des couches** est le mécanisme de compacité : le format intégral est conservé partout,
la légèreté vient de la divulgation progressive, jamais d'une amputation.

> **`protocole/` fait foi.** `skill/` en est un empaquetage. Une correction se fait dans
> `protocole/`, jamais dans `skill/` seul — et la CI échoue si les deux divergent.

## Vérifier soi-même

```bash
python -m pytest lab/tests/ -q
python lab/audit_v8.py --input-file lab/fixtures/coherence-violee.txt   # doit sortir en 1
```

Onze tests sur six fixtures. La CI les rejoue à chaque commit et contrôle en plus la dualité des
couches, la non-divergence du paquet Skill, et la concordance du délimiteur entre le template
d'émission et le vérificateur.

## Langue

**Le français est la langue source.** Une traduction anglaise est prévue ; en cas de divergence
future, le français fait foi jusqu'à arbitrage explicite et daté.

Les citations internes de la forme `01_noyau:363-398` sont des **marqueurs de provenance** : elles
renvoient aux documents de construction des versions antérieures, conservés hors de ce dépôt. Elles
attestent que l'auteur rattache une affirmation à une source, sans permettre de la vérifier.

---

## Contribuer

Ce protocole est **intrinsèquement collaboratif**. Une incohérence relevée vaut mieux qu'une
fonctionnalité ajoutée : un contre-exemple, une erreur, un défaut de portabilité, un cas où
l'instrument se trompe — tout cela fait avancer le travail plus sûrement qu'un ajout.

Une règle encadre les évolutions : **aucun durcissement ni assouplissement sans donnée empirique**.

> **Cette exigence vaut d'abord pour le dépôt.** Une seule mesure est publiée, sur un seul cas, avec
> des scores auto-déclarés. Les seuils qui apparaissent dans les modules — `0,70`, `0,80`,
> `SDA-I ≥ 4` — restent des paliers de travail, pas des valeurs mesurées. La contribution la plus
> utile qu'on puisse apporter ici est une **mesure**, en particulier une évaluation par un tiers
> hors contexte : c'est la seule façon de sortir de la circularité.

Voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

[MIT](LICENSE) — aucune restriction d'utilisation, de réutilisation ou de modification.
La seule obligation est l'attribution. `Copyright (c) 2026 Lazerr`.
