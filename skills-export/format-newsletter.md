---
name: format-newsletter
description: Format de newsletter hebdomadaire analytique — synthèse narrative, top 3 articles, pistes d'action concrètes, backstage. Structure éprouvée pour fidéliser une audience engagée. Charger pour la production de newsletters.
source: "Adapté de FLTR — formats/newsletter.md"
---

# Instructions de format — Newsletter hebdomadaire [NOM_MEDIA]

## Objectif

Synthétiser la semaine éditoriale en une newsletter qui relie des événements apparemment disparates pour révéler les structures de pouvoir sous-jacentes, puis donne au lecteur les moyens d'agir.

## Audience cible

Abonnés newsletter [NOM_MEDIA] — lecteurs engagés, sensibilisés aux enjeux traités, qui attendent une synthèse analytique sourcée chaque semaine.

## Positionnement

Ni pure curation, ni pure opinion, ni pure enquête. C'est de la **synthèse analytique sourcée** : un journaliste-analyste qui lit des dizaines d'articles par semaine et en extrait un fil directeur, enrichi par sa propre expertise et ses actions concrètes.

---

## Promesse éditoriale

Le lecteur doit se dire :
- "J'ai trouvé du **sens** à travers les articles de la semaine"
- "Ça me donne **envie d'agir**"
- "J'ai envie de **partager** avec ma communauté"
- "J'ai envie de lire les **sources originales**"

---

## Structure de la newsletter

### 1. Titre + sous-titre

- **Titre** : max 80 caractères. Affirmation-choc ou question rhétorique. Fonctionne comme thèse éditoriale autonome.
- **Sous-titre** : max 299 caractères. Rythme, contraste, question ouverte.
- Les jeux de mots géopolitiques fonctionnent bien.

### 2. Intro narrative (600-800 mots)

Coeur de la newsletter. Prose fluide, phrases courtes, tutoiement.

**Structure interne** :
1. Hook factuel qui claque (événement précis, date, nommé)
2. Mécanisme systémique expliqué simplement
3. 4-6 articles intégrés avec liens vers sources ORIGINALES
4. Citations exactes attribuées et VÉRIFIÉES
5. Pourquoi c'est un basculement
6. Question directe au lecteur

**RÈGLES ABSOLUES** :
- ZÉRO liste à puces dans l'intro
- Pas de "Cette semaine révèle un pattern fascinant..."
- Pas de listes mécaniques d'articles
- Prose fluide, transitions narratives
- "Tu vois le problème ?" / "Tu as déjà vécu ça ?"
- Minimum 2 questions directes au lecteur

### 3. Séparateur + "à propos"

```markdown
---
-> à propos
---
```

### 4. A lire absolument cette semaine (Top 3)

3 articles sélectionnés, chacun avec :
- Emoji + titre éditorialisé (pas le titre original)
- Teaser 80-120 mots : contexte + révélation + pourquoi ça compte pour le lecteur
- Lien cliquable vers la source ORIGINALE

```markdown
### [Emoji] [Titre éditorialisé]
[Teaser 80-120 mots]
[Lire l'enquête complète](URL_ORIGINALE?ref=[NOM_MEDIA])
```

### 5. Les pistes d'action concrètes

Des actions VRAIMENT réalisables, pas des voeux pieux.

**Structure flexible** (2 ou 3 niveaux — ne pas forcer) :

```markdown
### Quick wins (ce mois-ci)
Actions individuelles, peu de dépendances, résultat rapide.

**[Titre piste]**
[Description concrète : quoi faire, comment, résultat attendu]
-> Source : [Titre article](URL_ORIGINALE?ref=[NOM_MEDIA])
-> Pour aller plus loin : [Notre analyse]([URL_ARTICLE]?ref=[NOM_MEDIA])

### Long terme (1-2 ans)
Changement systémique, accords politiques, coalition large.

**[Titre piste]**
[...]
```

Le niveau "moyen terme" est optionnel. Ne pas forcer si peu de pistes pertinentes.

### 6. Si tu les as manqués

Format scannable, 3-5 articles :

```markdown
* [Titre](URL_ORIGINALE?ref=[NOM_MEDIA]) — Three-liner éditorialisé
```

### 7. Backstage

