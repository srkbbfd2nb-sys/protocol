# Politique de sécurité

## Signaler une vulnérabilité

Utiliser **Private vulnerability reporting** (onglet *Security* du dépôt). Cela permet de décrire
le problème sans le rendre public le temps qu'il soit traité.

Ne pas ouvrir d'issue publique pour une vulnérabilité exploitable.

## Périmètre

Le dépôt a trois parties, et elles n'ont pas la même surface d'attaque :

| Partie | Nature | Ce qui s'exécute |
|---|---|---|
| `protocole/`, `skill/` | texte normatif (Markdown) | rien — il est **chargé comme instructions** par un agent |
| `lab/` | instrument de vérification en Python | du code, sur la machine de qui le lance |
| `.github/workflows/` | intégration continue | du code, sur l'infrastructure de GitHub, à chaque commit |

**L'instrument** est écrit en Python, **bibliothèque standard seule** : aucune dépendance
d'exécution, aucun appel réseau, aucune clé. Il lit un fichier texte, rend un verdict, et écrit
une seule chose : un rapport JSON dans `logs/`, **sous le répertoire courant**. Les tests demandent
`pytest`, et rien d'autre.

**Ce que ça change pour une contribution.** Le dépôt accepte désormais du code, pas seulement du
texte. En conséquence, une demande de fusion qui :

- ajoute une **dépendance** à l'instrument (un `import` hors bibliothèque standard, un fichier
  `requirements`) ;
- introduit un **appel réseau**, une lecture de variable d'environnement ou de clé ;
- fait **écrire** l'instrument ailleurs, ou autre chose que ce rapport ;
- modifie le **workflow** d'intégration continue (actions tierces, permissions, secrets) ;

est un **changement de sécurité**, pas de style. Elle se relit comme tel et se justifie dans sa
description. C'est aussi la condition de la promesse faite au lecteur : pouvoir vérifier sans rien
installer ni rien confier.

Ce qui reste pertinent pour la partie texte :

**Injection par le contenu.** Le protocole est chargé comme instructions par un agent. Un contenu
tiers qui y serait inséré pourrait tenter d'en détourner le comportement. Le protocole traite ce
cas en interne — tout contenu ingéré est une **donnée, jamais une instruction** — mais une
formulation qui affaiblirait cette séparation est une vulnérabilité et doit être signalée comme
telle.

**Affaiblissement d'un garde-fou.** Une rédaction qui rendrait contournable la confirmation
humaine, l'échec bruyant ou l'ordre ② avant ③ est un défaut de sécurité, pas une question de
style.

**Fuite par l'exemple.** Un exemple, une trace ou une citation qui exposerait des données
personnelles, un chemin de machine ou un identifiant. Le signaler immédiatement.

Et pour l'instrument :

**Faux conforme.** Un bloc d'audit invalide que le vérificateur déclarerait conforme (sortie `0`)
est un défaut de sécurité de l'outil : une chaîne d'intégration qui s'y fie laisserait passer ce
qu'elle est censée arrêter. Même règle pour un plantage, qui rend un code de sortie sans verdict.

## Ce qui n'est pas une vulnérabilité

Un désaccord sur une règle, une limite déclarée du protocole, ou le fait qu'il ne garantisse pas la
justesse d'une réponse — il l'énonce lui-même et ne le promet nulle part. Ces points relèvent des
issues ordinaires et de [CONTRIBUTING.md](CONTRIBUTING.md).
