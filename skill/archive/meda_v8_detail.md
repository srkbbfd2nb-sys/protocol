# MEDA V.8 — Couche ARCHIVE (détail, hors contexte)

> Source de la couche active. Citations `module:ligne` sur `tj_v72/02_meda`. Passe fraîche.

---

## 1 · Les 8 dimensions & plages

Plage 8-24. Niveaux : **Light** [8-13] · **Complet** [14-19] · **Expert** [20-24].
Dimensions : 1. Nature de la demande · 2. Domaine · 3. Sources requises · 4. Longueur estimée · 5. Risque d'erreur · 6. Modules nécessaires · 7. Système réel · 8. Action technique. Chaque dimension scorée /3.

## 2 · Signaux dérivés

- **Phase 1.5 (EXT-01)** : si Système réel ≥ 2 et niveau ≥ Complet.
- **EXT-02** : si Action technique ≥ 2 et niveau ≥ Complet.
- **EEO** : production d'artefact fonctionnel.
- **MREO** : artefact analysable / déconstruction.
- **Contextualisation 5 couches** : interne · externe · direct · indirect · implicite.
- **Maïeutique auto** : sur signal de délégation. **V.8** : le signal provient de MAMD Champ 8 (multi-couches sémantique), non plus des patterns littéraux V.7.1 (« écris-moi »… — garde-fou anti-rigidité S3).

## 3 · Couplages (réf. Graphe V.8, `02_meda:509-510`)

REÇOIT : Noyau (déclencheur auto) · Lyra P1 (complexité) · EXT-01 (système réel) · EXT-02 (retour vérification) · Noyau Bloc C (⚠/✗) · Utilisateur (commandes, `#maieutique`). **+ V.8 : MAMD (signature, F)**. ENVOIE : modules aval (profondeur) · F-04 (maïeutique) · MECA (profondeur scoring) · EXT-01/EXT-02/F-02 (signaux dérivés). ACA↔MEDA (`17_aca:431`).

## 4 · Décisions de construction

- **Pôle ① seul** (correction cycle 22) : MEDA *évalue* la demande (acte épistémique) ; il *sert* ③ en dirigeant la production, mais n'est pas ③ lui-même. Note « sert ③ » sans double-rattachement (évite la conflation, cohérent Ax2-A2).
- **AMORCE→PROCESSUS→SORTIE** : AMORCE = auto post-MAMD ; PROCESSUS = scoring 8 dim → niveau → routing ; SORTIE = ligne MEDA Niveau/Score + signaux.
- **Coupe S4** : niveau + dimensions (noms) + maïeutique-sur-délégation + couplages clés → actif ; plages détaillées + patterns contextualisation + dégradation Pipeline → archive.

## 5 · Anomalie traitée

**Fragilité littérale de la détection délégation** → délégée à MAMD Champ 8 (sémantique). MEDA reçoit le signal, ne le calcule plus par regex de phrases. Cohérent avec la correction F-04 (pilote).

---

*Module behavioral ① V.8. Route selon MAMD + heuristiques. Vague 2.*
