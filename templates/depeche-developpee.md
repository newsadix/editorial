# Template : Dépêche développée (Contextualisée)

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-DEPECHE-DEVELOPPEE` |
| **User Need primaire** | `update_me` |
| **User Need secondaire** | `educate_me` |
| **Longueur** | Intermédiaire court : 300-600 mots |
| **Signé** | Non |
| **Supervision** | Phase 1 : humaine. Phase 2 : échantillonnage |

## Déclencheur

La dépêche développée est générée quand **l'une** de ces conditions est remplie :

1. **Escalade depuis dépêche courte** : une dépêche courte existe ET 3+ bits `contexte` sont disponibles avec relation `contextualise` vers les bits de la dépêche
2. **Sujet structurellement riche** : dès la détection, le fait central dispose de suffisamment de contexte dans la base pour justifier un traitement développé (événement récurrent, sujet suivi)
3. **Déclencheur temporel** : un événement programmé (élection, décision de banque centrale, verdict judiciaire) pour lequel des bits de contexte ont été pré-chargés

## Composition en bits

| Bit | Type | Obligatoire | Quantité | Rôle |
|-----|------|-------------|----------|------|
| Fait principal | `fait` | Oui | 1 | Lead — phrase d'ouverture |
| Faits complémentaires | `fait` | Oui | 1-3 | Développement factuel |
| Données | `donnée` | Non | 0-3 | Chiffres clés |
| Contexte | `contexte` | Oui | 2-4 | Le « pourquoi ça compte » |
| Sources | (métadonnée) | Oui | 2+ | Attribution diversifiée |

**Total : 5 à 11 bits assemblés. Zéro bit `point_de_vue`.**

La différence fondamentale avec la dépêche courte : l'introduction de bits `contexte`. C'est la première fois que le template explique, pas seulement constate.

## Structure de sortie

```
BLOC 1 — LEAD FACTUEL (1-2 phrases)
  Le fait principal, pyramide inversée.

BLOC 2 — DÉVELOPPEMENT (2-4 phrases)  
  Faits complémentaires en ordre chronologique ou logique.
  Données chiffrées si disponibles.

BLOC 3 — CONTEXTE (2-4 phrases)
  Pourquoi cette information compte.
  Cadrage historique, comparatif ou thématique.
  Relations utilisées : `contextualise`, `même_sujet` (précédents).

BLOC 4 — PROCHAINES ÉTAPES (1-2 phrases)
  Ce qui est connu sur la suite.
  Uniquement des faits programmés (dates, échéances, procédures).
  Pas de spéculation.

ATTRIBUTION : Sources (multiples)
```

### Exemple

```
La BCE a relevé son taux directeur de 25 points de base, portant le taux 
de dépôt à 4,75 %. La décision, annoncée jeudi à 14h15, était attendue 
par les marchés.

C'est la dixième hausse consécutive depuis juillet 2022. L'inflation 
dans la zone euro s'établit à 2,4 % en mars, contre 2,6 % en février. 
Le taux de chômage reste stable à 6,5 %.

Cette hausse s'inscrit dans un cycle de resserrement monétaire entamé 
il y a deux ans pour contenir l'inflation post-Covid. La BCE avait 
maintenu ses taux inchangés pendant huit ans entre 2016 et 2022. 
L'effet sur les taux de crédit immobilier en France est direct : 
le taux moyen sur 20 ans dépasse 4,2 %.

La prochaine réunion du conseil des gouverneurs est programmée le 
6 juin. La BCE publiera ses nouvelles projections économiques 
à cette occasion.

(Sources : BCE, Eurostat, Banque de France)
```

## Règles strictes

1. **Contexte =/= analyse.** Le bloc contexte situe le fait dans un cadre factuel (historique, comparatif, géographique). Il ne propose pas de grille de lecture ni d'interprétation causale
2. **Prochaines étapes = faits programmés uniquement.** Pas de « il est probable que », « cela pourrait entraîner »
3. **Pas de point de vue.** Même attribué — réservé à la dépêche d'angle
4. **Sources multiples.** Au moins 2 sources distinctes, idéalement de nature différente (institutionnelle + donnée publique, par exemple)
5. **Versionnement.** Mêmes règles que la dépêche courte

## Contrôles qualité automatisés

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur | 300-600 mots | Réécriture si hors bornes |
| Structure 4 blocs | Les 4 blocs sont présents et identifiables | Alerte qualité |
| Bits contexte | Au moins 2 bits `contexte` utilisés | Blocage — pas assez de matière |
| Conditionnel dans bloc 4 | Zéro verbe au conditionnel | Reformulation ou suppression |
| Point de vue détecté | Aucun bit `point_de_vue` dans l'assemblage | Blocage + redirection vers TPL-DEPECHE-ANGLE |
| Sources | 2+ sources distinctes | Alerte si < 2 |
| Cohérence amont | Si escalade, contient les bits de la dépêche courte source | Vérification automatique |

## Distribution

| Canal | Format | Délai |
|-------|--------|-------|
| Site web | Texte complet, 4 blocs distincts visuellement | < 30 min après déclencheur |
| Réseaux sociaux | Thread : 1 post par bloc | < 45 min |
| Newsletter | Version résumée (blocs 1+3) | Au prochain digest |
| Flux MCP/agence | JSON complet avec bits source et relations | Immédiat |
| Audio (TTS) | Lecture automatique intégrale | < 1h |

## Escalade

| Condition | Template déclenché |
|-----------|-------------------|
| 1+ bit `point_de_vue` attribué pertinent | `TPL-DEPECHE-ANGLE` |
| 5+ bits `donnée` structurés (série temporelle, comparatif) | `TPL-DEPECHE-DATA` |
| 3+ dépêches développées `même_sujet` en < 72h | `TPL-DEPECHE-SYNTHESE` |

## Cycle de vie

```
Création → Publication → Mises à jour (48h) → Gel → Archivage actif
                                                     (bits restent navigables)
```

---

Version : 0.1 | Date : 2026-04-14
