# Templates de production — Familles 1, 2 & 3

## Principe

Chaque template est un **schéma d'assemblage de bits** exécutable par la pipeline automatisée. Ce n'est pas un modèle d'article : c'est une recette de composition qui transforme des bits bruts en un format publiable.

Les templates sont organisés en trois familles :

| Famille | Rôle | Automatisation | Statut |
|---------|------|---------------|--------|
| **Famille 1** | Production éditoriale (dépêches) | Automatisable, supervision dégressive | Défini |
| **Famille 2** | Contenu signé (décryptage, analyse, enquête) | Intervention humaine requise | Défini |
| **Famille 3** | Distribution multi-canal (dérivés) | 100 % automatique dès jour 1 | Défini |

## Vocabulaire

- **Bit** : unité atomique d'information (donnée, fait, contexte, point_de_vue). Cf. `fondation/architecture-information-plexee.md`
- **Template** : règles d'assemblage qui produisent un format de sortie à partir de bits
- **Déclencheur** : condition qui lance l'exécution du template
- **Escalade** : condition qui provoque le passage à un template de niveau supérieur
- **Dérivé** : template Famille 3 qui recompose des contenus existants sans production originale

## Architecture globale

```
                        PRODUCTION AUTOMATISÉE (Famille 1)
                        ──────────────────────────────────
Événement détecté       alerte → depeche-courte → depeche-developpee → depeche-angle
par agent de veille                             → depeche-data
                                                → depeche-synthese
                               │                         │
                               │                         │ escalade (suggestion)
                               │                         ▼
                               │         CONTENU SIGNÉ (Famille 2)
                               │         ─────────────────────────
                               │         Bits F1 comme socle + valeur humaine :
                               │         decryptage · analyse · portrait
                               │         enquete · recit · interview
                               │
                               ▼
                        DISTRIBUTION (Famille 3)
                        ───────────────────────
                        F1 et F2 déclenchent les dérivés :
                               │
                    ┌──────────┼──────────┬─────────────┐
                    ▼          ▼          ▼             ▼
              carte-sociale  thread   newsletter    briefing-audio
              push-notif     social    digest        flux-mcp
```

## Chaîne d'escalade (Famille 1)

Les templates forment une chaîne naturelle. Chaque template peut déclencher le suivant :

```
alerte → depeche-courte → depeche-developpee → depeche-angle
                                              → depeche-synthese
                       → depeche-data (si bits dominants = données)
```

L'escalade n'est pas linéaire : une alerte peut déclencher directement une dépêche développée si suffisamment de contexte est disponible.

## Dérivation automatique (Famille 3)

Chaque publication Famille 1 déclenche automatiquement les dérivés applicables :

| Template source | Carte sociale | Thread | Newsletter | Briefing audio | Push | Flux MCP |
|----------------|:---:|:---:|:---:|:---:|:---:|:---:|
| Alerte | 1 carte | — | Prochain digest | Flash 30 sec | Oui (si prioritaire) | Oui |
| Dépêche courte | 1 carte | Si 3+ faits | Prochain digest | — | — | Oui |
| Dépêche développée | 1-2 cartes | 4-6 posts | Prochain digest | Lecture intégrale | — | Oui |
| Dépêche d'angle | 1-2 cartes | 5-8 posts | Prochain digest | Lecture intégrale | — | Oui |
| Dépêche synthèse | 1 + carrousel | 5-10 posts | Prochain digest | Résumé | — | Oui |
| Dépêche data | 1 + graphique | 3-5 posts | Prochain digest | Lecture adaptée | Si variation majeure | Oui |

## Supervision humaine

### Famille 1
- **Phase 1 (lancement)** : validation humaine systématique avant publication
- **Phase 2 (rodage)** : validation humaine par échantillonnage (1 sur N)
- **Phase 3 (croisière)** : publication automatique, revue humaine a posteriori + alertes qualité

### Famille 3
- Automatique dès le jour 1 (ce sont des dérivés de contenus déjà validés)
- Contrôles qualité embarqués dans chaque template (longueur, format, cohérence)

## Fichiers

Chaque template a deux représentations :
- **Documentation** (`.md`) : lisible par les humains — contexte, exemples, justifications
- **Spécification** (`specs/*.json`) : exécutable par l'orchestrateur — déclencheurs, composition, contrôles, distribution

Le schema de validation des specs est dans `specs/template-schema.json`.

### Famille 1 : Production

| Template | Documentation | Spécification JSON | User Need primaire |
|----------|-------------|-------------------|-------------------|
| Alerte | `alerte.md` | `specs/TPL-ALERTE.json` | update_me |
| Dépêche courte | `depeche-courte.md` | `specs/TPL-DEPECHE-COURTE.json` | update_me |
| Dépêche développée | `depeche-developpee.md` | `specs/TPL-DEPECHE-DEVELOPPEE.json` | update_me + educate_me |
| Dépêche d'angle | `depeche-angle.md` | `specs/TPL-DEPECHE-ANGLE.json` | give_me_perspective |
| Dépêche de synthèse | `depeche-synthese.md` | `specs/TPL-DEPECHE-SYNTHESE.json` | update_me + educate_me |
| Dépêche data | `depeche-data.md` | `specs/TPL-DEPECHE-DATA.json` | update_me + educate_me |

