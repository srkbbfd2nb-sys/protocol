# Glossaire

Les **codes de modules sont des noms propres** : ils identifient des nœuds d'un graphe et
apparaissent dans les couplages, dans le bloc d'audit et dans les tests. Ils ne se traduisent ni ne
se renomment. Ce qui se développe, c'est leur signification — une fois, ici.

---

## Modules

| Code | Développement | Ce qu'il fait |
|---|---|---|
| **SONDE** | *(mot conservé — un* sonde *est aussi, en anglais, un instrument envoyé dans un milieu pour mesurer et rendre compte)* | établit l'environnement avant la demande : inventorie les capacités, les éprouve, les classe `vérifié` / `déclaré` / `absent`, arme les garde-fous |
| **MAMD** | Module Analyse Multi-Dimensionnelle | signe chaque demande sur 8 champs, dont l'engagement de l'utilisateur et les signaux de délégation |
| **ACA** | Activation Contextuelle Automatique | décide quels modules activer et à quel niveau ; n'altère jamais leur contenu |
| **Lyra** | *(nom propre)* | gate P0 et structuration en 5 phases ; porte l'autorité éthique, non désactivable |
| **MEDA** | Module d'Évaluation Dialectique et Adaptative | route la demande : score sur 8 dimensions → niveau Light / Complet / Expert |
| **PADC-IA** | Protocole Anti-Dépendance Cognitive — Intelligence Artificielle | génère des alternatives réelles, élimine les leurres, compte honnêtement |
| **GDA** | Génération Divergente Authentifiée | le mécanisme porté par PADC-IA : produire les candidats *avant* de juger |
| **F-01** | *(module fusionné)* | vigilance épistémique : trace la chaîne inférentielle, mesure l'incertitude |
| **F-02** | *(module fusionné)* | orchestration ; dormant sauf escalade |
| **F-03** | *(module fusionné)* | intégrité de réponse, anti-fluence : 5 familles de défauts |
| **F-04** | *(module fusionné)* | souveraineté : détecte la délégation, expose les alternatives, applique le gate ②→③ |
| **MECA** | Moteur d'Évaluation Cognitive Adaptative | audite la sortie sur 5 axes et émet le bloc JSON |
| **MREO** | Module Reverse Engineering Opérationnel | déconstruit un artefact : décomposer, extraire, synthétiser |
| **EXT-01** | *(extension)* | modélise le système réel : entités, causalité, dynamique, prédiction |
| **EXT-02** | *(extension)* | gouverne les actions techniques : périmètre, spécification, garde-fous, vérification |
| **EXT-03** | *(extension)* | porte MREO |
| **I-05** | *(instrument)* | veille externe ; **propose** des mises à jour, ne les applique jamais seul |
| **I-06** | *(instrument)* | compatibilité : classe un environnement en palier A / B / C |
| **I-07** | *(instrument)* | réflexivité méthodologique : mesure l'écart entre le protocole **déclaré** et le protocole **exécuté** |
| **Noyau** | — | invariants, pôles, méta-principe |
| **Graphe** | — | référence structurelle des couplages |
| **Framework** | — | validation par couches, en campagne de test |

## Notions et métriques

| Sigle | Développement | Ce que c'est |
|---|---|---|
| **PECU** | Préservation Engagement Cognitif Utilisateur | le pôle ② : le protocole amplifie la pensée de l'utilisateur, ne s'y substitue pas |
| **INV.1–8** | Invariants | 8 règles qui limitent les **capacités**, pas seulement les intentions |
| **MI-1–5** | Méta-Invariants | 5 garanties qui surplombent les invariants et prévalent en cas de contradiction |
| **PA.1–3** | Principes Architecturaux | indépendance · auto-portage · compatibilité environnementale |
| **SDA-I** | *indice d'incertitude, sur 12* | 4 régimes, de Standard à Suspension |
| **MRS** | Mode de Réponse Suspendue | le régime le plus haut de F-01 : on ne produit pas |
| **G-LAB** | indice de **G**ouvernabilité | mesure à quel point une cible est gouvernable *par* le protocole ; macro ≥ 0,80, micro en dessous |
| **ESP** | Échelle de Sensibilité Pédagogique | 4 profils cognitifs ; pilote seuils, profondeur et verbosité |
| **PAH-R** | Protocole d'Analyse Hiérarchisée du **R**aisonnement | 6 phases de traçage de la chaîne inférentielle |
| **AED** | **A**lternatives par **É**valuation **D**ifférentielle | génère des variantes quand le score de sortie passe sous le seuil |
| **OPQ** | **O**bjectif / **P**roblématique / **Q**uestion | optimise la **demande** |
| **O/H/C** | **O**bjectif / **H**ypothèses / **C**ritères | engage la **pensée de l'utilisateur** — à ne jamais confondre avec OPQ |
| **OFI** | *(sigle opaque — glose : boucle d'optimisation itérative)* | relance bornée de la production après un rejet. La glose décrit la fonction ; ce n'est **pas** une expansion des initiales |
| **MAO** | *(sigle opaque — aucun développement écrit)* | les 3 régimes d'autonomie de F-02 |
| **EEO** | Extension d'Exécution Opérationnelle | mode de production soutenue |
| **CCR** | Coût Cognitif Requis | — |
| **MEX** | *(arbre décisionnel)* | structuration de choix, composant de F-04 |
| **DVS** | *(détection hors-domaine)* | signal de dérive |
| **FEED** | Flux d'Entrée Externe Dirigé | *(l'anglais* feed *dit exactement la même chose — coïncidence conservée)* |
| **F/E/O/P** | Fait / Estimation / Opinion / Prédiction | marqueurs de nature d'une affirmation |
| **N1/N2/N3** | niveaux de validité | force de l'appui d'une affirmation |
| **S4-E** | — | la règle de format intégral : on ne résume pas, on divulgue progressivement |

---

**Deux sigles opaques, par décision d'auteur (26 septembre 2026).** `MAO` n'a jamais reçu de
développement écrit ; le développement de `OFI` ne correspond pas à ses initiales. Plutôt que de
combler l'un ou de forcer l'autre, les deux sont déclarés **noms propres** : le code identifie, la
colonne « ce que c'est » décrit. Inventer une signification plausible aurait été exactement le genre
de faux qu'un protocole d'honnêteté épistémique doit refuser — et la retrouver, s'il en existe une,
ne changerait rien à ce que ces modules font.
