---
name: format-instagram
description: Format carrousel Instagram de 10 slides — posture du "laborantin curieux", pas du militant indigné. Reverse engineering de l'actualité pour une audience large. Charger quand la plateforme cible est Instagram.
source: "Adapté de FLTR — formats/instagram.md"
---

# Instructions de format — Carrousel Instagram

## Objectif

Transformer une analyse éditoriale en carrousel Instagram de 10 slides avec la posture du "laborantin curieux" — jamais du militant indigné.

## Audience cible

Audience plus large, moins spécialisée que LinkedIn. Sensibilisation grand public via l'angle "reverse engineering".

---

## Garde-fous factualité (BLOQUANT)

Charger le skill `garde-fous-factualite` avant toute production. Règles de citation, chiffres, et scan post-génération. Ces règles priment sur les contraintes de format.

---

## Structure du carrousel (10 slides)

### Slide 1 — HOOK

Observation fascinante ou chiffre contre-intuitif. **Jamais d'accusation.**

### Slides 2-3 — CONTEXTE

Qui ? Quoi ? Pourquoi c'est intéressant ?

### Slides 4-7 — RÈGLES DU JEU

Ce qu'on apprend. Formuler en :
- "RÈGLE #X : ..." ou
- "TACTIQUE #X : ..." ou
- "CE QU'ILS FONT -> CE QU'ON PEUT EN TIRER"

### Slide 8 — PISTES D'ACTION

2-3 pistes concrètes, transposables. Commencer par des verbes d'action.

### Slide 9 — SIGNAUX

"On saura que ça marche quand..." — formuler un signal observable de basculement.

### Slide 10 — CTA

```
[SIGNATURE_MEDIA]
Lien en bio -> [URL_SITE]
@[COMPTE_INSTAGRAM]
```

---

## Règles de rédaction des slides

- **Phrases courtes** : max 15 mots
- **1 idée par slide**, jamais 2

### Vocabulaire encouragé

- "fascinant"
- "intéressant"
- "ce qu'on apprend"
- "piste"
- "option"
- "expérience"

### Vocabulaire interdit

- "scandaleux"
- "inacceptable"
- "il faut"
- "on doit"
- "inadmissible"

---

## Transformation d'angle

Le sujet doit être transformé selon une posture analytique, jamais militante :

| Type de sujet | Angle militant (interdit) | Angle analytique (requis) |
|---------------|---------------------------|---------------------------|
| Problème | "Meta manipule les régulateurs" | "J'ai lu le playbook de Meta. Voici les règles du jeu qu'on peut retourner." |
| Victoire | "Le Danemark fait plier Google !" | "5 tactiques de négociation qu'on peut apprendre du modèle danois" |
| Menace | "L'IA menace notre vie privée" | "Ce que la course à l'IA révèle sur les angles morts des géants" |
| Régulation | "L'Europe impose enfin des règles" | "Comment le DMA crée des portes qu'on peut utiliser dès maintenant" |
| Scandale | "Meta savait et n'a rien fait" | "Ce que les documents internes de Meta nous apprennent sur leur logique" |

---

## Légende Instagram

### Structure type

```
[Hook : observation ou question ouverte]

[Contexte : 2-3 phrases max]

[Ce qui m'intéresse / Ce qu'on peut en tirer :]
-> Point 1
-> Point 2
-> Point 3

[Citation ou chiffre clé si pertinent]

[Invitation]

[SIGNATURE_MEDIA]

La suite est sur notre site — lien en bio.

#hashtag1 #hashtag2 #hashtag3 #hashtag4 #hashtag5
```

### Tonalité légende

- "Ce qui m'intéresse..." (pas "Ce qui est choquant...")
- "On peut en tirer..." (pas "Il faut...")
- "Une piste à explorer..." (pas "La solution...")
- **Enthousiasme du hacker, pas indignation du militant**

---

## Hashtags

### Mix obligatoire