### Famille 2 : Contenu signé

| Template | Documentation | Spécification JSON | User Need primaire | Radar |
|----------|-------------|-------------------|-------------------|-------|
| Décryptage | `decryptage.md` | `specs/TPL-DECRYPTAGE.json` | educate_me | Obligatoire |
| Analyse | `analyse.md` | `specs/TPL-ANALYSE.json` | give_me_perspective | Critique |
| Portrait | `portrait.md` | `specs/TPL-PORTRAIT.json` | keep_me_engaged | Obligatoire |
| Enquête | `enquete.md` | `specs/TPL-ENQUETE.json` | educate_me | Obligatoire |
| Récit | `recit.md` | `specs/TPL-RECIT.json` | inspire_me | Obligatoire |
| Interview | `interview.md` | `specs/TPL-INTERVIEW.json` | give_me_perspective | Double (intervieweur + invité) |

### Famille 3 : Distribution

| Template | Documentation | Spécification JSON | Canal principal |
|----------|-------------|-------------------|----------------|
| Carte sociale | `carte-sociale.md` | `specs/TPL-CARTE-SOCIALE.json` | Instagram, TikTok, X, LinkedIn |
| Thread social | `thread-social.md` | `specs/TPL-THREAD-SOCIAL.json` | X, Threads, Bluesky, LinkedIn |
| Newsletter digest | `newsletter-digest.md` | `specs/TPL-NEWSLETTER-DIGEST.json` | Email |
| Briefing audio | `briefing-audio.md` | `specs/TPL-BRIEFING-AUDIO.json` | Podcast, app, réseaux sociaux |
| Push notification | `push-notification.md` | `specs/TPL-PUSH.json` | App, navigateur web |
| Flux MCP / Agence | `flux-mcp.md` | `specs/TPL-FLUX-MCP.json` | API JSON (consommateurs machines) |

## Ordre de déploiement recommandé

### Jour 1 — Noyau minimal viable

1. **Dépêche data** (F1) — la plus automatisable
2. **Alerte** (F1) — ultra-courte, forte valeur
3. **Dépêche courte** (F1) — brique de base
4. **Carte sociale** (F3) — distribution immédiate
5. **Push notification** (F3) — pour les alertes prioritaires
6. **Flux MCP** (F3) — le format pivot existe déjà, autant l'exposer

### Semaine 2-4 — Enrichissement

7. **Newsletter digest** (F3) — dès qu'on a assez de volume
8. **Thread social** (F3) — pour les dépêches développées
9. **Dépêche synthèse** (F1) — assemblage de l'existant
10. **Dépêche développée** (F1) — introduction du contexte
11. **Briefing audio** (F3) — quand le TTS est calibré

### Mois 2+ — Maturité F1

12. **Dépêche d'angle** (F1) — la dernière F1, car PDV = risque éditorial

### Phase 2 — Contenu signé (Famille 2)

Déploiement quand des journalistes signés sont opérationnels. Ordre recommandé :

13. **Décryptage** — le plus proche de la F1, ajoute du contexte explicatif signé
14. **Interview** — format structuré, fact-check intégré, double radar
15. **Analyse** — grille de lecture assumée, bloc nuance obligatoire
16. **Portrait** — narration + regards croisés
17. **Récit** — le plus littéraire, nécessite du terrain
18. **Enquête** — le plus exigeant, nécessite temps long + double validation

## Spécificités Famille 2

### Radar de transparence (décision #38)

Tous les templates F2 exigent un **radar de transparence** affiché à côté de la signature. Variables :

| Variable | Question |
|----------|----------|
| Expertise déclarée | Légitimité sur le sujet ? |
| Position connue | Position publique exprimée ? |
| Liens d'intérêt | Liens avec les acteurs du sujet ? |
| Grille de lecture | Orientation assumée ? (analyse uniquement) |
| Relation sujet | Lien personnel avec la personne ? (portrait, interview) |

L'interview est le seul template avec **deux radars** (intervieweur + invité).

### Relation F1 ↔ F2

La Famille 2 **consomme** les bits de la Famille 1 mais ne les remplace pas :

```
F1 (bits factuels publiés)
  ↓ réutilisation
F2 (ajoute contexte original, PDV signé, narration)
  ↓ distribution
F3 (dérivés multi-canal)
```

Les bits originaux produits par la F2 (contexte, PDV signé) ne sont **pas exposés** dans le flux MCP — seuls les bits factuels F1 référencés le sont.

Exception : l'enquête produit des bits `fait` exclusifs qui, eux, sont exposés dans le flux MCP après publication sur le site.

### Supervision

Tous les templates F2 restent en **validation humaine systématique** — ils ne passent jamais en automatique.

---

Version : 0.3 | Date : 2026-04-14 | Statut : complet — 18 templates définis (6 F1 + 6 F2 + 6 F3)
