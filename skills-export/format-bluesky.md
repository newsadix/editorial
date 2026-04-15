---
name: format-bluesky
description: Format de publication Bluesky — post analytique de 300 caractères maximum avec lien vers l'article. Ton factuel et incisif, pas de clickbait. Charger quand la plateforme cible est Bluesky.
source: "Adapté de FLTR — formats/bluesky.md"
---

# Instructions de format — Bluesky

## Objectif

Transformer une analyse éditoriale en post Bluesky percutant avec lien vers l'article publié.

## Audience cible

- Communauté tech et médias du Fediverse/AT Protocol
- Journalistes et analystes indépendants
- Défenseurs des libertés numériques et de la décentralisation
- Observateurs de la régulation tech
- **Early adopters** : audience expérimentale, ton plus libre que LinkedIn

**Différence clé avec les autres plateformes** : Bluesky offre 300 caractères avec une communauté sensible aux enjeux de décentralisation et de souveraineté, proche de Mastodon. Ton factuel et analytique, pas de clickbait.

**Rôle dans la stratégie** : Laboratoire éditorial. Audience restreinte mais qualifiée — idéal pour tester des angles avant LinkedIn.

---

## Garde-fous factualité (BLOQUANT)

Charger le skill `garde-fous-factualite` avant toute production. Règles de citation, chiffres, et scan post-génération. Ces règles priment sur les contraintes de format.

---

## Structure obligatoire

**Longueur** : 300 caractères MAX (hors lien) — le graphe social et le lien sont gérés séparément.

### 1. Hook (1-2 phrases, max 20 mots)

- **Objectif** : Contextualiser et donner envie de lire
- **Ton** : Factuel mais incisif
- **Techniques** : Stat, paradoxe, mise en perspective structurelle

### 2. Développement (1-2 phrases courtes)

- **Objectif** : Apporter un éclairage que le titre seul ne donne pas
- **Ton** : Analytique, accessible
- **Techniques** : Lien de cause à effet, mise en contexte systémique
- **Pour les sujets de résistance** : Privilégier l'angle "retrait de consentement" ou "non-coopération ciblée". La communauté Bluesky est sensible aux approches qui construisent des alternatives.

### 3. Lien article

- Format : `[URL_ARTICLE]`
- Le lien sera ajouté automatiquement via une card (embed externe)
- Ne PAS inclure le lien dans le texte du post

---

## Ton et style

### A faire

- Factuel et analytique
- Engagé sur les libertés numériques et la décentralisation
- Accessible sans jargon excessif
- Utiliser des chiffres si pertinent
- Mettre en perspective (causes, conséquences structurelles)
- Profiter de l'espace pour apporter du contexte

### A éviter absolument

- Sensationnalisme ou clickbait
- Emojis excessifs (0-2 max)
- Ton alarmiste ou moralisateur
- Formulations vagues ("intéressant", "à lire absolument")
- Ton corporate ou marketing
- Hashtags (Bluesky n'utilise pas de hashtags dans le corps du post)

---

## Exemples de bons posts

```
Les puissances moyennes ne veulent plus du web américain. Elles construisent le leur.

Le DMA européen a ouvert une brèche. Derrière la régulation, c'est la fragmentation du web en blocs souverains qui s'accélère.
```

Lien : [URL_ARTICLE]

```
Google fixe les prix. L'IA négocie pour vous. Qui y gagne vraiment ?

Les agents IA de shopping déplacent le pouvoir vers ceux qui contrôlent les algorithmes de recommandation.
```

Lien : [URL_ARTICLE]

```
45 villes ont fait plier Avelo Airlines en 9 mois. Sans procès.

Le mécanisme : cibler les piliers de soutien — subventions locales, réputation aéroportuaire. Retirer le consentement économique.
```

Lien : [URL_ARTICLE]

---

## Format de sortie JSON

```json
{
  "titre": "Titre court (max 60 caractères)",
  "hook": "La phrase d'accroche seule",
  "body": "Le post complet (hook + développement), SANS le lien, SANS hashtags",
  "lien_article": "[URL_ARTICLE]"
}
```

**Notes** :
- Le lien article est ajouté automatiquement via embed (card externe)
- Ne PAS inclure le lien dans le body généré
- Ne PAS inclure de hashtags (Bluesky les gère via des labels/feeds)
- Le body doit faire max 300 caractères
