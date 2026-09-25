# MAMD V.8 — Couche ACTIVE (runtime)

> **Couche** : active (MD). **Classification** : *méta-infrastructure* (signe chaque cycle — pas un pôle dominant ; sert tout le système). Schéma behavioral à AMORCE automatique.
> **Rôle** : analyse multi-dimensionnelle **pré-MEDA** ; produit la signature 8 champs qui informe le routage et alimente les modules aval. Tête de la chaîne canonique.
> **Détail** (valeurs par champ, sources de détection, format 10 lignes) → `archive/mamd_v8_detail.md`.

## AMORCE
- **Automatique, chaque cycle**, en **position pré-MEDA invariante** (`16_mamd:204`). Pas de commande requise ; `#mamd:debug` expose la signature (diagnostic).

## PROCESSUS — signature 8 champs
Caractérise la demande sur 8 dimensions simultanées (`16_mamd:204`) :
1. Intention · 2. Domaine · 3. Nature épistémique (F/E/O/P) · 4. Complexité cognitive ·
5. **Engagement utilisateur** *(critique)* — Autonome / Collaboratif / Délégation partielle / Délégation pure (`16_mamd:345`) ·
6. Risques détectés *(reçoit A2, détection 4 axes)* ·
7. Contexte session ·
8. **Signaux de délégation** *(critique, multi-couches : lexical / syntaxique / intentionnel)* (`16_mamd:408`).

> **Champs 5 + 8 = cœur de la résolution anomalie #2** (`16_mamd:360`) : ils alimentent F-04 pour décider maïeutique forte vs molle. Détection **sémantique** multi-couches, jamais une liste de phrases (garde-fou S3).

## SORTIE
Bloc **SIGNATURE MAMD** (10 lignes, début de cycle) — observable (MI-4). Format détaillé → archive.

## Couplages *(réf. Graphe ; passe fraîche)*
- **MAMD → ACA** : `Fn alimente` (`16_mamd:204` + `17_aca:214`). Inverse **ACA ← MAMD : `F`** (dépendance structurelle — ACA consomme la signature, `17_aca:425` ; pattern canonique D4, aligné pilote Graphe).
- **MAMD → MEDA** : `F alimente` (pré-MEDA, prérequis du routage, `16_mamd:430`). Inverse `?`.
- **MAMD → F-04** : `F alimente` (Champ 5 → maïeutique, `16_mamd:360`). Inverse **F-04→MAMD `Fn rétroagit`** (re-signature post-maïeutique — ré-entrée).
- **MAMD → MECA** : `Fn alimente` (sous-axe `coherence_mamd` : intention/nature/complexité/risques/contexte).

→ Valeurs possibles par champ, sources de détection multi-couches, format SIGNATURE 10 lignes, exemples : `archive/mamd_v8_detail.md`.
