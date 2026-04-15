---
name: format-article-web
description: Format d'article web pour publication sur CMS — trois templates (Perspective, Éducation, Signal) selon le besoin informationnel du lecteur. Structure HTML standardisée avec analyse, pistes d'action et appels à l'échange. Charger pour la publication d'articles web.
source: "Adapté de FLTR — formats/ghost-article.md (templates Perspective/Educate/Signal)"
---

# Instructions de format — Article web (analyse individuelle)

## Objectif

Publier une analyse individuelle d'article sur le CMS de [NOM_MEDIA], avec une structure HTML standardisée.
Le template utilisé dépend du champ `distribution.template` dans le JSON pivot.

## Audience cible

Abonnés et lecteurs de [NOM_MEDIA] — audience engagée, sensibilisée aux enjeux traités.

## Choix du template

| Template | User Needs | Quand l'utiliser |
|----------|-----------|-----------------|
| **Perspective** | `give_me_perspective`, `inspire_me`, `connect_me` | Analyse approfondie, mise en perspective systémique, récit de victoire |
| **Educate** | `educate_me`, `help_me` | Explication de mécanisme, guide, pédagogie |
| **Signal** | `update_me`, `keep_me_engaged` | Fait court, signal rapide, découverte |

---

## Template PERSPECTIVE (défaut)

User Needs : `give_me_perspective`, `inspire_me`, `connect_me`

Analyse approfondie avec pistes d'action systémique. C'est le template par défaut.

### Structure HTML

### 1. URL Source (bookmark card)

```html
<p>{url_source}</p>
```

Le CMS transforme automatiquement l'URL en bookmark card avec preview.

### 2. Description longue (analyse principale)

```html
<p>{paragraphe_1}</p>

<p>{paragraphe_2}</p>

<p>{paragraphe_3}</p>
```

Chaque paragraphe de l'analyse dans une balise `<p>` séparée.
Double saut de ligne entre les paragraphes.

### 3. Points de vigilance

```html
<p><em>Points de vigilance : {points_vigilance}</em></p>
```

En italique pour signaler la nuance.

### 4. Score (blockquote)

```html
<blockquote>{score}/[SCORE_REFERENCE] : Score sur l'échelle d'analyse [NOM_MEDIA], basé sur la grille d'évaluation éditoriale</blockquote>
```

### 5. Lien méthodologique

```html
<p>[URL_METHODOLOGIE]</p>
```

### 6. Séparateur

```html
<hr>
```

### 7. Section "Et maintenant ?"

```html
<h3>Et maintenant ?</h3>

<p>Face à ces enjeux, plusieurs pistes d'action systémique se dessinent.</p>

<p>{emoji} <strong>{premiere_phrase_piste_1}</strong></p>

<p>{reste_contenu_piste_1}</p>

<p><em>{signaux_piste_1}</em></p>

<p>{emoji} <strong>{premiere_phrase_piste_2}</strong></p>

<p>{reste_contenu_piste_2}</p>

<p><em>{signaux_piste_2}</em></p>

<hr>
```

#### Emojis des pistes d'action

| Emoji | Type d'action |
|-------|---------------|
| Action de coalition (collectif organisé) | Emoji au choix de la rédaction |
| Action individuelle (choix personnels) | Emoji au choix de la rédaction |
| Action de résistance (opposition active) | Emoji au choix de la rédaction |
| Action de confrontation | Emoji au choix de la rédaction |
| Action de célébration/soutien | Emoji au choix de la rédaction |

#### Structure de chaque piste

1. **Première phrase** en gras (titre de la piste)
2. **Contenu développé** en paragraphes normaux
3. **Signaux** ("On saura que ça marche quand...") en italique

### 8. Citation finale

```html
<p><strong>Ces pistes ne sont pas des recettes toutes faites, mais des points d'entrée pour repenser nos systèmes selon une logique de liberté positive : non pas limiter, mais augmenter nos capacités collectives d'action.</strong></p>
```

### 9. Call to action

