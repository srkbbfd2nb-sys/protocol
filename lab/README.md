# LAB — l'instrument

La moitié qui vérifie. Le protocole affirme ; cet outil contrôle qu'une réponse produite sous
protocole respecte le contrat qu'elle prétend respecter.

```bash
python lab/audit_v8.py --input-file reponse.txt
```

Pas de clé, pas de compte, pas de serveur, aucune dépendance : bibliothèque standard seule.
Colle une réponse dans un fichier, lance la commande, obtiens un verdict.

## Pourquoi il est *hors* de la boucle

Ce n'est pas une économie d'infrastructure, c'est une contrainte du protocole lui-même :

> Une métrique dérivée de la structure qu'elle évalue est un majorant, jamais une validation.
> Un auditeur logé dans le même contexte que le producteur mesure sa propre cohérence, pas sa
> justesse.

Un vérificateur intercalé dans la boucle de génération partagerait ce contexte — il hériterait
exactement du biais qu'il est censé détecter. L'instrument lit donc une **trace**, après coup,
depuis l'extérieur. C'est la revue à contexte frais, appliquée à la machine.

## Ce qu'il vérifie

**La présence et la complétude** des cinq sections du bloc d'émission.

**Les cohérences arithmétiques** — celles qui ne demandent pas de relire le texte :

| Règle | Ce qu'elle attrape |
|---|---|
| `leurres = présentées − survivantes` | un comptage d'alternatives qui ne se tient pas |
| `effondrement ⇒ réfutation démontrée` | un effondrement déclaré sans la réfutation qui le justifie |
| `maïeutique forte ⇒ engagement = délégation pure` | un gate déclenché sans son motif |
| `ordre_2_3.viole = false` | une production lancée avant la sécurisation de la souveraineté |

**Le délimiteur**, avec une tolérance de transition `(?:LAB|TJ)` : une session tournant encore sur
l'ancien nom reste lisible. Refuser l'ancien jeton ne lèverait pas d'erreur — la lecture
basculerait en silence sur l'heuristique de repli, et une dégradation silencieuse est le mode
d'échec le plus coûteux du dispositif.

## Codes de sortie

| Code | Sens |
|---|---|
| `0` | conforme |
| `1` | non conforme — section manquante ou cohérence violée |
| `2` | bloc absent ou illisible |

Un instrument qui rend toujours `0` est un rapport, pas un garde-fou : aucune chaîne d'intégration
ne peut s'y brancher.

## Ce qu'il ne vérifie pas — et c'est le point important

Il lit **ce que le modèle a déclaré de lui-même**. Il contrôle la conformité et la cohérence
interne d'une auto-déclaration, **pas sa véracité**. Vérifier que `1 = 3 − 2` prouve que le compte
se tient, pas que trois alternatives ont réellement été explorées. **Un modèle qui mentirait de
façon cohérente passerait.**

C'est la limite fondamentale de l'instrument dans son état actuel, elle est connue, et elle est le
prochain chantier du projet — pas un détail à contourner.

## Tests

```bash
python -m pytest lab/tests/ -q
```

Onze tests sur six fixtures : extraction, tolérance de l'ancien jeton, bloc absent, JSON invalide,
cohérence violée, dégradation du score, codes de sortie, bout en bout par la ligne de commande, et
reproductibilité du verdict. Un clone nu suffit à les faire tourner.
