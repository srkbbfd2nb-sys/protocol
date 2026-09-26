"""
Cohérence du protocole — contrôles mécaniques.
===============================================================
Le protocole a grossi par accrétion. Ses incohérences ne sont pas des fautes
de frappe : un module pilote a ignoré SONDE pendant deux versions, un sigle
circule sans développement, un comptage annoncé dérive du réel. Ce script les
rend impossibles à introduire sans que la CI ne devienne rouge.

  python lab/coherence.py            # depuis la racine du dépôt
  python lab/coherence.py --lister   # toutes les violations, en JSON

Six contrôles :
  sigles     chaque code employé dans la couche active a une entrée au glossaire
  graphe     chaque module de la couche active apparaît dans le Graphe
  couplages  chaque module déclare ses couplages ; une paire citée d'un côté
             l'est de l'autre
  comptages  les nombres annoncés (pôles, invariants, modules…) valent le réel
  modeles    aucun nom de modèle ni de produit dans la couche normative
  paquet     skill/ reproduit protocole/ à l'octet près

**Dette de cohérence.** Les violations existantes sont inscrites, une par une,
dans lab/coherence_dette.json. La CI échoue sur toute violation qui n'y figure
pas — et sur toute entrée de la dette qui ne correspond plus à rien : une
dette soldée doit être retirée du registre, sinon le registre ment. La dette
ne peut donc que décroître, et son état est public.

Bibliothèque standard seule. Sortie 0 = rien de nouveau, dette exacte ;
1 = violation nouvelle ou dette soldée non retirée ; 2 = dépôt illisible.
"""

import json
import re
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

RACINE_DEFAUT = Path(__file__).resolve().parents[1]

# Alias déclarés au glossaire : EXT-03 « porte MREO » ; GDA est « le mécanisme porté
# par PADC-IA ». Un module cité sous son alias est cité.
ALIAS = {"MREO": "EXT-03", "GDA": "PADC-IA"}

# Le Noyau est le CADRE : ses relations sont la chaîne canonique et l'index des pôles,
# pas une section Couplages. Le Graphe est la RÉFÉRENCE : sa section porte le seul
# squelette structurel (F) par construction — sa complétude est le contrôle « graphe ».
SANS_SECTION_ADMIS = {"Noyau"}
HORS_SYMETRIE = {"Noyau", "Graphe"}

# Jetons en capitales qui ne sont PAS des codes du protocole. Chaque famille est
# déclarée ici, publiquement : l'élargir est une décision visible dans un diff.
PAS_DES_CODES = {
    "titres de section": {"AMORCE", "PROCESSUS", "SORTIE", "ACTIVE", "CADRE", "BEHAVIORAL",
                          "INVARIANT", "VALIDATION", "EXPLORATION", "FORMAT", "PHASE"},
    "blocs de sortie": {"ACTIVATIONS", "SIGNATURE", "CAPACITES", "ORCHESTRATION", "FLUENCE",
                        "SCANNER", "AUDIT", "FIN"},
    "valeurs et verdicts": {"DORMANT", "FORTE", "MOLLE", "ENVOIE", "GO", "NO-GO", "CONDITIONNEL"},
    "mots en capitales": {"ET", "OU", "PAS", "NE", "ICI"},
    "acronymes externes": {"JSON", "MD", "API", "LLM", "RLHF", "IA", "LAB"},
}
_NON_CODES = set().union(*PAS_DES_CODES.values())

MODELES = re.compile(
    r"\b(GPT[-\w.]*|ChatGPT|OpenAI|Claude[\w.]*|Anthropic|Gemini|Bard|Mistral|Mixtral|Llama|"
    r"LLaMA|Grok|Copilot|DeepSeek|Qwen|Opus|Sonnet|Haiku|Codex|Cursor|Perplexity)\b")

_JETON = re.compile(r"(?<![\w/.-])([A-Z][A-Z0-9]*(?:[-.][A-Z0-9]+)*)(?![\w-])")


# --------------------------------------------------------------------- lecture

class Depot:
    def __init__(self, racine: Path):
        self.racine = racine
        self.actif = racine / "protocole" / "actif"
        self.archive = racine / "protocole" / "archive"
        if not self.actif.is_dir():
            raise FileNotFoundError(f"couche active introuvable : {self.actif}")
        self.textes = {p.name: p.read_text(encoding="utf-8") for p in sorted(self.actif.glob("*.md"))}
        self.modules = {}                      # fichier -> code (1er mot du titre)
        for nom, texte in self.textes.items():
            if nom == "README.md" or nom.startswith("emission_audit"):
                continue
            titre = re.search(r"^# (\S+)", texte, re.M)
            self.modules[nom] = titre.group(1) if titre else nom
        self.glossaire = (racine / "GLOSSAIRE.md").read_text(encoding="utf-8")

    def lire(self, relatif):
        p = self.racine / relatif
        return p.read_text(encoding="utf-8") if p.is_file() else ""


