# Template : Dépêche de synthèse (Round-up)

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-DEPECHE-SYNTHESE` |
| **User Need primaire** | `update_me` |
| **User Need secondaire** | `educate_me` |
| **Longueur** | Intermédiaire : 400-800 mots |
| **Signé** | Non |
| **Supervision** | Phase 1 : humaine. Phase 3 : automatique |

## Déclencheur

La synthèse agrège des dépêches existantes sur un même sujet ou acteur. C'est un template de **consolidation**, pas de production primaire.

Conditions de déclenchement (**l'une** suffit) :

1. **Seuil d'accumulation** : 3+ dépêches (courtes ou développées) avec relation `même_sujet` en < 72h
2. **Seuil acteur** : 3+ dépêches avec relation `même_acteur` en < 7 jours
3. **Déclencheur calendaire** : fin de journée, fin de semaine ou fin d'événement multi-jours (sommet, procès, compétition)
4. **Déclencheur éditorial** : un sujet suivi atteint un point de bascule (vote final, verdict, résultat)

## Composition en bits

| Bit | Type | Obligatoire | Quantité | Rôle |
|-----|------|-------------|----------|------|
| Chapeau de synthèse | (généré) | Oui | 1 | Vue d'ensemble en 2-3 phrases |
| Faits chronologiques | `fait` | Oui | 3-8 | Les faits clés, ordonnés |
| Données cumulatives | `donnée` | Non | 0-4 | Chiffres de bilan |
| Contexte de cadrage | `contexte` | Oui | 1-2 | Rappel du cadre pour lecteur qui découvre |
| Points ouverts | `fait` ou `contexte` | Oui | 1-2 | Ce qui reste en suspens |

**Total : 6 à 15 bits assemblés. Les bits proviennent des dépêches existantes — la synthèse ne produit pas de bits originaux (sauf le chapeau).**

## Structure de sortie

```
BLOC 1 — CHAPEAU DE SYNTHÈSE (2-3 phrases)
  Résumé de l'ensemble du sujet en un coup d'oeil.
  Répond à : « Que s'est-il passé au total ? »
  Inclut la période couverte.

BLOC 2 — CHRONOLOGIE DES FAITS (paragraphes courts ou liste)
  Les faits clés dans l'ordre chronologique.
  Chaque fait = 1-2 phrases, avec date/heure.
  Relation utilisée : `même_sujet`, `conséquence`, `met_a_jour`.

BLOC 3 — ÉTAT DES LIEUX (2-3 phrases)
  Où en est-on maintenant ?
  Données cumulatives si disponibles (bilan chiffré).
  
BLOC 4 — POINTS OUVERTS (1-3 phrases)
  Ce qui n'est pas résolu.
  Prochaines échéances connues.
  Questions factuelles sans réponse.

ATTRIBUTION : Sources (agrégation des sources des dépêches)
```

### Exemple

```
L'ouragan Milton a touché la Floride mercredi soir et traversé l'État 
en 18 heures. Bilan provisoire : 16 morts, 3 millions de foyers 
privés d'électricité, dégâts estimés entre 50 et 80 milliards de dollars.

Chronologie :
- Lundi 7 oct. : Milton classé catégorie 5 dans le golfe du Mexique. 
  Ordre d'évacuation pour 5,9 millions de personnes.
- Mercredi 9 oct., 20h30 : atterrissage à Siesta Key en catégorie 3. 
  Vents mesurés à 205 km/h.
- Jeudi 10 oct. : traversée de l'État. Inondations majeures à Tampa, 
  Orlando et le long de la St. Johns River.
- Vendredi 11 oct. : Milton rétrogradé en tempête tropicale 
  en sortant dans l'Atlantique.

À ce stade, 16 décès sont confirmés par les autorités de Floride. 
La FEMA a déployé 1 200 agents. Le réseau électrique reste coupé 
pour 1,8 million de foyers. Les assureurs estiment les dégâts 
assurés entre 30 et 50 milliards de dollars.

Le gouverneur DeSantis a demandé une déclaration fédérale de catastrophe 
majeure, en attente de signature. Les opérations de recherche se 
poursuivent dans les zones inondées de Tampa.

(Sources : NHC, FEMA, État de Floride, Reuters, AP)
```

## Règles strictes

1. **Pas de production originale.** La synthèse assemble des bits existants. Le seul contenu « neuf » est le chapeau
2. **Chronologie factuelle.** Pas d'interprétation de la séquence d'événements
3. **Traçabilité.** Chaque fait de la chronologie renvoie au bit source (et donc à la dépêche d'origine)
4. **Pas de doublon informationnel.** Si un fait a été mis à jour (relation `met_a_jour`), seule la version la plus récente apparaît
5. **Zéro point de vue.** Même règle que la dépêche développée

## Contrôles qualité automatisés

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur | 400-800 mots | Ajustement automatique |
| Bits sources | Chaque fait renvoie à un bit existant | Alerte si bit orphelin |
| Doublons | Pas de fait répété (vérification `met_a_jour`) | Déduplication automatique |
| Chronologie | Ordre chronologique respecté | Réordonnancement |
| Fraîcheur | Tous les bits utilisés datent de < 7 jours | Alerte si bit ancien |
| Complétude | Toutes les dépêches `même_sujet` de la période sont représentées | Alerte si dépêche manquante |

## Distribution

| Canal | Format | Délai |
|-------|--------|-------|
| Site web | Texte complet avec frise chronologique interactive | < 2h après déclencheur |
| Réseaux sociaux | Thread chronologique (1 post par étape clé) | < 3h |
| Newsletter | Format digest avec chapeau + lien vers chronologie | Au prochain envoi |
| Flux MCP/agence | JSON avec graph complet des bits et relations | Immédiat |
| Audio (TTS) | Lecture chapeau + état des lieux | < 3h |

## Déclencheurs récurrents

Certaines synthèses sont **programmables** :

| Type | Fréquence | Déclencheur |
|------|-----------|-------------|
| Synthèse du jour | Quotidienne, fin de journée | 19h — top 5-8 sujets du jour |
| Synthèse hebdo | Hebdomadaire | Dimanche — sujets de la semaine |
| Synthèse événement | À la fin d'un événement multi-jours | Clôture détectée (résultat final, fin de sommet) |
| Synthèse suivi | Quand un sujet suivi atteint un jalon | Seuil de bits ou événement déclencheur |

## Cycle de vie

```
Création → Publication → Enrichissement (si sujet continue) → Gel → Archivage
```

La synthèse peut être enrichie tant que le sujet est actif. Une fois le sujet clos (ou après 7 jours sans nouveau bit), elle est gelée.

---

Version : 0.1 | Date : 2026-04-14
