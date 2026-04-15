# Template : Dépêche d'angle

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-DEPECHE-ANGLE` |
| **User Need primaire** | `give_me_perspective` |
| **User Need secondaire** | `educate_me` |
| **Longueur** | Intermédiaire : 500-1000 mots |
| **Signé** | Non (mais les points de vue sont attribués à leurs auteurs) |
| **Supervision** | Phase 1 : humaine systématique. Phase 2 : humaine allégée. Phase 3 : semi-automatique |

## Déclencheur

La dépêche d'angle est le template le plus délicat de la Famille 1. C'est le premier à intégrer des bits `point_de_vue`. Son automatisation complète sera la dernière à être validée.

Conditions de déclenchement (**toutes** réunies) :

1. Une dépêche courte ou développée existe sur le sujet
2. Au moins **2 bits `point_de_vue`** attribués sont disponibles avec relation vers les bits du sujet
3. Les points de vue sont **contradictoires ou complémentaires** (pas redondants — vérifié par l'agent de plexage via relation `contredit` ou absence de relation `même_sujet` entre PDV)
4. Suffisamment de bits `fait` et `contexte` pour ancrer les PDV dans le factuel

## Composition en bits

| Bit | Type | Obligatoire | Quantité | Rôle |
|-----|------|-------------|----------|------|
| Fait principal | `fait` | Oui | 1 | Ancrage factuel — phrase d'accroche |
| Faits sélectionnés | `fait` | Oui | 2-4 | Faits choisis selon l'angle |
| Contexte spécifique | `contexte` | Oui | 2-3 | Cadrage qui éclaire l'angle |
| Points de vue | `point_de_vue` | Oui | 2-4 | Positions divergentes, toujours attribuées |
| Données comparatives | `donnée` | Non | 0-3 | Chiffres qui étayent ou nuancent les PDV |

**Total : 7 à 15 bits assemblés.**

C'est le premier template où des bits `point_de_vue` apparaissent. Règle absolue : chaque PDV est explicitement attribué à son auteur, jamais intégré dans le corps narratif comme s'il était factuel.

## Structure de sortie

```
BLOC 1 — ACCROCHE ANGLE (1-2 phrases)
  Entrée par l'angle, pas par le fait brut.
  Reformulation du fait sous l'éclairage choisi.

BLOC 2 — FAITS SÉLECTIONNÉS (3-5 phrases)
  Les faits pertinents pour cet angle spécifique.
  Pas tous les faits — seulement ceux qui servent le cadrage.

BLOC 3 — CONTEXTE SPÉCIFIQUE (2-4 phrases)
  Le cadre qui donne sens à l'angle.
  Historique, comparaison, tendance — orienté par l'angle.

BLOC 4 — POINTS DE VUE (4-8 phrases)
  Présentation des positions divergentes.
  Chaque PDV explicitement attribué : « Selon X, … », « Pour Y, … »
  Au moins 2 PDV, idéalement contradictoires.
  Pas de hiérarchisation entre PDV (pas de « mais » qui invalide l'un au profit de l'autre).

BLOC 5 — OUVERTURE (1-2 phrases)
  Ce qui reste incertain ou à venir.
  Question ouverte ou prochaine échéance factuelle.

ATTRIBUTION : Sources (multiples, incluant les sources des PDV)
```

### Exemple

```
La hausse du taux directeur de la BCE divise économistes et politiques 
sur la capacité de la zone euro à absorber un resserrement prolongé.

La dixième hausse consécutive porte le taux de dépôt à 4,75 %. 
L'inflation recule (2,4 % en mars contre 2,6 % en février) mais reste 
au-dessus de la cible de 2 %. Parallèlement, la croissance du PIB 
de la zone euro a ralenti à 0,2 % au T1 2026.

Le cycle actuel est le plus long de l'histoire de la BCE. Entre 2016 
et 2022, le taux directeur était resté à zéro. La vitesse du 
resserrement est sans précédent dans la zone euro.

