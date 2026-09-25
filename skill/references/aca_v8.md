# ACA V.8 — Couche ACTIVE (runtime)

> **Couche** : active (MD). **Classification** : *méta-infrastructure* (orchestre chaque cycle, ne produit pas de contenu propre — `17_aca:223`). Schéma behavioral à AMORCE automatique.
> **Rôle** : activation contextuelle automatique **post-MAMD**, avant l'orchestration invariante. Décide quels modules activer selon la signature MAMD.
> **Détail** (8 règles, 5 principes, commandes) → `archive/aca_v8_detail.md`.

## AMORCE
- **Automatique, chaque cycle**, en **position post-MAMD pré-orchestration invariante** (`17_aca:216`) — non négociable : ACA consomme la signature MAMD.
- **Commandes** (couche de contrôle manuel par-dessus) : `#aca:off` (cycle), `#aca:off:session` — désactivation globale.

## PROCESSUS — activation contextuelle
Régi par **5 principes** (`17_aca:214`) : (1) détection avant activation · (2) réversibilité explicite · (3) **priorité aux commandes manuelles** · (4) trace permanente (source MAMD) · (5) désactivation globale possible.
Évalue ses règles d'activation contre la signature MAMD → active/désactive les modules du cycle. **N'altère pas le contenu** d'un module, seulement son *déclenchement* et son *niveau*.

## SORTIE
Bloc **ACTIVATIONS ACA** (modules activés · non activés malgré signal · commandes détectées · état). Observable (MI-4).

## Couplages *(réf. Graphe ; passe fraîche)*
- **ACA ← MAMD** : `F alimente` (consomme la signature, `17_aca:425`). *(inverse du MAMD→ACA `Fn`.)*
- **ACA → F-04** : `Fn active` — déclenche la maïeutique forte/molle selon Champ 5+8 (`17_aca:437-438`). *Résolution conjointe anomalie #2.* Inverse `?`.
- **ACA → F-03** : `Fn active` (`17_aca:443`). Inverse `?`.
- **ACA → Lyra** : `Fn active` — clause éthique sur risque Champ 6 (`17_aca:449`) ; **Lyra reste seul maître de l'application** (autorité non-désactivable). Inverse `?`.
- **ACA ↔ MEDA** : `Fn active` (`17_aca:431`) — bidirectionnel partiel.

> **Garantie** : ACA *propose* l'activation ; en fallback (`#aca:off`), retour aux heuristiques V.7.1 — la résolution structurelle de l'anomalie #2 n'est alors plus garantie (à usage diagnostique).

→ 8 règles d'activation détaillées, 5 principes régulateurs, portabilité des commandes : `archive/aca_v8_detail.md`.
