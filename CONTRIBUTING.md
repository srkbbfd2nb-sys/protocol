# Contribuer

Ce protocole est **intrinsèquement collaboratif**. Il ne progresse pas par accumulation de
fonctionnalités mais par **confrontation** : les retours négatifs, les erreurs relevées, les
incohérences, les cas où il échoue sont ce qui le fait avancer. Un contre-exemple vaut mieux qu'un
ajout.

## La règle qui encadre toute évolution

**Aucun durcissement ni assouplissement sans donnée empirique.**

Une proposition appuyée sur une mesure — un cas reproductible, un comptage, une comparaison avant
et après — a un chemin. Une intuition seule n'en a pas. Ce n'est pas de la défiance : c'est la
seule façon de savoir qu'un changement améliore quelque chose plutôt que de déplacer le problème.

Quatre règles ne relèvent pas de cette clause et ne s'assouplissent pas : la décision assistée, la
confirmation humaine, l'échec bruyant et la traçabilité proportionnelle. Elles sont strictement
restrictives.

## Ce qui est le plus utile

**Une contradiction.** Deux endroits du protocole qui ne peuvent pas être vrais en même temps.
Indiquer les deux, et pourquoi ils s'opposent.

**Un contre-exemple.** Un cas où une règle produit un résultat que le protocole condamne par
ailleurs. Donner la demande, le comportement observé, le comportement attendu.

**Un faux positif ou un faux négatif.** Le dispositif se déclenche là où il ne devrait pas, ou
reste muet là où il devrait parler.

**Un défaut de portabilité.** Le protocole se comporte différemment selon l'hôte ou le modèle.
Préciser lequel, et en quoi.

**Une proposition d'évolution avec sa donnée.** L'argument compte moins que la mesure qui
l'appuie.

## Ce qu'une bonne remontée contient

La demande exacte, ce que le protocole a produit, ce qui était attendu, et — si possible — le bloc
d'audit JSON émis en fin de cycle. Ce bloc porte plusieurs cohérences vérifiables mécaniquement ;
il rend un rapport bien plus exploitable qu'une description.

## Ce qui ne se modifie pas par contribution

L'ordre **② avant ③**, les quatre invariants strictement restrictifs, et l'archive des versions
antérieures. Réécrire un document daté falsifierait une mesure ; l'archive se cite, elle ne se
corrige pas.

## Langue

Le français est la langue source. Les remontées en anglais sont les bienvenues.
