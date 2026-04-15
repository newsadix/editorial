# Template : Analyse

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-ANALYSE` |
| **User Need primaire** | `give_me_perspective` |
| **User Need secondaire** | `educate_me` |
| **Longueur** | Intermédiaire à long : 1000-2500 mots |
| **Signé** | Oui — radar de transparence obligatoire |
| **Supervision** | Validation humaine systématique (toutes phases) |

## Principe

L'analyse est le template où le journaliste assume une grille de lecture. C'est la différence fondamentale avec le décryptage : le décryptage explique les mécanismes (pédagogie), l'analyse propose une interprétation (perspective).

Le radar de transparence est d'autant plus important ici : le lecteur doit savoir d'où parle l'auteur avant de lire son interprétation.

## Différence avec le décryptage

| | Décryptage | Analyse |
|-|-----------|---------|
| Question | « Comment ça marche ? » | « Qu'est-ce que ça signifie ? » |
| Posture | Pédagogue | Interprète |
| Bits originaux | Contexte (mécanismes) | Contexte + point de vue signé |
| Radar | Important | Critique |
| Conditionnel | Pour les hypothèses | Pour les projections |

## Prérequis

1. **Base factuelle solide.** Plus encore que le décryptage — l'analyse qui repose sur des faits fragiles est dangereuse
2. **Auteur avec expertise.** L'analyse demande une compétence reconnue sur le sujet. Le radar de transparence doit refléter cette expertise
3. **Pluralité de perspectives.** L'analyse n'est pas une tribune. Même si l'auteur assume une grille de lecture, les perspectives contradictoires doivent être présentées

## Déclencheur

Pas de déclenchement automatique. L'analyse est **commandée** :

- Par un chef de canal pour un sujet qui nécessite une mise en perspective
- Par un journaliste qui a une grille de lecture à proposer
- Suggestion : quand un sujet génère 3+ dépêches d'angle avec PDV divergents → signal qu'une analyse pourrait être pertinente

## Composition en bits

| Bit | Type | Obligatoire | Quantité | Origine | Rôle |
|-----|------|-------------|----------|---------|------|
| Faits existants | `fait` | Oui | 4-10 | Base F1 | Socle factuel solide |
| Données | `donnée` | Oui | 2-6 | Base F1 | Étayage chiffré |
| Contexte existant | `contexte` | Non | 0-4 | Base F1 | Cadrage |
| Contexte original | `contexte` | Oui | 3-5 | Produit par l'auteur | Interprétation contextuelle |
| PDV existants | `point_de_vue` | Oui | 2-4 | Base F1 + collecte | Pluralité |
| PDV auteur | `point_de_vue` | Oui | 1-2 | Produit par l'auteur | **La grille de lecture** |

**Différence clé avec le décryptage :** l'analyse produit des bits `point_de_vue` signés par l'auteur, en plus de bits `contexte`. C'est le seul template où l'auteur s'autorise une interprétation — toujours explicitement distinguée des faits.

## Structure de sortie

```
BLOC 1 — THÈSE (2-4 phrases)
  L'interprétation centrale de l'auteur, formulée clairement.
  Le lecteur sait dès le début ce que l'analyse va défendre.
  Ex. : « La hausse des taux de la BCE protège la monnaie unique 
  mais creuse les fractures entre Nord et Sud de la zone euro. »

BLOC 2 — FAITS QUI SOUTIENNENT (3-6 phrases + données)
  Les faits et données qui étayent la thèse.
  Tous issus de la base F1 ou de sources vérifiables.

BLOC 3 — FAITS QUI NUANCENT (3-6 phrases + données)
  Les faits et données qui contredisent ou nuancent la thèse.
  C'est ce bloc qui distingue l'analyse de la tribune.
  L'auteur joue fair play avec les éléments qui fragilisent sa lecture.

