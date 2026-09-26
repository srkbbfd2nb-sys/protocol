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

import copy
import json
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
FIXTURES = RACINE / "fixtures"
TEMPLATE = RACINE.parent / "protocole" / "actif" / "emission_audit_v8.md"
sys.path.insert(0, str(RACINE))

from audit.v8.json_extractor import extraire_bloc          # noqa: E402
from audit.v8.verifier import verifier                     # noqa: E402
from audit.v8.validation import (charger_schema, valider,  # noqa: E402
                                 SchemaNonSupporte)
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
                             ("ancien-jeton.txt", 0),
                             ("coherence-violee.txt", 1),
                             ("sections-manquantes.txt", 1),
                             ("sans-delimiteurs.txt", 1),
                             ("axe-hors-plage.txt", 1),
                             ("enumeration-inconnue.txt", 1),
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


# --------------------------------------------------------------------- contrat : validité, pas seulement présence
#
# Avant ces tests, le vérificateur contrôlait qu'un champ était *présent*, jamais
# qu'il était *valide*. Chacun des cas ci-dessous sortait en 0 — conforme — ou
# faisait planter l'instrument. Ils sont reproduits ici pour ne pas revenir.

def _bloc_conforme():
    data, _ = extraire_bloc(lire("conforme.txt"))
    return copy.deepcopy(data)


def _sortie(data, statut="ok"):
    return code_de_sortie(verifier(data), statut)


def test_repli_heuristique_ne_sort_jamais_en_0():
    """Un bloc sans délimiteurs est lisible, mais la réponse ne respecte pas le
    contrat d'émission. Le déclarer conforme affaiblirait le contrat en silence."""
    rapport, statut = auditer("sans-delimiteurs.txt")
    assert statut == "fallback_ok"
    assert rapport["verdict"] == "STRUCTURE", "le contenu est complet : seul le contrat manque"
    assert code_de_sortie(rapport, statut) == 1


def test_axe_hors_plage_est_refuse():
    rapport, statut = auditer("axe-hors-plage.txt")
    assert any("clarte" in v and "maximum" in v for v in rapport["violations_schema"])
    assert code_de_sortie(rapport, statut) == 1


def test_enumeration_inconnue_est_refusee():
    rapport, statut = auditer("enumeration-inconnue.txt")
    assert any("f04_mode" in v for v in rapport["violations_schema"])
    assert code_de_sortie(rapport, statut) == 1


def test_score_global_incoherent_avec_les_axes():
    """score_global = somme des axes ×0,20, arrondie à deux décimales
    (tj_v72/07_meca:285, :500). Ici les axes donnent 0,902 et le score annonce 0,99."""
    data = _bloc_conforme()
    data["meca"]["score_global"] = 0.99
    rapport = verifier(data)
    assert any("score_global" in c["regle"] and not c["ok"] for c in rapport["coherences"])
    assert _sortie(data) == 1


def test_arrondi_a_deux_decimales_est_tolere():
    """La tolérance est l'erreur d'un arrondi à deux décimales, pas un seuil
    empirique : 0,902 annoncé 0,90 doit passer, 0,902 annoncé 0,92 non."""
    data = _bloc_conforme()
    assert _sortie(data) == 0
    data["meca"]["score_global"] = 0.92
    assert _sortie(data) == 1


def test_section_entiere_absente_n_est_pas_conforme():
    """Sans le schéma, une section de poids 0,15 manquante laissait le score à
    0,85, donc STRUCTURE, donc sortie 0."""
    data = _bloc_conforme()
    del data["reflexivite_i07"]
    assert _sortie(data) == 1


@pytest.mark.parametrize("champ, valeur", [
    ("comptes en chaînes", {"presentees": "3", "survivantes": "2", "leurres": "1"}),
    ("comptes booléens", {"presentees": True, "survivantes": True, "leurres": 0}),
])
def test_comptes_mal_types_sont_refuses_sans_plantage(champ, valeur):
    """"3" − "2" faisait planter l'instrument ; True − True = 0 passait pour un
    compte de leurres juste. Le premier cas est un plantage, le second un faux
    négatif silencieux — le pire des deux."""
    data = _bloc_conforme()
    data["meca"]["authenticite_alternatives"].update(valeur)
    rapport = verifier(data)                       # ne doit pas lever
    assert any("presentees" in v for v in rapport["violations_schema"]), champ
    assert _sortie(data) == 1


