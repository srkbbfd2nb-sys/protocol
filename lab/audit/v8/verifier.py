"""
Instrument V.8 — Vérificateur structurel du bloc LAB AUDIT JSON.
===============================================================
Par section : présence (0.4) + complétude (0.4) + cohérence (0.2) → [0,1].
Global pondéré : signature .20 · activations .15 · gates .20 · meca .30 · i07 .15.
Verdict : STRUCTURE >= .75 · PARTIEL >= .40 · NON-STRUCTURE.

Les cohérences vérifiées sont STRUCTURELLES (invariants inter-champs déclarés
dans emission_audit_v8.md) — jamais un jugement sémantique du contenu.

Deux contrôles distincts, qui ne se remplacent pas :
  - le score mesure la **présence** des champs (inchangé depuis la mesure publiée) ;
  - la validation de schéma contrôle leur **validité** : types, plages, énumérations.
Un bloc peut être complet et faux : c'est la validation qui l'attrape.
"""

from audit.v8.validation import charger_schema, valider

# score_global = somme des 5 axes pondérés ×0,20, arrondie à deux décimales
# (tj_v72/07_meca:285 et :500 — la fiche V.8 dit « somme pondérée » sans les poids).
# La tolérance n'est pas un seuil empirique : c'est l'erreur maximale d'un arrondi
# à deux décimales (0,005), plus une marge de représentation flottante.
POIDS_AXE = 0.20
TOLERANCE_SCORE_GLOBAL = 0.005 + 1e-9

PONDERATIONS = {
    "signature_mamd": 0.20,
    "activations_aca": 0.15,
    "gates": 0.20,
    "meca": 0.30,
    "reflexivite_i07": 0.15,
}

CHAMPS_REQUIS = {
    "signature_mamd": ["intention", "domaine", "nature_epistemique", "complexite",
                       "engagement", "risques", "contexte_session", "signaux_delegation"],
    "activations_aca": ["actives", "non_activees_malgre_signal", "commandes", "etat"],
    "gates": ["lyra_p0", "f04_mode", "ordre_2_3"],
    "meca": ["axes", "score_global", "mode", "conformite_reflexive",
             "coherence_mamd", "authenticite_alternatives"],
    "reflexivite_i07": ["coherence_cycle", "auto_portage", "cohabitation", "derive"],
}

AXES_MECA = ["clarte", "valeur_cognitive", "coherence", "robustesse_ab", "integrite"]


def verifier(data):
    """Retourne le rapport structurel complet (dict)."""
    if not isinstance(data, dict):
        return {"score_global": 0.0, "verdict": "NON-STRUCTURE", "exploitable": False,
                "sections": {}, "coherences": [], "violations_schema": [],
                "notes": ["bloc absent ou non parsable"]}

    sections, notes = {}, []
    violations_schema = valider(data, charger_schema())
    non_declarees = [k for k in data if k not in PONDERATIONS]
    if non_declarees:
        notes.append("section(s) non déclarée(s) au template, admises sans contrôle : "
                     + ", ".join(non_declarees))
    for nom in PONDERATIONS:
        sections[nom] = _score_section(nom, data.get(nom))

    coherences = _coherences(data, notes)
    for echec in coherences:
        if not echec["ok"]:
            sec = echec["section"]
            if sec in sections:
                sections[sec]["details"].append("coherence: " + echec["regle"] + " VIOLEE")

    score_structurel = round(sum(sections[n]["score"] * p for n, p in PONDERATIONS.items()), 4)

    # Facteur de cohérence GLOBAL : une contradiction inter-champs est le signal le
    # plus fort d'une émission non fiable (le modèle ment sur son propre comportement).
    # Chaque violation applique -0.20 multiplicatif (cap 3). Ex. 2 violations -> x0.60.
    # Calibration MI-3 : révisable après validation empirique (Scénario 3, Dep).
    n_violations = sum(1 for c in coherences if not c["ok"])
    facteur_coherence = max(0.0, 1.0 - 0.20 * min(n_violations, 3))
    score = round(score_structurel * facteur_coherence, 4)

    verdict = "STRUCTURE" if score >= 0.75 else "PARTIEL" if score >= 0.40 else "NON-STRUCTURE"
    return {"score_global": score, "score_structurel": score_structurel,
            "facteur_coherence": facteur_coherence, "n_violations_coherence": n_violations,
            "verdict": verdict, "exploitable": True, "sections": sections,
            "coherences": coherences, "violations_schema": violations_schema, "notes": notes}


