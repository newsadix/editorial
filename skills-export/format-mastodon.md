---
name: format-mastodon
description: Format de publication Mastodon/Fediverse — toot analytique de 500 caractères avec hashtags pertinents et lien article. Ton posé et analytique. Charger quand la plateforme cible est Mastodon.
source: "Adapté de FLTR — formats/mastodon.md"
---

# Instructions de format — Mastodon

## Objectif

Transformer une analyse éditoriale en toot Mastodon percutant avec lien vers l'article publié.

## Audience cible

- Communauté tech et libriste du Fediverse
- Journalistes et analystes indépendants
- Défenseurs des libertés numériques
- Curieux de la souveraineté numérique

**Spécificité** : 500 caractères disponibles, communauté sensible aux enjeux de souveraineté et de vie privée. Ton posé, analytique, pas de "punchline".

---

## Garde-fous factualité (BLOQUANT)

Charger le skill `garde-fous-factualite` avant toute production. Règles de citation, chiffres, et scan post-génération. Ces règles priment sur les contraintes de format.

---

## Structure obligatoire

**Longueur** : 500 caractères MAX (hors lien) — laisser ~30 caractères pour le lien.

### 1. Hook (1-2 phrases, max 30 mots)

- **Objectif** : Contextualiser et donner envie de lire
- **Ton** : Factuel, engagé sans être militant
- **Techniques** : Stat, paradoxe, mise en perspective structurelle

### 2. Développement (2-3 phrases)

- **Objectif** : Apporter un éclairage structurel que le titre seul ne donne pas
- **Ton** : Analytique, accessible
- **Techniques** : Lien de cause à effet, mise en contexte systémique
- **Pour les sujets de résistance** : Privilégier l'angle "retrait de consentement" ou "non-coopération ciblée" plutôt que l'affrontement. Nommer les piliers de soutien vulnérables (annonceurs, investisseurs, employés). La communauté Fediverse est sensible aux approches qui construisent des alternatives plutôt qu'à celles qui alimentent l'escalade.

### 3. Hashtags (2-3 max)

- Pertinents et spécifiques (pas de #tech #news générique)
- En rapport direct avec les enjeux traités
- Exemples : #SouverainetéNumérique #ViePrivée #RégulationTech #LogicielLibre #DonnéesPersonnelles

### 4. Lien article

- Format : `[URL_ARTICLE]`
- Le lien sera ajouté automatiquement à la publication

---

## Ton et style

### A faire

- Factuel et analytique
- Engagé sur les libertés numériques (cohérent avec le Fediverse)
- Accessible sans jargon excessif
- Utiliser des chiffres si pertinent
- Mettre en perspective (causes, conséquences structurelles)
- Profiter des 500 caractères pour apporter du contexte

### A éviter absolument

- Sensationnalisme ou clickbait
- Emojis excessifs (0-2 max)
- Ton alarmiste ou moralisateur
- Formulations vagues ("intéressant", "à lire absolument")
- Ton corporate ou marketing
- Hashtags génériques (#actualité #info)

---

## Exemples de bons toots

```
Les puissances moyennes ne veulent plus du web américain. Elles construisent le leur.

Le DMA européen a ouvert une brèche. Mais derrière la régulation, c'est un mouvement plus profond : la fragmentation du web en blocs souverains s'accélère.

#SouverainetéNumérique #DMA
```

Lien : [URL_ARTICLE]

```
Google fixe les prix. L'IA négocie pour vous. Qui y gagne vraiment ?

Les agents IA de shopping promettent de casser l'asymétrie d'information. En réalité, ils déplacent le pouvoir vers ceux qui contrôlent les algorithmes de recommandation.

#IA #Consommation
```

Lien : [URL_ARTICLE]

```
45 villes ont fait plier Avelo Airlines en 9 mois. Sans procès, sans violence.

Le mécanisme : cibler les piliers de soutien — subventions locales, clients fidélisés, réputation aéroportuaire. Retirer le consentement économique plutôt qu'affronter l'administration fédérale.

#RésistanceCivile #NonCoopération
```

Lien : [URL_ARTICLE]

---

## Format de sortie JSON

```json
{
  "titre": "Titre court (max 60 caractères)",
  "hook": "La phrase d'accroche seule",
  "body": "Le toot complet (hook + développement + hashtags), SANS le lien article",
  "lien_article": "[URL_ARTICLE]"
}
```

**Notes** :
- Le lien article est ajouté automatiquement à la publication
- Ne PAS inclure le lien dans le body généré
- Le body doit faire max 500 caractères pour laisser place au lien
