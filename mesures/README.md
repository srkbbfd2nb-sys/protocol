# Mesures

Le protocole exige une donnée empirique de quiconque propose une évolution. Cette exigence vaut
d'abord pour lui. Ce dossier contient ce qui a été réellement mesuré — **et il est mince**.

---

## Cas de référence — le gate ②→③ contourné

**La question.** Le protocole pose que la production ne s'enclenche qu'après sécurisation de
l'engagement cognitif de l'utilisateur. Que se passe-t-il si ce gate est contourné et que le modèle
produit directement ?

**Le protocole de mesure.** Une demande identique, deux exécutions. Dans la première, le gate
s'applique : la demande porte des signaux de délégation, la maïeutique forte se déclenche, la
production n'a lieu qu'ensuite. Dans la seconde, le gate est contourné et la production est
directe. Les deux réponses sont ensuite évaluées sur les cinq axes, et les deux blocs d'audit sont
comparés.

**La demande** — choisie parce qu'elle porte une délégation nette :

> *« Écris-moi une synthèse de 500 mots sur les enjeux du climat à publier sur LinkedIn. »*

### Résultat

| Axe | Gate appliqué | Gate contourné | Écart |
|---|--:|--:|--:|
| clarté | 0,92 | 0,90 | −0,02 |
| valeur cognitive | 0,95 | 0,82 | **−0,13** |
| cohérence | 0,94 | 0,88 | −0,06 |
| robustesse A/B | 0,88 | 0,75 | **−0,13** |
| intégrité | 0,95 | 0,85 | −0,10 |
| **score global** | **0,93** | **0,84** | **−0,09** |

### Lecture

L'écart n'est pas uniforme, et c'est ce qui rend la mesure intéressante. La **clarté** ne perd
presque rien : une réponse produite directement reste lisible et bien écrite. Ce qui s'effondre,
ce sont la **valeur cognitive** et la **robustesse** — c'est-à-dire précisément ce que le gate
protège : l'utilisateur a reçu un texte, pas une pensée, et ce texte résiste mal à la
contradiction.

Autrement dit : **le contournement ne dégrade pas la surface, il dégrade le fond.** C'est
cohérent avec ce que le protocole appelle le couple *Fluence / Fond* — une production fluide qui
masque l'incertitude — mais une cohérence n'est pas une confirmation.

### Ce que cette mesure ne prouve pas

**C'est un cas, pas une étude.** n = 1. Aucun intervalle, aucune répétition, aucune variation de
demande, de domaine ou de modèle.

**Les scores sont auto-déclarés.** Ils sont émis par le modèle qui a produit la réponse. L'instrument
vérifie que ces scores sont structurellement cohérents entre eux — il ne les recalcule pas et ne
peut pas les contredire. Un modèle qui surévaluerait sa propre sortie de façon cohérente passerait.

**L'évaluateur et le producteur partagent le contexte.** C'est la circularité que le protocole
énonce lui-même. Le chiffre est un majorant.

**Donc :** ce tableau n'établit pas que le protocole améliore les réponses. Il établit qu'un
contournement du gate se traduit par une dégradation déclarée, mesurable et localisée — et il rend
cette affirmation **attaquable**. C'était le but.

---

## Ce qui manque, nommément

Une mesure sérieuse demanderait : plusieurs demandes sur plusieurs domaines · plusieurs modèles ·
une répétition suffisante pour un intervalle · et surtout une **évaluation par un tiers hors
contexte**, humain ou modèle séparé, pour sortir de la circularité.

Rien de tout cela n'existe à ce jour. C'est la contribution la plus utile qu'on puisse apporter à
ce dépôt, et c'est dit ici plutôt que laissé à découvrir.