```html
<h3>On en discute ?</h3>

<p>Tu veux recevoir le flux quotidien des articles publiés <a href="[URL_SITE]">sur le site</a> ? Suis-moi sur [RESEAUX_SOCIAUX_LIENS] !</p>

<p>Tu as des remarques, des suggestions, ou tu veux discuter d'une idée pour avancer dans tes propres projets ? Connecte-toi et laisse-moi un commentaire ou jette un oeil directement <a href="[LIEN_AGENDA]">à mon agenda</a>.</p>
```

---

### Template PERSPECTIVE — HTML complet

```html
<p>{url_source}</p>

<p>{paragraphe_analyse_1}</p>

<p>{paragraphe_analyse_2}</p>

<p>{paragraphe_analyse_3}</p>

<p><em>Points de vigilance : {points_vigilance}</em></p>

<blockquote>{score}/[SCORE_REFERENCE] : Score sur l'échelle d'analyse [NOM_MEDIA], basé sur la grille d'évaluation éditoriale</blockquote>

<p>[URL_METHODOLOGIE]</p>

<hr>

<h3>Et maintenant ?</h3>

<p>Face à ces enjeux, plusieurs pistes d'action systémique se dessinent.</p>

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

## Template EDUCATE

User Needs : `educate_me`, `help_me`

Structure didactique : poser le contexte, expliquer le mécanisme, montrer les implications, fournir des ressources.

### Structure HTML EDUCATE

#### 1. URL Source (bookmark card)

```html
<p>{url_source}</p>
```

#### 2. Contexte (pourquoi c'est important)

```html
<h3>De quoi parle-t-on ?</h3>

<p>{contexte_1}</p>

<p>{contexte_2}</p>
```

2-3 paragraphes qui posent le sujet de manière accessible. Pas de jargon sans explication.

#### 3. Mécanisme (comment ça marche)

```html
<h3>Comment ça fonctionne</h3>

<p>{mecanisme_1}</p>

<p>{mecanisme_2}</p>

<p>{mecanisme_3}</p>
```

3-4 paragraphes qui expliquent la chaîne causale, les acteurs, les dynamiques. Pédagogie avant tout.

#### 4. Implications (ce que ça change)

```html
<h3>Ce que ça implique</h3>

<p>{implication_1}</p>

<p>{implication_2}</p>
```

2-3 paragraphes sur les conséquences concrètes pour les individus, les collectifs, les institutions.

#### 5. Points de vigilance + Score

```html
<p><em>Points de vigilance : {points_vigilance}</em></p>

<blockquote>{score}/[SCORE_REFERENCE] : Score sur l'échelle d'analyse [NOM_MEDIA], basé sur la grille d'évaluation éditoriale</blockquote>

<p>[URL_METHODOLOGIE]</p>

<hr>
```

#### 6. Section "Pour aller plus loin"

```html
<h3>Pour aller plus loin</h3>

<p>{ressource_ou_piste_1}</p>

<p>{ressource_ou_piste_2}</p>

<hr>
```

1-2 pistes d'action ou ressources complémentaires. Plus court que la section "Et maintenant ?" du template Perspective.

#### 7. Call to action

```html
<h3>On en discute ?</h3>

<p>Tu veux recevoir le flux quotidien des articles publiés <a href="[URL_SITE]">sur le site</a> ? Suis-moi sur [RESEAUX_SOCIAUX_LIENS] !</p>

<p>Tu as des remarques, des suggestions, ou tu veux discuter d'une idée pour avancer dans tes propres projets ? Connecte-toi et laisse-moi un commentaire ou jette un oeil directement <a href="[LIEN_AGENDA]">à mon agenda</a>.</p>
```

### Template EDUCATE — HTML complet

```html
<p>{url_source}</p>

<h3>De quoi parle-t-on ?</h3>

<p>{contexte_1}</p>

<p>{contexte_2}</p>

<h3>Comment ça fonctionne</h3>

<p>{mecanisme_1}</p>