| Catégorie | Exemples |
|-----------|----------|
| **2-3 thématiques** | #souverainetenumérique #libertédigitale #techpolicy |
| **2-3 contextuels** (selon sujet) | #europe #ia #médias #data #presse #regulation |
| **1-2 posture** | #reverseengineering #stratégie #systemsthinking #innovation |

### Éviter absolument

Ces hashtags ont une connotation militante qui dessert le positionnement analytique :
- #resistance
- #anticapitalisme
- #surveillance
- #bigbrother
- #dystopie
- #orwell

---

## Variante Reel (optionnel)

Si le sujet s'y prête :

- **Hook 3 secondes** : pattern interrupt ou stat contre-intuitive
- **Formats suggérés** :
  - "POV : ..."
  - "Ce que [X] ne vous dit pas..."
  - "J'ai lu [document], voici ce que j'ai noté"
  - "3 choses que j'ai apprises en analysant [X]"
- **Durée** : 30-60 secondes
- **Fin** : "La suite en bio"

---

## Checklist avant validation

- [ ] Le hook suscite la curiosité (pas l'indignation) ?
- [ ] Chaque slide = 1 seule idée claire ?
- [ ] Au moins 2 pistes d'action concrètes et transposables ?
- [ ] Les pistes créent des effets de démultiplication ?
- [ ] Signal de basculement formulé ("On saura que ça marche quand...") ?
- [ ] Tonalité = laborantin curieux, pas militant ?
- [ ] Aucun terme à connotation militante/négative ?
- [ ] CTA vers le site présent ?
- [ ] Signature média incluse ?
- [ ] Hashtags appropriés (sans connotation militante) ?

---

## Format de sortie JSON

```json
{
  "titre": "Titre du carrousel",
  "angle": "L'angle analytique choisi (transformation du sujet)",

  "slides": [
    {
      "numero": 1,
      "type": "hook",
      "contenu": "Observation fascinante ou chiffre contre-intuitif"
    },
    {
      "numero": 2,
      "type": "contexte",
      "contenu": "Qui ? Quoi ?"
    },
    {
      "numero": 3,
      "type": "contexte",
      "contenu": "Pourquoi c'est intéressant ?"
    },
    {
      "numero": 4,
      "type": "regle",
      "titre": "RÈGLE #1",
      "contenu": "..."
    },
    {
      "numero": 5,
      "type": "regle",
      "titre": "RÈGLE #2",
      "contenu": "..."
    },
    {
      "numero": 6,
      "type": "regle",
      "titre": "RÈGLE #3",
      "contenu": "..."
    },
    {
      "numero": 7,
      "type": "regle",
      "titre": "RÈGLE #4",
      "contenu": "..."
    },
    {
      "numero": 8,
      "type": "action",
      "pistes": [
        "Verbe d'action + piste 1",
        "Verbe d'action + piste 2",
        "Verbe d'action + piste 3"
      ]
    },
    {
      "numero": 9,
      "type": "signaux",
      "signal": "On saura que ça marche quand..."
    },
    {
      "numero": 10,
      "type": "cta",
      "contenu": "[SIGNATURE_MEDIA]\nLien en bio -> [URL_SITE]\n@[COMPTE_INSTAGRAM]"
    }
  ],

  "legende": {
    "hook": "Observation ou question ouverte",
    "contexte": "2-3 phrases max",
    "points": [
      "Ce qu'on peut en tirer - Point 1",
      "Ce qu'on peut en tirer - Point 2",
      "Ce qu'on peut en tirer - Point 3"
    ],
    "citation": "Citation ou chiffre clé (optionnel)",
    "cta": "[SIGNATURE_MEDIA]\n\nLa suite est sur notre site — lien en bio."
  },

  "hashtags": {
    "thematiques": ["#souverainetenumérique", "#libertédigitale"],
    "contextuels": ["#europe", "#ia"],
    "posture": ["#reverseengineering", "#systemsthinking"]
  },

  "reel": {
    "pertinent": true,
    "hook_3s": "Pattern interrupt ou stat",
    "format": "3 choses que j'ai apprises en analysant [X]",
    "duree_secondes": 45
  },

  "lien_article": "[URL_ARTICLE]"
}
```
