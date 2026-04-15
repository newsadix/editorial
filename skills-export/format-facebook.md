---
name: format-facebook
description: Format de publication Facebook — post accessible et conversationnel de 300-400 mots pour une audience engagée. Tutoiement, ton direct et chaleureux. Charger quand la plateforme cible est Facebook.
source: "Adapté de FLTR — formats/facebook.md"
---

# Instructions de format — Facebook

## Objectif

Générer un post Facebook accessible et engageant pour une audience grand public. Publication native (texte + image), sans lien externe pour favoriser l'algorithme Facebook.

## Audience cible

- Grand public engagé
- Followers actifs de [NOM_MEDIA]
- Lecteurs curieux mais pas nécessairement spécialistes

---

## Garde-fous factualité (BLOQUANT)

Charger le skill `garde-fous-factualite` avant toute production. Règles de citation, chiffres, et scan post-génération. Ces règles priment sur les contraintes de format.

---

## Structure du post

**Longueur** : 300-400 mots MAX (Facebook favorise les posts plus courts)

### 1. Hook (1-2 phrases, max 20 mots)

- **Objectif** : Capter l'attention immédiatement
- **Ton** : Direct, intrigant, parfois légèrement provocateur
- **Techniques** : Question, stat surprenante, affirmation contre-intuitive

### 2. Contexte accessible (2-3 phrases, max 50 mots)

- **Objectif** : Rendre le sujet compréhensible par tous
- **Ton** : Pédagogique sans être condescendant
- **Éviter** : Le jargon technique, les acronymes non expliqués

### 3. L'essentiel (150-200 mots)

- **Objectif** : Expliquer pourquoi ça nous concerne tous
- **Ton** : Conversationnel, comme si on expliquait à un ami
- **Structure** : Alterner faits et implications concrètes

Développer les enjeux de manière accessible. Utiliser des analogies du quotidien si pertinent.

Intégrer UNE citation de l'article si disponible — en respectant strictement la discipline verbatim/paraphrase (voir skill garde-fous-factualite). Si la citation originale est en anglais : paraphraser sans guillemets OU citer un court fragment traduit avec mention "[traduit de l'anglais]".

### 4. Point de vigilance (1-2 phrases)

Nommer UNE limite de l'analyse ou un angle mort :
- Ce que l'article ne dit pas
- Ce qu'on ne sait pas encore
- Un contre-argument possible
- Une nuance importante

**Ton** : Honnête, pas défaitiste. Montrer qu'on a conscience des limites.

**Exemples** :
- "L'article ne dit pas si..."
- "Reste à voir comment..."
- "Ce que ça ne couvre pas : ..."

### 5. Piste d'ouverture (2-3 phrases)

Reprendre UNE piste systémique de l'analyse et la reformuler de manière accessible et constructive. Pas une injonction ("il faut"), mais une possibilité ("et si", "on pourrait imaginer", "une voie serait").

**Objectif** : Donner envie d'agir, pas culpabiliser. Montrer qu'il y a des leviers.

**Ton** : Prospectif, pas prescriptif. Ouvrir des portes, pas donner des ordres.

**Pour les pistes de résistance** : Formuler en termes de "retrait de soutien" ou "non-coopération" plutôt qu'affrontement. Exemples : "retirer son consentement", "ne plus alimenter", "créer des alternatives qui rendent X obsolète". Éviter les formulations qui donnent un prétexte de victimisation à l'adversaire.

**INTERDIT — CTA militants (règle T6)** : Ne JAMAIS terminer par un appel au boycott, un ultimatum collectif, ou une proposition d'action militante concrète (script, déconnexion massive, pétition). Le fond factuel suffit — le lecteur tire ses propres conclusions. Un CTA militant déplace la critique du fond vers la forme et affaiblit la crédibilité analytique.

**Exemples autorisés** :
- "Une piste : coaliser X et Y pour..."
- "Et si on commençait par..."
- "Ce qui pourrait changer la donne : ..."

**Exemples interdits** :
- "Et si on cessait collectivement de..." (trop proche d'un appel à l'action militant)

### 6. Invitation à l'échange (varier entre ces options)

- "Tu as déjà remarqué ça autour de toi ?"
- "Ça te parle ? Dis-moi en commentaire."
- "Curieux d'avoir ton avis là-dessus."
- "Tu gères ça comment de ton côté ?"

**Note** : Le CTA vers le site/newsletter est ajouté automatiquement à la publication, ne pas l'inclure dans le body généré.

---

## Ton et style

### A faire

- Tutoiement systématique
- Ton direct et chaleureux
- Phrases courtes et percutantes
- Analogies concrètes du quotidien
- Rester ancré dans les faits
- Doubles sauts de ligne pour aérer

### A éviter absolument

- Vouvoiement (réservé à LinkedIn)
- Jargon technique non expliqué
- Ton corporate ou institutionnel
- **Leçons de morale** ou ton prescriptif
- **Formulations prescriptives** : "il faut", "on doit", "tu dois"
- **Listes d'implications directes** : "Ce que ça change pour toi", "Ce que tu dois savoir"
- Alarmisme excessif ou catastrophisme
- Emojis à outrance (1-2 max par post)
- Posture de sachant ou donneur de leçons

---

## Formatage

### Bullets

Utiliser `->` (pas `-` ou puce) si besoin de listes.

**Note** : Éviter les listes à puces dans la section "Piste d'ouverture" — préférer des phrases fluides.

### Mise en valeur

Utiliser les majuscules avec parcimonie pour l'emphase (pas de gras sur Facebook mobile).

**Exemple** :
```
Et si la vraie question, c'était de savoir QUI décide des règles du jeu ?
```

### Sauts de ligne

Utiliser des doubles sauts de ligne entre chaque section pour aérer le post (crucial sur mobile).

---

## Format de sortie JSON

```json
{
  "titre": "Titre court (max 60 caractères)",
  "hook": "La phrase d'accroche seule",
  "body": "Le post complet (hook + contexte + essentiel + vigilance + ouverture + invitation)",
  "lien_article": "[URL_ARTICLE]"
}
```

**Note** : Publication native (texte + image uniquement), sans lien externe pour favoriser l'algorithme Facebook.
