# Spécification fournisseur — Contrat d'interface pour l'alimentation de Newsadix

## Objet

Ce document définit le contrat d'interface que tout fournisseur de contenu doit respecter pour alimenter Newsadix en bits d'information. Il est **agnostique** : il ne présuppose aucun pipeline, aucun outil, aucun framework d'analyse côté fournisseur.

Un fournisseur peut être un journaliste freelance, un média partenaire, un projet éditorial automatisé, un chercheur ou toute entité capable de produire des fragments d'information sourcés et conformes à ce schéma.

Ce document est le seul contrat entre Newsadix et ses fournisseurs. Tout ce qui n'est pas spécifié ici relève de la responsabilité du fournisseur.

---

## Sommaire

1. [Définitions](#1-définitions)
2. [Le bit — unité de livraison](#2-le-bit--unité-de-livraison)
3. [Champs obligatoires](#3-champs-obligatoires)
4. [Champs optionnels](#4-champs-optionnels)
5. [Règles de validation](#5-règles-de-validation)
6. [Taxonomie](#6-taxonomie)
7. [Cycle de vie](#7-cycle-de-vie)
8. [Interface de livraison](#8-interface-de-livraison)
9. [Contrat de qualité](#9-contrat-de-qualité) (dont [§9.3 Propriété intellectuelle](#93-propriété-intellectuelle))
10. [Identification du fournisseur](#10-identification-du-fournisseur)
11. [Corrections et mises à jour](#11-corrections-et-mises-à-jour)
12. [Annexe A — Référence des valeurs enum](#annexe-a--référence-des-valeurs-enum)
13. [Annexe B — Exemples de soumission](#annexe-b--exemples-de-soumission)

---

## 1. Définitions

| Terme | Définition |
|-------|-----------|
| **Bit** | Unité atomique d'information : un fragment sourcé, typé, horodaté. Réf. : `editorial/schema-bit.md` |
| **Fournisseur** | Toute entité qui soumet des bits à Newsadix |
| **Récepteur** | Newsadix, en tant que consommateur et assembleur des bits |
| **Assemblage** | Résultat de l'exécution d'un template Newsadix sur un ensemble de bits. Le fournisseur ne produit **jamais** d'assemblage — c'est la responsabilité exclusive de Newsadix |
| **Soumission** | Envoi d'un ou plusieurs bits au récepteur pour validation et intégration |
| **Lot** | Groupe de bits soumis en une seule opération |

---

## 2. Le bit — unité de livraison

Le fournisseur livre des **bits**, pas des articles, pas des dépêches, pas des analyses. Chaque bit est un fragment autonome : une phrase à un paragraphe court, sourcé et typé.

Un article de 500 mots ne constitue pas un bit. Il doit être décomposé en plusieurs bits avant soumission.

### Quatre types de bits

| Type | Contenu | Contrainte |
|------|---------|-----------|
| `fait` | Un événement ou un état documenté | Vérifiable, passé ou présent, pas conditionnel |
| `donnee` | Une valeur quantitative sourcée | Doit contenir au moins un chiffre |
| `contexte` | Un élément de cadrage qui éclaire un fait | Ne prend pas parti, ne prédit pas |
| `point_de_vue` | Une position attribuée à une personne nommée | L'acteur doit être identifié dans le champ `acteurs[]` |

### Taille

- Minimum : 1 caractère (un chiffre brut est un bit `donnee` valide)
- Maximum : 2 000 caractères
- Recommandé : 100 à 500 caractères

---

## 3. Champs obligatoires

Tout bit soumis **doit** contenir ces champs. L'absence de l'un d'eux entraîne le rejet de la soumission.

### 3.1 `id`

Identifiant unique attribué par le fournisseur.

- Format : `bit-YYYY-MM-DD-NNN` (date de création + numéro séquentiel)
- Le fournisseur gère sa propre séquence
- Newsadix peut réattribuer un ID interne, mais l'ID fournisseur est conservé pour traçabilité
- Exemples : `bit-2026-04-15-001`, `bit-2026-04-15-042`

### 3.2 `type`

Catégorie du bit. Valeurs autorisées : `fait`, `donnee`, `contexte`, `point_de_vue`.

### 3.3 `contenu`

Texte du fragment. 1 à 2 000 caractères. En français.

### 3.4 `sources[]`

Tableau de sources. **Minimum une source.**

Chaque source est un objet avec :

| Champ | Obligatoire | Type | Description |
|-------|:-----------:|------|-------------|
| `nom` | Oui | string | Nom de la source (organisme, personne, publication) |
| `type_source` | Oui | enum | Nature de la source (voir [Annexe A](#annexe-a--référence-des-valeurs-enum)) |
| `url` | **Oui** | URI | Lien vers la source primaire. Permet au récepteur de vérifier le bit et de remonter à l'origine |
| `date_acces` | Non | ISO 8601 | Date de consultation de la source |

L'URL est obligatoire. Un bit sans URL vérifiable est rejeté (code `E011`). Exception unique : les bits issus de déclarations orales directes (conférence de presse, interview en personne) où aucune URL n'existe — dans ce cas, le champ `type_source` doit être `declaration` ou `temoignage`.

### 3.5 `auteur`

Identité du producteur du bit.

| Champ | Obligatoire | Type | Description |
|-------|:-----------:|------|-------------|
| `type` | Oui | enum | `humain`, `agent`, `hybride` |
| `id` | Oui | string | Identifiant du producteur (nom, identifiant système, etc.) |
| `valide_par` | Conditionnel | string | Identifiant du validateur humain. **Obligatoire si `type` = `agent` ou `hybride`** |

### 3.6 `horodatage_creation`

Date et heure de création du bit. Format ISO 8601 avec fuseau horaire.

Exemple : `2026-04-15T14:30:00+02:00`

### 3.7 `geo`

Périmètre géographique du fait décrit.

Valeurs autorisées : `france`, `france_monde`, `monde`.

### 3.8 `pilier`

Catégorie taxonomique principale. 12 valeurs autorisées (voir [Annexe A](#annexe-a--référence-des-valeurs-enum)).

Le fournisseur assigne le pilier selon son propre jugement. Newsadix peut le reclassifier lors de la validation.

### 3.9 `user_need`

Besoin utilisateur adressé par ce bit.

| Champ | Obligatoire | Type | Description |
|-------|:-----------:|------|-------------|
| `primaire` | Oui | enum | Besoin dominant (8 valeurs, voir [Annexe A](#annexe-a--référence-des-valeurs-enum)) |
| `secondaire` | Non | array | 0 à 2 besoins complémentaires |

### 3.10 `statut`

État du bit au moment de la soumission.

Le fournisseur soumet des bits avec le statut `brouillon`. Newsadix les fait passer à `valide` puis `publie` selon son propre processus de validation. Le fournisseur ne peut pas soumettre un bit directement en statut `publie`.

---

## 4. Champs optionnels

Ces champs enrichissent le bit et améliorent son intégration dans la base Newsadix. Ils ne sont pas requis pour la validation, mais leur présence augmente la valeur du bit.

### 4.1 `horodatage_evenement`

Date/heure de l'événement décrit, si différente de la date de création du bit. ISO 8601.

**Recommandation forte** pour les bits `fait` et `donnee` : un fait a une date. La préciser permet l'ordonnancement chronologique et la détection de doublons.

### 4.2 `sous_theme`

Sous-catégorie du pilier. Texte libre, mais les valeurs standard de la taxonomie Newsadix sont préférées (voir `editorial/taxonomie-editoriale.md`).

Exemples : `intelligence_artificielle`, `cybersecurite`, `climat`, `politique_nationale`.

### 4.3 `relations[]`

Connexions sémantiques avec d'autres bits **du même fournisseur** (dans le même lot ou dans des lots précédents).

| Champ | Obligatoire | Type | Description |
|-------|:-----------:|------|-------------|
| `type` | Oui | enum | `met_a_jour`, `contextualise`, `contredit`, `illustre`, `meme_sujet`, `meme_acteur`, `consequence` |
| `cible` | Oui | string | ID du bit cible |
| `direction` | Non | enum | `sortante` (ce bit agit sur la cible) ou `entrante` (la cible agit sur ce bit) |
| `confiance` | Non | number | Score 0-1. 1 = relation certaine, < 1 = proposition |

**Note** : Newsadix enrichit les relations via son propre agent de plexage. Les relations fournisseur sont des indications, pas des contraintes.

### 4.4 `acteurs[]`

Personnes et organisations mentionnées dans le bit.

| Champ | Obligatoire | Type | Description |
|-------|:-----------:|------|-------------|
| `nom` | Oui | string | Nom complet |
| `role` | Non | string | Rôle dans le contexte du bit (sujet, source, réacteur, etc.) |
| `wikidata_id` | Non | string | Identifiant Wikidata pour désambiguïsation |

**Obligatoire** si `type` = `point_de_vue` : au moins un acteur doit être identifié.

### 4.5 `mots_cles[]`

Tags libres pour la recherche et le clustering. Tableau de chaînes de caractères.

### 4.6 `version`

Numéro de version du bit. Entier ≥ 1. Par défaut : 1.

---

## 5. Règles de validation

Newsadix applique les contrôles suivants à chaque bit reçu. Un échec entraîne le rejet du bit avec un code d'erreur.

### 5.1 Contrôles structurels (bloquants)

| Règle | Description | Code erreur |
|-------|-------------|:-----------:|
| Schéma JSON | Conformité au schéma `editorial/schema-bit.md` | `E001` |
| Source obligatoire | `sources[]` ne peut pas être vide | `E002` |
| Type cohérent | Un bit `donnee` contient au moins un chiffre. Un bit `point_de_vue` a un acteur attribué | `E003` |
| Longueur contenu | 1 à 2 000 caractères | `E004` |
| ID unique | Pas de doublon d'`id` fournisseur dans les soumissions précédentes du même fournisseur | `E005` |
| Horodatage valide | `horodatage_creation` est un ISO 8601 valide, pas dans le futur | `E006` |
| Pilier valide | Valeur dans l'enum des 12 piliers | `E007` |
| Geo valide | Valeur dans l'enum `france`, `france_monde`, `monde` | `E008` |
| User need valide | `primaire` dans l'enum des 8 besoins | `E009` |
| Validateur requis | Si `auteur.type` = `agent` ou `hybride`, `valide_par` est renseigné | `E010` |
| URL source requise | Chaque source doit avoir une `url`, sauf si `type_source` = `declaration` ou `temoignage` | `E011` |
| Propriété intellectuelle | Le `contenu` du bit est une extraction ou reformulation originale, pas une copie verbatim de la source (voir [§9.3](#93-propriété-intellectuelle)) | `E012` |

### 5.2 Contrôles éditoriaux (non bloquants — signalement)

| Règle | Description | Action |
|-------|-------------|--------|
| Déduplication | Contenu similaire à un bit existant (même `contenu` + `horodatage_evenement`) | Signalement au fournisseur, bit mis en attente |
| Anti-slop | Formulations génériques détectées | Signalement, bit accepté avec flag |
| Langue | Français non conforme (orthographe, grammaire) | Signalement |
| Relations orphelines | Relation pointant vers un bit inexistant | Relation ignorée, bit accepté |

### 5.3 Réponse de validation

Pour chaque bit soumis, Newsadix retourne :

```json
{
  "bit_id_fournisseur": "bit-2026-04-15-001",
  "bit_id_newsadix": "bit-2026-04-15-147",
  "statut": "accepte | rejete | en_attente",
  "erreurs": [],
  "signalements": [],
  "horodatage_reception": "2026-04-15T14:32:12+02:00"
}
```

---

## 6. Taxonomie

Le fournisseur doit utiliser les valeurs canoniques de la taxonomie Newsadix.

### 6.1 Piliers (12 valeurs)

| Valeur enum | Libellé |
|-------------|---------|
| `politique_institutions` | Politique & Institutions |
| `societe_dynamiques_sociales` | Société & Dynamiques sociales |
| `economie_entreprises_travail` | Économie, Entreprises & Travail |
| `technologie_numerique` | Technologie & Numérique |
| `sciences_sante` | Sciences & Santé |
| `environnement_energie` | Environnement & Énergie |
| `monde` | Monde |
| `sport` | Sport |
| `culture_arts_medias` | Culture, Arts & Médias |
| `mode_de_vie` | Mode de vie |
| `idees_pensee_decryptage` | Idées, Pensée & Décryptage |
| `divertissement_contenus_engageants` | Divertissement & Contenus engageants |

### 6.2 Types de source (7 valeurs)

`source_primaire`, `source_secondaire`, `document_officiel`, `donnees_publiques`, `declaration`, `temoignage`, `agence_presse`

### 6.3 User needs (8 valeurs)

`update_me`, `keep_me_engaged`, `help_me`, `connect_me`, `educate_me`, `give_me_perspective`, `divert_me`, `inspire_me`

### 6.4 Types de relation (7 valeurs)

`met_a_jour`, `contextualise`, `contredit`, `illustre`, `meme_sujet`, `meme_acteur`, `consequence`

---

## 7. Cycle de vie

### 7.1 Du côté fournisseur

Le fournisseur soumet des bits en statut `brouillon`. C'est le seul statut autorisé pour une soumission initiale.

```
Fournisseur                          Newsadix
──────────                           ────────
Produit un bit                       
  → statut: brouillon               
  → soumet via API                   Reçoit
                                     Valide (contrôles §5)
                                       → statut: valide
                                     Assemble (templates F1)
                                       → statut: publie
```

### 7.2 Le fournisseur ne contrôle pas la suite

Une fois le bit soumis et accepté :

- Newsadix peut le reclassifier (pilier, geo, user_need)
- Newsadix peut enrichir ses relations via l'agent de plexage
- Newsadix décide s'il est publié, quand, et dans quel assemblage
- Le fournisseur n'a **aucun droit de regard** sur l'assemblage

### 7.3 Notifications

Le fournisseur reçoit une notification quand :

| Événement | Contenu de la notification |
|-----------|--------------------------|
| Bit accepté | ID Newsadix attribué |
| Bit rejeté | Code(s) d'erreur + détail |
| Bit publié | URL de l'assemblage qui l'utilise (si le contrat le prévoit) |
| Demande de correction | Détail de l'anomalie détectée post-publication |

---

## 8. Interface de livraison

### 8.1 Format de soumission

Le fournisseur soumet un **lot** de bits sous forme de tableau JSON :

```json
{
  "fournisseur_id": "fltr-001",
  "horodatage_soumission": "2026-04-15T14:30:00+02:00",
  "bits": [
    { /* bit conforme au schéma */ },
    { /* bit conforme au schéma */ }
  ]
}
```

### 8.2 Modes de livraison

Trois modes sont supportés, du plus simple au plus intégré :

#### Mode A — Dépôt de fichier (batch)

Le fournisseur dépose un fichier JSON dans un emplacement convenu (bucket S3, répertoire partagé, dépôt Git).

- Fréquence : définie par contrat (ex. : toutes les heures, quotidien)
- Adapté aux fournisseurs avec pipeline batch
- Latence : haute (dépend de la fréquence de dépôt)

#### Mode B — API REST (temps réel)

Le fournisseur envoie les bits via une requête HTTP POST.

```
POST /api/fournisseurs/{fournisseur_id}/bits
Content-Type: application/json
Authorization: Bearer {token}

{
  "bits": [ ... ]
}
```

Réponse : tableau de résultats de validation par bit (voir §5.3).

- Adapté aux fournisseurs avec pipeline temps réel
- Latence : basse (réponse synchrone)
- Rate limit : défini par contrat (ex. : 100 bits/heure)

#### Mode C — MCP Server (intégration LLM)

Le fournisseur expose un MCP server que Newsadix interroge, ou Newsadix expose un MCP server que le fournisseur appelle.

- Adapté aux fournisseurs dont le pipeline est piloté par un LLM (Claude Code, etc.)
- Les outils MCP exposent les mêmes opérations que l'API REST
- Spécification MCP détaillée : à produire séparément

### 8.3 Authentification

Chaque fournisseur reçoit :

- Un `fournisseur_id` unique
- Un token d'authentification (Bearer token)
- Un contrat définissant : mode de livraison, fréquence, volume attendu, piliers couverts

---

## 9. Contrat de qualité

### 9.1 Engagements du fournisseur

| Engagement | Description |
|------------|------------|
| **Factualité** | Chaque bit `fait` et `donnee` est vérifiable via la source citée |
| **Sourçage** | Chaque bit a au moins une source identifiable. Les URL sont fonctionnelles au moment de la soumission |
| **Fraîcheur** | L'`horodatage_evenement` reflète la réalité. Un fait de la semaine dernière n'est pas horodaté aujourd'hui |
| **Neutralité** | Les bits `fait`, `donnee` et `contexte` ne contiennent pas de jugement de valeur, de prise de position, ni de recommandation d'action |
| **Attribution** | Les bits `point_de_vue` identifient explicitement l'auteur de la position |
| **Langue** | Français correct, avec accents et diacritiques |
| **Décomposition** | Le fournisseur livre des bits atomiques, pas des articles complets |
| **Originalité** | Le contenu de chaque bit est une extraction ou reformulation originale, jamais une copie du texte source (voir §9.3) |
| **URL source** | Chaque source porte une URL vérifiable permettant au récepteur de remonter à l'origine de l'information |

### 9.2 Engagements de Newsadix

| Engagement | Description |
|------------|------------|
| **Validation rapide** | Réponse de validation dans les 60 secondes (mode API) ou au prochain cycle (mode batch) |
| **Traçabilité** | L'ID fournisseur est conservé dans les métadonnées internes |
| **Non-altération** | Le contenu du bit n'est pas modifié sans notification au fournisseur. La reclassification (pilier, geo) est autorisée |
| **Notification** | Le fournisseur est informé de l'acceptation, du rejet, et de la publication de ses bits |
| **Muraille de Chine** | Les décisions éditoriales (publication, assemblage) sont indépendantes de toute considération commerciale |

### 9.3 Propriété intellectuelle

**Principe fondamental** : un bit est une *extraction d'information*, pas une copie de contenu. Le fournisseur extrait les faits, les données et les citations d'une source, puis les reformule en bits atomiques originaux. Il ne transmet jamais le texte intégral de la source.

#### Ce qui est autorisé

| Élément | Règle |
|---------|-------|
| **Faits** | Librement extractibles. Un fait n'est pas protégé par le droit d'auteur |
| **Données chiffrées** | Librement extractibles avec mention de la source |
| **Citations verbatim** | Autorisées dans les bits `point_de_vue`, à condition d'être attribuées (auteur + fonction) et courtes (< 500 caractères). C'est du droit de citation |
| **URL source** | Obligatoire. Permet au récepteur de vérifier et au lecteur final de remonter à l'original |

#### Ce qui est interdit

| Élément | Règle |
|---------|-------|
| **Texte intégral** | Jamais transmis. Le contenu source complet reste chez le fournisseur |
| **Paraphrase extensive** | Un bit qui reformule la quasi-totalité d'un article de 500 mots en 400 mots n'est pas une extraction — c'est une copie déguisée |
| **Reproduction structurelle** | Reproduire le plan, la progression et les enchaînements d'un article dans une série de bits ordonnés constitue une reproduction de l'œuvre |

#### Test de conformité

Pour chaque bit, le fournisseur peut se poser la question : *"Ce bit rend-il la lecture de la source originale inutile ?"* Si la réponse est oui, le bit est trop proche de la source. Le rôle du bit est de signaler l'existence d'une information et de la rendre vérifiable via l'URL — pas de se substituer à la source.

#### Responsabilité

Le fournisseur est responsable du respect du droit d'auteur sur les contenus qu'il soumet. Newsadix n'est pas en position de vérifier la conformité de chaque bit au droit d'auteur, mais se réserve le droit de rejeter ou retirer tout bit signalé comme contrefaisant.

### 9.4 Taux de rejet

Newsadix surveille le taux de rejet par fournisseur. Un taux supérieur à 20 % sur une période glissante de 7 jours déclenche une revue du contrat et un accompagnement du fournisseur.

Un taux supérieur à 50 % peut entraîner la suspension temporaire du flux.

---

## 10. Identification du fournisseur

### 10.1 Enregistrement

Avant toute soumission, le fournisseur est enregistré auprès de Newsadix avec :

| Champ | Description |
|-------|------------|
| `fournisseur_id` | Identifiant unique attribué par Newsadix |
| `nom` | Nom du fournisseur (personne, organisation, projet) |
| `type` | `journaliste`, `media`, `projet_editorial`, `chercheur`, `institution` |
| `piliers_couverts` | Liste des piliers que le fournisseur prévoit de couvrir |
| `mode_livraison` | A (batch), B (API), C (MCP) |
| `frequence` | Fréquence de livraison prévue |
| `contact` | Adresse de contact pour les notifications |

### 10.2 Métadonnées fournisseur dans les bits

Le champ `auteur.id` de chaque bit doit permettre d'identifier le fournisseur. Convention recommandée :

- Journaliste humain : `prenom-nom` (ex. : `damien-va`)
- Pipeline automatisé : `{fournisseur_id}-{nom_agent}` (ex. : `fltr-001-agent-veille`)
- Hybride : `{fournisseur_id}-{nom_agent}` avec `valide_par` = identifiant humain

---

## 11. Corrections et mises à jour

### 11.1 Correction d'un bit publié

Si le fournisseur détecte une erreur dans un bit déjà soumis et accepté :

1. Soumettre un nouveau bit avec le même `id` + un champ `version` incrémenté + un objet `correction` :

```json
{
  "id": "bit-2026-04-15-001",
  "version": 2,
  "correction": {
    "est_correction": true,
    "detail": "Chiffre corrigé : 7,3 % et non 7,1 %",
    "horodatage": "2026-04-15T16:00:00+02:00"
  },
  "contenu": "Le taux de chômage atteint 7,3 % au T1 2026.",
  /* ... reste des champs obligatoires ... */
}
```

2. Newsadix traite la correction, met à jour le bit en base, et signale la correction dans le flux MCP.

### 11.2 Mise à jour par relation

Pour signaler qu'un fait évolue sans invalider le bit précédent, le fournisseur soumet un nouveau bit avec une relation `met_a_jour` :

```json
{
  "id": "bit-2026-04-16-003",
  "type": "fait",
  "contenu": "Le ministre a précisé que la mesure entrerait en vigueur le 1er juillet, et non le 1er juin.",
  "relations": [
    {
      "type": "met_a_jour",
      "cible": "bit-2026-04-15-001",
      "direction": "sortante"
    }
  ],
  /* ... */
}
```

---

## Annexe A — Référence des valeurs enum

### Types de bit

```
fait | donnee | contexte | point_de_vue
```

### Piliers taxonomiques

```
politique_institutions | societe_dynamiques_sociales | economie_entreprises_travail |
technologie_numerique | sciences_sante | environnement_energie | monde | sport |
culture_arts_medias | mode_de_vie | idees_pensee_decryptage | divertissement_contenus_engageants
```

### Types de source

```
source_primaire | source_secondaire | document_officiel | donnees_publiques |
declaration | temoignage | agence_presse
```

### User needs

```
update_me | keep_me_engaged | help_me | connect_me |
educate_me | give_me_perspective | divert_me | inspire_me
```

### Périmètre géographique

```
france | france_monde | monde
```

### Types de relation

```
met_a_jour | contextualise | contredit | illustre | meme_sujet | meme_acteur | consequence
```

### Statuts

```
brouillon | valide | publie | archive | corrige
```

### Types d'auteur

```
humain | agent | hybride
```

### Types de fournisseur

```
journaliste | media | projet_editorial | chercheur | institution
```

---

## Annexe B — Exemples de soumission

### B.1 — Lot minimal (1 bit fait, fournisseur humain)

```json
{
  "fournisseur_id": "freelance-jdupont",
  "horodatage_soumission": "2026-04-15T10:15:00+02:00",
  "bits": [
    {
      "id": "bit-2026-04-15-001",
      "type": "fait",
      "contenu": "Le Parlement européen a adopté le règlement sur l'intelligence artificielle par 523 voix contre 46.",
      "sources": [
        {
          "nom": "Parlement européen",
          "type_source": "source_primaire",
          "url": "https://www.europarl.europa.eu/news/...",
          "date_acces": "2026-04-15T09:45:00+02:00"
        }
      ],
      "auteur": {
        "type": "humain",
        "id": "jean-dupont"
      },
      "horodatage_creation": "2026-04-15T10:00:00+02:00",
      "horodatage_evenement": "2026-04-15T09:30:00+02:00",
      "geo": "france_monde",
      "pilier": "technologie_numerique",
      "user_need": {
        "primaire": "update_me"
      },
      "statut": "brouillon",
      "acteurs": [
        {
          "nom": "Parlement européen",
          "role": "sujet"
        }
      ]
    }
  ]
}
```

### B.2 — Lot enrichi (3 bits liés, fournisseur automatisé)

```json
{
  "fournisseur_id": "fltr-001",
  "horodatage_soumission": "2026-04-15T14:30:00+02:00",
  "bits": [
    {
      "id": "bit-2026-04-15-010",
      "type": "fait",
      "contenu": "Meta a signé des accords de licence de contenu avec six éditeurs de presse pour alimenter ses modèles d'IA.",
      "sources": [
        {
          "nom": "The Information",
          "type_source": "source_secondaire",
          "url": "https://www.theinformation.com/...",
          "date_acces": "2026-04-15T13:00:00+02:00"
        }
      ],
      "auteur": {
        "type": "hybride",
        "id": "fltr-001-agent-veille",
        "valide_par": "damien-va"
      },
      "horodatage_creation": "2026-04-15T14:00:00+02:00",
      "horodatage_evenement": "2026-04-14T00:00:00+02:00",
      "geo": "monde",
      "pilier": "technologie_numerique",
      "sous_theme": "intelligence_artificielle",
      "user_need": {
        "primaire": "update_me",
        "secondaire": ["give_me_perspective"]
      },
      "statut": "brouillon",
      "acteurs": [
        { "nom": "Meta", "role": "sujet", "wikidata_id": "Q380" }
      ],
      "mots_cles": ["IA", "licence", "presse", "Meta"]
    },
    {
      "id": "bit-2026-04-15-011",
      "type": "donnee",
      "contenu": "L'accord avec News Corp est évalué à 50 millions de dollars par an sur trois ans.",
      "sources": [
        {
          "nom": "The Wall Street Journal",
          "type_source": "source_secondaire",
          "url": "https://www.wsj.com/...",
          "date_acces": "2026-04-15T13:15:00+02:00"
        }
      ],
      "auteur": {
        "type": "hybride",
        "id": "fltr-001-agent-veille",
        "valide_par": "damien-va"
      },
      "horodatage_creation": "2026-04-15T14:05:00+02:00",
      "geo": "monde",
      "pilier": "economie_entreprises_travail",
      "user_need": {
        "primaire": "update_me"
      },
      "statut": "brouillon",
      "relations": [
        {
          "type": "illustre",
          "cible": "bit-2026-04-15-010",
          "direction": "sortante",
          "confiance": 0.9
        }
      ],
      "acteurs": [
        { "nom": "News Corp", "role": "sujet" },
        { "nom": "Meta", "role": "sujet" }
      ]
    },
    {
      "id": "bit-2026-04-15-012",
      "type": "contexte",
      "contenu": "Ces accords interviennent après deux ans de rupture entre Meta et l'industrie de la presse. En 2023, Meta avait supprimé l'onglet Actualités de Facebook et cessé de financer son programme de soutien aux médias.",
      "sources": [
        {
          "nom": "Reuters Institute — Digital News Report 2025",
          "type_source": "source_secondaire",
          "url": "https://reutersinstitute.politics.ox.ac.uk/...",
          "date_acces": "2026-04-15T13:30:00+02:00"
        }
      ],
      "auteur": {
        "type": "hybride",
        "id": "fltr-001-agent-veille",
        "valide_par": "damien-va"
      },
      "horodatage_creation": "2026-04-15T14:10:00+02:00",
      "geo": "monde",
      "pilier": "technologie_numerique",
      "user_need": {
        "primaire": "educate_me"
      },
      "statut": "brouillon",
      "relations": [
        {
          "type": "contextualise",
          "cible": "bit-2026-04-15-010",
          "direction": "sortante",
          "confiance": 1.0
        }
      ]
    }
  ]
}
```

### B.3 — Réponse de validation (lot B.2)

```json
{
  "fournisseur_id": "fltr-001",
  "horodatage_reception": "2026-04-15T14:30:02+02:00",
  "resultats": [
    {
      "bit_id_fournisseur": "bit-2026-04-15-010",
      "bit_id_newsadix": "bit-2026-04-15-147",
      "statut": "accepte",
      "erreurs": [],
      "signalements": []
    },
    {
      "bit_id_fournisseur": "bit-2026-04-15-011",
      "bit_id_newsadix": "bit-2026-04-15-148",
      "statut": "accepte",
      "erreurs": [],
      "signalements": [
        "Le pilier 'economie_entreprises_travail' pourrait être reclassifié en 'technologie_numerique' par cohérence avec le bit parent"
      ]
    },
    {
      "bit_id_fournisseur": "bit-2026-04-15-012",
      "bit_id_newsadix": "bit-2026-04-15-149",
      "statut": "accepte",
      "erreurs": [],
      "signalements": []
    }
  ]
}
```

---

## Historique

| Version | Date | Modification |
|---------|------|-------------|
| 0.1 | 2026-04-15 | Création initiale — premier fournisseur : FLTR |

---

Réf. interne : `editorial/schema-bit.md`, `editorial/taxonomie-editoriale.md`, `editorial/pipeline-production.md`, `editorial/templates/flux-mcp.md`