Contenu fourni par l'auteur. Inclure :
- Stats détaillées de la semaine (impressions, reach, abonnés, taux d'ouverture)
- Apparitions médias avec contexte
- Projets en cours
- Ton personnel et reconnaissant

### 8. Tu en veux plus ? On en discute ?

```markdown
Je te partage le flux quotidien des articles repérés au cours de ma veille
-> sur [RESEAUX_SOCIAUX_LIENS]
```

### 9. Signature

```markdown
---
-> [NOM_MEDIA]

À la semaine prochaine,

[SIGNATURE_AUTEUR]
```

---

## Stratégie de liens (SEO + cliquabilité)

### Format

Tous les liens en Markdown cliquable : `[texte descriptif](URL)`

### Hiérarchie

| Priorité | Type | Usage |
|----------|------|-------|
| PRIMAIRE | Source ORIGINALE | Envoyer les lecteurs vers le journal, l'étude, le rapport |
| SECONDAIRE | Article [NOM_MEDIA] | Quand l'article du site approfondit significativement le sujet |

### Règles

- **Tracking** : `?ref=[NOM_MEDIA]` sur TOUS les liens externes
- **Anchor text** : Descriptif et riche en mots-clés (pas de "cliquez ici")
- **Maillage interne** : Les articles du site de la semaine liés dans l'intro ET dans les teasers
- **Sources internes** : Format `-> Pour aller plus loin : [Notre analyse complète]([URL_ARTICLE]?ref=[NOM_MEDIA])`
- **Attribution** : Toujours citer la source ORIGINALE, pas l'analyse du site comme source finale

### Exemples

```markdown
<!-- BON : anchor text descriptif, source originale, tracking -->
[l'enquête du Washington Post sur la surveillance algorithmique](https://washingtonpost.com/article?ref=[NOM_MEDIA])

<!-- BON : lien secondaire vers le site -->
-> Pour aller plus loin : [Notre analyse des enjeux de souveraineté]([URL_SITE]/[SLUG_ARTICLE]?ref=[NOM_MEDIA])

<!-- MAUVAIS : anchor text générique -->
[cliquez ici](https://...)

<!-- MAUVAIS : citer le site comme source primaire -->
Selon [notre article]([URL_SITE]/...), la surveillance...
```

---

## Ton et style

- **Tutoiement** systématique
- **Prose fluide**, phrases courtes, parfois fragmentaires pour l'emphase
- **Tirets cadratins** utilisés massivement
- **Questions plutôt qu'affirmations** dans les transitions
- **Alternance données factuelles / interprétation**
- **Ironie mesurée** : références culturelles pop, jamais de sarcasme gratuit
- **Urgence sans catastrophisme** : "La bonne nouvelle, c'est..." / "Et maintenant ?"
- Le lecteur est co-analyste, pas récepteur passif
- "Nous" (citoyens), "on" (inclusif), pas de "je" sauf backstage

### Ce qui est interdit

- AI-speak (formules creuses, jargon IA : "fascinant", "remarquable", "intéressant", "édifiant")
- Condescendance pédagogique
- Neutralité fausse
- Catastrophisme
- Listes à puces dans l'intro narrative

---

## Thèse de convergence

Pattern éditorial distinctif : montrer comment différents acteurs (étatiques, technologiques, économiques, infrastructurels) convergent vers un même objectif de contrôle ou de transformation systémique. Ne pas forcer, mais identifier quand ce pattern émerge naturellement des articles de la semaine.

---

## Contraintes de longueur

| Section | Longueur |
|---------|----------|
| Intro narrative | 600-800 mots |
| Teasers top 3 | 80-120 mots chacun |
| Total newsletter | 1500-1900 mots |
| Temps de lecture | 5-10 minutes |

---

## Checklist de validation finale

Avant livraison, vérifier :

- [ ] Intro : 600-800 mots max
- [ ] Teasers top 3 : 80-120 mots chacun
- [ ] Tutoiement partout
- [ ] 2+ questions directes au lecteur
- [ ] Tous les liens pointent vers sources ORIGINALES + `?ref=[NOM_MEDIA]`
- [ ] Pistes d'action catégorisées (quick wins + long terme, moyen terme optionnel)
- [ ] Fact-check effectué sur tous les faits clés
- [ ] Total : 1500-1900 mots
- [ ] Zéro AI-speak (scanner pour mots/tournures interdits)
- [ ] Aucune citation inventée
- [ ] Aucune URL inventée
- [ ] Cadres théoriques invisibles (aucun framework nommé dans le texte)
- [ ] Maillage interne : articles du site liés dans l'intro + teasers

---

## Rappels

Ce format s'appuie sur la charte éditoriale et le framework analytique du média. Ces documents DOIVENT être chargés AVANT la rédaction. Le socle éditorial et la grille d'analyse priment sur les instructions de format.
