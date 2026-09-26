"""
Instrument V.8 — Décision de conformité, en un seul endroit.
===============================================================
Le code de sortie et la ligne CONFORMITÉ du rapport lisent tous deux cette
fonction : ils ne peuvent pas se contredire.

  0  conforme      — extraction par délimiteurs, schéma valide, aucune
                     cohérence violée, verdict STRUCTURE
  1  non conforme  — au moins une raison ci-dessous
  2  inexploitable — pas de bloc, JSON illisible, ou JSON qui n'est pas un objet

Le repli heuristique (bloc trouvé sans ses délimiteurs) ne sort **jamais** en
0 : le bloc est lisible, mais la réponse ne respecte pas le contrat
d'émission. Le déclarer conforme affaiblirait le contrat en silence.
"""

INEXPLOITABLE = ("bloc_absent", "json_invalide")


def evaluer(rapport, statut):
    """Retourne (code, raisons). `raisons` est vide si et seulement si code == 0."""
    if statut in INEXPLOITABLE or not rapport.get("exploitable", True):
        return 2, [f"bloc inexploitable ({statut})"]

    raisons = []
    if statut == "fallback_ok":
        raisons.append("bloc extrait par repli heuristique : délimiteurs absents, "
                       "contrat d'émission non respecté")
    n_schema = len(rapport.get("violations_schema", []))
    if n_schema:
        raisons.append(f"{n_schema} violation(s) du schéma")
    n_coh = sum(1 for c in rapport.get("coherences", []) if not c.get("ok", True))
    if n_coh:
        raisons.append(f"{n_coh} cohérence(s) violée(s)")
    if rapport.get("verdict") != "STRUCTURE":
        raisons.append(f"verdict structurel {rapport.get('verdict')}")
    return (1 if raisons else 0), raisons
