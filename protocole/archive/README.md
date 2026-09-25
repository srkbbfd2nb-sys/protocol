# Couche ARCHIVE (hors contexte)

> Dualité actif / archive. Ce dossier est l'autre moitié du mécanisme : il porte tout ce que la
> couche active ne porte pas, sans que le modèle ait à le charger.

**Rôle** — documentation exhaustive, consultée à la demande, **jamais chargée par défaut** dans le
contexte d'exécution :

- documentation complète de chaque module et rationale des choix
- historique des décisions, cas limites, exemples
- notes de conception

**Format** : Markdown, une fiche `<module>_detail.md` par module.

**Principe réconciliateur** — « ne rien réduire » et « réduire le poids » ne s'opposent que si l'on
confond le contenu et ce qui est porté en contexte. Ici, rien n'est retiré ; c'est la charge de
contexte qui est réduite, pas le protocole.

**Contenu** : 20 fiches de détail, appariées une pour une aux 20 modules de
[`../actif/`](../actif/). Cet appariement est une propriété vérifiable : un module sans fiche, ou
une fiche sans module, est un défaut.
