"""
Instrument V.8 — Extracteur du bloc LAB AUDIT JSON.
===============================================================
Extraction TOLÉRANTE (accents/casse/espaces sur les délimiteurs), puis parse
strict. Fallback : dernier objet JSON valide contenant "signature_mamd".
Pas de regex de prose : on localise un bloc déclaré, on parse des données.
"""

import json
import re

# Délimiteurs tolérants (=== x3+, espaces variables, casse indifférente).
# (?:LAB|TJ) : tolérance de transition. Le protocole émet désormais
# « LAB AUDIT JSON » ; « TJ AUDIT JSON » reste accepté parce que des sessions
# en cours tournent encore sur la Skill d'avant renommage. Refuser l'ancien
# jeton ne produirait pas une erreur : la lecture basculerait en silence sur
# le fallback signature_mamd. À retirer quand plus aucune session V.7.x n'émet.
_PATTERN_BLOC = re.compile(
    r'={3,}\s*(?:LAB|TJ)\s+AUDIT\s+JSON\s*={3,}'
    r'([\s\S]*?)'
    r'={3,}\s*FIN\s+(?:LAB|TJ)\s+AUDIT\s+JSON\s*={3,}',
    re.IGNORECASE,
)


def extraire_bloc(texte: str):
    """
    Retourne (data: dict | None, statut: str).
    statuts : "ok" | "bloc_absent" | "json_invalide" | "fallback_ok"
    """
    if not texte:
        return None, "bloc_absent"

    match = _PATTERN_BLOC.search(texte)
    if match:
        brut = match.group(1).strip()
        # Tolérance : le modèle peut avoir encapsulé en ```json … ```
        brut = re.sub(r'^```(?:json)?\s*|\s*```$', '', brut, flags=re.MULTILINE).strip()
        try:
            return json.loads(brut), "ok"
        except json.JSONDecodeError:
            return None, "json_invalide"

    # Fallback : dernier objet JSON top-level contenant signature_mamd
    data = _dernier_json_avec_cle(texte, "signature_mamd")
    if data is not None:
        return data, "fallback_ok"
    return None, "bloc_absent"


def _dernier_json_avec_cle(texte: str, cle: str):
    """Scan par équilibrage d'accolades ; retourne le dernier candidat parsable contenant `cle`."""
    candidats = []
    profondeur, debut = 0, None
    for i, c in enumerate(texte):
        if c == '{':
            if profondeur == 0:
                debut = i
            profondeur += 1
        elif c == '}':
            if profondeur > 0:
                profondeur -= 1
                if profondeur == 0 and debut is not None:
                    fragment = texte[debut:i + 1]
                    if cle in fragment:
                        candidats.append(fragment)
                    debut = None
    for fragment in reversed(candidats):
        try:
            return json.loads(fragment)
        except json.JSONDecodeError:
            continue
    return None
