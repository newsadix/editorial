# Template : Alerte (Flash)

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-ALERTE` |
| **User Need** | `update_me` |
| **Longueur** | Ultra-court : 1-3 phrases, < 280 caractères utiles |
| **Signé** | Non |
| **Supervision** | Phase 1 : humaine. Phase 3 : automatique |

## Déclencheur

L'alerte est générée quand **toutes** ces conditions sont réunies :

1. Un bit de type `fait` est créé par un agent de veille
2. Le fait est **nouveau** (pas de bit `même_sujet` avec horodatage < 2h dans la base)
3. Au moins **1 source primaire** confirme le fait (agence, source officielle, document public)
4. Le fait concerne un des 12 piliers de la taxonomie

### Critères de priorité (au moins 1)

- Décision politique majeure (gouvernement, justice constitutionnelle, institution)
- Événement de sécurité (attentat, catastrophe, accident majeur)
- Donnée économique clé (taux directeur, chômage, PIB)
- Résultat électoral
- Décès ou événement concernant une figure publique de premier plan
- Événement sportif majeur (résultat, record, décision disciplinaire)

Si aucun critère de priorité n'est rempli, le bit alimente directement le template `depeche-courte` sans passer par l'alerte.

## Composition en bits

| Bit | Type | Obligatoire | Règle |
|-----|------|-------------|-------|
| Bit principal | `fait` | Oui | Le fait central, 1 phrase |
| Bit horodatage | `donnée` | Oui | Date/heure précise de l'événement |
| Bit source | (métadonnée) | Oui | Attribution explicite de la source |

**Total : 1 à 2 bits assemblés.**

## Structure de sortie

```
[ALERTE] {fait principal en une phrase}. {horodatage si pertinent}. (Source : {source})
```

### Exemples

```
[ALERTE] Le Conseil constitutionnel invalide l'article 12 de la loi immigration. 
Décision publiée à 14h32. (Source : Conseil constitutionnel)
```

```
[ALERTE] Séisme de magnitude 6.2 au large de Nice, ressenti sur la Côte d'Azur. 
(Source : CSEM)
```

```
[ALERTE] La BCE relève son taux directeur de 25 points de base à 4,75 %. 
(Source : BCE)
```

## Règles strictes

1. **Zéro interprétation.** Aucun adjectif qualificatif, aucun adverbe de jugement
2. **Zéro contexte.** Le contexte viendra dans la dépêche courte qui suivra
3. **Zéro conditionnel.** Ne pas publier d'alerte sur un fait non confirmé
4. **Source identifiée.** Toujours entre parenthèses en fin d'alerte
5. **Pas de point de vue.** Même attribué — réservé aux templates supérieurs

## Contrôles qualité automatisés

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur | < 280 caractères (hors mention source) | Réécriture automatique |
| Adjectifs | Aucun adjectif qualificatif détecté | Suppression + alerte humaine |
| Conditionnel | Aucun verbe au conditionnel | Blocage publication |
| Source | Champ `sources[]` non vide | Blocage publication |
| Doublon | Pas de bit `même_sujet` < 2h | Blocage + fusion avec existant |
| Factualité | Vérification croisée si 2+ sources disponibles | Enrichissement automatique |

## Distribution

| Canal | Format | Délai |
|-------|--------|-------|
| Push notification (app) | Texte brut, < 100 caractères | Immédiat |
| Site web (fil) | Texte complet + badge ALERTE | < 1 min |
| Réseaux sociaux | Texte + visuel minimal (couleur pilier) | < 3 min |
| Newsletter | Intégré au prochain digest | Au prochain envoi |
| Flux MCP/agence | JSON brut | Immédiat |

## Escalade

L'alerte déclenche **automatiquement** la création d'une dépêche courte (`TPL-DEPECHE-COURTE`) :

- **Immédiatement** si des bits de contexte existent déjà dans la base (relation `contextualise`)
- **Sous 15 minutes** dans tous les cas : l'agent de veille cherche activement du contexte complémentaire

## Cycle de vie

```
Création → Publication → Lien vers dépêche courte (dès disponible) → Archivage
```

L'alerte n'est jamais modifiée après publication. Si le fait évolue, c'est un nouveau bit avec relation `met_a_jour`, et c'est la dépêche courte qui intègre la mise à jour.

---

Version : 0.1 | Date : 2026-04-14
