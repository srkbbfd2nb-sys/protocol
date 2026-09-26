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

**La validité du bloc**, contre un schéma publié :
[`schema/lab_audit_v8.schema.json`](schema/lab_audit_v8.schema.json), transcription du template
d'émission — types, plages (les axes dans [0, 1]), énumérations, champs requis. Un test vérifie que
le schéma et le template ne divergent pas. Le validateur est écrit à la main, bibliothèque standard
seule, et **refuse de charger** un schéma qui emploierait un mot-clé qu'il n'applique pas : il ne
peut pas promettre une contrainte qu'il ne vérifie pas. Le schéma reste du JSON Schema standard,
rejouable avec n'importe quel validateur conforme.

**La présence et la complétude** des cinq sections — c'est ce que mesure le score structurel.
Présence et validité sont deux contrôles distincts : un bloc peut être complet et faux.

**Les cohérences arithmétiques** — celles qui ne demandent pas de relire le texte :

| Règle | Ce qu'elle attrape |
|---|---|
| `leurres = présentées − survivantes` | un comptage d'alternatives qui ne se tient pas |
| `effondrement ⇒ réfutation démontrée` | un effondrement déclaré sans la réfutation qui le justifie |
| `maïeutique forte ⇒ engagement = délégation pure` | un gate déclenché sans son motif |
| `maïeutique forte ⇒ ordre ②→③ sécurisé` | une maïeutique forte qui laisserait produire |
| `ordre_2_3.viole = false` | une production lancée avant la sécurisation de la souveraineté |
| `score_global = somme des axes × 0,20` | un score global qui ne découle pas des axes annoncés |

La dernière règle vient du module MECA (5 axes, ×0,20 chacun, arrondi à deux décimales). Sa
tolérance, 0,005, n'est pas un seuil choisi : c'est l'erreur maximale d'un arrondi à deux décimales.
Une règle ne s'évalue que si ses champs ont le bon type ; sinon c'est le schéma qui porte l'échec,
et l'instrument ne plante pas.

**Le délimiteur**, avec une tolérance de transition `(?:LAB|TJ)` : une session tournant encore sur
l'ancien nom reste lisible. Refuser l'ancien jeton ne lèverait pas d'erreur — la lecture
basculerait en silence sur l'heuristique de repli, et une dégradation silencieuse est le mode
d'échec le plus coûteux du dispositif.

**Le repli lui-même** — un bloc trouvé *sans* délimiteurs — est lu, pour que le rapport reste utile,
mais il ne sort **jamais** en `0` : le contenu peut être complet, la réponse ne respecte pas le
contrat d'émission.

## Codes de sortie

| Code | Sens |
|---|---|
| `0` | conforme — délimiteurs présents, schéma valide, aucune cohérence violée |
| `1` | non conforme — violation de schéma, cohérence violée, section manquante, ou bloc extrait par repli |
| `2` | inexploitable — bloc absent, JSON illisible ou qui n'est pas un objet, fichier introuvable |

Le rapport imprimé se termine par une ligne `CONFORMITÉ`, qui lit la même fonction que le code de
sortie : les deux ne peuvent pas se contredire.

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

26 tests sur 9 fixtures : extraction, tolérance de l'ancien jeton, bloc absent, JSON invalide,
cohérence violée, dégradation du score, codes de sortie, bout en bout par la ligne de commande,
reproductibilité du verdict — et, depuis la seconde revue externe, la **validité** : repli sans
délimiteurs, axe hors plage, énumération inconnue, score global incohérent, section entière absente,
comptes mal typés, concordance schéma ↔ template. Chacun de ces derniers cas sortait en `0` ou
faisait planter l'instrument avant correction. Un clone nu suffit à les faire tourner.
