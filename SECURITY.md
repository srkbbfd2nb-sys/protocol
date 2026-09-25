# Politique de sécurité

## Signaler une vulnérabilité

Utiliser **Private vulnerability reporting** (onglet *Security* du dépôt). Cela permet de décrire
le problème sans le rendre public le temps qu'il soit traité.

Ne pas ouvrir d'issue publique pour une vulnérabilité exploitable.

## Périmètre

Ce dépôt ne contient **que du texte** : des fichiers Markdown décrivant un protocole. Aucun code
exécutable, aucune dépendance, aucun service. La surface d'attaque classique — exécution, chaîne
d'approvisionnement, secrets — est donc absente par construction.

Ce qui reste pertinent :

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

## Ce qui n'est pas une vulnérabilité

Un désaccord sur une règle, une limite déclarée du protocole, ou le fait qu'il ne garantisse pas la
justesse d'une réponse — il l'énonce lui-même et ne le promet nulle part. Ces points relèvent des
issues ordinaires et de [CONTRIBUTING.md](CONTRIBUTING.md).
