# Template : Enquête (Investigation)

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-ENQUETE` |
| **User Need primaire** | `educate_me` |
| **User Need secondaire** | `give_me_perspective` |
| **Longueur** | Long : 2000+ mots, potentiellement en série |
| **Signé** | Oui — radar de transparence obligatoire |
| **Supervision** | Validation humaine + relecture juridique si nécessaire |

## Principe

L'enquête est le format le plus exigeant. Il révèle des informations que le public ne connaît pas, appuyées sur des documents, des données et des témoignages. C'est le seul template qui produit des bits `fait` exclusifs — des faits qui n'existaient pas dans la base avant l'enquête.

La rigueur documentaire est maximale : chaque fait renvoie à sa source, chaque document est identifié (C2PA si disponible), chaque témoignage est contextualisé.

## Prérequis

1. **Faits exclusifs.** L'enquête apporte des informations inédites. Sans révélation, c'est un décryptage
2. **Documentation.** Chaque fait exclusif est étayé par un document, une donnée ou un témoignage direct
3. **Auteur expérimenté.** L'enquête engage la responsabilité du média. L'auteur doit avoir l'expertise et la rigueur nécessaires
4. **Validation éditoriale renforcée.** Relecture par un second journaliste, et si nécessaire relecture juridique

## Déclencheur

Jamais automatique. L'enquête est :

- Proposée par un journaliste avec un dossier documenté
- Commandée par la rédaction sur un sujet identifié
- Le résultat d'un travail de fond (semaines ou mois)

## Composition en bits

| Bit | Type | Obligatoire | Quantité | Origine | Rôle |
|-----|------|-------------|----------|---------|------|
| Faits exclusifs (révélations) | `fait` | Oui | 2-10 | **Produit par l'auteur** | Le cœur de l'enquête |
| Documents sources | (métadonnée) | Oui | 1+ | Collecte auteur | Preuves |
| Données exclusives | `donnée` | Non | 0-10 | Analyse auteur | Données inédites ou retraitées |
| Contexte institutionnel | `contexte` | Oui | 2-5 | Base F1 + auteur | Cadre légal, réglementaire, historique |
| Faits publics existants | `fait` | Oui | 2-6 | Base F1 | Ancrage dans l'existant |
| Réactions | `point_de_vue` | Oui | 1-3 | Collecte auteur | Réponse des acteurs mis en cause |

**Spécificité :** c'est le seul template Famille 2 qui **produit des bits `fait`** originaux. Dans tous les autres, les faits viennent de la base F1.

## Structure de sortie

```
BLOC 1 — RÉVÉLATION PRINCIPALE (3-5 phrases)
  Le fait central que l'enquête met au jour.
  Formulé de manière factuelle et sourcée.
  Le lecteur comprend immédiatement ce qui est nouveau.

BLOC 2 — PREUVES DOCUMENTÉES (paragraphes + encadrés)
  Les documents, données et témoignages qui étayent la révélation.
  Chaque preuve est identifiée : nature, source, date, mode d'obtention.
  Si possible : lien vers le document source ou reproduction partielle.
  Encadrés pour les documents clés.

BLOC 3 — CONTEXTE SYSTÉMIQUE (3-6 phrases)
  Le cadre qui donne sa portée à la révélation.
  Cadrage institutionnel, juridique, historique.
  Ce qui est normal vs. ce qui est anormal dans ce qui est révélé.

BLOC 4 — RÉACTIONS (3-6 phrases)
  Les réponses des acteurs mis en cause.
  Toujours sollicitées avant publication (droit de réponse).
  Si pas de réponse : « Contacté par Newsadix, X n'a pas répondu à nos questions. »

BLOC 5 — CE QUI RESTE À DÉCOUVRIR (1-3 phrases)
  Ce que l'enquête n'a pas pu établir.
  Les questions qui restent ouvertes.
  Les pistes pour la suite.

MÉTHODOLOGIE (encadré)
  Comment l'enquête a été menée.
  Période, nombre de sources, type de documents, méthode d'analyse.
  Transparence sur les limites.

SIGNATURE + RADAR
ATTRIBUTION COMPLÈTE
```

## Règles strictes

1. **Droit de réponse.** Les acteurs mis en cause sont systématiquement contactés avant publication. Leur réponse (ou leur silence) est incluse dans l'article
2. **Protection des sources.** Les sources confidentielles sont protégées. Le média assume les conséquences juridiques (charte §4)
3. **Documentation traçable.** Chaque fait exclusif renvoie à un document ou témoignage identifié. Pas de « selon nos informations » sans substance
4. **Méthodologie transparente.** L'encadré méthodologique est obligatoire
5. **Pas de mise en scène.** Les faits sont présentés factuellement. L'écriture narrative (s'il y en a) ne déforme pas la réalité
6. **Relecture renforcée.** Au moins 2 personnes valident avant publication

## Contrôles qualité

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur | 2000+ mots | Alerte si < 2000 |
| Faits exclusifs | Au moins 2 bits `fait` produits par l'auteur (non issus de F1) | Blocage — ce n'est pas une enquête |
| Documents | Au moins 1 document source identifié | Blocage |
| Droit de réponse | Bloc 4 présent avec réponse ou mention de non-réponse | Blocage publication |
| Méthodologie | Encadré méthodologique présent | Blocage |
| Radar | Complet, avec liens d'intérêt déclarés | Blocage |
| Double validation | 2+ validateurs identifiés | Blocage |

## Distribution

| Canal | Format | Délai |
|-------|--------|-------|
| Site web | Long-read avec documents intégrés, encadrés, méthodologie | Dès validation |
| Newsletter | Alerte spéciale « Enquête Newsadix » avec révélation + lien | Publication simultanée |
| Réseaux sociaux | Thread chronologique de la révélation | Publication simultanée |
| Audio | Résumé narré (pas lecture intégrale — trop long) | < 12h |
| Flux MCP | Bits factuels exclusifs uniquement (pas l'appareil narratif) | Après publication site |

**Note : embargo.** L'enquête est publiée simultanément sur tous les canaux. Pas de fuite vers le flux MCP avant la publication sur le site.

## Série d'enquête

Si le sujet le justifie, l'enquête peut être publiée en **série** :

- Épisode 1 : révélation principale
- Épisode 2 : contexte systémique approfondi
- Épisode 3 : réactions et conséquences
- Chaque épisode est un assemblage autonome (lisible seul) mais relié aux autres (relation `même_sujet`)

## Cycle de vie

```
Investigation (semaines/mois) → Rédaction → Relecture croisée → Relecture juridique (si nécessaire) 
→ Validation rédacteur en chef → Publication simultanée tous canaux → Suivi des réactions → Archivage actif
```

---

Version : 0.1 | Date : 2026-04-14
