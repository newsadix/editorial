# Template : Décryptage

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-DECRYPTAGE` |
| **User Need primaire** | `educate_me` |
| **User Need secondaire** | `give_me_perspective` |
| **Longueur** | Intermédiaire à long : 800-2000 mots |
| **Signé** | Oui — radar de transparence obligatoire |
| **Supervision** | Validation humaine systématique (toutes phases) |

## Principe

Le décryptage est le premier template de la Famille 2. Il apporte une valeur que l'automatisation ne peut pas produire : un **fil explicatif signé** qui guide le lecteur à travers un sujet complexe. Le journaliste sélectionne et ordonne les bits existants, puis ajoute des bits de contexte originaux pour construire une compréhension.

La différence avec la dépêche développée (F1) : le décryptage assume un travail de pédagogie. Il ne se contente pas de poser le contexte — il explique les mécanismes, les chaînes causales, les enjeux sous-jacents.

## Prérequis

1. **Bits factuels existants.** Le décryptage s'appuie sur des bits `fait` et `donnée` déjà publiés (via F1). Il ne crée pas sa propre base factuelle ex nihilo
2. **Auteur identifié.** Le décryptage est signé. L'auteur dispose d'un profil avec radar de transparence renseigné (décision #38)
3. **Sujet justifié.** Le sujet a généré au moins 1 dépêche F1 et le traitement factuel seul ne suffit pas à répondre au besoin `educate_me`

## Déclencheur

Pas de déclenchement automatique. Le décryptage est **commandé** par :

- Un chef de canal qui identifie un besoin d'explication sur un sujet couvert en F1
- Un journaliste qui propose un angle pédagogique
- Une suggestion automatique : quand un sujet accumule 10+ bits sans qu'aucun décryptage n'existe (signal, pas déclencheur)

## Composition en bits

| Bit | Type | Obligatoire | Quantité | Origine | Rôle |
|-----|------|-------------|----------|---------|------|
| Faits existants | `fait` | Oui | 3-8 | Base F1 (réutilisation) | Socle factuel |
| Données existantes | `donnée` | Non | 0-5 | Base F1 | Appui chiffré |
| Contexte existant | `contexte` | Non | 0-3 | Base F1 | Cadrage déjà publié |
| Contexte original | `contexte` | Oui | 3-6 | Produit par l'auteur | **La valeur ajoutée** : mécanismes, chaînes causales, enjeux |
| Points de vue | `point_de_vue` | Non | 0-2 | Base F1 ou produit | Éclairage expert si pertinent |

**Le contenu original signé est principalement du type `contexte`.** Le journaliste ne fabrique pas de faits — il construit des ponts entre les faits.

## Structure de sortie

```
BLOC 1 — QUESTION (1-2 phrases)
  La question à laquelle le décryptage répond.
  Formulée simplement, comme le lecteur la poserait.
  Ex. : « Pourquoi la BCE relève-t-elle ses taux alors que l'inflation baisse ? »

BLOC 2 — RÉPONSE COURTE (2-3 phrases)
  La réponse en version condensée.
  Le lecteur pressé s'arrête ici et a compris l'essentiel.

BLOC 3 — DÉVELOPPEMENT PAR COUCHES
  Le cœur du décryptage, structuré en couches :

  COUCHE 1 — Les faits (bits F1 existants)
    Ce qui s'est passé. Rappel factuel ancré dans les dépêches.

  COUCHE 2 — Les mécanismes (bits contexte originaux)
    Comment ça fonctionne. Les rouages, les règles du jeu.
    Ex. : comment la BCE décide, quels sont les mandats, quels leviers.

  COUCHE 3 — Les enjeux (bits contexte originaux)
    Pourquoi ça compte. Les conséquences directes et indirectes.
    Ex. : impact sur les crédits, l'emploi, l'épargne.

  Chaque couche est identifiable visuellement (intertitre ou séparation).

BLOC 4 — CE QU'ON NE SAIT PAS ENCORE (1-3 phrases)
  Les incertitudes honnêtement nommées.
  Les questions ouvertes.
  Engagement de factualité : ne pas prétendre tout expliquer.

SIGNATURE
  Nom de l'auteur + lien vers profil/radar de transparence.

ATTRIBUTION
  Sources (bits F1 référencés + sources complémentaires).
