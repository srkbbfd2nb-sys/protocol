# -*- coding: utf-8 -*-
"""
Tests de lab/coherence.py — chaque contrôle est vu échouer.

Un contrôle qu'on n'a jamais vu échouer n'est pas un contrôle. Chaque test
ci-dessous copie le dépôt dans un dossier temporaire, y injecte UNE
incohérence d'un type donné, et vérifie que le contrôle correspondant la
signale comme nouvelle.
"""

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RACINE / "lab"))

import coherence  # noqa: E402

A_COPIER = ["protocole", "skill", "GLOSSAIRE.md", "README.md", "CITATION.cff", "CONTRIBUTING.md",
            "lab/coherence.py", "lab/coherence_dette.json"]


@pytest.fixture
def copie(tmp_path):
    for rel in A_COPIER:
        src, dst = RACINE / rel, tmp_path / rel
        if src.is_dir():
            shutil.copytree(src, dst)
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
    return tmp_path


def _modifier(racine, relatif, avant, apres, partout=False):
    p = racine / relatif
    t = p.read_text(encoding="utf-8")
    assert avant in t, f"ancre absente de {relatif} : {avant!r}"
    p.write_text(t.replace(avant, apres) if partout else t.replace(avant, apres, 1), encoding="utf-8")


def _nouvelles(racine, controle):
    return coherence.verifier(racine)[controle]["nouvelles"]


# --------------------------------------------------------------------- l'état publié

def test_le_depot_publie_est_coherent_a_sa_dette_pres():
    bilan = coherence.verifier(RACINE)
    for nom, b in bilan.items():
        assert not b["nouvelles"], f"{nom} : violation(s) hors dette {b['nouvelles']}"
        assert not b["soldees"], f"{nom} : dette soldée à retirer du registre {b['soldees']}"


def test_les_comptages_reels_sont_lus_et_non_nuls():
    """Un compteur cassé qui rendrait 0 partout ne produirait aucun écart
    visible si rien n'annonçait ce nombre. On fixe donc les valeurs lues."""
    assert coherence.comptages_reels(coherence.Depot(RACINE)) == {
        "modules": 20, "pôles": 3, "invariants": 8, "méta-invariants": 5,
        "principes architecturaux": 3, "natures": 7, "invariants strictement restrictifs": 4}


# --------------------------------------------------------------------- chaque contrôle, vu échouer

def test_sigles_un_code_sans_glossaire_est_refuse(copie):
    _modifier(copie, "protocole/actif/aca_v8.md", "## AMORCE", "Le module ZQX-9 opère ici.\n\n## AMORCE")
    assert "ZQX-9" in _nouvelles(copie, "sigles")


def test_graphe_un_module_absent_du_graphe_est_refuse(copie):
    (copie / "protocole/actif/zeta_v8.md").write_text(
        "# ZETA V.8 — Couche ACTIVE\n\n## Couplages\n- **ZETA → ACA** : `Fn informe`.\n",
        encoding="utf-8")
    assert "ZETA" in _nouvelles(copie, "graphe")


def test_couplages_une_paire_declaree_d_un_seul_cote_est_refusee(copie):
    _modifier(copie, "protocole/actif/aca_v8.md", "## Couplages", "## Couplages\n- **ACA → I-06** : `Fn informe`.")
    assert "ACA cite I-06, I-06 ne cite pas ACA" in _nouvelles(copie, "couplages")


def test_couplages_un_module_sans_section_est_refuse(copie):
    _modifier(copie, "protocole/actif/lyra_v8.md", "## Couplages", "## Liens")
    assert "Lyra : pas de section Couplages" in _nouvelles(copie, "couplages")


def test_couplages_un_alias_declare_vaut_citation():
    """EXT-03 porte MREO : un module qui cite MREO cite EXT-03."""
    assert coherence.ALIAS["MREO"] == "EXT-03"
    assert coherence._cite("→ MREO (E-1/E-2)", "MREO")


def test_comptages_un_nombre_annonce_faux_est_refuse(copie):
    _modifier(copie, "README.md", "20 modules", "21 modules")
    assert any("21 modules" in v for v in _nouvelles(copie, "comptages"))


def test_comptages_un_sous_ensemble_declare_est_verifie_lui_aussi(copie):
    _modifier(copie, "CONTRIBUTING.md", "quatre invariants strictement restrictifs",
              "trois invariants strictement restrictifs")
    assert any("trois invariants" in v for v in _nouvelles(copie, "comptages"))


def test_modeles_un_nom_de_modele_dans_la_couche_normative_est_refuse(copie):
    _modifier(copie, "protocole/actif/meca_v8.md", "## PROCESSUS", "Testé sur GPT-5.\n\n## PROCESSUS")
    assert "meca_v8.md : GPT-5" in _nouvelles(copie, "modeles")


def test_paquet_une_copie_divergente_est_refusee(copie):
    _modifier(copie, "skill/references/aca_v8.md", "## AMORCE", "## AMORCE modifiée")
    assert any("aca_v8.md" in v for v in _nouvelles(copie, "paquet"))


# --------------------------------------------------------------------- la dette elle-même

def test_une_dette_soldee_non_retiree_fait_echouer(copie):
    """Corriger sans mettre à jour le registre laisserait un registre qui ment."""
    for rel in ("protocole/actif/i06_v8.md", "skill/references/i06_v8.md"):
        _modifier(copie, rel, "Claude.ai", "l'application conversationnelle", partout=True)
    bilan = coherence.verifier(copie)["modeles"]
    assert "i06_v8.md : Claude.ai" in bilan["soldees"]
    assert not bilan["nouvelles"]


def test_sans_registre_toute_la_dette_devient_nouvelle(copie):
    (copie / "lab/coherence_dette.json").unlink()
    assert _nouvelles(copie, "graphe"), "le registre ne doit pas être optionnel en silence"


# --------------------------------------------------------------------- ligne de commande

def _cli(racine):
    return subprocess.run([sys.executable, str(racine / "lab" / "coherence.py"), str(racine)],
                          capture_output=True, text=True, encoding="utf-8")


def test_cli_codes_de_sortie(copie, tmp_path):
    assert _cli(copie).returncode == 0
    _modifier(copie, "README.md", "20 modules", "21 modules")
    assert _cli(copie).returncode == 1
    vide = tmp_path / "vide"
    (vide / "lab").mkdir(parents=True)
    shutil.copy2(copie / "lab" / "coherence.py", vide / "lab" / "coherence.py")
    assert _cli(vide).returncode == 2
