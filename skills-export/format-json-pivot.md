---
name: format-json-pivot
description: Format JSON pivot pour le transit de données entre agents éditoriaux — structure complète d'un bit d'analyse avec metadata, scoring, analyse narrative, besoins utilisateur, distribution et pistes d'action. Contrat d'interface entre les agents de la chaîne éditoriale.
source: "Adapté de FLTR — format-json.md + format-json-light.md (structure JSON pivot)"
---

# Format JSON pivot [NOM_MEDIA]

## Structure complète

```json
{
  "metadata": {
    "url_source": "https://...",
    "titre_original": "...",
    "date_analyse": "2025-01-08T14:30:00Z",
    "source_type": "rss|bookmarklet|manuel"
  },

  "scoring": {
    "pertinence": {
      "total": 8,
      "intensite_dimensions": 3,
      "multi_dimensionnalite": 2,
      "activabilite": 2,
      "qualite_source": 1,
      "malus": 0
    },
    "documentaire": {
      "total": 7,
      "citations_nommees": 2,
      "donnees_chiffrees": 1,
      "cas_concret": 2,
      "acteurs_identifies": 1,
      "originalite_source": 1
    }
  },

  "analyse": {
    "pertinent": true,
    "nom": "Titre ÉDITORIALISÉ révélant l'enjeu systémique (ex: 'Quand X transforme Y en Z') - max 80 caractères",
    "description_courte": "Résumé en 1-2 phrases (max 280 caractères)",
    "description_longue": "Analyse narrative fluide et éditoriale (~1800 caractères, 3-4 paragraphes). Style : prose engagée, chiffres intégrés au récit, ton personnel assumé (cf. charte éditoriale). Chaque paragraphe apporte un éclairage différent sur les dynamiques systémiques, rapports de force, asymétries de pouvoir. Conclure par une phrase de synthèse qui révèle l'enjeu de fond.",

    "dimension_majeure": "[DIMENSION_1]",
    "dimensions": ["[DIMENSION_1]", "[DIMENSION_2]"],
    "dimensions_touchees": {
      "[DIMENSION_1]": ["Sous-dimension A", "Sous-dimension B"],
      "[DIMENSION_2]": ["Sous-dimension C"]
    },

    "niveau_levier": 7,
    "archetype": "Tragédie des communs",

    "points_vigilance": "Risque de greenwashing si l'initiative reste cosmétique..."
  },

  "user_needs": {
    "primary": "give_me_perspective",
    "secondary": ["educate_me"],
    "direction": "understanding",
    "value_gap": "Le post social pose la question. L'article web donne les clés de lecture systémique."
  },

  "distribution": {
    "template": "perspective",
    "linkedin_format": "A",
    "facebook_perso": true,
    "bluesky": true,
    "facebook_page": true
  },

  "pistes_systemiques": [
    {
      "type": "coalition",
      "emoji": "...",
      "titre": "VERBE À L'INFINITIF + complément concis (max 80 caractères). Ex: 'Créer des coalitions de données pour l'interopérabilité'",
      "description": "Explication DÉTAILLÉE de la piste (200-500 caractères). Nommer les acteurs spécifiques, le mécanisme précis, l'effet de levier visé. Expliquer COMMENT cette action crée un changement systémique.",
      "acteurs": ["société civile", "régulateurs"],
      "signal_structurel": "On saura que ça marche quand... (changement structurel mesurable, observable concrètement)"
    },
    {
      "type": "individuel",
      "emoji": "...",
      "titre": "VERBE À L'INFINITIF + action concrète. Ex: 'Auditer ses propres données avant de changer de service'",
      "description": "Explication de l'action individuelle avec effet démultiplicateur (pas juste 'migrer vers' ou 'boycotter'). Détailler le mécanisme d'effet de levier.",
      "signal_structurel": "On saura que ça marche quand..."
    }
  ],

  "citations_cles": [
    {
      "verbatim": "Citation TRADUITE EN FRANÇAIS (indiquer '[traduit de l'anglais]' si besoin). Minimum 15 mots pour être contextuelle.",
      "auteur": "Prénom Nom",
      "fonction": "Titre, Organisation",
      "contexte": "Dans quel cadre cette citation a été faite"
    }
  ],

  "contenu_source": "Texte complet de l'article (si score_documentaire >= 8)",

  "initiatives_detectees": [
    {
      "nom": "Nom de l'initiative/organisation/loi/outil (max 60 caractères)",
      "description": "Ce qu'elle fait ou a accompli concrètement (1-2 phrases, max 300 caractères)",
      "type_acteur": "Coalition|Institution publique|ONG|Mouvement citoyen|Entreprise/Startup|Individu",
      "pays": "Pays principal concerné (ou 'International')",
      "dimension_dominante": "[DIMENSION_1]",
      "dimensions": ["[DIMENSION_1]", "[DIMENSION_2]"],
      "source_url": "URL de la source primaire (site officiel, PAS l'article analysé)",
      "impact": "OBLIGATOIRE - Résultat chiffré concret (ex: '1,2 milliard d'amende', '50 000 utilisateurs', 'loi adoptée le 15/03/2025'). Si tu ne peux pas remplir ce champ avec un chiffre vérifiable, NE PAS inclure cette initiative.",
      "message_cle": "Pourquoi c'est une victoire ou un exemple à suivre (1 phrase percutante)"
    }
  ]
}
```

