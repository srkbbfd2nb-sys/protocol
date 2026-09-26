"""
Instrument V.8 — vérificateur du bloc LAB AUDIT JSON.
===============================================================
Audite une réponse EXTERNE : un texte arbitraire contenant le bloc d'audit
qu'un modèle sous protocole émet en fin de cycle. Il ne génère rien, ne
contacte rien, n'a besoin d'aucune clé : il lit un texte et rend un verdict.

C'est volontaire. Le protocole pose qu'un auditeur logé dans le même contexte
que le producteur mesure sa propre cohérence, pas sa justesse. Le vérificateur
est donc **hors du contexte de production**, et son entrée est une trace, pas
une conversation.

Usage :
  python audit_v8.py --input-file reponse.txt
  python audit_v8.py --stdin        (coller le texte, finir par Ctrl-D / Ctrl-Z)

Codes de sortie : 0 conforme · 1 non conforme · 2 inexploitable (bloc absent,
JSON illisible, fichier introuvable). Le bloc est validé contre
schema/lab_audit_v8.schema.json ; un bloc trouvé sans ses délimiteurs est lu,
mais ne sort jamais en 0.

Portée : il vérifie la **conformité et la cohérence interne** d'une
auto-déclaration. Pas sa véracité. Un modèle qui mentirait de façon cohérente
passerait — cette limite est documentée, pas contournée.
"""

import sys
import os

if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from audit.v8.json_extractor import extraire_bloc
from audit.v8.verifier import verifier
from audit.v8 import report_v8
from audit.v8 import conformite


def auditer_texte(texte: str, source: str = "texte"):
    data, statut = extraire_bloc(texte)
    rapport = verifier(data)
    report_v8.imprimer(rapport, statut)
    report_v8.sauvegarder(rapport, statut, source)
    return rapport, statut


def code_de_sortie(rapport, statut) -> int:
    """
    0 = conforme · 1 = non conforme · 2 = bloc inexploitable.

    Un instrument qui rend toujours 0 est un rapport, pas un garde-fou : aucune
    chaine d'integration ne peut s'y brancher. La non-conformite doit etre
    bruyante au sens d'INV.5, y compris pour un programme appelant.
    La decision elle-meme vit dans audit/v8/conformite.py, que le rapport lit aussi.
    """
    return conformite.evaluer(rapport, statut)[0]


def main():
    args = sys.argv[1:]
    if "--help" in args or "-h" in args or not args:
        print(__doc__)
        return

    texte, source = None, "texte"
    if "--input-file" in args:
        idx = args.index("--input-file")
        if idx + 1 < len(args):
            chemin = args[idx + 1]
            if not os.path.isfile(chemin):
                # 2, pas 1 : un chemin faux n'est pas une reponse non conforme.
                # Sortir en 1 ferait passer une CI qui attend un refus sans
                # avoir jamais lu le fichier.
                print(f"ERREUR — fichier introuvable : {chemin}")
                sys.exit(2)
            with open(chemin, "r", encoding="utf-8") as f:
                texte = f.read()
            source = chemin
    elif "--stdin" in args:
        print("[Instrument V.8] Colle la reponse, puis Ctrl-Z (Windows) / Ctrl-D :")
        texte = sys.stdin.read()
        source = "stdin"

    if texte is None:
        print("ERREUR — fournir --input-file <chemin> ou --stdin.")
        sys.exit(1)

    rapport, statut = auditer_texte(texte, source)
    sys.exit(code_de_sortie(rapport, statut))


if __name__ == "__main__":
    main()
