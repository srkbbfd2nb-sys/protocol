"""
Instrument V.8 — Rapport (console + JSON persisté logs/rapport_v8_*.json).
"""

import json
import os
from datetime import datetime

from audit.v8 import conformite


def imprimer(rapport, statut_extraction):
    print("=" * 68)
    print("  INSTRUMENT V.8 — Audit structurel LAB AUDIT JSON")
    print("=" * 68)
    print(f"  Extraction : {statut_extraction}")
    print(f"  VERDICT    : {rapport['verdict']}  (score {rapport['score_global']:.4f})")
    print("-" * 68)
    for nom, sec in rapport["sections"].items():
        print(f"  {nom:<20} : {sec['score']:.3f}  | " + " · ".join(sec["details"]))
    if rapport["coherences"]:
        print("-" * 68)
        for c in rapport["coherences"]:
            marque = "OK " if c["ok"] else "VIOLATION"
            print(f"  [{marque}] {c['regle']}")
    if rapport.get("violations_schema"):
        print("-" * 68)
        for v in rapport["violations_schema"]:
            print(f"  [SCHEMA] {v}")
    for note in rapport.get("notes", []):
        print(f"  note: {note}")
    print("-" * 68)
    code, raisons = conformite.evaluer(rapport, statut_extraction)
    if code == 0:
        print("  CONFORMITÉ : OUI")
    else:
        print(f"  CONFORMITÉ : NON (sortie {code}) — " + " · ".join(raisons))
    print("=" * 68)


def sauvegarder(rapport, statut_extraction, source, output_dir="logs/"):
    os.makedirs(output_dir, exist_ok=True)
    horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
    chemin = os.path.join(output_dir, f"rapport_v8_{horodatage}.json")
    code, raisons = conformite.evaluer(rapport, statut_extraction)
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump({"timestamp": datetime.now().isoformat(), "source": source,
                   "extraction": statut_extraction,
                   "conformite": {"code": code, "raisons": raisons}, **rapport},
                  f, ensure_ascii=False, indent=2)
    print(f"[Instrument V.8] Rapport sauvegarde : {chemin}")
    return chemin