def _cite(texte, code):
    return re.search(r"(?<![\w-])" + re.escape(code) + r"(?![\w-])", texte) is not None


# --------------------------------------------------------------------- 1. sigles

def _couverture_glossaire(glossaire):
    couverts = set()
    for code in re.findall(r"^\| \*\*([^*|]+)\*\* \|", glossaire, re.M):
        code = code.strip()
        couverts.add(code)
        for membre in code.split("/"):
            couverts.add(membre)
        m = re.fullmatch(r"(.*?)(\d+)[–-](\d+)", code)          # INV.1–8, MI-1–5, PA.1–3
        if m:
            prefixe, a, b = m.group(1), int(m.group(2)), int(m.group(3))
            couverts |= {f"{prefixe}{i}" for i in range(a, b + 1)}
    return couverts


def _couvert(jeton, couverts):
    if jeton in couverts or jeton in _NON_CODES or re.fullmatch(r"V\.\d+(\.\d+)*", jeton):
        return True
    m = re.fullmatch(r"(.*?)(\d+)-(\d+)", jeton)                 # INV.1-8, MI-1-5
    if m and f"{m.group(1)}{m.group(2)}" in couverts and f"{m.group(1)}{m.group(3)}" in couverts:
        return True
    return False


def controle_sigles(d: Depot):
    couverts = _couverture_glossaire(d.glossaire)
    vus = set()
    for texte in d.textes.values():
        vus |= {j for j in _JETON.findall(texte) if len(j) >= 2}
    return sorted(j for j in vus if not _couvert(j, couverts))


# --------------------------------------------------------------------- 2. graphe

def controle_graphe(d: Depot):
    graphe = d.textes.get("graphe_v8.md", "") + d.lire("protocole/archive/graphe_v8_detail.md")
    alias_de = {v: k for k, v in ALIAS.items()}
    absents = []
    for code in sorted(set(d.modules.values())):
        if code == "Graphe":
            continue
        if not (_cite(graphe, code) or (code in alias_de and _cite(graphe, alias_de[code]))):
            absents.append(code)
    return absents


# --------------------------------------------------------------------- 3. couplages

def _section_couplages(texte):
    m = re.search(r"^## Couplages[^\n]*\n(.*?)(?=^## |^→ |^---|\Z)", texte, re.M | re.S)
    return m.group(1) if m else None


def controle_couplages(d: Depot):
    codes = set(d.modules.values())
    partenaires, violations = {}, []
    for nom, code in d.modules.items():
        section = _section_couplages(d.textes[nom])
        if section is None:
            if code not in SANS_SECTION_ADMIS:
                violations.append(f"{code} : pas de section Couplages")
            continue
        cites = {ALIAS.get(c, c) for c in codes | set(ALIAS) if _cite(section, c)}
        partenaires[code] = cites - {code}
    for x in sorted(partenaires):
        if x in HORS_SYMETRIE:
            continue
        for y in sorted(partenaires[x]):
            if y in HORS_SYMETRIE or y not in partenaires:
                continue
            if x not in partenaires[y]:
                violations.append(f"{x} cite {y}, {y} ne cite pas {x}")
    return violations


# --------------------------------------------------------------------- 4. comptages

_NOMBRES = {"deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8,
            "neuf": 9, "dix": 10, "vingt": 20}


def comptages_reels(d: Depot):
    noyau = d.textes["noyau_v8.md"]

    def ligne_apres(entete):
        m = re.search(re.escape(entete) + r"[^\n]*\n([^\n]+)", noyau)
        return m.group(1) if m else ""

    poles = re.search(r"^## Les 3 pôles.*?(?=^## |\Z)", noyau, re.M | re.S)
    natures = re.search(r"^## Les 7 natures[^\n]*\n+([^\n]+)", noyau, re.M)
    garde_fou = re.search(r"ne s'applique PAS à (INV\.[\d/]+)", noyau)
    return {
        "modules": len(d.modules),
        "pôles": len(re.findall(r"^- \*\*[①②③]", poles.group(0), re.M)) if poles else 0,
        "invariants": len(set(re.findall(r"INV\.(\d+)", ligne_apres("**Bloc A —")))),
        "méta-invariants": len(set(re.findall(r"MI-(\d+)", ligne_apres("**Méta-Invariant Structurel —")))),
        "principes architecturaux": len(set(re.findall(r"PA\.(\d+)", ligne_apres("**Principes Architecturaux")))),
        "natures": len(re.findall(r"`[^`]+` \(", natures.group(1))) if natures else 0,
        "invariants strictement restrictifs":
            len(garde_fou.group(1).replace("INV.", "").split("/")) if garde_fou else 0,
    }


_ANNONCE = re.compile(
    r"\b(\d+|" + "|".join(_NOMBRES) + r")\s+(?:\*\*)?"
    r"(pôles|invariants strictement restrictifs|méta-invariants|invariants|garanties|"
    r"principes architecturaux|modules|natures)\b", re.IGNORECASE)
