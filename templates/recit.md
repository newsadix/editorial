# Template : Récit / Reportage immersif

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-RECIT` |
| **User Need primaire** | `inspire_me` |
| **User Need secondaire** | `keep_me_engaged` |
| **Longueur** | Long : 1500-4000 mots |
| **Signé** | Oui — radar de transparence obligatoire |
| **Supervision** | Validation humaine systématique |

## Principe

Le récit est le format le plus littéraire. Il raconte une histoire vraie à travers des scènes, des personnages, des tensions et des résolutions. C'est le seul template où la narration domine et où les bits factuels sont au service de l'histoire (et non l'inverse).

C'est aussi le format le plus risqué par rapport à la charte : la frontière entre récit immersif et storytelling fictif doit être tenue. Chaque scène décrite a été observée ou documentée. Chaque dialogue est réel.

## Prérequis

1. **Terrain.** Le récit repose idéalement sur un reportage de terrain (observation directe, immersion, rencontres). Sans terrain, c'est un décryptage narratif, pas un récit
2. **Personnages réels.** Au moins 1 personne dont le parcours incarne l'enjeu raconté
3. **Faits vérifiables.** La narration s'appuie sur des faits documentés et sourcés
4. **Auteur avec radar renseigné**

## Déclencheur

Commandé. Jamais automatique. Typiquement :

- Un sujet de fond qui mérite un traitement immersif
- Un terrain accessible (lieu, événement, communauté)
- Contenu planifié pour les User Needs `inspire_me` ou `keep_me_engaged`

## Composition en bits

| Bit | Type | Obligatoire | Quantité | Origine | Rôle |
|-----|------|-------------|----------|---------|------|
| Faits documentés | `fait` | Oui | 3-8 | Base F1 + terrain | Ancrage factuel |
| Observations terrain | `fait` | Oui | 2-6 | Produit par l'auteur | Scènes vécues |
| Contexte | `contexte` | Oui | 2-4 | Base F1 + auteur | Cadrage de l'enjeu |
| Témoignages | `point_de_vue` | Oui | 2-6 | Terrain | Paroles des personnages |
| Données | `donnée` | Non | 0-3 | Base F1 | Chiffres d'ancrage |
| Éléments multimédia | (métadonnée) | Non | 0-5 | Terrain | Photos, sons, vidéos |

## Structure de sortie

La structure du récit est **narrative**, pas pyramidale. Elle ne suit pas l'ordre de l'information mais celui de l'histoire.

```
BLOC 1 — OUVERTURE (scène)
  Un lieu, un moment, un personnage.
  Le lecteur est immergé. Pas de contexte abstrait :
  une image concrète, sensorielle.

BLOC 2 — ENJEU (transition)
  Ce que cette scène représente.
  Le pont entre l'histoire individuelle et l'enjeu collectif.
  Les faits et données qui ancrent le récit dans le réel.

BLOC 3 — DÉVELOPPEMENT (narration)
  L'histoire se déploie. Alternance entre :
  - Scènes (observation de terrain)
  - Contexte (bits qui éclairent l'enjeu)
  - Voix (témoignages des personnages)
  Tension narrative : obstacle, transformation, enjeu.

BLOC 4 — RÉSOLUTION / OUVERTURE
  Pas nécessairement un happy end.
  Ce qui a changé (ou pas). Ce que l'histoire révèle.
  Retour au concret : un détail, un mot, un geste.

ENCADRÉ FACTUEL (optionnel mais recommandé)
  Les faits et données clés extraits du récit,
  présentés sous forme synthétique pour le lecteur
  qui veut les faits sans la narration.

SIGNATURE + RADAR
ATTRIBUTION
```

## Règles strictes

1. **Zéro fiction.** Chaque scène a été observée, rapportée ou documentée. Pas de reconstitution imaginée (charte §1 : « aucun storytelling fictif »)
2. **Dialogues réels.** Les dialogues sont des citations exactes ou des reformulations fidèles, jamais des inventions
3. **Transparence sur la méthode.** L'auteur indique comment il a observé les scènes (présent sur place, reconstitution d'après témoignages, documents)
4. **L'enjeu dépasse l'anecdote.** Le récit raconte une histoire individuelle qui éclaire un enjeu collectif
5. **Encadré factuel.** Le lecteur qui veut les faits sans la narration doit pouvoir les trouver
6. **Consentement.** Les personnes dont la vie est racontée ont donné leur consentement (sauf figures publiques dans l'exercice de leurs fonctions)

## Contrôles qualité

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur | 1500-4000 mots | Alerte si hors bornes |
| Scènes terrain | Au moins 2 scènes d'observation directe | Blocage — ce n'est pas un récit |
| Personnages | Au moins 1 personnage identifié et cité | Blocage |
| Faits sourcés | Chaque fait du récit renvoie à un bit sourcé | Vérification |
| Encadré factuel | Présent | Alerte |
| Radar | Complet | Blocage |
| Vérification fiction | Aucune scène non documentée | Revue humaine approfondie |

## Distribution

| Canal | Format | Délai |
|-------|--------|-------|
| Site web | Long-read immersif, multimédia intégré, encadré factuel | Dès validation |
| Newsletter | Teaser narratif (ouverture tronquée) + lien | Prochain digest ou envoi dédié |
| Instagram | Stories : scènes visuelles du terrain | < 6h |
| Audio | Version podcast narratif (adapté, pas lu) | < 24h |

---

Version : 0.1 | Date : 2026-04-14
