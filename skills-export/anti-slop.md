---
name: anti-slop
description: Détection et élimination du "slop" (formulations artificielles générées par IA) dans les contenus éditoriaux. Dictionnaire de mots et formulations à proscrire en français et en anglais, avec reformulations attendues.
source: "Adapté de FLTR — socle-commun.md (anti-IA-speak) + editorial-feedback.md (tournures) + quality-checks.md (AI slop detection)"
---

# Anti-slop — Détection et élimination des formulations artificielles

Le "slop" désigne les formulations creuses, génériques et artificielles typiques des textes générés par IA. Ce skill liste les marqueurs à détecter et éliminer, en français et en anglais.

---

## Section FR — Marqueurs en français

### Marqueurs d'enthousiasme artificiel

- "Cet exemple est fascinant"
- "Voici un exemple parfait de..."
- "C'est vraiment intéressant de voir que..."
- "Il est important de noter que..."
- "Cela soulève des questions importantes"
- "Dans un monde où..."
- "À l'ère du numérique..."
- "Force est de constater que..."
- "Il est indéniable que..."

### Marqueurs de structure artificielle

- "Plongeons dans..."
- "Décortiquons ensemble..."
- "Explorons les implications de..."
- "Commençons par..."
- "En conclusion..."
- "Pour résumer..."
- "En fin de compte..."
- "Sans plus attendre..."
- "Mais ce n'est pas tout..."

### Marqueurs de fausse nuance

- "Il convient de souligner..."
- "Il est crucial de comprendre..."
- "On ne peut pas ignorer le fait que..."
- "Cela ne fait aucun doute que..."
- "Il serait naïf de penser que..."
- "Bien que cela puisse sembler..."
- "Certes... mais..."

### Marqueurs d'exhaustivité simulée

- "De nombreux experts s'accordent à dire..."
- "Les études montrent que..." (sans citation)
- "Comme nous l'avons vu..."
- "Tout cela pour dire que..."
- "Il existe de nombreuses raisons pour lesquelles..."
- "La liste est longue..."

### Formules-accroches creuses

- "Un pattern troublant émerge de ces affaires"
- "Un fil rouge relie ces situations"
- "Ce qui se dessine est préoccupant"
- "La convergence est frappante"
- Toute phrase qui annonce une révélation sans rien révéler

Ce qu'il faut faire à la place : entrer directement dans le sujet avec des faits, des noms, des mécanismes concrets.

---

## Tournures interdites FR (haute sévérité)

### Mots bannis

| Mot/expression | Pourquoi c'est interdit | Alternative |
|----------------|------------------------|-------------|
| "fascinant" | Enthousiasme artificiel, non-informatif | Décrire ce qui est notable et pourquoi |
| "intéressant" | Jugement de valeur vide | Expliquer ce que ça change concrètement |
| "remarquable" | Superlatif creux | Préciser ce qui distingue le cas |
| "fait froid dans le dos" | Dramatisation vague | Nommer la conséquence précise |
| "glaçant" | Dramatisation vague | Idem |
| "édifiant" | Jugement moral déguisé | Décrire le mécanisme |

### Dramatiques vagues

"Fatal", "catastrophique", "désastreux" : ces mots ne sont autorisés que s'ils sont accompagnés de précisions :
- Pour QUI exactement ?
- À QUELLE échéance ?
- Par quel mécanisme ?

Sans ces précisions, reformuler avec des termes neutres et factuels.

### Adjectifs hyperboliques à la place de données

| Interdit | Pourquoi | Ce qu'il faut |
|----------|----------|---------------|
| "astronomique" | Pas une mesure | Le chiffre exact ou rien |
| "colossal" | Pas une mesure | Le chiffre exact ou rien |
| "vertigineux" | Pas une mesure | Le chiffre exact ou rien |
| "dérisoire" | Pas une mesure | Le chiffre exact ou rien |
| "pharaonique" | Pas une mesure | Le chiffre exact ou rien |

**Règle** : impact mesurable (eau, énergie, coût, émissions) = chiffre sourcé ou rien. Un adjectif n'est pas un chiffre.

### Formes pronominales interdites

- Jamais de "je" / "me" / "mon" dans les analyses
- Exception : formats qui exigent explicitement la première personne (éditorial signé, chronique)

---

## Section EN — Marqueurs en anglais

### Mots bannis (haute sévérité)

| Mot | Pourquoi |
|-----|----------|
| delve | Marqueur IA quasi-systématique, n'apporte rien |
| realm | Pompeux et vague |
| tapestry | Métaphore creuse |
| synergy | Jargon corporate vide de sens |

### Mots bannis (moyenne sévérité)

| Mot | Contexte interdit | Contexte accepté |
|-----|-------------------|-----------------|
| landscape | Usage métaphorique ("the AI landscape") | Usage littéral (paysage physique) |
| leverage | Comme verbe ("leverage this technology") | Comme nom technique en finance |
| utilize | Toujours | Remplacer par "use" |
| robust | Comme remplissage ("a robust solution") | Usage technique documenté |
| seamless | Comme marketing ("seamless experience") | Jamais, en pratique |
| paradigm | Comme remplissage ("a paradigm shift") | Usage épistémologique précis |

### Phrases bannies EN

- "It's important to note..."
- "In today's X landscape..."
- "Let's dive into..."
- "Let's delve into..."
- "At the end of the day..."
- "This is a game-changer"
- "Moving forward..."
- "It goes without saying..."
- "Needless to say..."

### Structures EN à proscrire

- "So," / "Now," / "Basically," / "Essentially," en début de phrase
- Title Case dans les titres quand sentence case est attendu (selon la convention éditoriale du média)

---

## Transparence structurelle

- JAMAIS mentionner le nombre d'articles ou de sources qui alimentent l'analyse ("sept cas", "trois enquêtes", "cinq analyses")
- Le lecteur ne doit PAS pouvoir deviner la mécanique de production (combien de sources, quel pipeline)
- Écrire comme si l'analyse était le fruit d'une réflexion organique, pas d'un assemblage

---

## Règle d'or

Si une formule peut s'appliquer à n'importe quel sujet sans modification, elle est probablement creuse. Chaque phrase doit être spécifique au contenu analysé.

**Test pratique** : Relire chaque phrase en se demandant *"Est-ce que je dirais ça à l'oral à quelqu'un que je respecte ?"*

- Si oui : garder.
- Si non : reformuler ou supprimer.
- Si hésitation : reformuler.

---

## Protocole de détection

Après toute génération de contenu, scanner le texte pour :

1. Présence de mots/expressions des listes ci-dessus (FR et EN)
2. Phrases applicables à n'importe quel sujet sans modification
3. Adjectifs hyperboliques non accompagnés de données chiffrées
4. Structures de phrases typiques de l'IA (ouvertures, transitions, conclusions)
5. Title Case là où sentence case est attendu

**Si un marqueur est détecté** : avertir avec les lignes concernées et proposer des alternatives spécifiques au contenu.