def test_ordre_2_3_mal_type_ne_fait_pas_planter():
    """ "viole" in "non viole" est vrai en Python : une chaîne à la place de
    l'objet déclenchait une recherche de sous-chaîne, puis un plantage."""
    data = _bloc_conforme()
    data["gates"]["ordre_2_3"] = "non viole"
    rapport = verifier(data)                       # ne doit pas lever
    assert any("ordre_2_3" in v for v in rapport["violations_schema"])
    assert _sortie(data) == 1


def test_json_qui_n_est_pas_un_objet_est_inexploitable():
    rapport = verifier([1, 2, 3])
    assert code_de_sortie(rapport, "ok") == 2


def test_fichier_introuvable_sort_en_2():
    """Un chemin faux n'est pas une réponse non conforme. Sortir en 1 ferait
    passer une CI qui attend un refus sans avoir jamais lu le fichier."""
    r = subprocess.run([sys.executable, str(RACINE / "audit_v8.py"),
                        "--input-file", str(FIXTURES / "n-existe-pas.txt")],
                       capture_output=True, text=True, cwd=str(RACINE))
    assert r.returncode == 2


def test_section_non_declaree_est_signalee_pas_refusee():
    """Les fixtures portent une section `capacites` (sortie de SONDE) que le
    template ne déclare pas. Elle est admise — le contrat V.8 ne l'interdit
    pas — mais elle doit être visible, jamais absorbée en silence."""
    rapport, _ = auditer("conforme.txt")
    assert any("capacites" in n for n in rapport["notes"])


# --------------------------------------------------------------------- le schéma lui-même

def test_le_validateur_refuse_un_mot_cle_qu_il_n_applique_pas(tmp_path):
    """Un validateur partiel qui ignorerait un mot-clé laisserait croire qu'une
    contrainte est vérifiée. Il doit refuser de charger le schéma."""
    faux = tmp_path / "faux.schema.json"
    faux.write_text(json.dumps({"type": "string", "pattern": "^a"}), encoding="utf-8")
    with pytest.raises(SchemaNonSupporte):
        charger_schema(faux)


def _enumerations_du_template(noeud, chemin="$"):
    """Dans le template, une énumération s'écrit "a|b|c". Retourne {chemin: [...]}."""
    trouve = {}
    if isinstance(noeud, dict):
        for k, v in noeud.items():
            trouve.update(_enumerations_du_template(v, f"{chemin}.{k}"))
    elif isinstance(noeud, str) and "|" in noeud:
        trouve[chemin] = noeud.split("|")
    return trouve


def _enumerations_du_schema(schema, chemin="$"):
    trouve = {}
    if "enum" in schema:
        trouve[chemin] = schema["enum"]
    for k, sous in (schema.get("properties") or {}).items():
        trouve.update(_enumerations_du_schema(sous, f"{chemin}.{k}"))
    return trouve


def test_schema_et_template_d_emission_ne_divergent_pas():
    """Le template est le contrat ; le schéma en est la transcription. Chaque
    énumération du template doit figurer à l'identique dans le schéma, et
    inversement. Sans ce test, le premier ajout d'une valeur au template
    rendrait non conformes des réponses qui le respectent."""
    template, statut = extraire_bloc(TEMPLATE.read_text(encoding="utf-8"))
    assert statut == "ok", "le bloc d'exemple du template doit rester du JSON lisible"
    schema = charger_schema()
    assert _enumerations_du_template(template) == _enumerations_du_schema(schema)


def test_le_template_est_structurellement_valide_hors_enumerations():
    """Le bloc d'exemple du template, une fois ses énumérations remplacées par
    leur première valeur, doit passer le schéma : sinon le schéma exige plus
    que le contrat."""
    template, _ = extraire_bloc(TEMPLATE.read_text(encoding="utf-8"))

    def instancier(n):
        if isinstance(n, dict):
            return {k: instancier(v) for k, v in n.items()}
        if isinstance(n, str) and "|" in n:
            return n.split("|")[0]
        return n

    assert valider(instancier(template), charger_schema()) == []
