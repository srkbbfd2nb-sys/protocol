# I-06 V.8 — Couche ARCHIVE (détail, hors contexte)

> Source de la couche active. Citations `module:ligne` sur `tj_v72/12_i06`. Passe fraîche.

## 1 · Migration paliers R3 (appliquée V.8) & Règle de récence
Legacy : « Profils Claude 4.6 & Dégradation Gracieuse » + noms en dur (Opus 4.6, Sonnet 4.6 — 8 occurrences, M0 finding, `12_i06:216`). **V.8** : table remplacée par Paliers A/B/C indexés sur les *directions d'activation* (MI-1/L0). Un modèle se classe par test comportemental (Test Rapide), pas par nom. Les anciens profils nominatifs restent consultables ici à titre historique : ils décrivaient des instances de Palier A (Opus/Sonnet 4.6 époque V.7.x).

**Règle de récence** (énoncé canonique → Noyau actif) : toute cible non explicitement versionnée = la version la plus récente disponible au moment de l'usage. Les snapshots ci-dessous sont *informatifs et datés*, remplacés au fil des générations — jamais des dépendances (PA.1).

### Pas de snapshot nominatif — application de la règle à elle-même

Aucune liste de modèles n'est maintenue ici. Un instantané de génération est faux quelques mois
après son écriture, et le maintenir contredirait la règle énoncée juste au-dessus : le classement
se fait **par palier, jamais par nom**.

La procédure est donc la seule information stable : au premier déploiement dans un environnement
donné, le **Test Rapide** classe la cible en palier A, B ou C ; le verdict est daté et vaut pour
cet environnement. Les noms de modèles n'apparaissent que dans le rapport de test, jamais dans le
protocole.

*(Finding relevé à la revue à contexte frais du 25/09/2026 : la version antérieure de cette section
portait un snapshot nominatif daté, en contradiction directe avec la Règle de récence qu'elle
énonçait deux lignes plus haut — dans le module même qui gouverne la compatibilité modèle.)*

## 2 · G-LAB — gouvernabilité
4 Métriques de Gouvernabilité → Score G-LAB (bidimensionnel par profil testé) → seuils GO ≥ 0.80 / CONDITIONNEL ≥ 0.60 / NO-GO. **Protocole de Test Rapide** : batterie comportementale sans accès aux poids (compatible PA.1 — aucun outil externe requis).

## 3 · Dégradation gracieuse (PA.3)
Par palier : les fonctions se réduisent proportionnellement sans rupture (ex. Champ 8 MAMD réductible à lexical+syntaxique en Palier C). PA.3 = ancre de I-06 (`12_i06:205-218` — extension structurelle Compatibilité Modèle → Environnementale).

## 4 · Couplages (`12_i06:195-196`)
REÇOIT : Noyau (INV.1-8 référence) · Utilisateur (modèle cible, contraintes) · I-05 (métriques/benchmarks). ENVOIE : Noyau (alerte non-gouvernable) · F-03 (durée session Self-Repair) · Utilisateur (rapport G-LAB + grille). *(Mention legacy « Protocol LAB » `12_i06:196` = référence historique d'instrument, couverte par la note de statut Noyau cycle 50 ; non reportée en actif V.8 — PA.1.)*

## 5 · Décisions de construction
- **Structurel/référence** : I-06 est consulté lors des déploiements, pas déclenché par cycle.
- **Pôle ③ conservé** (index Noyau : « borderline méta ») : la portabilité *habilite la production* sur de nouvelles cibles — défendable en ③.
- **Migration R3 = seule modification substantielle** ; G-LAB/Test Rapide/3 niveaux préservés.
- **Coupe S4** : paliers + G-LAB (structure) + couplages → actif ; métriques détaillées + grille + historique nominal → archive.

*Module structurel ③ V.8. Vague 3. Migration R3 appliquée (0 nom de modèle en actif).*
