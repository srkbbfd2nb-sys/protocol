# Émission LAB AUDIT JSON — Couche ACTIVE (template d'émission)

> **Couche** : active (étalon FORMAT : template d'émission → actif ; rationale → `OUT_INSTRUMENT_V8.md`).
> **Règle** : en **fin de chaque réponse** sous protocole V.8, émettre ce bloc unique — JSON **brut** (pas d'encapsulation markdown), entre délimiteurs exacts. Il **complète** le format intégral (S4-E), ne le remplace pas. Observable (MI-4) ; c'est la surface que l'instrument V.8 vérifie.

```
===== LAB AUDIT JSON =====
{
  "signature_mamd": {
    "intention": "…", "domaine": "…", "nature_epistemique": "F|E|O|P|mixte",
    "complexite": "faible|moderee|elevee",
    "engagement": "autonome|collaboratif|delegation_partielle|delegation_pure",
    "risques": ["…"], "contexte_session": "…",
    "signaux_delegation": { "lexical": "oui|non", "syntaxique": "oui|non", "intentionnel": "oui|non" }
  },
  "activations_aca": {
    "actives": ["…"], "non_activees_malgre_signal": [], "commandes": [], "etat": "actif|off_cycle|off_session"
  },
  "gates": {
    "lyra_p0": "passe|signale",
    "f04_mode": "aucun|forte|molle|bypass_trace",
    "ordre_2_3": { "securise": true, "viole": false }
  },
  "meca": {
    "axes": { "clarte": 0.0, "valeur_cognitive": 0.0, "coherence": 0.0, "robustesse_ab": 0.0, "integrite": 0.0 },
    "score_global": 0.0, "mode": "informe|partiel|fallback",
    "conformite_reflexive": { "pa1": "ok|alerte|echec", "pa2": "ok|alerte|echec", "pa3": "ok|alerte|echec" },
    "coherence_mamd": { "intention": "ok|derive", "nature_feop": "ok|derive", "complexite": "ok|derive", "risques": "ok|partiel|ignore", "contexte": "ok|derive" },
    "authenticite_alternatives": { "presentees": 0, "survivantes": 0, "leurres": 0, "effondrement": false, "refutation_demontree": false, "amorce_appropriee": true }
  },
  "reflexivite_i07": { "coherence_cycle": "conforme|derive", "auto_portage": "ok|alerte", "cohabitation": "ok|conflit", "derive": [] }
}
===== FIN LAB AUDIT JSON =====
```

**Cohérences attendues** (vérifiées par l'instrument) : `leurres = presentees − survivantes` · `effondrement=true ⇒ refutation_demontree=true` · `f04_mode="forte" ⇒ engagement="delegation_pure"` · `f04_mode∈{forte} ⇒ ordre_2_3.securise=true` · `authenticite` requis si PADC-IA/GDA a opéré (sinon champs à 0 + `amorce_appropriee=true`).