_QUANTITE = {"garanties": "méta-invariants"}
DOCUMENTS_ANNONCANT = ["README.md", "CITATION.cff", "CONTRIBUTING.md", "GLOSSAIRE.md",
                       "skill/SKILL.md", "skill/README.md", "protocole/archive/README.md"]


def controle_comptages(d: Depot):
    reels = comptages_reels(d)
    sources = {rel: d.lire(rel) for rel in DOCUMENTS_ANNONCANT}
    sources.update({f"protocole/actif/{n}": t for n, t in d.textes.items()})
    ecarts = []
    for rel, texte in sources.items():
        for m in _ANNONCE.finditer(texte):
            brut, nom = m.group(1).lower(), m.group(2).lower()
            annonce = int(brut) if brut.isdigit() else _NOMBRES[brut]
            quantite = _QUANTITE.get(nom, nom)
            if quantite in reels and annonce != reels[quantite]:
                ecarts.append(f"{rel} : « {m.group(0)} » — réel {reels[quantite]}")
    return sorted(set(ecarts))


# --------------------------------------------------------------------- 5. modèles

def controle_modeles(d: Depot):
    trouves = set()
    for nom, texte in d.textes.items():
        for m in MODELES.findall(texte):
            trouves.add(f"{nom} : {m}")
    return sorted(trouves)


# --------------------------------------------------------------------- 6. paquet

def controle_paquet(d: Depot):
    ecarts = []
    paires = [(p, d.racine / "skill" / "references" / p.name)
              for p in d.actif.glob("*.md") if p.name != "README.md"]
    paires += [(p, d.racine / "skill" / "archive" / p.name) for p in d.archive.glob("*.md")]
    for source, copie in sorted(paires):
        if not copie.is_file():
            ecarts.append(f"{copie.relative_to(d.racine).as_posix()} : absent du paquet")
        elif source.read_bytes() != copie.read_bytes():
            ecarts.append(f"{copie.relative_to(d.racine).as_posix()} : diffère de la source")
    return ecarts


CONTROLES = {
    "sigles": controle_sigles,
    "graphe": controle_graphe,
    "couplages": controle_couplages,
    "comptages": controle_comptages,
    "modeles": controle_modeles,
    "paquet": controle_paquet,
}


# --------------------------------------------------------------------- dette et verdict

def violations(racine: Path):
    d = Depot(racine)
    return {nom: fn(d) for nom, fn in CONTROLES.items()}


def charger_dette(racine: Path):
    chemin = racine / "lab" / "coherence_dette.json"
    if not chemin.is_file():
        return {}
    data = json.loads(chemin.read_text(encoding="utf-8"))
    dette = {}
    for entree in data.get("violations", []):
        dette.setdefault(entree["controle"], set()).add(entree["cle"])
    return dette


def verifier(racine: Path = RACINE_DEFAUT):
    """Retourne {controle: {"nouvelles": [...], "soldees": [...], "dette": n}}."""
    trouve, dette = violations(racine), charger_dette(racine)
    bilan = {}
    for nom in CONTROLES:
        actuelles, connues = set(trouve[nom]), dette.get(nom, set())
        bilan[nom] = {"nouvelles": sorted(actuelles - connues),
                      "soldees": sorted(connues - actuelles),
                      "dette": len(actuelles & connues)}
    for nom in set(dette) - set(CONTROLES):
        bilan[nom] = {"nouvelles": [], "soldees": sorted(dette[nom]), "dette": 0}
    return bilan


def main():
    args = sys.argv[1:]
    racine = Path(next((a for a in args if not a.startswith("--")), RACINE_DEFAUT))
    try:
        if "--lister" in args:
            print(json.dumps(violations(racine), ensure_ascii=False, indent=2))
            return
        bilan = verifier(racine)
    except (FileNotFoundError, KeyError) as e:
        print(f"ERREUR — dépôt illisible : {e}")
        sys.exit(2)

    echec = False
    print("=" * 68)
    print("  COHÉRENCE DU PROTOCOLE")
    print("=" * 68)
    for nom, b in bilan.items():
        etat = "OK " if not (b["nouvelles"] or b["soldees"]) else "ÉCHEC"
        print(f"  [{etat}] {nom:<10} dette connue : {b['dette']}")
        for v in b["nouvelles"]:
            print(f"      + NOUVELLE — {v}")
        for v in b["soldees"]:
            print(f"      − SOLDÉE, à retirer de lab/coherence_dette.json — {v}")
        echec |= bool(b["nouvelles"] or b["soldees"])
    total = sum(b["dette"] for b in bilan.values())
    print("-" * 68)
    print(f"  Dette de cohérence publiée : {total} violation(s) connue(s), inscrites une par une.")
    print("=" * 68)
    sys.exit(1 if echec else 0)


if __name__ == "__main__":
    main()
