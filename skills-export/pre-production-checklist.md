---
name: pre-production-checklist
description: Checklist bloquante avant toute production éditoriale — chargement des référentiels, vérification pré-écriture, signalement proactif. Inclut le protocole renforcé pour les productions hors pipeline (articles de fond, transcriptions, synthèses). BLOQUANT — aucun contenu ne doit être généré avant complétion.
source: "Adapté de FLTR — rules/editorial-pre-production.md + rules/article-hors-pipeline.md"
---

# Pré-production éditoriale (BLOQUANT)

Avant toute production de contenu éditorial — posts réseaux sociaux, articles, analyses, newsletters, synthèses — ces étapes sont OBLIGATOIRES. Aucun contenu ne doit être généré avant leur complétion.

---

## Étape 1 : Charger les référentiels éditoriaux

Charger dans cet ordre :

1. **Charte éditoriale** (skill `charte-editoriale`) : règles non-négociables — factualité, ton, posture, IA-speak interdit, invisibilité des cadres théoriques
2. **Analyse systémique** (skill `analyse-systemique`) : framework analytique — grilles d'analyse, leviers systémiques, archétypes, modes d'action

Ces référentiels PRIMENT sur les instructions de format par plateforme. En cas de conflit, ils gagnent.

La grille d'analyse structure le raisonnement en coulisses. Ses cadres théoriques ne doivent JAMAIS apparaître dans le texte final.

## Étape 2 : Charger le format cible

Charger le skill de format correspondant à la plateforme visée (LinkedIn, Facebook, Bluesky, Mastodon, Instagram, newsletter, etc.).

Un format ne dispense jamais de la charte éditoriale ni de la grille d'analyse.

## Étape 3 : Vérification pré-écriture

Avant de rédiger, vérifier sur chaque affirmation prévue :

- **FAIT documenté et sourcé ?** → formuler comme fait
- **Contexte inférable mais non sourcé ?** → formuler comme contexte, signaler la limite
- **Interprétation ou analyse ?** → utiliser le ton analytique, pas affirmatif
- **Hypothèse ou projection ?** → conditionnel obligatoire

## Étape 4 : Signalement proactif

Si une formulation pose un doute factuel, de ton ou de posture : le signaler AVANT de livrer le texte, pas attendre la relecture du demandeur.

---

## Déclencheurs

Cette règle s'applique dès qu'une demande implique la production de texte destiné à être publié ou diffusé. Cela inclut :

- Posts réseaux sociaux (LinkedIn, Facebook, Twitter/X, Bluesky, Mastodon, Instagram)
- Articles web
- Newsletters
- Synthèses éditoriales
- Tout contenu dérivant d'une analyse éditoriale

Ne s'applique PAS : code, config, documentation technique, messages conversationnels.

---

---

# Protocole hors pipeline (BLOQUANT)

## Pourquoi ce protocole existe

Quand un pipeline automatisé est en place, chaque claim est classifié avant de devenir prose — le format structuré (JSON pivot, base de données) protège contre la fabrication. Hors pipeline, il n'y a pas d'équivalent automatique. La prose commence trop tôt, comble les lacunes avec des détails plausibles, et présente comme certains des éléments qui ne le sont pas.

Ce protocole reproduit manuellement les contraintes d'un pipeline structuré.

**Ces étapes sont séquentielles et bloquantes. Aucune étape ne commence avant que la précédente soit validée.**

---

## Étape HP-1 — Délimitation des sources (BLOQUANT)

Avant tout, identifier et lister explicitement :

- **Quelles sont les sources primaires disponibles ?** (fichier, URL, transcription, document)
- **Quelle est la fiabilité de chaque source ?** (article publié / transcription automatique / témoignage / donnée utilisateur)
- **Quelles sont les limites connues de chaque source ?** (transcription automatique = attributions incertaines, données utilisateur = non vérifiées, etc.)

### Règle transcription automatique (Whisper, sous-titres, etc.)

- Les attributions de locuteurs sont considérées **INCERTAINES** par défaut
- Tout nom propre attribué à un locuteur doit être accompagné d'un **timestamp vérifiable**
- Sans timestamp → pas de nom propre dans l'article, **formulation anonyme obligatoire**
- Ne jamais consolider deux phrases d'un locuteur en une citation condensée présentée comme verbatim

**Ne pas passer à l'étape suivante avant que la liste des sources et leurs limites soient posées.**

---

## Étape HP-2 — Inventaire des claims (PIVOT MANUEL — BLOQUANT)

Avant d'écrire une ligne de prose, produire le tableau suivant pour TOUS les claims factuels prévus dans l'article. Ce tableau est livré à l'utilisateur pour validation avant rédaction.