<p>{mecanisme_2}</p>

<p>{mecanisme_3}</p>

<h3>Ce que ça implique</h3>

<p>{implication_1}</p>

<p>{implication_2}</p>

<p><em>Points de vigilance : {points_vigilance}</em></p>

<blockquote>{score}/[SCORE_REFERENCE] : Score sur l'échelle d'analyse [NOM_MEDIA], basé sur la grille d'évaluation éditoriale</blockquote>

<p>[URL_METHODOLOGIE]</p>

<hr>

<h3>Pour aller plus loin</h3>

<p>{ressource_ou_piste_1}</p>

<p>{ressource_ou_piste_2}</p>

<hr>

<h3>On en discute ?</h3>

<p>Tu veux recevoir le flux quotidien des articles publiés <a href="[URL_SITE]">sur le site</a> ? Suis-moi sur [RESEAUX_SOCIAUX_LIENS] !</p>

<p>Tu as des remarques, des suggestions, ou tu veux discuter d'une idée pour avancer dans tes propres projets ? Connecte-toi et laisse-moi un commentaire ou jette un oeil directement <a href="[LIEN_AGENDA]">à mon agenda</a>.</p>
```

---

## Template SIGNAL

User Needs : `update_me`, `keep_me_engaged`

Format court (~300 mots). Fait brut, mise en contexte minimale, lien vers la source. Idéal pour les signaux rapides et les découvertes.

### Structure HTML SIGNAL

#### 1. URL Source (bookmark card)

```html
<p>{url_source}</p>
```

#### 2. Signal (l'essentiel en 2-3 paragraphes)

```html
<p>{signal_1}</p>

<p>{signal_2}</p>
```

2-3 paragraphes courts. Le fait, son contexte immédiat, pourquoi ça compte. Pas d'analyse systémique — on reste au niveau du signal.

#### 3. Score + Lien méthodologique

```html
<blockquote>{score}/[SCORE_REFERENCE] : Score sur l'échelle d'analyse [NOM_MEDIA], basé sur la grille d'évaluation éditoriale</blockquote>

<p>[URL_METHODOLOGIE]</p>
```

#### 4. Call to action

```html
<hr>

<h3>On en discute ?</h3>

<p>Tu veux recevoir le flux quotidien des articles publiés <a href="[URL_SITE]">sur le site</a> ? Suis-moi sur [RESEAUX_SOCIAUX_LIENS] !</p>

<p>Tu as des remarques, des suggestions, ou tu veux discuter d'une idée pour avancer dans tes propres projets ? Connecte-toi et laisse-moi un commentaire ou jette un oeil directement <a href="[LIEN_AGENDA]">à mon agenda</a>.</p>
```

Pas de section "Et maintenant ?", pas de pistes d'action développées. Le signal suffit.

### Template SIGNAL — HTML complet

```html
<p>{url_source}</p>

<p>{signal_1}</p>

<p>{signal_2}</p>

<blockquote>{score}/[SCORE_REFERENCE] : Score sur l'échelle d'analyse [NOM_MEDIA], basé sur la grille d'évaluation éditoriale</blockquote>

<p>[URL_METHODOLOGIE]</p>

<hr>

<h3>On en discute ?</h3>

<p>Tu veux recevoir le flux quotidien des articles publiés <a href="[URL_SITE]">sur le site</a> ? Suis-moi sur [RESEAUX_SOCIAUX_LIENS] !</p>

<p>Tu as des remarques, des suggestions, ou tu veux discuter d'une idée pour avancer dans tes propres projets ? Connecte-toi et laisse-moi un commentaire ou jette un oeil directement <a href="[LIEN_AGENDA]">à mon agenda</a>.</p>
```

---

## Format de sortie JSON

```json
{
  "titre": "Titre de l'article",
  "slug": "[SLUG_ARTICLE]",
  "html": "Contenu HTML complet selon le template ci-dessus",
  "tags": ["[NOM_MEDIA]", "dimension_majeure"],
  "featured": false
}
```