---

## NOTE : Dimensions thématiques paramétrables

Le champ `dimensions` (et ses dérivés `dimension_majeure`, `dimensions_touchees`, `dimension_dominante`) est **paramétrable** selon la ligne éditoriale du média. Chaque média définit ses propres dimensions d'analyse — thématiques, géographiques, sectorielles — qui structurent le scoring et la classification des contenus.

Exemples de configurations possibles :
- Un média tech : `["Vie privée", "Régulation", "Innovation", "Souveraineté", "Inclusion"]`
- Un média environnemental : `["Climat", "Biodiversité", "Énergie", "Justice sociale", "Gouvernance"]`
- Un média généraliste : `["Politique", "Économie", "Société", "Technologie", "International"]`

Le framework d'analyse sous-jacent (niveaux de levier, archétypes systémiques) reste générique.

---

## Règles de remplissage

### Champs obligatoires (toujours présents)
- `metadata.*`
- `scoring.pertinence.total`
- `scoring.documentaire.total`
- `analyse.pertinent`
- `analyse.nom`
- `analyse.description_courte`
- `analyse.dimension_majeure`
- `analyse.dimensions`

### Champs User Needs (toujours présents si pertinent = true)
- `user_needs.primary` : un des 8 codes (`update_me`, `keep_me_engaged`, `help_me`, `connect_me`, `educate_me`, `give_me_perspective`, `divert_me`, `inspire_me`)
- `user_needs.secondary` : tableau de 0-2 codes complémentaires
- `user_needs.direction` : `knowledge`, `doing`, `understanding`, `feeling`
- `user_needs.value_gap` : 1 phrase décrivant ce que le post social donne vs ce que l'article web approfondit
- `distribution.template` : `perspective`, `educate`, ou `signal`
- `distribution.linkedin_format` : `A`, `B`, ou `C`
- `distribution.facebook_perso` : boolean — publier sur le profil perso (copie manuelle)
- `distribution.bluesky` : boolean
- `distribution.facebook_page` : boolean (toujours true, syndication auto)

### Champs conditionnels
- `analyse.description_longue` : si pertinent = true
- `pistes_systemiques` : si pertinent = true
- `citations_cles` : si score_documentaire >= 5
- `contenu_source` : si score_documentaire >= 8
- `initiatives_detectees` : si pertinent = true ET initiative(s) remplissant les 5 critères d'inclusion. En cas de doute, retourner un tableau vide `[]`. La majorité des articles ne contiennent AUCUNE initiative qualifiée.

### Emojis pistes d'action
- Actions de coalition (collectif organisé) : emoji au choix du média
- Actions individuelles (choix personnels) : emoji au choix du média
- Actions de résistance (opposition active) : emoji au choix du média

