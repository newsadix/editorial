---
name: scoring-editorial
description: Méthodologie de scoring bidimensionnel pour évaluer la pertinence et la valeur documentaire des articles. Paramétrable — le média peut injecter ses propres critères de pertinence. Charger pour le tri et la sélection d'articles.
source: "Adapté de FLTR — scoring.md (scores de pertinence et documentaire)"
---

# Méthodologie de scoring éditorial

---

## Score de pertinence (0-10)

Évalue la pertinence de l'article par rapport aux dimensions thématiques du média ET sa valeur activable (exemples concrets, bonnes pratiques reproductibles).

### Calcul

| Composante | Points max | Critères |
|------------|------------|----------|
| Intensité par critère thématique | 4 | 0-2 points par dimension touchée (divisé par le nombre de dimensions / 2) |
| Multi-dimensionnalité | 2 | 1 dimension = 0 / 2 dimensions = +1 / 3+ dimensions = +2 |
| **Activabilité** | 3 | Exemples concrets + mécanismes explicités + reproductibilité |
| Qualité source | 1 | Source fiable et originale |

> **NOTE PARAMÉTRABLE** : Les critères d'intensité sont définis par le média. le média d'origine utilise 5 dimensions thématiques ; un autre média peut définir les siennes (géopolitique, économie, société, environnement, culture, etc.). Le mécanisme de scoring reste identique : chaque dimension est notée sur 2 points, le total est rapporté à 4 points maximum.

### Détail de l'activabilité (0-3 points)

L'activabilité mesure la capacité de l'article à inspirer l'action par l'exemple positif.

| Critère | Points | Ce qu'on cherche |
|---------|--------|------------------|
| Exemple concret existant | +1 | Initiative réelle, documentée (nom, lieu, contexte) — pas hypothétique |
| Mécanisme explicité | +1 | L'article explique POURQUOI ça marche (pas juste "ça marche") |
| Reproductibilité | +1 | Conditions de réplication identifiées OU coalition activable nommée |

**Exemples activables :**
- Bonne pratique déployée quelque part (ville, entreprise, pays)
- Innovation systémique en action avec résultats mesurables
- Coalition ou mouvement organisé avec résultats documentés
- Législation ou régulation ayant produit des effets observables

**Contre-exemples (score activabilité = 0) :**
- Article purement alarmiste sans piste de solution
- Théorie/recommandation sans ancrage dans le réel
- "Il faudrait que..." sans exemple de qui l'a déjà fait

### Malus (appliqués au score total)

| Condition | Malus | Raison |
|-----------|-------|--------|
| Article purement alarmiste, aucune piste | -1 | Ne correspond pas à la posture "liberté positive" |
| Théorie/opinion sans ancrage concret | -1 | Pas activable, pas inspirant |

### Seuil d'entrée

- Score < 7 : L'article n'entre pas dans la base
- Score >= 7 : L'article entre dans la base de traitement

> Ce seuil est paramétrable. Un média plus sélectif peut monter à 8 ; un média en phase de constitution de base peut descendre à 6 temporairement.

### Philosophie du scoring

> **Objectif** : Sélectionner des articles qui montrent que "c'est possible" — des exemples de liberté positive en action, pas des constats d'impuissance ou des leçons théoriques.
>
> Un article score haut quand il permet au lecteur de dire : *"Tiens, ça se fait déjà quelque part, et voilà comment."*

---

## Score documentaire (0-10)

Évalue la valeur documentaire de l'article (qualité des sources, citations, données).

### Calcul

| Critère | Points | Description |
|---------|--------|-------------|
| Citations nommées | 0-2 | Personnes citées avec nom et fonction |
| Données chiffrées sourcées | 0-2 | Statistiques, montants, pourcentages avec source |
| Cas concret documenté | 0-2 | Exemple détaillé avec contexte |
| Acteurs identifiés | 0-2 | Organisations/personnes avec rôle précisé |
| Originalité source | 0-2 | 0 = agrégateur / 1 = média / 2 = source primaire |

### Matrice de stockage

| Pertinence | Documentaire | Action de stockage |
|------------|--------------|-------------------|
| < 7 | — | Ne rentre pas dans la base |
| >= 7 | < 5 | Métadonnées + analyse seulement |
| >= 7 | 5-7 | + Résumé structuré (500 mots max) |
| >= 7 | >= 8 | + Contenu complet archivé + Citations clés |

---

## Signaux de basculement

Pour chaque piste d'action systémique, définir des signaux de basculement.

### Format

- "On saura que ça marche quand..." (narratif, pas quantitatif)
- Double horizon : signaux précoces (6-12 mois) + impact structurel (3-5 ans)
- Fonction : boussole heuristique + outil rhétorique

### Exemple

> **Piste** : Coalition médias européens pour négociation collective avec les plateformes
>
> **Signal précoce** : "On saura que ça avance quand au moins 3 groupes de presse de pays différents annonceront une structure juridique commune."
>
> **Impact structurel** : "On saura que ça marche quand les plateformes négocieront des accords-cadres européens plutôt que des deals bilatéraux."

---

## Calibrage et adaptation

### Pour un nouveau média

1. Définir ses dimensions thématiques (3 à 7 recommandées)
2. Pour chaque dimension, lister 3-5 sous-critères d'intensité
3. Appliquer le mécanisme de scoring tel quel
4. Ajuster le seuil d'entrée après 50-100 articles évalués
5. Documenter les cas limites pour affiner les critères

### Erreurs courantes

- Scorer trop généreusement par biais de confirmation (l'article "nous plaît" donc il score haut)
- Confondre qualité journalistique et pertinence thématique (un article peut être excellent mais hors sujet)
- Ignorer le score documentaire (un article pertinent mais mal sourcé a une valeur limitée)
- Oublier l'activabilité (les constats sans pistes ne font pas avancer le lecteur)
