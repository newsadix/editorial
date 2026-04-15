# Template : Dépêche courte (Factuelle)

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-DEPECHE-COURTE` |
| **User Need** | `update_me` |
| **Longueur** | Court : 3-6 phrases, 100-200 mots |
| **Signé** | Non |
| **Supervision** | Phase 1 : humaine. Phase 3 : automatique |

## Déclencheur

La dépêche courte est générée quand **l'une** de ces conditions est remplie :

1. **Escalade depuis alerte** : une alerte (`TPL-ALERTE`) a été publiée et du contexte minimal est disponible
2. **Fait confirmé sans urgence** : un bit `fait` est créé, confirmé par 1+ source, mais ne remplit pas les critères de priorité de l'alerte
3. **Accumulation de bits** : 2+ bits `fait` ou `donnée` sur le même sujet sont disponibles sans qu'aucune dépêche n'existe encore

## Composition en bits

| Bit | Type | Obligatoire | Règle |
|-----|------|-------------|-------|
| Fait principal | `fait` | Oui | L'événement central — phrase d'ouverture |
| Fait(s) complémentaire(s) | `fait` | Non | 0 à 2 faits supplémentaires (qui, où, comment) |
| Donnée(s) | `donnée` | Non | 0 à 2 chiffres clés |
| Source(s) | (métadonnée) | Oui | Attribution(s) explicite(s) |

**Total : 2 à 5 bits assemblés. Zéro bit de type `contexte` ou `point_de_vue`.**

## Structure de sortie

La dépêche courte suit la **pyramide inversée stricte** :

```
PHRASE 1 : Quoi (le fait principal)
PHRASE 2 : Qui + Quand/Où
PHRASE 3-4 : Comment / Détails factuels complémentaires
PHRASE 5-6 : Chiffre(s) clé(s) si disponible(s)
ATTRIBUTION : Source(s)
```

### Exemple

```
Le premier ministre a annoncé mardi la dissolution de l'Assemblée nationale. 
La décision a été communiquée à 20h lors d'une allocution télévisée 
depuis l'Élysée.

Les élections législatives anticipées sont fixées aux 22 et 29 juin. 
L'actuelle législature comptait 577 députés élus en juillet 2024.

(Sources : Élysée, Journal officiel)
```

## Règles strictes

1. **Pyramide inversée.** L'information la plus importante en premier, toujours
2. **Zéro analyse.** Pas de « ce qui signifie que », « ce qui pourrait entraîner »
3. **Zéro adjectif qualificatif.** « Important », « historique », « majeur » sont interdits
4. **Zéro adverbe de jugement.** « Seulement », « déjà », « enfin » sont interdits
5. **Faits attribués.** Chaque fait renvoie à sa source
6. **Versionnement visible.** Si mise à jour, le numéro de version est affiché (v1, v2, v3)

## Mise à jour (versionnement)

La dépêche courte est un **document vivant** pendant les premières heures :

| Événement | Action |
|-----------|--------|
| Nouveau bit `fait` avec relation `met_a_jour` | Mise à jour du contenu, incrémentation version |
| Nouveau bit `fait` avec relation `même_sujet` | Ajout si pertinent, incrémentation version |
| Bit existant corrigé | Correction propagée, mention « Corrigé à {heure} » |

Après **24 heures** sans mise à jour, la dépêche courte est gelée.

## Contrôles qualité automatisés

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur | 100-200 mots | Réécriture si hors bornes |
| Pyramide inversée | Fait principal = phrase 1 | Réordonnancement automatique |
| Adjectifs/adverbes | Liste noire de qualificatifs | Suppression automatique |
| Conditionnel | Aucun verbe au conditionnel | Blocage ou reformulation |
| Source | Au moins 1 source identifiée | Blocage publication |
| Doublon | Pas de dépêche courte `même_sujet` < 4h | Fusion ou mise à jour de l'existante |
| Cohérence alerte | Si escalade, le fait principal = fait de l'alerte | Vérification automatique |

## Distribution

| Canal | Format | Délai |
|-------|--------|-------|
| Site web (fil) | Texte complet + métadonnées pilier/geo | < 5 min après déclencheur |
| Réseaux sociaux | Version tronquée (phrase 1-2) + lien | < 10 min |
| Newsletter | Intégré au digest | Au prochain envoi |
| Flux MCP/agence | JSON complet avec bits source | Immédiat |
| Audio (TTS) | Lecture automatique du texte | < 15 min |

## Escalade

La dépêche courte peut déclencher des templates supérieurs :

| Condition | Template déclenché |
|-----------|-------------------|
| 3+ bits `contexte` disponibles sur `même_sujet` | `TPL-DEPECHE-DEVELOPPEE` |
| 5+ bits `donnée` sur `même_sujet` | `TPL-DEPECHE-DATA` |
| 3+ dépêches courtes avec relation `même_sujet` en < 48h | `TPL-DEPECHE-SYNTHESE` |
| 1+ bit `point_de_vue` attribué disponible | Candidat pour `TPL-DEPECHE-ANGLE` (évaluation) |

## Cycle de vie

```
Création → Publication → Mises à jour (v1, v2…) → Gel (24h) → Archivage actif
                                                                (reste navigable dans le réseau de bits)
```

---

Version : 0.1 | Date : 2026-04-14
