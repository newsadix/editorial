# Template : Thread social

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-THREAD-SOCIAL` |
| **User Need** | `update_me` + `educate_me` |
| **Mode d'engagement** | Scroll, Seek |
| **Signé** | Non |
| **Supervision** | Automatique dès le jour 1 (dérivé pur) |

## Principe

Le thread social est une adaptation multi-posts d'une dépêche. Il découpe un contenu structuré en une séquence de posts natifs pour les plateformes qui supportent le format thread (X/Twitter, Threads, Bluesky, LinkedIn). C'est un dérivé — chaque post du thread correspond à un bit ou un bloc du template source.

## Déclencheur

Automatique pour les templates qui ont assez de matière :

| Template source | Thread généré ? | Nombre de posts |
|----------------|----------------|----------------|
| `TPL-ALERTE` | Non — trop court, la carte sociale suffit | — |
| `TPL-DEPECHE-COURTE` | Non — trop court, sauf si 3+ faits | 3-4 posts |
| `TPL-DEPECHE-DEVELOPPEE` | Oui | 4-6 posts |
| `TPL-DEPECHE-ANGLE` | Oui | 5-8 posts |
| `TPL-DEPECHE-SYNTHESE` | Oui (format naturel) | 5-10 posts |
| `TPL-DEPECHE-DATA` | Oui | 3-5 posts + visuels data |

## Structure de sortie

Le thread suit une structure invariable :

```
POST 1 — ACCROCHE (obligatoire)
  Le fait principal en 1-2 phrases.
  Doit fonctionner seul si le lecteur ne lit que celui-là.
  Pas de « thread » ou « 1/ » — la numérotation est implicite.

POST 2-N — DÉVELOPPEMENT (2 à 8 posts)
  1 bit par post, dans l'ordre logique du template source :
  - Dépêche développée : faits → contexte → prochaines étapes
  - Dépêche d'angle : faits → contexte → PDV 1 → PDV 2 → ouverture
  - Dépêche synthèse : chronologie, 1 étape par post
  - Dépêche data : chiffre principal → comparaisons → méthodologie

POST FINAL — FERMETURE (obligatoire)
  Source(s) + lien vers le contenu complet sur le site.
  Pas de CTA agressif. Formulation : « Dépêche complète : [lien] »
```

### Mapping template source → posts

#### Depuis TPL-DEPECHE-DEVELOPPEE

```
Post 1 : Bloc 1 (lead factuel)
Post 2 : Bloc 2 (développement — faits complémentaires)
Post 3 : Bloc 2 suite (données chiffrées si disponibles)
Post 4 : Bloc 3 (contexte)
Post 5 : Bloc 4 (prochaines étapes)
Post 6 : Sources + lien
```

#### Depuis TPL-DEPECHE-ANGLE

```
Post 1 : Bloc 1 (accroche angle)
Post 2 : Bloc 2 (faits sélectionnés)
Post 3 : Bloc 3 (contexte spécifique)
Post 4 : Bloc 4a (PDV 1 — « Selon X, … »)
Post 5 : Bloc 4b (PDV 2 — « Pour Y, … »)
Post 6 : Bloc 5 (ouverture)
Post 7 : Sources + lien
```

#### Depuis TPL-DEPECHE-SYNTHESE

```
Post 1 : Bloc 1 (chapeau de synthèse)
Post 2-N : Bloc 2 (1 post par étape chronologique)
Post N+1 : Bloc 3 (état des lieux)
Post N+2 : Bloc 4 (points ouverts) + sources + lien
```

#### Depuis TPL-DEPECHE-DATA

```
Post 1 : Bloc 1 (chiffre principal) + visuel chiffré
Post 2 : Bloc 2 (comparaison) + tableau ou graphique
Post 3 : Bloc 3 (source et méthodologie)
Post 4 : Bloc 4 (ce que ça ne dit pas) + lien source données brutes
```

## Règles par post

| Règle | Détail |
|-------|--------|
| Longueur max | 280 caractères (X/Twitter), 500 (Threads/Bluesky), 700 (LinkedIn) |
| Autonomie | Chaque post doit être compréhensible isolément |
| Pas de suspense | Ne pas couper une phrase entre deux posts |
| Visuels | 1 visuel max par post (carte sociale ou graphique data) |
| Hashtags | 0-2 par thread, uniquement sur le post 1 ou le post final |
| Mentions | Uniquement si la source est un compte identifié sur la plateforme |

## Adaptations par plateforme

| Plateforme | Longueur/post | Visuels | Ton |
|-----------|--------------|---------|-----|
| X/Twitter | 280 car. | Images, pas de carrousel dans un thread | Factuel, dense |
| Threads | 500 car. | Images possibles | Factuel, légèrement plus développé |
| Bluesky | 300 car. | Images possibles | Identique X |
| LinkedIn | 700 car. | 1 image ou document par post | Plus contextualisé, ton professionnel |

## Contrôles qualité automatisés

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur par post | Respecte la limite de la plateforme | Réécriture automatique |
| Autonomie | Chaque post est une phrase complète | Vérification syntaxique |
| Post 1 autonome | Le post 1 fonctionne comme une carte sociale | Test de complétude |
| Lien final | Le dernier post inclut le lien vers le site | Ajout automatique |
| Nombre de posts | 3-10 posts. Au-delà, le thread perd son audience | Condensation |
| Cohérence source | Tous les bits utilisés proviennent du template source | Vérification |

## Distribution

| Canal | Délai après publication source | Condition |
|-------|-------------------------------|-----------|
| X/Twitter | < 10 min | Si template source >= dépêche développée |
| Threads | < 15 min | Idem |
| Bluesky | < 15 min | Idem |
| LinkedIn | < 30 min | Seulement si pilier pertinent (politique, économie, tech, société) |

## Métriques

| Métrique | Usage |
|----------|-------|
| Taux de lecture du thread complet | Le thread maintient-il l'attention ? |
| Engagement post 1 vs post final | Où décroche-t-on ? |
| Taux de clic sur le lien final | Conversion vers le site |
| Reposts/partages | Viralité du contenu |

---

Version : 0.1 | Date : 2026-04-14
