---
name: format-linkedin
description: Format de publication LinkedIn optimisé pour un média d'analyse — trois formats (A décryptage, B récit, C questionnement) avec structures, longueurs cibles, formatage et exemples. Charger quand la plateforme cible est LinkedIn.
source: "Adapté de FLTR — formats/linkedin.md"
---

# Instructions de format — LinkedIn

## Objectif

Transformer une analyse éditoriale en post LinkedIn engageant et professionnel, prêt à publier.

## Audience cible

- Journalistes
- Professionnels des médias
- Communicants
- Défenseurs des libertés numériques

---

## Règles communes aux 3 formats

### Qualité non-négociable

- **Charte éditoriale** : toutes les règles de la charte s'appliquent intégralement (factualité, ton, posture, IA-speak interdit, invisibilité des cadres théoriques). Charger le skill `charte-editoriale` avant toute production.
- **Garde-fous factualité** : charger le skill `garde-fous-factualite` — règles de citation, chiffres, et scan post-génération. Ces règles priment sur les contraintes de format.
- **Contrainte factuelle** : ne JAMAIS compresser une chaîne causale multi-étapes (A -> B -> C) en raccourci (A -> C)
- **Pistes systémiques** : toujours présentes dans le post, quelle que soit la forme
- **Citation** : intégrer UNE citation précise de l'article original en respectant strictement la discipline verbatim/paraphrase (voir garde-fous-factualite). Si la citation originale est en langue étrangère : paraphraser sans guillemets OU citer un court fragment traduit avec mention "[traduit de l'anglais]".
- **Longueur max** : 2990 caractères (limite LinkedIn)

### Ton et style

#### A faire

- Ton factuel, pédagogique
- Expliciter les enjeux pour l'audience
- Rester ancré dans les faits de l'article
- Utiliser doubles sauts de ligne pour aérer
- Varier la longueur des phrases (mélanger phrases courtes et longues)

#### A éviter

- Jargon technique excessif
- Ton condescendant ou moralisateur
- Sensationnalisme
- Anecdotes personnelles inventées
- Wishful thinking sans ancrage
- Phrases de longueur uniforme (signal IA)
- Transitions trop lisses entre paragraphes (signal IA)

### Format de sortie JSON

```json
{
  "titre": "Titre court (max 60 caractères)",
  "hook": "La phrase d'accroche seule",
  "body": "Le post complet (tout le contenu du post)",
  "cta_commentaire": "Le CTA à poster en premier commentaire (optionnel)",
  "format_used": "A",
  "lien_article": "[URL_ARTICLE]"
}
```

Le champ `format_used` doit contenir "A", "B" ou "C" selon le format utilisé.

---

## Choix du format par User Need

| User Need primaire | Format LinkedIn | Raison |
|---|---|---|
| `give_me_perspective` | **A** (Décryptage) | Analyse structurée avec implications |
| `educate_me` | **A** (Décryptage) | Pédagogie avec bullets d'implications |
| `help_me` | **A** (Décryptage) | Guide pratique structuré |
| `inspire_me` | **B** (Récit) | Narration de victoire, dynamique positive |
| `connect_me` | **B** (Récit) | Récit de coalition, voix collectives |
| `update_me` | **C** (Questionnement) | Fait bref + question de perspective |
| `keep_me_engaged` | **C** (Questionnement) | Angle inattendu, curiosité |
| `divert_me` | Pas de post LinkedIn | — |

---

## FORMAT A — Décryptage structuré

**Quand l'utiliser** : sujets techniques, outils concrets, régulations, guides pratiques, analyses avec données chiffrées.

**Longueur cible** : 1300-1800 caractères

### Structure

#### 1. Hook (1 phrase, max 15 mots)

- **Objectif** : Arrêter le scroll
- **Ton** : Percutant, factuel
- **Variantes possibles** : constat chiffré, question factuelle, fait brut inattendu

#### 2. Contexte (2-3 phrases, max 60 mots)

- **Objectif** : Planter le décor
- **Ton** : Factuel, situe rapidement le sujet

#### 3. Analyse (200-300 mots)

- **Objectif** : Corps pédagogique
- **Ton** : Conversationnel mais précis
- Développer les mécanismes, enjeux de pouvoir, dynamiques systémiques
- Intégrer la citation de l'article original

#### 4. Implications concrètes (3-4 bullets)

Ce que ça change concrètement :
-> Impact pour l'audience (journalistes, communicants, professionnels)
-> Impact pour l'écosystème plus large
-> Signaux à surveiller ou conséquences systémiques

#### 5. Piste d'action en question (2-3 phrases, max 60 mots)

Transformer UNE des pistes systémiques en question **"Et si..."** engageante.
Formuler de manière prospective et ouverte (pas prescriptive).