Pour l'économiste Agnès Bénassy-Quéré, « la BCE n'a pas d'autre choix 
que de maintenir le cap tant que l'inflation sous-jacente reste 
au-dessus de 2,5 % ». Le ministre de l'Économie Bruno Le Maire 
estime à l'inverse que « l'Europe risque de sacrifier sa croissance 
sur l'autel de l'orthodoxie monétaire ». L'économiste en chef de 
Natixis, Patrick Artus, pointe un risque spécifique : « L'écart 
se creuse entre les pays du Nord, qui absorbent la hausse, et ceux 
du Sud, où l'immobilier et la dette publique amplifient le choc. »

La BCE publiera ses nouvelles projections le 6 juin. La question 
d'une pause dans le cycle de hausse sera au centre des débats.

(Sources : BCE, Eurostat, Le Monde, Les Échos, BFM Business)
```

## Règles strictes

1. **PDV toujours attribués.** Jamais de « certains estiment que » ou « les observateurs notent ». Nom + fonction + citation ou paraphrase attribuée
2. **Pas de PDV du rédacteur.** Le texte hors citations est factuel. L'angle est un cadrage, pas une opinion
3. **Équilibre des PDV.** Au moins 2 positions distinctes. Pas de PDV unique présenté comme consensuel
4. **L'angle est explicite.** Le lecteur comprend dès la première phrase quel éclairage est proposé
5. **Les faits restent vérifiables.** Tout fait cité dans la dépêche d'angle doit exister comme bit `fait` ou `donnée` dans la base

## Contrôles qualité automatisés

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur | 500-1000 mots | Réécriture si hors bornes |
| Structure 5 blocs | Les 5 blocs sont identifiables | Alerte qualité |
| PDV attribués | Chaque bit `point_de_vue` a un `auteur` identifié | Blocage publication |
| PDV multiples | Au moins 2 PDV distincts | Blocage — redirection vers TPL-DEPECHE-DEVELOPPEE |
| PDV équilibrés | Aucun PDV n'occupe > 60 % du bloc 4 | Alerte déséquilibre |
| Faits vérifiables | Chaque fait renvoie à un bit `fait` ou `donnée` existant | Vérification croisée |
| Conditionnel | Toléré uniquement dans le bloc 5 (ouverture) | Vérification ciblée |
| Cohérence amont | Si escalade, contient les bits clés de la dépêche source | Vérification automatique |

## Distribution

| Canal | Format | Délai |
|-------|--------|-------|
| Site web | Texte complet, blocs distincts, PDV visuellement différenciés | < 1h après déclencheur |
| Réseaux sociaux | Carrousel : 1 card par bloc principal | < 2h |
| Newsletter | Version résumée (accroche + PDV clés) | Au prochain digest |
| Flux MCP/agence | JSON complet avec graph de bits et relations | Immédiat |

## Escalade

La dépêche d'angle est le **dernier template de la Famille 1**. Au-delà, on entre dans la Famille 2 (contenu signé, intervention humaine) :

| Condition | Direction |
|-----------|-----------|
| L'angle mérite un traitement de fond | Candidat `Décryptage` (Famille 2) |
| Le sujet génère un engagement fort | Candidat `Analyse` (Famille 2) |
| Un acteur clé du sujet est disponible pour interview | Candidat `Interview` (Famille 2) |

Ces escalades ne sont pas automatiques. Elles génèrent une **suggestion** pour la rédaction.

## Cycle de vie

```
Création → Publication → Mises à jour PDV (72h) → Gel → Archivage actif
```

Les bits `point_de_vue` peuvent s'accumuler après publication. Si un nouveau PDV significatif apparaît dans les 72h, la dépêche est mise à jour. Au-delà, un nouveau template est créé.

---

Version : 0.1 | Date : 2026-04-14
