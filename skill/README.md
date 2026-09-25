# Protocole LAB V.8 — paquet Agent Skill

Paquet généré par `build_skill_v8.py`. **Ne pas éditer à la main** : la source est
`prompts/lab_v8/{actif,archive}/`, régénérer avec `py build_skill_v8.py`.

- `SKILL.md` — frontmatter + contrat de chargement + index
- `references/` — 20 modules de la couche active + le template d'émission (intégraux)
- `archive/` — 20 fiches de détail (lues à la demande), une par module

## Installation selon l'environnement

**Agent de code (Claude Code, Cursor, Codex…)** — copier ce dossier dans le répertoire de skills du
harness, **en le renommant `protocol-lab`** : le nom du dossier doit correspondre au champ `name` du
frontmatter de `SKILL.md`, sans quoi la skill ne se déclenche pas. Le `description` suffit ensuite au
déclenchement ; rien à coller.

**Conversation (claude.ai, projet)** — déposer `SKILL.md` et `references/` dans les fichiers du projet.
`SKILL.md` sert de point d'entrée : il indique quoi lire et dans quel ordre.

**Pipeline / API** — charger `SKILL.md` + `references/noyau_v8.md` en system prompt ; résoudre les autres
références à la demande. La sonde de capacités s'exécute à l'ouverture de cycle.

**Hôte minimal** — `SKILL.md` + `references/noyau_v8.md` seuls constituent un protocole opérant, dégradé
mais honnête : la sonde déclarera le régime `degrade` et la sortie dira ce qui n'a pas pu être fait.

## Ce que ce paquet ne fait pas

Il ne réduit pas le protocole. Il n'en produit pas de version « allégée ». Il fixe un **ordre de lecture**
qui rend la charge proportionnée à la demande — c'est la dualité actif/archive (S4) rendue portable.
