# Graphe V.8 — Couche ARCHIVE (détail, hors contexte)

> **Couche** : archive (consultée à la demande, jamais chargée en runtime). Source de la couche active.
> **Méthode** : passe fraîche Ax2 (Fork C), chaque couplage cité `module:ligne` sur `tj_v72/`.
> **Format unifié** (résout A4) : un seul format `source → cible · intensité · nature · inverse · réf.`.
> **Rendu HTML final** : optionnel, cosmétique (priorité basse, #11) — la donnée prime.

-----

## 1 · Inventaire typé complet

### Relations inter-pôles (socle V.8, portées par modules)

|Source → Cible|Int.|Nature      |Réf. porteur                                      |Inverse                     |
|--------------|----|------------|--------------------------------------------------|----------------------------|
|② → ③         |F   |conditionne*|F-04 `10_f04:437-438` + Lyra `04_lyra:218`        |③→② : `?`                   |
|① → ③         |Fn  |borne       |F-01 `05_f01:176`                                 |③→① : rétroagit (ci-dessous)|
|① → ②         |Fn  |**informe** |I-07 → PECU *(corrigé A1 : informe, pas alimente)*|②→① : `?`                   |
|③ → ①         |Fn  |rétroagit   |MECA `07_meca:178` + OFI                          |①→③ : = borne               |

* *②→③ est un invariant d’ordonnancement (contrainte de séquence), distinct d’un couplage de données — voir couche active.*

### Chaîne T2 (PADC-IA → F-04 → MECA)

|Source → Cible          |Int.|Nature  |Réf.                                |Inverse                                |
|------------------------|----|--------|------------------------------------|---------------------------------------|
|PADC-IA → F-04          |Fn  |alimente|`06_padc_ia:171`                    |F-04→PADC-IA : Fn alimente `10_f04:171`|
|F-04 → MECA             |Fn  |alimente|`10_f04:171`                        |MECA→F-04 : Fn rétroagit `07_meca:178` |
|MECA → T2 (authenticité)|Fn  |audite  |`MOTEUR_T2_V8 §6` (différé driver 2)|T2→MECA : alimente                     |

### Couche d’activation (MAMD / ACA / I-07)

|Source → Cible|Int.|Nature  |Réf.                         |Inverse                                                                         |
|--------------|----|--------|-----------------------------|--------------------------------------------------------------------------------|
|MAMD → ACA    |Fn  |alimente|`16_mamd:204` + `17_aca:214` |ACA→MAMD : **F** alimente `17_aca:425`                                          |
|MAMD → MEDA   |F   |alimente|`16_mamd:204,430`            |MEDA→MAMD : `?`                                                                 |
|MAMD → F-04   |F   |alimente|`16_mamd:360`                |F-04→MAMD : Fn rétroagit                                                        |
|ACA → F-04    |Fn  |active  |`17_aca:437-438`             |F-04→ACA : `?`                                                                  |
|ACA → F-03    |Fn  |active  |`17_aca:443`                 |F-03→ACA : `?`                                                                  |
|ACA → Lyra    |Fn  |active  |`17_aca:449`                 |Lyra→ACA : `?`                                                                  |
|ACA ↔ MEDA    |Fn  |active  |`17_aca:431`                 |bidirectionnel partiel                                                          |
|I-07 → Noyau  |F   |audite  |`13_i07:247` + `01_noyau:509`|Noyau→I-07 : F conditionne `01_noyau:510` **(terminateur : acte Noyau tranche)**|
|I-07 ↔ I-05   |Fn  |informe |`11_i05:169`                 |symétrique (veille interne/externe)                                             |

### Lignes legacy sortantes (vérifiées)

Lyra → {F-04, F-01, MECA, MEDA, EXT-01, EXT-02} `04_lyra:219` (alimente) · F-01 → {Noyau, MECA, PADC-IA(active), F-02(active), EXT-02} `05_f01:176` · F-03 → {MECA, F-02(active), F-04} `09_f03:178` · F-04 → {PADC-IA, Lyra(rétroagit), F-03, MECA, EXT-02} `10_f04:171` · MECA → {F-04, F-03, F-02→OFI} `07_meca:178` (rétroagit) · EXT-02 → {Agent technique(active), MECA, F-01, F-02(active)} `14_ext02:225`.

## 2 · Rétroactions (cartographiées pour la 1re fois)

F-04→MAMD (re-signature) · MECA→OFI→production (relance) · A2→INV.5 (arrêt) · ③→① (réexamen) · capacité défaillante→SONDE (re-sonde). Réf. détaillées dans `AX2_COUPLAGES §5`.

## 3 · Matrice — état d’honnêteté (résout A2)

380 couplages possibles (20×20 − diagonale ; 20 nœuds depuis l'ajout de SONDE). Documentés : ~26 legacy + ~34 typés cette passe. **Reste (~280-300) = `?` (non documenté)**, PAS `L` vérifié. La matrice legacy se présentait comme complète en documentant <8 % — conflation corrigée.

## 4 · Anomalies Ax2 — résolution dans ce module

- **A1** (informe ∉ natures) → **résolu** : 7ᵉ nature ajoutée ; `①→②` reclassé `informe`.
- **A2** (conflation L) → **résolu** : sémantique `L`/`?` appliquée ; reste = `?`.
- **A3** (②→③ non encodé) → **partiel** : la chaîne active référence le gate ; l’**invariant** lui-même s’inscrit dans Noyau V.8 + F-04/Lyra (différé à leur construction).
- **A4** (deux formats) → **résolu** : format unique adopté ici.
- **Challenge relecture (②→③ marqué F)** → résolu : noté comme contrainte de séquence distincte.
- **Challenge relecture (boucle I-07↔Noyau F↔F)** → résolu : terminateur explicite (l’acte Noyau tranche).

## 5 · Décisions de construction (pilote)

- Coupe actif/archive : **vue dynamique + couplages F → actif** ; **inventaire complet + matrice + citations → archive**. Plancher auto-cohérence respecté (l’actif contient la chaîne + le squelette F + les relations de pôles).
- `Fn` par défaut, `F` réservé aux dépendances structurelles attestées (validé relecture).
- Inverse non attesté → `?` (jamais inventé).

-----

*Module pilote — valide : coupe actif/archive · format MD · traçabilité · résolution d’anomalies. NE valide PAS : schéma AMORCE→PROCESSUS→SORTIE (le Graphe est consulté, non « déclenché ») → un pilote behavioral (ex. F-04) reste nécessaire pour cette convention.*