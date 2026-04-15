# Template : Dépêche data (Factuelle chiffrée)

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-DEPECHE-DATA` |
| **User Need primaire** | `update_me` |
| **User Need secondaire** | `educate_me` |
| **Longueur** | Court à intermédiaire : 200-500 mots |
| **Signé** | Non |
| **Supervision** | Phase 1 : humaine. Phase 3 : automatique (forte automatisabilité) |

## Déclencheur

La dépêche data est optimisée pour les informations à dominante numérique. C'est le template le plus automatisable de la Famille 1 car les données structurées sont les plus faciles à vérifier et à mettre en forme.

Conditions de déclenchement (**l'une** suffit) :

1. **Publication de données officielles** : un organisme publie des chiffres (INSEE, Eurostat, BCE, ministères, fédérations sportives, etc.)
2. **Seuil de données** : 5+ bits `donnée` sur le même sujet sont disponibles et permettent une comparaison (temporelle, géographique, sectorielle)
3. **Escalade** : une dépêche courte ou développée contient un ratio bits `donnée` / bits `fait` > 50 %
4. **Déclencheur calendaire** : date connue de publication statistique (chômage mensuel, inflation, PIB trimestriel, résultats électoraux)

## Composition en bits

| Bit | Type | Obligatoire | Quantité | Rôle |
|-----|------|-------------|----------|------|
| Donnée principale | `donnée` | Oui | 1 | Le chiffre clé — ouverture |
| Données comparatives | `donnée` | Oui | 2-5 | Comparaison temporelle ou géographique |
| Fait d'interprétation minimale | `fait` | Oui | 1-2 | Ce que le chiffre dit factuellement (hausse, baisse, record) |
| Contexte méthodologique | `contexte` | Oui | 1 | Comment le chiffre est produit, par qui |
| Limites | `contexte` | Non | 0-1 | Ce que le chiffre ne dit pas |

**Total : 5 à 10 bits assemblés. Dominante `donnée`.**

## Structure de sortie

```
BLOC 1 — CHIFFRE PRINCIPAL (1-2 phrases)
  Le chiffre clé, mis en évidence.
  Variation par rapport à la période précédente si pertinent.

BLOC 2 — COMPARAISON (2-4 phrases ou tableau)
  Série temporelle : évolution sur N périodes.
  OU comparaison géographique : même indicateur, plusieurs pays/régions.
  OU ventilation : le chiffre global décomposé par catégorie.
  Présentation en tableau ou liste si > 3 points de comparaison.

BLOC 3 — SOURCE ET MÉTHODOLOGIE (1-2 phrases)
  Qui produit le chiffre, quelle méthode, quelle périodicité.
  Lien vers la source primaire.

BLOC 4 — CE QUE ÇA NE DIT PAS (1-2 phrases, optionnel)
  Limites connues de l'indicateur.
  Biais méthodologiques si documentés.
  Ce champ est ce qui distingue Newsadix d'un simple relais de données.

ATTRIBUTION : Source(s) avec lien direct vers les données brutes
```

### Exemple

```
Le taux de chômage en France s'établit à 7,3 % au premier trimestre 
2026, en hausse de 0,2 point par rapport au T4 2025.

| Période | Taux |
|---------|------|
| T1 2025 | 7,5 % |
| T2 2025 | 7,4 % |
| T3 2025 | 7,2 % |
| T4 2025 | 7,1 % |
| T1 2026 | 7,3 % |

En zone euro, le taux moyen est de 6,5 % (Eurostat, mars 2026). 
L'Allemagne affiche 3,1 %, l'Espagne 11,4 %.

Ces chiffres sont produits par l'INSEE selon la définition du BIT 
(Bureau international du travail), sur la base de l'enquête Emploi. 
Publication trimestrielle, échantillon de 110 000 personnes.

