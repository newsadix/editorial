# Template : Carte sociale (Social Card)

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-CARTE-SOCIALE` |
| **User Need** | `update_me` |
| **Mode d'engagement** | Scroll |
| **Durée d'attention** | < 2 secondes pour accrocher |
| **Signé** | Non |
| **Supervision** | Automatique dès le jour 1 (dérivé pur) |

## Principe

La carte sociale est le format de distribution le plus élémentaire. Elle traduit **un seul bit** (ou un assemblage minimal de 2-3 bits) en un visuel natif pour les plateformes sociales. C'est un dérivé automatique — aucune production éditoriale originale.

## Déclencheur

Automatique : **toute publication d'un template Famille 1** génère au moins une carte sociale.

| Template source | Cartes générées |
|----------------|----------------|
| `TPL-ALERTE` | 1 carte (le fait) |
| `TPL-DEPECHE-COURTE` | 1 carte (fait principal + 1 donnée si disponible) |
| `TPL-DEPECHE-DEVELOPPEE` | 1-2 cartes (fait principal ; chiffre clé si pertinent) |
| `TPL-DEPECHE-ANGLE` | 1-2 cartes (accroche angle ; PDV opposés en diptyque) |
| `TPL-DEPECHE-SYNTHESE` | 1 carte chapeau + 1 carrousel chronologie |
| `TPL-DEPECHE-DATA` | 1 carte chiffre principal + 1 carte graphique |

## Composition en bits

| Bit | Type | Obligatoire | Règle |
|-----|------|-------------|-------|
| Bit principal | `fait` ou `donnée` | Oui | 1 phrase, < 120 caractères |
| Bit secondaire | `donnée` ou `fait` | Non | 1 phrase complémentaire, si pertinent |
| Source | (métadonnée) | Oui | Nom de la source, pas d'URL |

**Total : 1-2 bits par carte. Maximum 3 pour un carrousel.**

## Formats de sortie par plateforme

### Carte simple (image statique)

```
┌─────────────────────────────┐
│  [PILIER] en couleur pilier │
│                             │
│  FAIT PRINCIPAL             │
│  en gros, 2-3 lignes max   │
│                             │
│  Donnée clé (si dispo)     │
│  en plus petit              │
│                             │
│  Source · newsadix.com      │
│  [logo Newsadix]            │
└─────────────────────────────┘
```

**Règles visuelles :**
- Fond : couleur associée au pilier taxonomique (palette à définir par Skan)
- Texte : blanc ou noir selon contraste
- Typographie : la même partout — identité reconnaissable en < 1 seconde
- Pas de photo — le texte est le contenu (sauf dépêche data : graphique possible)

### Carrousel (multi-cartes)

Pour les dépêches de synthèse et les dépêches data :

```
CARTE 1 : Chapeau / Chiffre principal (accroche)
CARTE 2-N : Un fait ou une donnée par carte
CARTE FINALE : Source(s) + CTA (lien vers le site)
```

**Maximum : 6 cartes par carrousel.** Au-delà, on perd l'attention.

### Adaptations par plateforme

| Plateforme | Format | Ratio | Spécificité |
|-----------|--------|-------|-------------|
| Instagram (feed) | Image carrée | 1:1 (1080x1080) | Texte lisible sans zoom |
| Instagram (stories) | Image verticale | 9:16 (1080x1920) | Swipe up vers site |
| TikTok | Image ou vidéo courte | 9:16 | Texte animé si vidéo |
| X/Twitter | Image horizontale | 16:9 (1200x675) | Texte + lien dans le post |
| Threads | Image carrée | 1:1 | Similaire Instagram |
| LinkedIn | Image horizontale | 1.91:1 (1200x628) | Ton plus institutionnel |

## Règles strictes

1. **Un message par carte.** Pas de paragraphe. Une phrase, un chiffre, un fait
2. **Lisible en 2 secondes.** Si le texte dépasse 3 lignes (taille affichée), c'est trop long
3. **Identité visuelle constante.** Même template graphique partout — la reconnaissance de marque se construit par la répétition
4. **Pas de clickbait.** Le fait est complet sur la carte. Le lien vers le site offre plus de profondeur, pas la réponse à une question laissée en suspens
5. **Source toujours visible.** Même réduite à un nom, jamais absente
6. **Pas d'opinion.** Même dans le choix des mots — la carte est factuelle par construction

## Contrôles qualité automatisés

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur texte | < 120 caractères (texte principal) | Réécriture automatique |
| Lisibilité | Contraste texte/fond >= 4.5:1 (WCAG AA) | Ajustement couleur |
| Pilier | Couleur correspond au pilier du bit source | Correction automatique |
| Source | Présente sur chaque carte | Ajout automatique |
| Ratio image | Correct pour la plateforme cible | Recadrage automatique |
| Doublon | Pas de carte identique publiée < 4h | Blocage |

## Distribution

| Canal | Délai après publication source | Fréquence max |
|-------|-------------------------------|---------------|
| Instagram (feed) | < 10 min | 6 cartes/jour |
| Instagram (stories) | < 5 min | Illimité |
| TikTok | < 15 min | 4/jour |
| X/Twitter | < 5 min | 10/jour |
| Threads | < 10 min | 6/jour |
| LinkedIn | < 30 min | 2/jour |

**Règle de fréquence :** ne pas saturer un canal. Les limites ci-dessus sont des plafonds, pas des objectifs. La pertinence prime sur le volume.

## Lien avec le template source

Chaque carte inclut un lien (ou CTA) vers le contenu source complet sur le site Newsadix. La carte est un point d'entrée dans le réseau de bits, pas une fin en soi.

```
Carte sociale → Dépêche sur le site → Bits dépliables → Réseau de bits
```

## Métriques de performance

| Métrique | Usage |
|----------|-------|
| Impressions | Volume de diffusion |
| Taux d'engagement (likes, partages, commentaires) | Résonance du sujet |
| Taux de clic vers le site | Efficacité du CTA |
| Temps moyen de visionnage (vidéo/stories) | Accroche réussie ou non |

Les métriques alimentent la boucle analytics du pipeline (cf. `editorial/pipeline-production.md`).

---

Version : 0.1 | Date : 2026-04-14
