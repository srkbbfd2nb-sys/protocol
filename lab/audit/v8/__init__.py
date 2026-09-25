"""
audit/v8/ — Instrument V.8 resémantisé (étape Out, driver 2)
===============================================================
Patron MECA-JSON généralisé : l'instrument vérifie des DONNÉES STRUCTURÉES
(bloc LAB AUDIT JSON émis par le modèle, spec emission_audit_v8.md), jamais
de la prose par regex (leçon L3-instrument, tâche 5 empirique).

Vérifications : présence · complétude · cohérence structurelle inter-champs.
La qualité sémantique du contenu reste au modèle-auditeur (palier A).

N'altère RIEN de l'existant : audit/ (V.7.1.1) et audit/v72/ intacts.
Point d'entrée dédié : audit_v8.py (racine) — l'intégration main.py viendra
avec Dep (loader). Réf. : OUT_INSTRUMENT_V8.md.
"""

__version__ = "8.0.0"
