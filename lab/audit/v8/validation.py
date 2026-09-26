"""
Instrument V.8 — Validation du bloc contre son schéma publié.
===============================================================
Validateur écrit à la main, bibliothèque standard seule : l'instrument ne
doit dépendre de rien. Il couvre un **sous-ensemble déclaré** de JSON Schema
(draft 2020-12) — exactement ce dont le contrat d'émission a besoin :

  type · properties · required · enum · minimum · maximum · items ·
  additionalProperties (booléen)

plus les mots-clés d'annotation, sans effet : $schema · $id · title ·
description · $comment.

Tout autre mot-clé fait échouer le **chargement** du schéma. C'est le point
important : un validateur partiel qui ignorerait en silence un mot-clé qu'il
ne sait pas appliquer laisserait croire qu'une contrainte est vérifiée alors
qu'elle ne l'est pas — INV.5, échec bruyant, appliqué à l'outil lui-même.

Le schéma reste du JSON Schema standard : un tiers peut le rejouer avec
n'importe quel validateur conforme et doit obtenir le même verdict.
"""

import json
from pathlib import Path

MOTS_CLES_APPLIQUES = {"type", "properties", "required", "enum", "minimum",
                       "maximum", "items", "additionalProperties"}
MOTS_CLES_ANNOTATION = {"$schema", "$id", "title", "description", "$comment"}

CHEMIN_SCHEMA = Path(__file__).resolve().parents[2] / "schema" / "lab_audit_v8.schema.json"


class SchemaNonSupporte(ValueError):
    """Le schéma emploie un mot-clé que ce validateur n'applique pas."""


def charger_schema(chemin=CHEMIN_SCHEMA):
    with open(chemin, "r", encoding="utf-8") as f:
        schema = json.load(f)
    _controler_mots_cles(schema, "$")
    return schema


def _controler_mots_cles(noeud, chemin):
    if not isinstance(noeud, dict):
        raise SchemaNonSupporte(f"{chemin} : un schéma doit être un objet")
    inconnus = set(noeud) - MOTS_CLES_APPLIQUES - MOTS_CLES_ANNOTATION
    if inconnus:
        raise SchemaNonSupporte(
            f"{chemin} : mot-clé non appliqué par l'instrument : {', '.join(sorted(inconnus))}")
    if "additionalProperties" in noeud and not isinstance(noeud["additionalProperties"], bool):
        raise SchemaNonSupporte(f"{chemin} : additionalProperties doit être un booléen")
    for nom, sous in (noeud.get("properties") or {}).items():
        _controler_mots_cles(sous, f"{chemin}.{nom}")
    if "items" in noeud:
        _controler_mots_cles(noeud["items"], f"{chemin}[]")


def _est_du_type(valeur, attendu):
    # bool est une sous-classe d'int en Python : sans cette exclusion, `true`
    # passerait pour un entier et `true - true` pour un compte de leurres nul.
    if attendu == "object":
        return isinstance(valeur, dict)
    if attendu == "array":
        return isinstance(valeur, list)
    if attendu == "string":
        return isinstance(valeur, str)
    if attendu == "boolean":
        return isinstance(valeur, bool)
    if attendu == "integer":
        return isinstance(valeur, int) and not isinstance(valeur, bool)
    if attendu == "number":
        return isinstance(valeur, (int, float)) and not isinstance(valeur, bool)
    if attendu == "null":
        return valeur is None
    raise SchemaNonSupporte(f"type inconnu : {attendu}")


def valider(instance, schema, chemin="$"):
    """Retourne la liste des violations (chaînes lisibles). Vide = conforme."""
    violations = []

    attendu = schema.get("type")
    if attendu is not None:
        types = attendu if isinstance(attendu, list) else [attendu]
        if not any(_est_du_type(instance, t) for t in types):
            violations.append(f"{chemin} : type attendu {'|'.join(types)}, "
                              f"reçu {_nom_du_type(instance)}")
            return violations  # inutile de descendre dans une valeur du mauvais type

    if "enum" in schema and instance not in schema["enum"]:
        violations.append(f"{chemin} : valeur {json.dumps(instance, ensure_ascii=False)} "
                          f"hors énumération {schema['enum']}")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            violations.append(f"{chemin} : {instance} < minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            violations.append(f"{chemin} : {instance} > maximum {schema['maximum']}")

    if isinstance(instance, dict):
        proprietes = schema.get("properties") or {}
        for requis in schema.get("required", []):
            if requis not in instance:
                violations.append(f"{chemin} : champ requis absent « {requis} »")
        for nom, valeur in instance.items():
            if nom in proprietes:
                violations += valider(valeur, proprietes[nom], f"{chemin}.{nom}")
            elif schema.get("additionalProperties") is False:
                violations.append(f"{chemin} : champ non déclaré « {nom} »")

    if isinstance(instance, list) and "items" in schema:
        for i, element in enumerate(instance):
            violations += valider(element, schema["items"], f"{chemin}[{i}]")

    return violations


def _nom_du_type(valeur):
    if isinstance(valeur, bool):
        return "boolean"
    if isinstance(valeur, int):
        return "integer"
    if isinstance(valeur, float):
        return "number"
    if isinstance(valeur, str):
        return "string"
    if isinstance(valeur, list):
        return "array"
    if isinstance(valeur, dict):
        return "object"
    if valeur is None:
        return "null"
    return type(valeur).__name__