Le taux BIT ne compte pas les personnes en sous-emploi 
(temps partiel subi) ni celles qui ont cessé de chercher un emploi. 
Le « halo du chômage » représente 1,9 million de personnes 
supplémentaires selon l'INSEE.

(Source : INSEE, Enquête Emploi T1 2026 — données brutes : insee.fr)
```

## Règles strictes

1. **Le chiffre parle.** Pas de superlatif (« historique », « record ») sauf si c'est factuellement vrai et sourcé
2. **Comparaison obligatoire.** Un chiffre seul ne dit rien. La comparaison (temporelle, géographique ou catégorielle) est indispensable
3. **Source méthodologique.** Toujours indiquer comment le chiffre est produit
4. **Lien vers données brutes.** Le lecteur doit pouvoir accéder aux données sources
5. **Pas d'extrapolation.** Ne pas prolonger une tendance. Un trimestre de hausse n'est pas une « reprise du chômage »

## Contrôles qualité automatisés

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur | 200-500 mots | Ajustement automatique |
| Donnée principale | Le premier chiffre est identifié et mis en évidence | Restructuration |
| Comparaison | Au moins 2 points de comparaison | Recherche automatique de données complémentaires |
| Source | Lien vers données brutes inclus | Alerte si manquant |
| Méthodologie | Bloc 3 présent | Alerte qualité |
| Cohérence numérique | Les pourcentages et variations sont arithmétiquement corrects | Vérification automatique — blocage si incohérence |
| Fraîcheur | Les données sont les plus récentes disponibles | Vérification auprès de la source |

## Automatisation avancée

La dépêche data est la meilleure candidate pour l'automatisation complète :

| Capacité | Détail |
|----------|--------|
| **Détection de publication** | Monitoring des calendriers statistiques officiels (INSEE, Eurostat, BLS, etc.) |
| **Extraction automatique** | Parsing des communiqués de presse et fichiers de données |
| **Mise en forme** | Génération automatique de tableaux et comparaisons |
| **Enrichissement** | Ajout automatique de données historiques depuis la base de bits |
| **Vérification** | Contrôle arithmétique automatisé (variations, pourcentages) |

## Distribution

| Canal | Format | Délai |
|-------|--------|-------|
| Site web | Texte + tableau interactif + graphique | < 15 min après publication source |
| Réseaux sociaux | Visuel chiffré (1 card avec le chiffre principal + variation) | < 30 min |
| Newsletter | Intégré au digest avec mini-graphique | Au prochain envoi |
| Flux MCP/agence | JSON structuré avec données brutes | Immédiat |

## Escalade

| Condition | Template déclenché |
|-----------|-------------------|
| Les données révèlent un fait politique ou social | `TPL-DEPECHE-COURTE` ou `TPL-DEPECHE-DEVELOPPEE` sur l'angle non-data |
| Les données nourrissent un débat avec PDV existants | `TPL-DEPECHE-ANGLE` |
| Publication de données multiples sur même thème en < 48h | `TPL-DEPECHE-SYNTHESE` |

## Sujets récurrents automatisables

| Sujet | Fréquence | Source |
|-------|-----------|--------|
| Chômage France | Trimestriel | INSEE |
| Inflation zone euro | Mensuel | Eurostat |
| Taux directeur BCE | ~6 semaines | BCE |
| PIB France | Trimestriel | INSEE |
| Résultats électoraux | Ad hoc | Ministère de l'Intérieur |
| Classements sportifs | Hebdo/journalier | Fédérations |
| Indices boursiers | Quotidien (clôture) | Euronext |
| Météo événementielle | Ad hoc | Météo-France |

## Cycle de vie

```
Création → Publication → Correction si erreur données → Archivage
                          (pas de mise à jour : la prochaine publication = nouvelle dépêche data)
```

La dépêche data n'est pas versionnée comme les autres. Chaque nouvelle publication de données produit une nouvelle dépêche. L'historique est dans le réseau de bits (relation `met_a_jour`).

---

Version : 0.1 | Date : 2026-04-14
