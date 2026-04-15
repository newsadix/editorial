# Template : Newsletter digest

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-NEWSLETTER-DIGEST` |
| **User Need** | `update_me` |
| **Mode d'engagement** | Subscribe |
| **Signé** | Non (sauf édito d'ouverture si ajouté en Famille 2) |
| **Supervision** | Phase 1 : relecture humaine. Phase 3 : automatique |

## Principe

La newsletter digest est une compilation automatique des bits et dépêches publiés sur une période donnée. Elle sert le mode Subscribe : le lecteur reçoit l'essentiel sans aller chercher. C'est un assemblage de contenus existants, pas une production originale.

## Déclencheur

Déclenchement calendaire (programmable) :

| Variante | Fréquence | Heure d'envoi | Contenu |
|----------|-----------|---------------|---------|
| **Matinale** | Quotidienne | 7h00 | Top 5-8 sujets des dernières 24h |
| **Flash midi** | Quotidienne | 12h30 | Nouveautés depuis la matinale |
| **Hebdo** | Dimanche | 10h00 | Synthèse de la semaine |
| **Thématique** | Variable | Variable | 1 pilier taxonomique, déclenchée quand N bits seuil atteint |

La matinale est le format prioritaire au lancement.

## Composition

### Newsletter matinale

```
BLOC 0 — EN-TÊTE
  Date · Nombre d'articles · Temps de lecture estimé

BLOC 1 — L'ESSENTIEL (obligatoire)
  3-5 items, classés par importance éditoriale.
  Chaque item = 1-3 phrases dérivées du template source.
  Lien vers la dépêche complète.

  Format par item :
  ┌──────────────────────────────────────┐
  │ [PILIER]                             │
  │ TITRE (= fait principal du bit)     │
  │ 1-2 phrases de contexte minimal     │
  │ → Lire la dépêche                    │
  └──────────────────────────────────────┘

BLOC 2 — EN CHIFFRES (optionnel, si dépêches data disponibles)
  2-3 données clés avec source.
  Format : le chiffre en gros + 1 phrase d'explication.

BLOC 3 — À SUIVRE (optionnel)
  1-3 sujets dont les prochaines étapes sont connues.
  Dérivé des blocs « prochaines étapes » des dépêches développées.

BLOC 4 — PIED
  Lien vers le site · Lien de désabonnement · Mention légale
```

### Newsletter hebdo

Même structure que la matinale, avec :
- Bloc 1 élargi à 8-12 items
- Ajout d'un **bloc synthèse** : les 2-3 sujets les plus couverts de la semaine (dérivé de `TPL-DEPECHE-SYNTHESE` si existantes)
- Bloc « En chiffres » plus étoffé

### Newsletter thématique

Mono-pilier. Déclenchée quand un pilier accumule 5+ dépêches en < 7 jours.
- Même structure, tous les items du même pilier
- Titre = nom du pilier

## Règles de sélection des items

L'algorithme de sélection classe les dépêches candidates selon :

| Critère | Poids | Détail |
|---------|-------|--------|
| Fraîcheur | Élevé | Dépêches les plus récentes d'abord |
| Niveau de template | Moyen | Développée > courte > alerte (plus de matière = meilleur résumé) |
| Diversité de piliers | Élevé | Pas plus de 2 items du même pilier dans le top 5 |
| Engagement (si données disponibles) | Faible au début | Pondéré par les métriques site/social |
| Couverture géographique | Moyen | Au moins 1 item international dans le top 5 |

## Règles strictes

1. **Pas de réécriture.** Les phrases de la newsletter sont extraites ou condensées depuis les bits et dépêches. Pas de formulation originale
2. **Chaque item renvoie à sa source.** Le lien « Lire la dépêche » est obligatoire
3. **Pas de hiérarchisation opinionnée.** L'ordre est factuel (importance, fraîcheur), pas éditorial
4. **Temps de lecture affiché.** Le lecteur sait en ouvrant combien de temps il lui faut
5. **Désabonnement en 1 clic.** Obligation légale et engagement de transparence

## Contrôles qualité automatisés

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Nombre d'items | 3-8 (matinale), 8-12 (hebdo) | Alerte si < 3, sélection si > plafond |
| Diversité piliers | Max 2 items/pilier dans le top 5 | Rééquilibrage automatique |
| Longueur totale | < 800 mots (matinale), < 1500 mots (hebdo) | Condensation |
| Liens | Chaque item a un lien fonctionnel | Vérification automatique |
| Doublon | Pas d'item identique à la newsletter précédente | Exclusion automatique |
| Heure d'envoi | Envoi à l'heure programmée ± 5 min | Alerte si retard |

## Distribution

| Variante | Canal | Format |
|----------|-------|--------|
| Matinale | Email (Brevo, Mailchimp ou équivalent) | HTML responsive |
| Flash midi | Email | HTML responsive (version courte) |
| Hebdo | Email | HTML responsive |
| Thématique | Email | HTML responsive |

### Abonnement

- Inscription sur le site (email uniquement, pas de compte)
- Choix des variantes à la souscription (matinale, hebdo, thématiques par pilier)
- Modification des préférences à tout moment

## Métriques

| Métrique | Usage |
|----------|-------|
| Taux d'ouverture | Pertinence du sujet + heure d'envoi |
| Taux de clic | Qualité des résumés + intérêt des sujets |
| Taux de désabonnement | Satisfaction globale |
| Items les plus cliqués | Feedback pour la sélection future |

---

Version : 0.1 | Date : 2026-04-14
