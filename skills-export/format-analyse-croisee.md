---
name: format-analyse-croisee
description: Format complet pour la publication d'analyses croisées multi-sources sur site web — structure HTML, templates par besoin informationnel, règles de synthèse non-négociables et format JSON pivot étendu. Charger pour toute publication multi-sources.
source: "Adapté de FLTR — formats/cross-analysis.md + format-json-cross.md"
---

# Instructions de format — Analyse croisée web (multi-sources)

## Objectif

Publier une analyse croisée multi-sources sur le site de [NOM_MEDIA], avec la structure HTML standardisée.
L'analyse croisée fait dialoguer 2-5 articles qui couvrent le même sujet ou la même dynamique systémique.

## Audience cible

Abonnés et lecteurs de [NOM_MEDIA] — audience engagée, sensibilisée aux enjeux traités.

## Différence avec l'article individuel

| Article individuel | Analyse croisée |
|-------------------|-----------------|
| 1 source, 1 bookmark card | 2-5 sources, multiples bookmark cards |
| Analyse d'un fait ou d'une initiative | Dialogue entre sources, convergences, tensions |
| Pistes issues de l'article | Pistes ÉMERGENTES du croisement |
| ~1800 caractères de description | ~2500 caractères (plus riche) |
| Score standard | Score + bonus transversal + convergence |

---

## Choix du template

Le template dépend du champ `distribution.template` dans le JSON pivot.

| Template | User Needs | Quand l'utiliser |
|----------|-----------|-----------------|
| **Perspective** | `give_me_perspective`, `inspire_me`, `connect_me` | Analyse croisée approfondie, mise en perspective systémique |
| **Educate** | `educate_me`, `help_me` | Explication de mécanisme vu sous plusieurs angles |
| **Signal** | `update_me`, `keep_me_engaged` | Convergence rapide de signaux, panorama |

---

## Template PERSPECTIVE (défaut pour les analyses croisées)

### Structure HTML

#### 1. Chapeau éditorial

```html
<p><strong>{synthesis_framework}</strong></p>
```

Le fil conducteur en gras. 1-2 phrases qui posent la thèse éditoriale transversale.

#### 2. Sources (bookmark cards multiples)

```html
<p>{url_source_1}</p>

<p>{url_source_2}</p>

<p>{url_source_3}</p>
```

Le CMS transforme automatiquement chaque URL en bookmark card avec preview. Une ligne vide entre chaque URL.

#### 3. Description longue (analyse croisée)

```html
<p>{paragraphe_1}</p>

<p>{paragraphe_2}</p>

<p>{paragraphe_3}</p>

<p>{paragraphe_4}</p>
```

4-5 paragraphes narratifs qui font dialoguer les sources. Chaque paragraphe dans une balise `<p>` séparée. Double saut de ligne entre les paragraphes.

**Règles spécifiques :**
- JAMAIS de résumé séquentiel ("Le premier article dit... Le deuxième article dit...")
- TOUJOURS une structure analytique : convergences -> tensions -> angles morts -> synthèse
- Attribuer chaque fait à sa source : "Selon [Source A]..." ou "Comme le documente [Source B]..."
- Les chiffres sont intégrés au récit, pas listés

#### 4. Points de vigilance consolidés

```html
<p><em>Points de vigilance : {points_vigilance_consolides}</em></p>
```

En italique. Agréger les vigilances des sources, éliminer les redondances, identifier les risques émergents du croisement.

#### 5. Score (blockquote)

```html
<blockquote>{score}/[SCORE_REFERENCE] : Score sur l'échelle d'analyse [NOM_MEDIA], basé sur la grille d'évaluation éditoriale</blockquote>
```

#### 6. Lien méthodologique

```html
<p>[URL_METHODOLOGIE]</p>
```

#### 7. Séparateur

```html
<hr>
```

#### 8. Section "Et maintenant ?"

```html
<h3>Et maintenant ?</h3>

<p>Le croisement de ces sources fait apparaître des pistes d'action que chaque article seul ne révélait pas.</p>

<p>{emoji} <strong>{premiere_phrase_piste_1}</strong></p>

<p>{reste_contenu_piste_1}</p>

<p><em>{signaux_piste_1}</em></p>

<p>{emoji} <strong>{premiere_phrase_piste_2}</strong></p>

<p>{reste_contenu_piste_2}</p>

<p><em>{signaux_piste_2}</em></p>

<hr>
```

**Règle clé** : les pistes doivent être ÉMERGENTES du croisement. Si une piste pourrait apparaître dans n'importe lequel des articles individuels, elle n'est pas assez spécifique à la synthèse.