### Limites de caractères
- `nom` : max 80 caractères, ÉDITORIALISÉ (révéler l'enjeu, pas résumer les faits)
- `description_courte` : max 280 caractères
- `description_longue` : ~1800 caractères, 3-4 paragraphes narratifs fluides
- `points_vigilance` : max 500 caractères

---

## Règles spécifiques pour les titres (`nom`)

### RÈGLE ABSOLUE : DIVERSITÉ DES STRUCTURES

**INTERDIT** : Commencer par "Quand" plus d'une fois sur 5 articles.

Tu DOIS alterner entre ces structures (choisir une structure DIFFÉRENTE à chaque article) :

| Structure | Exemple |
|-----------|---------|
| **[Sujet] + verbe d'action fort** | "L'Europe impose ses règles aux géants du cloud" |
| **[Chiffre/Fait] + conséquence** | "28 milliards de dollars : ICE se transforme en armée numérique" |
| **Question rhétorique** | "Qui contrôlera l'interface de demain ?" |
| **Deux-points révélateur** | "Modération algorithmique : le grand renoncement des plateformes" |
| **Opposition/Paradoxe** | "Plus de données, moins de vérité : le paradoxe de l'IA générative" |
| **Métaphore concrète** | "Les lunettes IA chinoises transforment chaque passant en suspect" |
| **Verbe à l'infinitif** | "Résister à la surveillance : le guide pratique des manifestants" |
| **Formule [X] vs [Y]** | "Vie privée vs innovation : le faux dilemme de la Silicon Valley" |

### À PROSCRIRE dans les titres
- **"Quand..." en début de titre** (sauf exception rare, max 1 sur 5)
- Acronymes anglo-saxons non traduits : CSAM, AI, ML, GDPR...
- Jargon technique sans explication : "nudify", "deepfake", "scraping"...
- Verbes anglais francisés : "générer du X", "pusher", "targeter"...
- Structures calquées de l'anglais

### À PRIVILÉGIER
- **Variété des attaques** : alterner les structures ci-dessus
- Français clair et accessible
- Si un terme technique est nécessaire, l'expliquer ou le remplacer :
  - "CSAM" -> "images pédocriminelles" ou "contenus pédopornographiques"
  - "nudify" -> "déshabillage par IA" ou "fausses images intimes"
  - "AI-generated" -> "générées par intelligence artificielle"
- Un titre doit faire sens pour quelqu'un qui ne connaît pas le sujet

### Style des titres
- **Éditorialisé** : révéler l'enjeu systémique, pas juste résumer les faits
- **Tension intellectuelle** : créer une friction, un paradoxe, une question
- **Éviter le sensationnalisme** : pas de formules choc gratuites
- **Mettre en lumière le mécanisme** : le "comment" plutôt que le "quoi"

### Exemples de BONS titres (structures variées)

| Structure utilisée | Exemple |
|-------------------|---------|
| Sujet + verbe fort | "Grok génère des images pédocriminelles sans aucun filtre" |
| Deux-points | "Modération IA : les plateformes choisissent l'aveuglement volontaire" |
| Paradoxe | "Plus on filtre, moins on protège : l'échec des algorithmes de modération" |
| Question | "Qui modère les modérateurs algorithmiques ?" |
| Chiffre + impact | "200 000 images illégales par jour : le déluge que personne ne veut voir" |
| Métaphore | "Les app stores deviennent des zones de non-droit numérique" |

### Exemples de MAUVAIS titres

- "Quand l'IA transforme..." (structure sur-utilisée)
- "Quand les plateformes..." (encore "Quand")
- "Grok génère du CSAM" (jargon + factuel)
- "L'IA de Musk produit des images pédocriminelles en masse" (sensationnalisme)

---

## Règles spécifiques pour les pistes d'action (`pistes_systemiques`)

### Format obligatoire
Chaque piste comprend :
- **titre** : VERBE À L'INFINITIF + complément concis (max 80 caractères)
- **description** : Explication détaillée (200-500 caractères)
- **signal_structurel** : Indicateur observable de succès

### Style des titres de pistes
- **Toujours commencer par un verbe à l'infinitif** : Créer, Transformer, Construire, Organiser, Développer...
- Le titre doit être autonome et compréhensible sans la description
- Éviter les verbes faibles : "Faire", "Mettre en place", "Permettre"

Exemples de bons titres :
- "Créer des coalitions de données pour la résistance par l'interopérabilité"
- "Transformer l'opacité budgétaire en transparence algorithmique obligatoire"
- "Construire des marchés alternatifs pour casser la dépendance technologique"

Exemples de mauvais titres :
- "Faire pression sur les régulateurs" (trop générique)
- "Migrer vers des alternatives" (trop vague)

### Qualité des pistes d'action
Les pistes doivent être :
1. **Spécifiques** : nommer les acteurs précis, les mécanismes concrets
2. **Créatives** : aller au-delà des évidences (boycott, pétition, migration)
3. **Systémiques** : viser des effets de levier, pas des actions isolées
4. **Réalistes** : s'ancrer dans des dynamiques existantes ou émergentes

### Pistes de résistance : approche non-violente stratégique

Pour les pistes de type Résistance, privilégier les méthodes qui **retirent le consentement** plutôt que d'affronter directement :

**À privilégier :**
- Identifier un **pilier de soutien vulnérable** (annonceurs, investisseurs, fournisseurs, employés-clés)
- Proposer des actions de **non-coopération** ciblées (retrait coordonné, boycott précis avec objectif mesurable)
- Créer des **alternatives parallèles** qui rendent l'adversaire obsolète
- Nommer des **coalitions inhabituelles** (ex: syndicats tech + associations consommateurs)

**À éviter :**
- Appels au boycott génériques sans mécanisme précis ni cible identifiée
- Actions qui donneraient un prétexte de victimisation à l'adversaire
- Formulations pouvant être perçues comme incitation à l'illégalité
- Confrontations directes quand le retrait de consentement est possible

**Exemple transformé :**
- Mauvais : "Boycotter les plateformes qui exploitent les données"
- Bon : "Organiser un retrait coordonné des comptes Premium avec un collectif citoyen pour fragiliser le pilier 'clients entreprise' du fournisseur"

### Pistes à ÉVITER (trop génériques)
- "Migrer vers des alternatives"
- "Faire pression sur les régulateurs"
- "Sensibiliser le public"
- "Exiger plus de transparence"
- "Boycotter la plateforme"

### Pistes à PRIVILÉGIER (créatives et spécifiques)
- Identifier des coalitions inhabituelles (ex: "alliance régulateurs + assureurs")
- Exploiter des leviers économiques concrets (ex: "cibler les annonceurs du secteur X")
- Proposer des mécanismes innovants (ex: "certification indépendante avec audit public")
- S'appuyer sur des précédents (ex: "utiliser le modèle du recours collectif Y")

### Structure d'une bonne piste
1. **Titre** : verbe infinitif + action concrète
2. **Description** : qui + quoi + comment + effet de levier
3. **Signal** : changement structurel observable

---

## Règles spécifiques pour les citations (`citations_cles`)

### Langue
- **Toujours traduire** les citations en français
- Indiquer entre crochets la langue originale si pertinent : "[traduit de l'anglais]"

### Longueur minimale
- Une citation doit faire **minimum 15 mots** pour être contextuelle
- Éviter les citations trop courtes qui ne veulent rien dire hors contexte
- Mauvais : "illegal and appalling" -> trop court
- Bon : "Ces contenus sont illégaux et révoltants, et nous attendons de la plateforme qu'elle prenne des mesures immédiates" -> contextualisé

### Sélection des citations
- Privilégier les citations qui révèlent une position, un rapport de force, une tension
- Éviter les déclarations corporate vides ("nous prenons ce sujet très au sérieux")
- Inclure le contexte : qui parle, à quelle occasion, avec quel enjeu

### Nombre de citations
- 2-4 citations maximum
- Mieux vaut 2 bonnes citations que 4 médiocres

---

## Style narratif de la `description_longue`

### Ton éditorial
- Écrire en **prose fluide**, pas en liste de faits
- Adopter un ton personnel et engagé (cf. charte éditoriale)
- Les chiffres doivent être **intégrés au récit**, pas listés
- Utiliser des formulations qui créent du relief : "ce qui frappe", "le problème systémique", "on observe ici"

### Structure recommandée (3-4 paragraphes)
1. **Accroche contextuelle** : situer l'enjeu, donner l'échelle (chiffres clés intégrés)
2. **Analyse des mécanismes** : expliquer le "comment", les dynamiques à l'oeuvre
3. **Enjeu systémique** : relier aux dimensions, montrer les rapports de force
4. **Phrase de synthèse** : révéler l'enjeu de fond en une formule

### Exemples de style

Mauvais (style liste/factuel) :
> "Budget de 28,7 milliards. Triple de 2024. 14ème force militaire mondiale. Outils : Cellebrite (11M$), Paragon (2M$), Clearview AI (10M$)."

Bon (style narratif/éditorial) :
> "Cette initiative fait froid dans le dos : ICE dispose désormais d'un budget de 28,7 milliards de dollars pour 2025, soit le triple de 2024. Pour donner une idée de l'ampleur, ce montant placerait ICE comme la 14e force militaire la mieux financée au monde."

### À éviter
- Énumérations sèches de faits ou d'outils
- Répétition des termes techniques sans contextualisation
- Ton neutre/journalistique qui ne révèle pas les enjeux
- Conclusions vagues ("c'est préoccupant", "à surveiller")

---

## Règles spécifiques pour les initiatives (`initiatives_detectees`)

### Qu'est-ce qu'une initiative ?

Une initiative est une **action concrète avec un résultat mesurable** qui illustre une ou plusieurs dimensions en action. Ce sont des exemples de victoires, d'outils, de coalitions ou de régulations qui fonctionnent.

### Critères d'inclusion (TOUS les 5 requis, sans exception)

1. **Action CONCRÈTE ET ACHEVÉE** : un résultat obtenu, pas un projet en cours ou une annonce
2. **Résultat MESURABLE avec chiffre** : victoire juridique (amende, décision rendue), adoption d'une loi (date, pays), nombre d'utilisateurs/membres, impact quantifiable. Si tu ne peux pas citer UN chiffre concret, ce n'est pas une initiative qualifiée.
3. **Source VÉRIFIABLE** : URL vers site officiel ou source primaire (pas l'article analysé lui-même)
4. **Réplicable ou inspirant** : peut servir de modèle pour d'autres contextes
5. **Lien DIRECT avec les dimensions thématiques du média** : l'initiative doit porter sur le périmètre éditorial défini. Une initiative hors périmètre ne qualifie PAS.

### Critères d'exclusion (un seul suffit pour exclure)

- Simples annonces, déclarations d'intention, déclarations diplomatiques
- Projets en cours sans résultat tangible obtenu
- Entreprises/outils mentionnés négativement (surveillance, exploitation, contournement)
- Initiatives déjà très connues sans nouvel élément
- Études, rapports ou recherches académiques (ce sont des sources, pas des initiatives)
- Groupes politiques, PACs, partis ou coalitions électorales
- Initiatives hors périmètre éditorial
- Contournements réglementaires ou pratiques de zone grise légale
- Entités simplement MENTIONNÉES dans l'article sans action propre décrite

### Nombre d'initiatives par article

- **0** : Cas le plus fréquent. La majorité des articles ne contiennent PAS d'initiative qualifiée.
- **1** : Cas typique quand une initiative existe. UNE seule, la plus significative.
- **2** : Maximum absolu. Uniquement si deux initiatives DISTINCTES et TOUTES DEUX exceptionnelles.
- **Jamais 3 ou plus** : Si tu en trouves plus de 2, c'est que tes critères sont trop lâches.

**RÈGLE CLÉ** : En cas de doute, ne PAS inclure. Mieux vaut 0 initiative de qualité que 3 initiatives médiocres.

### Qualité du `message_cle`

Le message clé doit répondre à : **"Pourquoi cette initiative est-elle inspirante ?"**

Bons exemples :
- "La mobilisation citoyenne peut façonner la régulation de l'IA"
- "Une ville peut créer des outils souverains ET les partager"
- "Le droit à l'effacement à l'échelle industrielle"

Mauvais exemples :
- "C'est une bonne initiative" (vide)
- "Ils ont fait quelque chose" (non informatif)
- Description technique sans angle inspirant

### Priorité des sources

Pour `source_url`, privilégier dans cet ordre :
1. Site officiel de l'organisation/initiative
2. Page gouvernementale/institutionnelle
3. Article de presse de référence (si pas de site officiel)

---

## Contexte éditorial allégé (pour les générateurs de posts sociaux)

Ce document décrit les conventions éditoriales des champs d'analyse que l'agent transforme en post social. Il permet de comprendre l'intention derrière chaque champ reçu.

### Champs principaux de l'analyse

- **`nom`** : Titre ÉDITORIALISÉ révélant l'enjeu systémique (max 80 caractères)
- **`description_courte`** : Résumé en 1-2 phrases (max 280 caractères)
- **`description_longue`** : Analyse narrative fluide et éditoriale (~1800 caractères, 3-4 paragraphes). Prose engagée, chiffres intégrés au récit, ton personnel assumé.
- **`dimensions`** : Liste des dimensions thématiques touchées (paramétrables par le média)
- **`points_vigilance`** : Risques, limites, angles morts de l'initiative analysée
- **`pistes_systemiques`** : Actions concrètes avec titre (verbe infinitif), description et signal structurel

Ce contexte allégé suffit pour les agents en aval (générateurs de posts sociaux). Le JSON complet est le contrat d'interface pour les agents d'analyse.