**Pour les pistes de résistance** : Privilégier les formulations qui évoquent le retrait de consentement ou de soutien (économique, symbolique) plutôt que l'affrontement direct. Nommer si possible le "pilier de soutien" ciblable (annonceurs, investisseurs, clients entreprise, employés-clés).

#### 6. Call to action (varier entre ces options)

- "Et vous, avez-vous déjà été confronté à ce problème ? Vous avez mis en place des solutions ?"
- "Vous avez observé des signaux similaires dans votre secteur ?"
- "Des exemples concrets de cette dynamique que vous auriez documentés ?"

### Formatage Format A

- Bullets avec `->` (pas `-` ou puce)
- Piste d'action entre guillemets : "Et si [proposition] ?"
- Doubles sauts de ligne entre chaque section
- **PAS de gras sur le hook** (incompatible VoiceOver/accessibilité)

---

## FORMAT B — Récit systémique

**Quand l'utiliser** : mécanismes systémiques complexes (2+ dimensions impliquées), dynamiques de pouvoir, sujets où l'enchaînement causal est central, articles à forte dimension narrative.

**Longueur cible** : 1400-2000 caractères

### Structure

Un récit continu, sans sections visibles. Le lecteur suit un fil qu'on déroule.

#### 1. Ouverture par un fait concret et spécifique (1-2 phrases)

Pas de hook générique. Un fait daté, localisé, précis. Le lecteur doit se dire "ah, tiens".

#### 2. Premier niveau : ce qu'on voit en surface (2-3 phrases)

Poser ce que l'article décrit factuellement. Intégrer la citation ici si elle illustre bien la surface.

#### 3. Deuxième niveau : le mécanisme sous-jacent (3-5 phrases)

Tirer le fil. Montrer ce qui se joue en dessous — les rapports de force, les incitations structurelles, les logiques économiques ou politiques. C'est ici que l'analyse systémique opère, sans nommer les cadres.

#### 4. Troisième niveau : la dynamique systémique (2-3 phrases)

Élargir. Montrer en quoi ce cas illustre une tendance plus large, un pattern récurrent. Connecter à d'autres signaux si pertinent.

#### 5. Ouverture prospective intégrée au récit (2-3 phrases)

Pas de "Et si..." formel. La piste d'action émerge naturellement du récit. Formuler comme une suite logique du raisonnement.

#### 6. Question ouverte de clôture (1 phrase)

Une question sincère, intégrée au flux du texte. Pas un CTA mécanique — une vraie question qui prolonge la réflexion.

### Formatage Format B

- **Aucun bullet**, aucune liste, aucun `->`.
- **Aucune section visible** (pas de "Ce que ça change", pas de "Et si...")
- Paragraphes de longueur variable (certains courts — 1 phrase — d'autres plus développés)
- Doubles sauts de ligne entre paragraphes pour aérer
- La citation de l'article s'intègre dans le flux narratif (entre guillemets)
- Ton : comme une conversation entre pairs qui réfléchissent ensemble

---

## FORMAT C — Questionnement éclairant

**Quand l'utiliser** : sujets qui questionnent un paradigme, une croyance dominante, un consensus apparent. Quand l'angle le plus intéressant est une question, pas une réponse.

**Longueur cible** : 900-1500 caractères (le plus compact des 3 formats)

### Structure

#### 1. Question d'ouverture (1-2 phrases)

Une question sincère qui recadre le sujet sous un angle inattendu.
Pas une question rhétorique dont on connaît la réponse. Une vraie question qui déstabilise une certitude.

Formulations possibles :
- "Que se passerait-il si [hypothèse contre-intuitive] ?"
- "Et si on regardait [sujet] sous l'angle de [perspective inattendue] ?"
- "[Fait concret]. Et si c'était le symptôme de [dynamique plus profonde] ?"

#### 2. Exploration (3-4 paragraphes denses)

Explorer la question avec rigueur.
- Premier paragraphe : poser les faits de l'article, le contexte factuel
- Deuxième paragraphe : explorer l'angle soulevé par la question, avec la citation de l'article
- Troisième paragraphe : élargir — connecter à une dynamique systémique, montrer les implications

Chaque paragraphe doit faire avancer la réflexion, pas tourner en rond.

#### 3. Retournement ou ouverture inattendue (1-2 phrases)

Un éclairage que le lecteur n'avait pas anticipé. Pas une "conclusion" — un déplacement du regard. La piste d'action systémique peut s'intégrer ici comme une possibilité à explorer.

#### 4. Invitation à la réflexion collective (1 phrase)

Pas un CTA classique. Une invitation directe, courte, qui prolonge le questionnement.

### Formatage Format C

- **Paragraphes denses** mais aérés (doubles sauts de ligne)
- Peut utiliser un ou deux `->` pour des implications, mais pas obligatoire
- La question d'ouverture n'est PAS en gras (accessibilité VoiceOver)
- Ton : doute constructif, curiosité, jamais provocation ou polarisation
- Plus court que les formats A et B — la concision est une force ici