#### Emojis des pistes d'action

| Type d'action | Description |
|---------------|-------------|
| Action de coalition | Collectif organisé |
| Action individuelle | Choix personnels |
| Action de résistance | Opposition active |
| Action de confrontation | Pression directe |
| Action de célébration/soutien | Renforcement positif |

#### Structure de chaque piste

1. **Première phrase** en gras (titre de la piste — verbe à l'infinitif)
2. **Contenu développé** en paragraphes normaux
3. **Signaux** ("On saura que ça marche quand...") en italique

#### 9. Citation finale

```html
<p><strong>Ces pistes ne sont pas des recettes toutes faites, mais des points d'entrée pour repenser nos systèmes selon une logique de liberté positive : non pas limiter, mais augmenter nos capacités collectives d'action.</strong></p>
```

#### 10. Call to action

```html
<h3>On en discute ?</h3>

<p>Tu veux recevoir le flux quotidien des articles publiés <a href="[URL_SITE]">sur le site</a> ? Suis-moi sur [RESEAUX_SOCIAUX_LIENS] !</p>

<p>Tu as des remarques, des suggestions, ou tu veux discuter d'une idée pour avancer dans tes propres projets ? Connecte-toi et laisse-moi un commentaire ou jette un oeil directement <a href="[LIEN_AGENDA]">à mon agenda</a>.</p>
```

---

### Template PERSPECTIVE — HTML complet

```html
<p><strong>{synthesis_framework}</strong></p>

<p>{url_source_1}</p>

<p>{url_source_2}</p>

<p>{url_source_3}</p>

<p>{paragraphe_analyse_1}</p>

<p>{paragraphe_analyse_2}</p>

<p>{paragraphe_analyse_3}</p>

<p>{paragraphe_analyse_4}</p>

<p><em>Points de vigilance : {points_vigilance_consolides}</em></p>

<blockquote>{score}/[SCORE_REFERENCE] : Score sur l'échelle d'analyse [NOM_MEDIA], basé sur la grille d'évaluation éditoriale</blockquote>

<p>[URL_METHODOLOGIE]</p>

<hr>

<h3>Et maintenant ?</h3>

<p>Le croisement de ces sources fait apparaître des pistes d'action que chaque article seul ne révélait pas.</p>

<p>{emoji} <strong>{titre_piste_1}</strong></p>

<p>{contenu_piste_1}</p>

<p><em>{signaux_piste_1}</em></p>

<p>{emoji} <strong>{titre_piste_2}</strong></p>

<p>{contenu_piste_2}</p>

<p><em>{signaux_piste_2}</em></p>

<hr>

<p><strong>Ces pistes ne sont pas des recettes toutes faites, mais des points d'entrée pour repenser nos systèmes selon une logique de liberté positive : non pas limiter, mais augmenter nos capacités collectives d'action.</strong></p>

<h3>On en discute ?</h3>

<p>Tu veux recevoir le flux quotidien des articles publiés <a href="[URL_SITE]">sur le site</a> ? Suis-moi sur [RESEAUX_SOCIAUX_LIENS] !</p>

<p>Tu as des remarques, des suggestions, ou tu veux discuter d'une idée pour avancer dans tes propres projets ? Connecte-toi et laisse-moi un commentaire ou jette un oeil directement <a href="[LIEN_AGENDA]">à mon agenda</a>.</p>
```

---

## Template EDUCATE (multi-sources)

### Structure HTML EDUCATE

#### 1. Chapeau + Sources

```html
<p><strong>{synthesis_framework}</strong></p>

<p>{url_source_1}</p>

<p>{url_source_2}</p>
```

#### 2. Contexte croisé

```html
<h3>De quoi parle-t-on ?</h3>

<p>{contexte_1}</p>

<p>{contexte_2}</p>
```

2-3 paragraphes posant le sujet à partir de PLUSIEURS sources. Pas de jargon sans explication.

#### 3. Mécanisme (dialogue des sources)

```html
<h3>Comment ça fonctionne</h3>

<p>{mecanisme_1}</p>

<p>{mecanisme_2}</p>

<p>{mecanisme_3}</p>
```

3-4 paragraphes explicatifs. Faire dialoguer les sources : "Selon [Source A], le mécanisme repose sur... [Source B] nuance en montrant que..."

#### 4. Implications croisées

```html
<h3>Ce que ça implique</h3>

<p>{implication_1}</p>

<p>{implication_2}</p>
```

Ce que le CROISEMENT des sources révèle comme implications non visibles dans les articles individuels.

#### 5. Points de vigilance + Score + Pour aller plus loin + CTA

Structure identique au template Educate individuel, avec score et lien méthodologique.

---

## Template SIGNAL (multi-sources)

Format court pour convergence rapide de signaux.

```html
<p><strong>{synthesis_framework}</strong></p>

<p>{url_source_1}</p>

<p>{url_source_2}</p>

<p>{signal_1}</p>

<p>{signal_2}</p>

<blockquote>{score}/[SCORE_REFERENCE] : Score sur l'échelle d'analyse [NOM_MEDIA], basé sur la grille d'évaluation éditoriale</blockquote>

<p>[URL_METHODOLOGIE]</p>

<hr>

<h3>On en discute ?</h3>

<p>Tu veux recevoir le flux quotidien des articles publiés <a href="[URL_SITE]">sur le site</a> ? Suis-moi sur [RESEAUX_SOCIAUX_LIENS] !</p>

<p>Tu as des remarques, des suggestions, ou tu veux discuter d'une idée pour avancer dans tes propres projets ? Connecte-toi et laisse-moi un commentaire ou jette un oeil directement <a href="[LIEN_AGENDA]">à mon agenda</a>.</p>
```

Pas de section "Et maintenant ?", pas de pistes développées. La convergence des signaux suffit.

---

## Règles de synthèse (non-négociables)

### Factualité multi-source
- Chaque fait doit être attribué à sa source : "Selon [nom du média]..." ou "[Source] documente que..."
- Si deux sources se contredisent, le SIGNALER explicitement
- Ne JAMAIS présenter une convergence comme un fait si les sources ne le confirment pas indépendamment
- Les citations doivent indiquer leur source d'origine

### Synthèse vs juxtaposition
- INTERDIT : résumer les articles l'un après l'autre
- OBLIGATOIRE : organiser par thèmes transversaux (convergences, tensions, angles morts)
- Le lecteur ne doit PAS pouvoir deviner combien d'articles composent la synthèse
- JAMAIS mentionner le nombre d'articles sources ("sept cas", "trois enquêtes", "cinq analyses")

### Formules interdites
- INTERDIT : les accroches-formules creuses qui habillent le vide ("Un pattern troublant émerge de ces affaires", "Sept cas révèlent un paradoxe systémique", "Un fil rouge relie ces situations")
- INTERDIT : toute phrase qui annonce une révélation sans rien révéler ("Ce qui se dessine est préoccupant", "La convergence est frappante")
- OBLIGATOIRE : entrer directement dans le sujet avec des faits, des noms, des mécanismes concrets

### Pistes émergentes
- Les pistes d'action doivent naître du CROISEMENT, pas être recopiées des articles individuels
- Test : "Cette piste serait-elle identique si je n'avais lu qu'UN seul des articles ?" Si oui, elle n'est pas émergente.
- Privilégier les pistes qui exploitent des connexions entre les domaines couverts par les différentes sources

---

## Format JSON pivot étendu (analyse croisée)

```json
{
  "metadata": {
    "type": "cross-analysis",
    "date_analyse": "2025-03-13T14:30:00Z",
    "theme_commun": "Le thème qui relie les articles (max 120 caractères)",
    "articles_nombre": 3,
    "url_sources": [
      {
        "url": "https://...",
        "titre_original": "Titre de l'article",
        "source_nom": "Nom du média",
        "date_publication": "2025-03-10",
        "contribution": "Ce que cet article apporte spécifiquement à la synthèse (1 phrase)"
      }
    ]
  },

  "scoring": {
    "pertinence": {
      "total": 9,
      "intensite_dimensions": 3,
      "multi_dimensionnalite": 2,
      "activabilite": 3,
      "qualite_source": 1,
      "bonus_transversal": 1,
      "malus": 0
    },
    "documentaire": {
      "total": 8,
      "citations_nommees": 2,
      "donnees_chiffrees": 2,
      "cas_concret": 2,
      "acteurs_identifies": 1,
      "originalite_source": 1,
      "bonus_citations_croisees": 1
    },
    "convergence": {
      "sources_convergentes": 3,
      "tensions_identifiees": 1,
      "angles_complementaires": 2
    }
  },

  "analyse": {
    "nom": "Titre ÉDITORIALISÉ révélant l'enjeu systémique transversal — max 80 caractères",
    "description_courte": "Résumé en 1-2 phrases (max 280 caractères)",
    "synthesis_framework": "Le fil conducteur qui relie les sources entre elles. 1-2 phrases. JAMAIS de formule creuse.",
    "description_longue": "Analyse narrative fluide et éditoriale (~2500 caractères, 4-5 paragraphes).",
    "dimension_majeure": "[DIMENSION_1]",
    "dimensions": ["[DIMENSION_1]", "[DIMENSION_2]", "[DIMENSION_3]"],
    "points_vigilance": "Points de vigilance CONSOLIDÉS (max 600 caractères).",
    "tensions_identifiees": [
      {
        "description": "Description de la tension ou contradiction entre sources (1-2 phrases)",
        "sources": ["url1", "url2"],
        "implication": "Ce que cette tension révèle sur l'enjeu de fond"
      }
    ],
    "convergences": [
      {
        "theme": "Le point de convergence (max 60 caractères)",
        "description": "Ce sur quoi les sources s'accordent et pourquoi c'est significatif",
        "sources": ["url1", "url2", "url3"]
      }
    ]
  },

  "pistes_systemiques": [
    {
      "type": "coalition",
      "emoji": "...",
      "titre": "VERBE À L'INFINITIF + complément concis (max 80 caractères)",
      "description": "Explication DÉTAILLÉE (200-500 caractères). Les pistes doivent ÉMERGER de la synthèse.",
      "acteurs": ["société civile", "régulateurs"],
      "signal_structurel": "On saura que ça marche quand...",
      "origine": "emergente"
    }
  ],

  "citations_comparatives": [
    {
      "theme": "Le sujet que ces citations éclairent (max 60 caractères)",
      "citations": [
        {
          "source_url": "url1",
          "verbatim": "Citation TRADUITE EN FRANÇAIS (min 15 mots).",
          "auteur": "Prénom Nom",
          "fonction": "Titre, Organisation"
        }
      ]
    }
  ]
}
```

---

## Différences clés avec le JSON standard

| Aspect | JSON standard | JSON cross-analysis |
|--------|---------------|---------------------|
| Sources | `url_source` (string) | `url_sources` (tableau d'objets) |
| Type | implicite (article) | `metadata.type = "cross-analysis"` |
| Titre | Éditorialisé sur l'article | Éditorialisé sur l'ENJEU TRANSVERSAL |
| Description longue | ~1800 caractères | ~2500 caractères (dialogue des sources) |
| Pistes | Issues de l'article | ÉMERGENTES de la synthèse |
| Citations | Individuelles | + `citations_comparatives` (dialogue) |
| Scoring | Standard | + `bonus_transversal` + `convergence` |
| Convergences | Absent | Obligatoire |
| Tensions | Absent | Si applicable |

---

## Scoring spécifique cross-analysis

### Bonus transversal (pertinence)
- +1 si 2 dimensions thématiques différentes couvertes par les articles sources
- +2 si 3+ dimensions thématiques différentes couvertes
- +1 si pattern systémique identifié (archétype visible dans le croisement)

### Bonus citations croisées (documentaire)
- +1 si citations complémentaires identifiées (même thème, sources différentes)
- +1 si contradiction sourcée documentée entre articles

### Score de convergence (nouveau)
- `sources_convergentes` : nombre d'articles qui convergent sur le même constat
- `tensions_identifiees` : nombre de tensions/contradictions entre sources
- `angles_complementaires` : nombre d'angles uniques apportés par les sources

---

## Limites de caractères

| Champ | Limite |
|-------|--------|
| `nom` | max 80 caractères |
| `description_courte` | max 280 caractères |
| `synthesis_framework` | max 200 caractères |
| `description_longue` | ~2500 caractères (4-5 paragraphes) |
| `points_vigilance` | max 600 caractères |
| `theme_commun` | max 120 caractères |
| `contribution` (par source) | max 150 caractères |

---

## Exemples d'attribution de sources dans le texte

### Bon (dialogue)

> Cette dynamique se confirme à travers des prismes différents. Le Guardian documente l'ampleur du phénomène côté utilisateurs, tandis que Wired révèle les mécanismes techniques sous-jacents. Ce qui relie ces deux perspectives, c'est l'asymétrie fondamentale entre la plateforme et ses usagers.

### Mauvais (juxtaposition)

> Le Guardian a publié un article sur le sujet. De son côté, Wired a également couvert cette question. Enfin, Ars Technica apporte un troisième angle.

---

## Format de sortie JSON (publication)

```json
{
  "titre": "Titre de l'analyse croisée",
  "slug": "[SLUG_ARTICLE]",
  "html": "Contenu HTML complet selon le template ci-dessus",
  "tags": ["[NOM_MEDIA]", "Analyse croisée", "dimension_majeure"],
  "featured": false
}
```