def _score_section(nom, contenu):
    if not isinstance(contenu, dict):
        return {"score": 0.0, "details": ["section absente"]}
    details, score = [], 0.4  # présence
    requis = CHAMPS_REQUIS[nom]
    presents = [c for c in requis if c in contenu]
    score += 0.4 * (len(presents) / len(requis))
    manquants = [c for c in requis if c not in contenu]
    if manquants:
        details.append("champs manquants: " + ", ".join(manquants))
    else:
        details.append("complet (" + str(len(requis)) + " champs)")
    # 0.2 de cohérence acquis par défaut. Une violation ne le décrémente pas ici :
    # elle est pénalisée globalement par facteur_coherence (voir verifier()).
    score += 0.2
    # Sous-structure MECA : 5 axes attendus
    if nom == "meca" and isinstance(contenu.get("axes"), dict):
        absents = [a for a in AXES_MECA if a not in contenu["axes"]]
        if absents:
            score -= 0.1
            details.append("axes MECA manquants: " + ", ".join(absents))
    return {"score": round(min(score, 1.0), 3), "details": details}


def _objet(valeur):
    """Une sous-section du mauvais type est traitée comme absente. La validation
    de schéma la signale ; les cohérences ne doivent pas planter dessus."""
    return valeur if isinstance(valeur, dict) else {}


def _entier(valeur):
    return isinstance(valeur, int) and not isinstance(valeur, bool)


def _nombre(valeur):
    return isinstance(valeur, (int, float)) and not isinstance(valeur, bool)


def _coherences(data, notes):
    """Invariants inter-champs (emission_audit_v8.md). Structurels uniquement.

    Une règle ne s'évalue que si ses champs ont le bon type : sinon elle est
    notée « non évaluable » et c'est la validation de schéma qui porte l'échec.
    """
    resultats = []

    def _regle(section, regle, ok):
        resultats.append({"section": section, "regle": regle, "ok": bool(ok)})

    meca = _objet(data.get("meca"))
    auth = _objet(meca.get("authenticite_alternatives"))
    comptes = ("presentees", "survivantes", "leurres")
    if all(k in auth for k in comptes):
        if all(_entier(auth[k]) for k in comptes):
            _regle("meca", "leurres = presentees - survivantes",
                   auth["leurres"] == auth["presentees"] - auth["survivantes"])
        else:
            notes.append("règle « leurres = presentees - survivantes » non évaluable : "
                         "comptes non entiers")
    if auth.get("effondrement") is True:
        _regle("meca", "effondrement => refutation_demontree",
               auth.get("refutation_demontree") is True)

    axes = _objet(meca.get("axes"))
    if "score_global" in meca and all(a in axes for a in AXES_MECA):
        if _nombre(meca["score_global"]) and all(_nombre(axes[a]) for a in AXES_MECA):
            attendu = sum(axes[a] * POIDS_AXE for a in AXES_MECA)
            _regle("meca", f"score_global = somme des axes x{POIDS_AXE} (attendu {attendu:.3f}, "
                           f"tolerance {TOLERANCE_SCORE_GLOBAL:.3f})",
                   abs(meca["score_global"] - attendu) <= TOLERANCE_SCORE_GLOBAL)
        else:
            notes.append("règle « score_global = somme des axes » non évaluable : "
                         "valeurs non numériques")

    gates = _objet(data.get("gates"))
    sig = _objet(data.get("signature_mamd"))
    ordre = _objet(gates.get("ordre_2_3"))
    if gates.get("f04_mode") == "forte":
        _regle("gates", "f04_mode=forte => engagement=delegation_pure",
               sig.get("engagement") == "delegation_pure")
        _regle("gates", "f04_mode=forte => ordre_2_3.securise",
               ordre.get("securise") is True)
    if "viole" in ordre:
        _regle("gates", "ordre_2_3.viole = false (gate souverainete)",
               ordre.get("viole") is False)

    return resultats