| # | Claim | Type | Source | Statut |
|---|---|---|---|---|
| 1 | [affirmation exacte] | STAT / CITATION / FAIT / CHIFFRE / ANALYSE / HYPOTHÈSE | [source précise + URL ou timestamp] | VÉRIFIÉ / À VÉRIFIER / INCERTAIN / SUPPRIMER |

### Types de claims

- `STAT` : statistique chiffrée
- `CITATION` : parole attribuée à une personne nommée
- `FAIT` : événement ou état documenté
- `CHIFFRE` : donnée quantitative (budget, nombre, date)
- `ANALYSE` : interprétation — doit être formulée comme telle dans le texte
- `HYPOTHÈSE` : projection ou inférence — conditionnel obligatoire dans le texte

### Statuts

- `VÉRIFIÉ` : source primaire confirmée, URL ou timestamp disponible
- `À VÉRIFIER` : source probable mais non confirmée — lancer la vérification avant de continuer
- `INCERTAIN` : source introuvable ou attribution douteuse — reformuler ou supprimer
- `SUPPRIMER` : introuvable dans les sources disponibles — ne pas utiliser

### Règles absolues sur le statut

- Un claim `À VÉRIFIER` ne peut pas entrer dans la prose avant d'avoir changé de statut
- Un claim `INCERTAIN` ne peut jamais apparaître comme fait dans le texte
- Un claim `SUPPRIMER` n'apparaît pas, quelle que soit sa vraisemblance

### Règle sur les données fournies par l'utilisateur

Tout chiffre, fait ou affirmation introduit par l'utilisateur dans la conversation est automatiquement taggué `À VÉRIFIER`. L'utilisateur n'est pas une source primaire vérifiable. Sa bonne foi n'est pas en question — la traçabilité l'est.

**Ne pas passer à l'étape suivante avant que le tableau soit validé par l'utilisateur.**

---

## Étape HP-3 — Vérification avant prose (BLOQUANT)

Pour chaque claim taggué `À VÉRIFIER` dans le tableau :

1. Lancer la vérification (recherche web, consultation du fichier source, recoupement)
2. Mettre à jour le statut dans le tableau : `VÉRIFIÉ` avec URL/timestamp, ou `SUPPRIMER`
3. Pour les citations : distinguer **VERBATIM** (texte exact) ou **PARAPHRASE** (sens général)

**Le tableau complété et validé est la condition nécessaire pour commencer la rédaction.**

---

## Étape HP-4 — Rédaction avec discipline citation

### Règle citations (non négociable)

Deux catégories, strictement étanches :

**VERBATIM** = guillemets + source citée dans la même phrase ou le paragraphe immédiat
- Exemple correct : Le ministre a déclaré : « C'est du jamais vu. » [source, date]
- Si la source ne peut pas être citée dans la même phrase → pas de guillemets

**PARAPHRASE** = pas de guillemets + formulation signalante obligatoire
- Formulations autorisées : "selon ses propres termes", "il a indiqué que", "dans l'esprit de ce qu'il a dit"
- Formulations interdites : toute formulation qui fait croire à une citation directe sans l'être

**Aucun entre-deux.** Une formulation qui ressemble à une citation sans en être une est une erreur factuelle, pas stylistique.

### Règle chiffres ronds

Tout chiffre terminant par 0 ou 5 sans source dans le tableau de claims déclenche un flag automatique. Les chiffres ronds sont les plus susceptibles d'être des approximations présentées comme des faits.

### Stades du document

Marquer le fichier selon son stade d'avancement :

- `[DRAFT-1]` : claims en cours de vérification — ne pas partager
- `[DRAFT-2]` : tous les claims vérifiés, en attente de relecture
- `[FINAL]` : validé par l'utilisateur pour publication

---

## Scan post-rédaction automatique

Après écriture, scanner le texte pour :

1. **Guillemets sans source** dans la même phrase → flag
2. **Noms propres de locuteurs** issus d'une transcription sans timestamp → flag
3. **Statistiques (%)** sans lien source → flag
4. **"Selon", "d'après", "a déclaré"** sans attribution sourcée → flag
5. **Chiffres fournis en conversation** par l'utilisateur sans vérification externe → flag

Chaque flag est signalé avant livraison. L'utilisateur décide de corriger ou d'assumer.

---

## Déclencheurs du protocole hors pipeline

Ce protocole s'active pour :

- Articles de fond construits de zéro (pas d'article source unique)
- Analyses de transcriptions (Whisper, sous-titres, notes de réunion)
- Synthèses multi-sources (plus de deux sources primaires)
- Articles combinant sources externes et témoignages/données utilisateur
- Tout contenu où la source primaire n'est pas un article publié par un média identifié

Ne s'active PAS pour le pipeline standard qui a ses propres contraintes structurelles via le format pivot.
