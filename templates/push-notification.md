# Template : Push notification

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-PUSH` |
| **User Need** | `update_me` |
| **Mode d'engagement** | Subscribe |
| **Longueur** | Ultra-court : < 100 caractères |
| **Signé** | Non |
| **Supervision** | Automatique dès le jour 1 |

## Principe

La push notification est le format le plus contraint et le plus invasif. Elle interrompt l'utilisateur. Chaque push doit le mériter. C'est un dérivé direct de l'alerte, avec des règles de fréquence strictes pour ne pas saturer.

## Déclencheur

La push est réservée aux événements de haute priorité :

| Condition | Push ? |
|-----------|--------|
| `TPL-ALERTE` publiée avec critère de priorité rempli | Oui |
| `TPL-ALERTE` publiée sans critère de priorité | Non |
| `TPL-DEPECHE-DATA` sur indicateur économique majeur | Oui (si variation significative) |
| Autres templates | Non — jamais de push pour une dépêche courte ou développée |

### Seuil de fréquence

| Règle | Limite |
|-------|--------|
| Maximum par jour | 5 push |
| Délai minimum entre 2 push | 30 minutes |
| Maximum par heure | 2 push |
| Plage horaire | 7h00-23h00 (heure locale utilisateur) |

Si le seuil est atteint, les alertes suivantes sont empilées et envoyées dans le prochain créneau disponible ou absorbées par la newsletter flash.

## Composition

```
[PILIER] Fait principal en < 100 caractères.
```

C'est tout. La push est un pointeur vers l'alerte ou la dépêche.

### Exemples

```
[Politique] Le Conseil constitutionnel invalide l'article 12 de la loi immigration.
```

```
[Économie] BCE : taux directeur relevé à 4,75 % (+25 pb).
```

```
[Monde] Séisme de magnitude 6.2 au large de Nice, ressenti sur la Côte d'Azur.
```

## Hiérarchie de destination

Quand l'utilisateur tape sur la push, il arrive sur :

1. **L'alerte** si elle vient d'être publiée et qu'aucune dépêche n'existe encore
2. **La dépêche courte** si elle est déjà disponible
3. **La dépêche développée** si elle existe

La destination est dynamique : elle pointe toujours vers le contenu le plus complet disponible au moment du clic.

## Contrôles qualité automatisés

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur | < 100 caractères | Réécriture automatique |
| Fréquence | Respect des seuils quotidiens/horaires | Mise en file d'attente |
| Plage horaire | 7h-23h | Report au lendemain 7h |
| Pertinence | Critère de priorité de l'alerte rempli | Blocage si non-prioritaire |
| Destination | Le lien pointe vers un contenu existant | Vérification avant envoi |
| Doublon | Pas de push identique en < 4h | Blocage |

## Distribution

| Canal | Format | Délai |
|-------|--------|-------|
| App (si existante) | Notification native iOS/Android | Immédiat |
| Navigateur web | Web Push API | Immédiat |

## Ce que la push n'est pas

- **Pas un teaser.** Le fait est complet dans la notification. Pas de « Découvrez ce qui s'est passé »
- **Pas un outil de rétention.** On n'envoie pas de push pour « ramener » les utilisateurs sur l'app
- **Pas un canal de promotion.** Jamais de push pour un contenu sponsorisé ou une fonctionnalité

---

Version : 0.1 | Date : 2026-04-14
