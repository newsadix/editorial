---
name: format-synthese
description: Format de synthèse multi-articles — fusionner 2-5 articles liés en une analyse croisée originale qui apporte plus de valeur que la somme des parties. Charger pour les analyses croisées, évolutions temporelles, patterns transversaux et dossiers thématiques.
source: "Adapté de FLTR — formats/synthese.md"
---

# Instructions de format — Synthèse multi-articles

## Objectif

Fusionner 2-5 articles liés en une analyse croisée originale qui apporte plus de valeur que la somme des parties.

## Types de synthèses

| Type | Description | Exemple |
|------|-------------|---------|
| **Analyse croisée** | Angles différents sur un même sujet | 3 articles sur une même régulation vus par 3 pays |
| **Évolution temporelle** | Suivi d'un sujet dans le temps | Saga d'un dossier sur 6 mois |
| **Pattern transversal** | Même dynamique dans des domaines différents | Un même mécanisme dans 3 secteurs |
| **Dossier thématique** | Compilation exhaustive sur un thème | Tout sur un texte de loi majeur |

---

## Structure de la synthèse

### 1. Angle éditorial (fourni par l'utilisateur ou généré)

- **Définit la direction** de la synthèse
- **Ne force pas** les articles dans un moule
- **Exemple** : "Comment l'Europe et les États-Unis divergent sur la régulation des plateformes"

### 2. Introduction (150-200 mots)

- Poser la problématique transversale
- Annoncer les articles synthétisés (sans les lister mécaniquement)
- Donner envie de lire

### 3. Corps de la synthèse (500-800 mots)

- **Pas de résumé séquentiel** des articles
- **Analyse croisée** : faire dialoguer les sources
- **Identifier les convergences et divergences**
- **Extraire les patterns** non visibles dans les articles individuels

### 4. Points de vigilance consolidés

Agréger les points de vigilance des articles sources :
- Éliminer les redondances
- Identifier les risques systémiques
- Nuancer si les sources se contredisent

### 5. Pistes systémiques consolidées

Fusionner et enrichir les pistes d'action :
- Garder les plus pertinentes
- Combiner les complémentaires
- Ajouter des pistes nouvelles qui émergent de la synthèse

### 6. Citations clés

Extraire les meilleures citations des articles sources :
- Celles qui incarnent le mieux les enjeux
- Celles qui se répondent entre articles
- Maximum 3-4 citations

---

## Règles de synthèse

### A faire

- Apporter une valeur analytique nouvelle
- Faire émerger des patterns invisibles dans les articles individuels
- Citer explicitement les sources ("Comme le souligne [Source A]...")
- Identifier les tensions ou contradictions entre sources

### A éviter

- Simple juxtaposition des résumés
- Forcer une cohérence artificielle
- Ignorer les nuances ou contradictions
- Ajouter des informations non présentes dans les sources

---

## Scoring de la synthèse

### Score de pertinence (agrégé)

```
score_synthese = max(scores_articles) + bonus_transversal
```

Bonus transversal :
- +1 si 2 dimensions thématiques différentes couvertes
- +2 si 3+ dimensions thématiques différentes couvertes
- +1 si pattern systémique identifié

### Score documentaire (agrégé)

```
score_doc_synthese = moyenne(scores_doc_articles) + bonus_citations
```

Bonus citations :
- +1 si citations complémentaires identifiées
- +1 si contradiction sourcée documentée

---

## Format de sortie JSON

```json
{
  "type": "analyse_croisee|evolution_temporelle|pattern_transversal|dossier",
  "angle_editorial": "L'angle choisi pour cette synthèse",

  "articles_sources": [
    {"id": "xxx", "titre": "...", "contribution": "Ce que cet article apporte à la synthèse"},
    {"id": "xxx", "titre": "...", "contribution": "..."}
  ],

  "scoring": {
    "pertinence": {
      "total": 9,
      "max_articles": 8,
      "bonus_transversal": 1
    },
    "documentaire": {
      "total": 7,
      "moyenne_articles": 6,
      "bonus_citations": 1
    }
  },

  "synthese": {
    "titre": "Titre de la synthèse",
    "introduction": "...",
    "corps": "Analyse croisée complète (500-800 mots)",
    "points_vigilance": "Points de vigilance consolidés",
    "patterns_identifies": ["Pattern 1", "Pattern 2"]
  },

  "pistes_systemiques": [
    {
      "type": "coalition",
      "emoji": "...",
      "action": "...",
      "origine": "nouvelle|article_1|fusion"
    }
  ],

  "citations_cles": [
    {
      "verbatim": "...",
      "auteur": "...",
      "source_article_id": "xxx",
      "pertinence_synthese": "Pourquoi cette citation est clé pour la synthèse"
    }
  ],

  "dimensions": ["[DIMENSION_1]", "[DIMENSION_2]", "[DIMENSION_3]"],
  "dimension_majeure": "[DIMENSION_1]",

  "user_needs": {
    "primary": "give_me_perspective",
    "secondary": ["educate_me"],
    "direction": "understanding"
  },
  "distribution": {
    "template": "perspective",
    "linkedin_format": "A",
    "facebook_perso": true,
    "bluesky": true,
    "facebook_page": true
  }
}
```

---

## Rappels

La synthèse s'appuie sur la charte éditoriale et le framework analytique du média. Ces documents priment sur le format. Les cadres théoriques restent invisibles dans le texte final.
