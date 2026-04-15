# Pipeline de production Newsadix

Réf. visuelle : board Miro des fondateurs (screenshot versé le 2026-03-11)

## Vue d'ensemble

```
SOURCES → ANALYSE/FILTRAGE → BITS → [VALIDATION] → ASSEMBLAGE (F1) → DISTRIBUTION (F3) → AMPLIFICATION → MONÉTISATION
                                         ↑                                                        ↑
                                   Muraille de Chine                                          ANALYTICS
                                (humain phase 1,                                            (transversal)
                                auto phase 3)
```

### Changement clé par rapport à la v0.2

Le pipeline ne produit plus des « pièces de contenu » mais des **bits** (cf. `fondation/architecture-information-plexee.md`). Les bits sont ensuite assemblés par les **templates Famille 1** en dépêches publiables, puis dérivés automatiquement par les **templates Famille 3** en formats natifs pour chaque canal.

---

## 1. SOURCES — « Qu'est-ce qu'il y a à dire »

### Principe
Curation de sources sélectionnées sur les 12 piliers de la taxonomie éditoriale. Audience cible : **France** (décision #22).

### Types de sources

| Type | Couverture géographique | Automatisation |
|------|------------------------|----------------|
| Agences de presse (AFP, Reuters, AP) | France + international | Flux automatisé |
| Presse écrite | France, US, UK, Allemagne, Japon | RSS + monitoring |
| Télévision | France | Transcription automatisée |
| Radio | France | Transcription automatisée |
| Comptes clés X/Twitter | Sélection manuelle | Monitoring API |
| Threads Reddit | International | Monitoring |
| Sources officielles | France + UE | Monitoring (JO, BCE, INSEE, etc.) |
| Données publiques | Multi-pays | Calendriers statistiques |

### Règles
- Chaque source est sélectionnée à la main, pas de scraping aveugle
- La liste des sources est revisable et documentée
- Les calendriers de publications statistiques sont pré-chargés (déclencheurs `TPL-DEPECHE-DATA`)

---

## 2. ANALYSE / FILTRAGE — Du bruit au signal

### Agents de veille

Les agents de veille transforment le flux brut en **bits candidats** :

```
Flux source brut
  → Agent de veille (spécialisé par pilier ou par type de source)
  → Évaluation : factualité + pertinence + nouveauté
  → Production de bits candidats (type : fait, donnée)
  → Statut : brouillon
```

### Critères de filtrage

| Critère | Question | Action si non |
|---------|----------|--------------|
| Factualité | Le fait est-il vérifiable et sourcé ? | Rejet |
| Pertinence | Cette information répond-elle à un User Need ? | Rejet |
| Nouveauté | Existe-t-il déjà un bit `même_sujet` récent ? | Fusion ou enrichissement |
| Fiabilité source | La source est-elle dans la liste validée ? | Vérification supplémentaire |

### Livrable
Des bits au format JSON canonique (cf. `editorial/schema-bit.md`), statut `brouillon`.

---

## 3. BITS — L'unité de production

### Production de bits

| Qui produit | Type de bits | Processus |
|-------------|-------------|-----------|
| Agents de veille | `fait`, `donnée` | Automatique à partir des sources |
| Agent de plexage | (relations) | Automatique : propose les relations entre bits |
| Journaliste/validateur | `contexte`, `point_de_vue` | Manuel (Famille 2) ou validation de suggestions IA |

### Format pivot

Le **bit JSON** est la source unique de vérité. Schéma complet : `editorial/schema-bit.md`.

Champs clés :
- `type` : donnée | fait | contexte | point_de_vue
- `sources[]` : traçabilité complète
- `relations[]` : connexions sémantiques avec la base existante
- `user_need` : besoin utilisateur adressé
- `pilier` : taxonomie éditoriale
- `statut` : brouillon → validé → publié → archivé

---

## 4. VALIDATION — La Muraille de Chine

### Point de contrôle

| Phase | Processus | Latence |
|-------|-----------|---------|
| Phase 1 (lancement) | Validation humaine de chaque bit et assemblage | 5-30 min |
| Phase 2 (rodage) | Validation par échantillonnage (1 sur N) | < 5 min |
| Phase 3 (croisière) | Automatique + revue a posteriori + alertes qualité | < 1 min |

### Contrôles automatisés (toutes phases)

Chaque template embarque ses propres contrôles (détaillés dans `editorial/templates/*.md`). Socle commun :

| Contrôle | Détail |
|----------|--------|
| Source présente | `sources[]` non vide |
| Cohérence type ↔ contenu | Un bit `donnée` contient un chiffre, un `point_de_vue` est attribué |
| Déduplication | Pas de bit identique récent |
| Longueur | Conforme aux bornes du template |
| Langue | Français, orthographe, grammaire |
| Anti-slop | Détection de formulations creuses ou génériques (décision #34) |

### Muraille de Chine

La séparation stricte entre éditorial et commercial s'applique à ce stade : tout ce qui est en amont (sources, bits, validation, assemblage) est **exclusivement éditorial**. La monétisation n'a aucune visibilité ni influence sur ce qui se passe avant cette ligne.

---

## 5. ASSEMBLAGE — Templates Famille 1

### Principe

Les bits validés sont assemblés par les templates de la Famille 1 pour produire des dépêches publiables. Le template sélectionné dépend des bits disponibles et des conditions de déclenchement.

### Chaîne d'escalade

```
Bit fait prioritaire → TPL-ALERTE
                         ↓ (+ bits complémentaires)
                       TPL-DEPECHE-COURTE
                         ↓ (+ bits contexte)        ↓ (+ bits donnée)
                       TPL-DEPECHE-DEVELOPPEE      TPL-DEPECHE-DATA
                         ↓ (+ bits PDV)              ↓ (accumulation)
                       TPL-DEPECHE-ANGLE           TPL-DEPECHE-SYNTHESE
```

### Templates disponibles

| Template | Fichier | Bits requis | Longueur |
|----------|---------|-------------|----------|
| Alerte | `templates/alerte.md` | 1 fait | < 280 car. |
| Dépêche courte | `templates/depeche-courte.md` | 2-5 faits + données | 100-200 mots |
| Dépêche développée | `templates/depeche-developpee.md` | 5-11 faits + contexte | 300-600 mots |
| Dépêche d'angle | `templates/depeche-angle.md` | 7-15 faits + contexte + PDV | 500-1000 mots |
| Dépêche synthèse | `templates/depeche-synthese.md` | 6-15 agrégation | 400-800 mots |
| Dépêche data | `templates/depeche-data.md` | 5-10 données | 200-500 mots |

### Livrable

Un **assemblage** au format JSON (cf. `editorial/schema-bit.md` §2) contenant :
- Référence au template utilisé
- Liste ordonnée des bits avec leurs rôles
- Texte rendu (prêt à publier)
- Métadonnées (pilier, géo, user need)

---

## 6. DISTRIBUTION — Templates Famille 3

### Principe

Chaque assemblage Famille 1 déclenche automatiquement les dérivés Famille 3 pertinents. Pas de production originale : reformatage de l'existant.

### Matrice de dérivation

| Template F1 → | Carte sociale | Thread | Newsletter | Audio | Push | Flux MCP |
|---------------|:---:|:---:|:---:|:---:|:---:|:---:|
| Alerte | 1 carte | — | Digest | Flash 30s | Si prioritaire | Oui |
| Dépêche courte | 1 carte | Si 3+ faits | Digest | — | — | Oui |
| Dépêche développée | 1-2 cartes | 4-6 posts | Digest | Lecture | — | Oui |
| Dépêche d'angle | 1-2 cartes | 5-8 posts | Digest | Lecture | — | Oui |
| Dépêche synthèse | Carrousel | 5-10 posts | Digest | Résumé | — | Oui |
| Dépêche data | Graphique | 3-5 posts | Digest | Adaptée | Si majeur | Oui |

### Canaux

| Canal | Type | Rôle | Templates F3 |
|-------|------|------|-------------|
| **Site web** | Owned | Camp de base, monétisation | Tous les assemblages F1 |
| **Newsletter(s)** | Owned | Relation audience directe | `TPL-NEWSLETTER-DIGEST` |
| **Flux MCP / API** | Owned | Distribution machine | `TPL-FLUX-MCP` |
| **Instagram** | Rented | Acquisition via Scroll | `TPL-CARTE-SOCIALE` |
| **TikTok** | Rented | Acquisition via Scroll | `TPL-CARTE-SOCIALE` + audio |
| **X/Twitter** | Rented | Distribution + Seek | `TPL-CARTE-SOCIALE`, `TPL-THREAD-SOCIAL` |
| **Threads** | Rented | Distribution | `TPL-THREAD-SOCIAL` |
| **LinkedIn** | Rented | Distribution professionnelle | `TPL-CARTE-SOCIALE`, `TPL-THREAD-SOCIAL` |
| **Podcasts** | Owned | Subscribe, consommation passive | `TPL-BRIEFING-AUDIO` |
| **App (push)** | Owned | Alertes prioritaires | `TPL-PUSH` |

### Hiérarchie
1. **Site + newsletter + flux MCP** = canaux owned. Newsadix contrôle la relation et monétise
2. **Réseaux sociaux** = canaux rented. Acquisition et amplification, pas monétisation directe

---

## 7. PRODUCTION GRAPHIQUE — « Sous quel format je le fais ? »

À partir des assemblages et dérivés, production du meilleur format natif pour chaque plateforme de destination.

### Formats par template F3

| Template F3 | Format graphique | Responsable |
|-------------|-----------------|-------------|
| Carte sociale | Image statique (palette pilier) | Moteur automatisé (Skan) |
| Thread social | Texte pur (pas de visuel obligatoire) | Automatique |
| Newsletter | HTML responsive (template email) | Automatique |
| Briefing audio | MP3/AAC + visuel animé pour réseaux | TTS + moteur graphique |
| Push | Texte pur | Automatique |
| Flux MCP | JSON (pas de graphique) | Automatique |

### Lead
Skan Triki — moteur graphique propriétaire, automation de templates visuels.

---

## 8. AMPLIFICATION — « Comment je le fais vivre ? »

Pas de « publish and pray ». Processus actif post-publication.

### Tactiques

| Tactique | Détail | Automatisable |
|----------|--------|:---:|
| Premier commentaire | Posté ~3 min après publication sociale | Oui |
| Réactions aux commentaires | Réponses aux premiers commentaires | Oui (phase 2) |
| Follow-backs | TikTok : suivre les nouveaux followers | Oui |
| Cross-posting temporel | Republier une carte à un horaire différent si engagement faible | Oui |
| Analytics par plateforme | Mesurer et ajuster en continu | Oui |

### Lead
PJ, Yann Casset, Geoffrey — micro-algos d'engagement et analytics.

---

## 9. MONÉTISATION — « Comment je le rends rentable ? »

Le workflow entier doit être rentable. La monétisation est séparée de l'éditorial (Muraille de Chine).

Levier principal : publicité contextuelle sur le site web (cf. `fondation/modele-economique.md`).

La granularité des bits ouvre la possibilité d'une publicité contextuelle fine : par pilier, par sous-thème, par cluster de sujets — pas par page.

---

## ANALYTICS — Transversal

Les analytics irriguent **tout le pipeline** :

| Étape | Question analytics |
|-------|-------------------|
| Sources | Quelles sources produisent le signal le plus pertinent ? |
| Bits | Quels types de bits sont les plus consommés ? |
| Assemblage | Quels templates génèrent le plus d'engagement ? |
| Distribution | Quelles plateformes performent pour quels User Needs ? |
| Amplification | Quelles stratégies d'engagement fonctionnent ? |
| Monétisation | Quels piliers/clusters génèrent des revenus ? |

Boucle de feedback continue. Voir aussi : `editorial/pennmap.md` pour la mesure de neutralité.

---

## Flux complet — Exemple concret

```
1. L'INSEE publie le taux de chômage T1 2026
   → Agent de veille « données publiques » détecte la publication

2. Bits générés :
   - bit-001 : type=donnée, contenu="7,3 % au T1 2026", source=INSEE
   - bit-002 : type=donnée, contenu="7,1 % au T4 2025", source=INSEE
   - bit-003 : type=fait, contenu="hausse de 0,2 point", source=INSEE

3. Agent de plexage :
   - Relie bit-001 → bit-002 (relation : met_a_jour)
   - Relie bit-003 → bit-existant-chômage-eurozone (relation : contextualise)

4. Validation (phase 1 : humaine)

5. Template sélectionné : TPL-DEPECHE-DATA (bits dominants = données)
   → Assemblage : chiffre principal + comparaison + méthodologie + limites

6. Dérivés F3 générés automatiquement :
   - Carte sociale : image avec "7,3 %" en gros, couleur pilier Économie
   - Thread X : 4 posts (chiffre → comparaison → méthodo → limites)
   - Newsletter : intégré au prochain digest matinal
   - Flux MCP : JSON disponible immédiatement

7. Amplification : premier commentaire automatique sur la carte Instagram

8. Analytics : suivi engagement par canal
```

---
Version : 1.0 | Date : 2026-04-14 | Statut : complété — intègre les templates F1 et F3
