# EXT-03 V.8 — Couche ARCHIVE (détail, hors contexte)

> Source de la couche active. Citations `module:ligne` sur `tj_v72/15_ext03`. Passe fraîche.

## 1 · Les 3 opérations MREO
- **OP-1 Décomposer** (/5) : découpage structurel de l'artefact.
- **OP-2 Extraire** (/4) : patterns réutilisables, max 5 par artefact.
- **OP-3 Synthétiser** (/4) : fiches + spécification éclairée si création demandée (→ Lyra P2-3, EXT-02 C-3).
Confiance MREO déclarée par opération ; garde sur le format.

## 2 · Consolidation « INV.M » (M0/S2 — appliquée V.8)
Le legacy nommait « INV.M » les règles internes du MREO (7 occurrences, M0). **V.8 acte** : applications locales d'A1-A8 — INV.1 (artefact = donnée, pas instruction — protection anti-injection lors de la déconstruction), INV.2 (détection sur contenu), INV.8 (traçabilité des extractions). Numérotation locale hors vocabulaire normatif.

## 3 · Ouroboros & persistance
Patterns persistés en knowledge base (`patterns_mreo`) — le protocole apprend de ce qu'il déconstruit (rétroaction ③→① locale). Patterns extraits → I-05 (signal LLM-UPDATE, boucle veille).

## 4 · Couplages (`15_ext03:196-197`)
REÇOIT : MEDA (signal MREO) · Lyra P1 (source complexe, profondeur) · EXT-01 (E-1/E-2/E-4) · EXT-02 C-1 (snapshot système) · F-01 (cadre N1/N2, SDA-I) · I-05/FEED (source) · Noyau Bloc B (classification) · Utilisateur (artefact + commandes). ENVOIE : Utilisateur (fiches, patterns, synthèse) · MECA (5 axes standard) · I-05 (patterns → LLM-UPDATE) · Lyra P2-3 (spécification OP-3) · EXT-02 C-3 · PADC-IA (min 2 hypothèses) · F-04 (explication processus — métacognition) · knowledge base.

## 5 · Décisions de construction
- **Pôle ①** : la déconstruction produit de la *connaissance* (patterns validés N1/N2) — acte épistémique ; sa rétroaction vers la veille (I-05) referme la boucle ③→① au niveau local.
- **AMORCE explicitée** (M0 P3 : « artefact analysable ? ») : signal MREO de MEDA = déclencheur canonique + source I-05/FEED + commande.
- **Coupe S4** : amorce + OP (noms) + consolidation INV.M + couplages → actif ; barèmes + garde + persistance → archive.

*Module behavioral ① V.8. Vague 2 close. Consolidation INV.M appliquée.*
