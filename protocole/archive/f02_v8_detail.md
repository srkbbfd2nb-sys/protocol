# F-02 V.8 — Couche ARCHIVE (détail, hors contexte)

> Source de la couche active. Citations `module:ligne` sur `tj_v72/08_f02`. Passe fraîche.

## 1 · Statut dormant (`08_f02:42-46`)
Encadré dormant explicite dans le legacy : F-02 ne s'exécute pas par défaut. Signaux d'éveil = escalade (voir AMORCE actif). Coût nul hors escalade — cohérent S4.

## 2 · Pipeline & OFI (`08_f02:49-85`)
Pipeline visuel 8 étapes ; F-03 invoqué en étape 5. **OFI** (Orchestration-Feedback-Itération) : MECA rejette → F-02 relance la production avec ajustements, itérations bornées ; rapport OFI final. C'est la ré-entrée `MECA→OFI→production` de la chaîne canonique.

## 3 · MAO & registre (`08_f02:87-106`)
Régimes MAO (configuration par system prompt/API — profil de déploiement). Registre des invocations : champs horodatés, exportable API/LAB, application d'INV.8 (traçabilité proportionnelle à l'autonomie).

## 4 · Complémentarité ACA / F-02
ACA = activation contextuelle **par cycle** (signature MAMD, léger). F-02 = orchestration **globale multi-modules** (escalade, lourd). Pas de recouvrement : ACA décide *qui s'active*, F-02 décide *dans quel ordre et avec quels paramètres* quand le pipeline complet est requis.

## 5 · Couplages (`08_f02:198-199`)
REÇOIT : Noyau (escalade, fail_safe) · MEDA (Expert/≥5, EEO) · F-01 (MRS ≥ 9, critique 6-8) · MEDA/DVS (dérive) · MECA (rejet) · system prompt/API (MAO). ENVOIE : tous modules actifs (ordre, profondeur, EEO) · MECA (fin pipeline + OFI) · Utilisateur (ORCHESTRATION ACTIVE, registre, rapport OFI) · API/LAB (log INV.8).

## 6 · Décisions de construction
- **Méta-infrastructure** (correction cycle 22) : F-02 orchestre, ne produit ni ne juge — aucun pôle défendable.
- **AMORCE explicitée** (M0 P3 : « quand F-02 escalade ? » était implicite) : liste fermée de signaux d'éveil, sinon dormant.
- **Coupe S4** : amorce d'escalade + OFI + couplages → actif ; pipeline détaillé + MAO + registre → archive.

*Module méta-infrastructure V.8 (dormant sauf escalade). Vague 2.*