BLOC 4 — PERSPECTIVES CONTRADICTOIRES (3-6 phrases)
  Les PDV d'autres experts/acteurs qui proposent une lecture différente.
  Chaque PDV attribué (même règle que la dépêche d'angle).
  L'auteur ne les invalide pas — il les confronte à sa propre lecture.

BLOC 5 — CONCLUSION OUVERTE (2-4 phrases)
  L'auteur assume sa thèse tout en reconnaissant ses limites.
  Pas de conclusion définitive — la réalité est plus complexe qu'un article.
  Prochaines étapes ou conditions qui confirmeraient/infirmeraient la thèse.

SIGNATURE + RADAR DE TRANSPARENCE
  Nom + expertise déclarée + position connue + liens d'intérêt.

ATTRIBUTION
  Sources complètes.
```

## Radar de transparence (critique pour ce template)

L'analyse est le template où le radar est le plus important. Il doit répondre à :

| Variable | Question pour l'analyse |
|----------|----------------------|
| Expertise | Sur quoi l'auteur est-il légitime pour cette analyse ? |
| Position | L'auteur a-t-il une position publique sur le sujet ? |
| Liens d'intérêt | L'auteur a-t-il des liens avec les acteurs du sujet ? |
| Grille de lecture | L'auteur assume-t-il une orientation idéologique, économique, politique ? |

Le radar n'est pas punitif. Il est un acte de transparence : « Voilà d'où je parle, à vous de peser mon interprétation en connaissance de cause. »

## Règles strictes

1. **Thèse explicite.** Pas d'analyse qui masque sa conclusion. Le lecteur sait dès le bloc 1 ce que l'auteur défend
2. **Fair play factuel.** Le bloc 3 (faits qui nuancent) est obligatoire. Pas d'analyse qui occulte les éléments gênants
3. **Perspectives contradictoires.** Au moins 2 PDV différents de celui de l'auteur
4. **Fait =/= interprétation.** La distinction est toujours visible (charte §1). Les faits sont sourcés, les interprétations sont attribuées à l'auteur
5. **Conclusion ouverte.** Pas de verdict final. Le monde est complexe, l'analyse éclaire un aspect
6. **Radar complet.** Toutes les variables du radar sont renseignées

## Contrôles qualité

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Longueur | 1000-2500 mots | Alerte si hors bornes |
| Structure 5 blocs | Tous identifiables | Alerte qualité |
| Socle factuel | Au moins 4 bits `fait` de la base F1 | Blocage |
| Bloc nuance | Bloc 3 présent et non trivial (> 100 mots) | Blocage — l'analyse est partisane sans nuance |
| PDV contradictoires | Au moins 2 PDV distincts de celui de l'auteur | Blocage |
| Radar complet | Toutes variables renseignées | Blocage publication |
| Distinction fait/interprétation | Vérification que les bits `fait` ne contiennent pas d'interprétation | Revue humaine |

## Distribution

| Canal | Format | Délai |
|-------|--------|-------|
| Site web | Texte complet, blocs distincts, radar visible | Dès validation |
| Newsletter | Thèse (bloc 1) + lien | Prochain digest ou newsletter thématique |
| Réseaux sociaux | Thread : thèse → faits → nuances → conclusion | < 2h |
| LinkedIn | Publication longue (bien adapté au format) | < 4h |
| Audio | Lecture intégrale | < 6h |
| Flux MCP | JSON — seulement les bits factuels (pas la grille de lecture signée) | Bits F1 uniquement |

**Note flux MCP :** les bits `point_de_vue` signés par l'auteur ne sont **pas** exposés dans le flux MCP (décision : Famille 2 exclue du flux). Les bits factuels utilisés dans l'analyse, eux, sont déjà dans le flux via leur publication F1.

## Cycle de vie

```
Commande → Rédaction → Relecture croisée → Validation rédacteur en chef → Publication → Archivage actif
```

L'analyse n'est pas mise à jour. Si le sujet évolue, une nouvelle analyse est produite (potentiellement par un autre auteur avec une autre grille de lecture).

---

Version : 0.1 | Date : 2026-04-14
