# Template : Portrait / Profil

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-PORTRAIT` |
| **User Need primaire** | `keep_me_engaged` |
| **User Need secondaire** | `give_me_perspective` |
| **Longueur** | Intermédiaire à long : 800-2000 mots |
| **Signé** | Oui — radar de transparence obligatoire |
| **Supervision** | Validation humaine systématique |

## Principe

Le portrait raconte une personne à travers les faits. C'est le template le plus narratif de la Famille 2, mais il reste ancré dans la rigueur factuelle : chaque affirmation biographique est un bit sourcé, chaque citation est attribuée.

La valeur ajoutée du journaliste : la sélection des faits, l'angle narratif, les observations de première main (rencontre, interview), la mise en perspective du parcours.

## Prérequis

1. **Bits `même_acteur` existants.** Le sujet du portrait a déjà fait l'objet de dépêches F1
2. **Contact direct.** Le portrait implique idéalement une rencontre ou un échange direct avec le sujet (pas obligatoire pour les portraits post-mortem ou de figures inaccessibles)
3. **Auteur avec radar renseigné**, en particulier : relation éventuelle avec le sujet

## Déclencheur

Commandé. Jamais automatique. Typiquement :

- Une personne est au cœur de l'actualité et mérite un éclairage plus profond que la dépêche
- Un sujet de fond nécessite d'incarner un enjeu à travers une personne
- Contenu de type « keep_me_engaged » / « inspire_me » planifié en rédaction

## Composition en bits

| Bit | Type | Obligatoire | Quantité | Origine | Rôle |
|-----|------|-------------|----------|---------|------|
| Faits biographiques | `fait` | Oui | 3-8 | Base F1 + recherche auteur | Parcours factuel |
| Faits d'actualité | `fait` | Oui | 2-4 | Base F1 | Ancrage dans l'actualité |
| Contexte de parcours | `contexte` | Oui | 2-4 | Produit par l'auteur | Mise en perspective du parcours |
| Citations directes | `point_de_vue` | Non | 0-4 | Interview / déclarations | Parole du sujet |
| Regards croisés | `point_de_vue` | Non | 0-3 | Tiers (collègues, adversaires, proches) | Points de vue sur le sujet |
| Données | `donnée` | Non | 0-3 | Base F1 | Chiffres pertinents |

## Structure de sortie

```
BLOC 1 — SCÈNE D'OUVERTURE (3-5 phrases)
  Un moment, un lieu, un geste. Le lecteur entre dans le portrait 
  par une image concrète, pas par une bio Wikipedia.
  Observation de première main si possible.

BLOC 2 — PARCOURS (faits biographiques clés)
  Les étapes qui définissent le sujet.
  Sélection éditoriale : pas un CV, mais les moments qui éclairent 
  l'enjeu actuel.
  Chaque fait sourcé.

BLOC 3 — ENJEU ACTUEL (2-4 phrases)
  Pourquoi ce portrait maintenant.
  Lien avec l'actualité couverte en F1.
  Ce que cette personne incarne ou représente dans le débat.

BLOC 4 — REGARDS CROISÉS (3-6 phrases)
  Ce que les autres disent du sujet.
  Au moins 2 perspectives (un allié + un contradicteur, idéalement).
  Chaque regard attribué.

BLOC 5 — SCÈNE DE FERMETURE (2-4 phrases)
  Retour à l'humain. Un détail, un mot, un geste qui reste.
  Pas de conclusion moralisatrice — le lecteur se fait son idée.

SIGNATURE + RADAR
ATTRIBUTION
```

## Règles strictes

1. **Pas d'hagiographie.** Le portrait présente la personne avec ses zones d'ombre. Les regards croisés incluent des voix critiques
2. **Pas de fiction.** Les scènes d'ouverture et de fermeture sont des observations réelles, pas des reconstitutions inventées (charte : « aucun storytelling fictif »)
3. **Chaque fait biographique est sourcé.** Même les plus anciens
4. **Les citations sont exactes.** Pas de paraphrase présentée comme citation
5. **Transparence sur la relation.** Le radar indique explicitement si l'auteur connaît personnellement le sujet

## Contrôles qualité

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur | 800-2000 mots | Alerte si hors bornes |
| Structure | 5 blocs identifiables | Alerte qualité |
| Scène d'ouverture | Bloc 1 présent et narratif (pas biographique) | Revue humaine |
| Regards croisés | Au moins 2 voix distinctes | Alerte — risque d'hagiographie |
| Faits sourcés | Chaque fait biographique renvoie à un bit sourcé | Vérification |
| Radar relation | Le champ « relation avec le sujet » est renseigné | Blocage publication |
| Lien actualité | Le portrait est ancré dans un sujet F1 existant | Vérification |

## Distribution

| Canal | Format | Délai |
|-------|--------|-------|
| Site web | Texte complet, format long-read | Dès validation |
| Newsletter | Teaser (scène d'ouverture tronquée) + lien | Prochain digest |
| Instagram | Carrousel visuel : scène + parcours + regards | < 4h |
| Audio | Lecture adaptée (format podcast narratif) | < 8h |

---

Version : 0.1 | Date : 2026-04-14
