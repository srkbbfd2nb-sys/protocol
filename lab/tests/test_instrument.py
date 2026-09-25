# -*- coding: utf-8 -*-
"""
Tests de l'instrument — ils portent sur ce qui est publié, et rien d'autre.

Un clone nu de ce dépôt suffit à les faire tourner : bibliothèque standard,
pytest, aucune clé, aucun réseau. C'est la condition pour qu'un lecteur puisse
vérifier au lieu de croire.

Ce qu'ils établissent, et c'est tout ce qu'ils établissent : l'instrument lit
un bloc, en contrôle la structure et les cohérences déclarées, et rend un
verdict reproductible. Il ne dit rien de la justesse de la réponse auditée.
"""

import json
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
FIXTURES = RACINE / "fixtures"
sys.path.insert(0, str(RACINE))

from audit.v8.json_extractor import extraire_bloc          # noqa: E402
from audit.v8.verifier import verifier                     # noqa: E402
from audit_v8 import code_de_sortie                        # noqa: E402


def lire(nom):
    return (FIXTURES / nom).read_text(encoding="utf-8")


def auditer(nom):
    data, statut = extraire_bloc(lire(nom))
    return verifier(data), statut


# --------------------------------------------------------------------- extraction

def test_extraction_bloc_conforme():
    data, statut = extraire_bloc(lire("conforme.txt"))
    assert statut == "ok", "un bloc bien délimité doit être extrait sans repli"
    assert "signature_mamd" in data


def test_extraction_tolere_l_ancien_jeton():
    """Transition : une session tournant encore sur l'ancien nom reste lisible.

    Refuser l'ancien jeton ne produirait pas une erreur — la lecture basculerait
    en silence sur l'heuristique de repli. C'est le mode de défaillance que
    cette tolérance rend impossible.
    """
    data, statut = extraire_bloc(lire("ancien-jeton.txt"))
    assert statut == "ok"
    assert data is not None


def test_bloc_absent_est_declare_et_non_devine():
    data, statut = extraire_bloc(lire("bloc-absent.txt"))
    assert statut == "bloc_absent"
    assert data is None


def test_json_invalide_est_declare():
    _, statut = extraire_bloc(lire("json-invalide.txt"))
    assert statut in ("json_invalide", "bloc_absent")


# --------------------------------------------------------------------- vérification

def test_bloc_conforme_est_structure():
    rapport, statut = auditer("conforme.txt")
    assert statut == "ok"
    assert rapport["verdict"] == "STRUCTURE"
    assert not [c for c in rapport["coherences"] if not c["ok"]]


def test_coherence_arithmetique_violee_est_detectee():
    """leurres = présentées − survivantes. Ici 0 au lieu de 1."""
    rapport, _ = auditer("coherence-violee.txt")
    violees = [c for c in rapport["coherences"] if not c["ok"]]
    assert violees, "une incohérence arithmétique doit être relevée"
    assert any("leurres" in c["regle"] for c in violees)


def test_sections_manquantes_degradent_le_score():
    complet, _ = auditer("conforme.txt")
    partiel, _ = auditer("sections-manquantes.txt")
    assert partiel["score_global"] < complet["score_global"]


def test_absence_de_bloc_ne_produit_pas_un_verdict_favorable():
    rapport, _ = auditer("bloc-absent.txt")
    assert rapport["verdict"] == "NON-STRUCTURE"
    assert rapport["score_global"] == 0.0


# --------------------------------------------------------------------- codes de sortie

def test_codes_de_sortie():
    """0 conforme · 1 non conforme · 2 inexploitable — c'est ce qui rend
    l'instrument branchable sur une chaîne d'intégration."""
    for fixture, attendu in [("conforme.txt", 0),
                             ("coherence-violee.txt", 1),
                             ("sections-manquantes.txt", 1),
                             ("bloc-absent.txt", 2),
                             ("json-invalide.txt", 2)]:
        rapport, statut = auditer(fixture)
        assert code_de_sortie(rapport, statut) == attendu, fixture


def test_cli_de_bout_en_bout():
    """L'outil tel qu'un lecteur l'utilisera réellement."""
    r = subprocess.run(
        [sys.executable, str(RACINE / "audit_v8.py"),
         "--input-file", str(FIXTURES / "coherence-violee.txt")],
        capture_output=True, text=True, cwd=str(RACINE))
    assert r.returncode == 1
    assert "VIOLATION" in r.stdout


# --------------------------------------------------------------------- déterminisme

def test_verdict_reproductible():
    """Deux passes sur la même entrée donnent le même verdict : sans quoi
    aucune mesure comparative n'aurait de sens."""
    a, _ = auditer("conforme.txt")
    b, _ = auditer("conforme.txt")
    assert json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)
