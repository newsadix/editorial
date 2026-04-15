# Template : Interview / Conversation structurée

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-INTERVIEW` |
| **User Need primaire** | `give_me_perspective` |
| **User Need secondaire** | `connect_me` |
| **Longueur** | Intermédiaire à long : 800-2500 mots |
| **Signé** | Oui — radar de transparence obligatoire (pour l'intervieweur ET l'invité) |
| **Supervision** | Validation humaine systématique |

## Principe

L'interview est une conversation structurée avec un acteur du sujet — expert, décideur, témoin, praticien. Elle donne une voix directe à une personne dont la perspective éclaire un enjeu.

La valeur ajoutée du journaliste : la préparation (bits F1 maîtrisés), la qualité des questions, le fact-checking en temps réel, la structuration post-interview.

## Prérequis

1. **Invité pertinent.** La personne a une perspective unique ou une expertise reconnue sur un sujet couvert en F1
2. **Ancrage F1.** L'interview est reliée à des dépêches existantes — ce n'est pas une conversation déconnectée de l'actualité
3. **Préparation factuelle.** L'intervieweur maîtrise les bits F1 du sujet pour pouvoir vérifier en temps réel les affirmations de l'invité

## Déclencheur

Commandé. Jamais automatique. Typiquement :

- Un acteur clé d'un sujet couvert en F1 est disponible ou sollicité
- Une dépêche d'angle a généré des PDV qui méritent approfondissement
- Un expert peut éclairer un décryptage en cours

## Composition en bits

| Bit | Type | Obligatoire | Quantité | Origine | Rôle |
|-----|------|-------------|----------|---------|------|
| Faits de contexte | `fait` | Oui | 2-5 | Base F1 | Ancrage dans l'actualité |
| Données de contexte | `donnée` | Non | 0-3 | Base F1 | Chiffres de cadrage |
| Contexte | `contexte` | Oui | 1-3 | Base F1 + auteur | Présentation de l'invité et du cadre |
| PDV invité (réponses) | `point_de_vue` | Oui | 5-15 | Interview | **Le cœur du template** |
| Vérifications factuelles | `fait` ou `donnée` | Non | 0-5 | Base F1 | Fact-check intégré |

## Structure de sortie

```
BLOC 1 — PRÉSENTATION (2-4 phrases)
  Qui est l'invité. Pourquoi cette personne sur ce sujet.
  Lien avec l'actualité F1 (quelle dépêche, quel enjeu).

BLOC 2 — QUESTION STRUCTURANTE
  La première question cadre le territoire de l'échange.
  Elle est ouverte, pas binaire.

BLOC 3 — ÉCHANGE (le corps)
  Alternance questions / réponses.
  
  Pour chaque échange :
  Q : Question du journaliste (courte, directe)
  R : Réponse de l'invité (fidèle, éditée pour clarté mais pas déformée)
  
  [VÉRIFICATION] — en incise après une affirmation vérifiable :
  encadré factuel avec le bit source qui confirme ou nuance.
  Ex. : « [Vérification : le taux cité par X est exact — INSEE, T1 2026] »
  Ex. : « [Vérification : le chiffre avancé par X est inexact. 
  Selon l'INSEE, le taux est de 7,3 %, pas 6,8 %] »

BLOC 4 — POINTS DE DÉSACCORD (optionnel)
  Si l'intervieweur et l'invité sont en désaccord sur un fait,
  le désaccord est explicité avec les sources des deux côtés.

BLOC 5 — FERMETURE
  Question de conclusion (ouverte, tournée vers l'avenir).

PRÉSENTATION INVITÉ (encadré)
  Bio courte + radar de transparence de l'invité.
  Expertise, positions connues, liens d'intérêt.

SIGNATURE INTERVIEWEUR + RADAR
ATTRIBUTION
```

## Double radar de transparence

L'interview est le seul template avec **deux radars** :

### Radar de l'intervieweur
| Variable | Question |
|----------|----------|
| Expertise | Maîtrise du sujet |
| Position connue | A-t-il exprimé un avis public sur ce sujet ? |
| Relation avec l'invité | Le connaît-il personnellement ? |

### Radar de l'invité
| Variable | Question |
|----------|----------|
| Expertise | Sur quoi est-il/elle légitime ? |
| Position connue | A-t-il/elle une position publique sur le sujet ? |
| Liens d'intérêt | Liens financiers, professionnels, politiques avec les acteurs du sujet ? |
| Rôle dans le sujet | Est-il/elle acteur, observateur, ou les deux ? |

Le radar de l'invité peut être renseigné par l'intervieweur (avec vérification).

## Règles strictes

1. **Citations fidèles.** Les réponses sont éditées pour clarté (suppression des hésitations, restructuration syntaxique) mais ne sont jamais déformées. L'invité peut relire ses citations
2. **Fact-check intégré.** Les affirmations vérifiables sont vérifiées dans le texte. Les incises [Vérification] sont visibles par le lecteur
3. **Questions non complaisantes.** L'intervieweur pose les questions difficiles. L'interview n'est pas un exercice de communication de l'invité
4. **Droit de réponse intégré.** Si l'invité est mis en cause par des faits ou PDV existants, la question lui est posée
5. **Double radar.** Les deux profils sont exposés

## Contrôles qualité

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur | 800-2500 mots | Alerte si hors bornes |
| Structure Q/R | Format question/réponse identifiable | Alerte qualité |
| Vérifications | Au moins 1 incise [Vérification] dans l'échange | Alerte — l'interview n'est pas fact-checkée |
| Présentation invité | Encadré présent avec bio + radar | Blocage |
| Radar intervieweur | Complet | Blocage |
| Radar invité | Complet | Blocage |
| Ancrage F1 | L'interview est reliée à au moins 1 dépêche F1 | Vérification |
| Relecture invité | L'invité a validé ses citations (si politique éditoriale) | Vérification process |

## Distribution

| Canal | Format | Délai |
|-------|--------|-------|
| Site web | Format Q/R avec incises fact-check, radars intégrés | Dès validation |
| Newsletter | 1-2 échanges clés + lien | Prochain digest |
| Réseaux sociaux | Extraits vidéo/audio si interview filmée, sinon cartes citations | < 4h |
| Audio/Vidéo | Intégrale ou extraits si interview enregistrée | < 12h |
| Flux MCP | Bits factuels de vérification uniquement | Immédiat |

## Variantes

| Variante | Détail |
|----------|--------|
| Interview écrite | Questions envoyées par email, réponses écrites. Moins vivante mais plus précise |
| Interview live | Conversation enregistrée (audio ou vidéo), transcrite et éditée |
| Conversation à plusieurs | 2+ invités avec perspectives différentes. Même format Q/R mais gestion des interactions |

---

Version : 0.1 | Date : 2026-04-14