```

### Exemple de structure

```
POURQUOI LA BCE RELÈVE-T-ELLE SES TAUX ALORS QUE L'INFLATION BAISSE ?

En bref : parce que la BCE regarde l'inflation sous-jacente, pas le chiffre 
global. Et l'inflation sous-jacente reste au-dessus de sa cible.

LES FAITS
La BCE a relevé son taux directeur à 4,75 % jeudi. C'est la dixième hausse 
depuis juillet 2022. L'inflation globale recule à 2,4 % en mars...

COMMENT LA BCE DÉCIDE
Le mandat de la BCE est la stabilité des prix, définie comme une inflation 
proche de 2 %. Mais le Conseil des gouverneurs ne regarde pas seulement 
le chiffre global...
[Explication des mécanismes : inflation sous-jacente, forward guidance, 
transmission monétaire]

POURQUOI ÇA VOUS CONCERNE
Le taux directeur de la BCE se répercute sur les taux de crédit immobilier 
avec un délai de 3 à 6 mois...
[Impact concret : crédits, épargne, pouvoir d'achat]

CE QU'ON NE SAIT PAS
La BCE n'a pas indiqué si cette hausse serait la dernière. Les projections 
de juin seront déterminantes...

Par [Auteur] · Profil et transparence
Sources : BCE, Eurostat, Banque de France, [expert cité]
```

## Radar de transparence

Obligatoire pour tout contenu Famille 2. Affiché à côté de la signature.

Le radar de transparence expose les biais potentiels de l'auteur sur le sujet traité (décision #38). Variables à afficher pour chaque décryptage :

| Variable | Question |
|----------|----------|
| Expertise déclarée | L'auteur a-t-il une expertise particulière sur ce sujet ? |
| Position connue | L'auteur a-t-il exprimé publiquement une position sur ce sujet ? |
| Liens d'intérêt | L'auteur a-t-il des liens (financiers, professionnels, personnels) avec les acteurs du sujet ? |

Si aucun biais n'est identifiable, le radar l'indique : « Aucun conflit d'intérêt identifié. »

Le radar renvoie au profil complet de l'auteur (visualisation type FIFA, ~12 variables, décision #38).

## Règles strictes

1. **Les faits viennent de F1.** Le décryptage ne fabrique pas ses propres faits. Il les importe de la base de bits
2. **Le contexte original est le produit.** La valeur ajoutée est dans l'explication, pas dans les faits
3. **Réponse courte obligatoire.** Le lecteur pressé doit pouvoir comprendre en 30 secondes
4. **Incertitudes nommées.** Le bloc « ce qu'on ne sait pas » est obligatoire — c'est un engagement de la charte
5. **Conditionnel pour les hypothèses.** Si l'auteur avance une hypothèse, le conditionnel est obligatoire (charte §1)
6. **Signature + radar.** Jamais de décryptage anonyme

## Contrôles qualité

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur | 800-2000 mots | Alerte si hors bornes |
| Structure | 4 blocs identifiables + signature | Alerte qualité |
| Bits F1 présents | Au moins 3 bits `fait` provenant de la base F1 | Blocage — pas assez de socle factuel |
| Contexte original | Au moins 3 bits `contexte` originaux | Blocage — pas assez de valeur ajoutée |
| Réponse courte | Bloc 2 présent et < 80 mots | Alerte |
| Incertitudes | Bloc 4 présent | Alerte |
| Radar | Profil auteur avec radar renseigné | Blocage publication |
| Cohérence F1 | Les faits cités correspondent à des bits publiés | Vérification croisée |

## Distribution

| Canal | Format | Délai |
|-------|--------|-------|
| Site web | Texte complet, couches visuellement distinctes, radar intégré | Dès validation |
| Newsletter | Résumé (question + réponse courte) + lien | Prochain digest |
| Réseaux sociaux | Carrousel : question → réponse courte → 2-3 mécanismes clés | < 2h |
| Audio | Lecture intégrale adaptée oral | < 4h |
| Flux MCP | JSON avec bits originaux + bits F1 référencés | Immédiat |

## Cycle de vie

```
Commande → Rédaction → Validation humaine → Publication → Mise à jour si évolution → Archivage actif
```

Le décryptage peut être mis à jour si le sujet évolue significativement (nouveau fait majeur). Sinon, un nouveau décryptage est créé.

---

Version : 0.1 | Date : 2026-04-14
