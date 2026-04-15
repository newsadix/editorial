---
name: user-needs
description: Cadre de segmentation des besoins informationnels du public — 8 besoins organisés en 4 directions (connaissance, action, compréhension, ressenti). Détermine le template d'article, le format LinkedIn et la stratégie de distribution. Charger pour le routing éditorial.
source: "Adapté de FLTR — user-needs.md (Boussole des besoins)"
---

# Couche stratégique — User Needs 2.0

## Position dans la chaîne

Ce skill se charge APRÈS l'analyse éditoriale et AVANT les formats par plateforme.
Il ne remplace rien : il ajoute une couche de décision entre l'analyse (quoi dire) et le format (comment le dire).

**Chaîne complète** : charte éditoriale → analyse systémique → scoring → **user-needs** → formats plateformes

---

## Les 8 besoins du public (Boussole des besoins)

### Direction CONNAISSANCE (savoir ce qui se passe)

| Besoin | Code | Définition | Signal dans l'article |
|--------|------|------------|----------------------|
| **Tiens-moi au courant** | `update_me` | Faits bruts, dernière heure, suivi | L'article rapporte un événement récent sans analyse approfondie |
| **Fais-moi découvrir** | `keep_me_engaged` | Curiosité, sujets inattendus, hors radar | Le sujet est peu couvert, angle original, découverte |

### Direction ACTION (savoir quoi faire)

| Besoin | Code | Définition | Signal dans l'article |
|--------|------|------------|----------------------|
| **Aide-moi** | `help_me` | Guides, outils, méthodes, solutions pratiques | L'article contient des étapes concrètes, des outils, des tutos |
| **Connecte-moi** | `connect_me` | Communauté, témoignages, appartenance | L'article met en avant des collectifs, des coalitions, des voix |

### Direction COMPRÉHENSION (comprendre le monde)

| Besoin | Code | Définition | Signal dans l'article |
|--------|------|------------|----------------------|
| **Apprends-moi** | `educate_me` | Pédagogie, mécanismes, fonctionnement | L'article explique un "comment ça marche", un mécanisme, une chaîne causale |
| **Éclaire-moi** | `give_me_perspective` | Analyse, mise en perspective, enjeux de fond | L'article révèle des dynamiques sous-jacentes, des rapports de force, des paradoxes |

### Direction RESSENTI (ressentir quelque chose)

| Besoin | Code | Définition | Signal dans l'article |
|--------|------|------------|----------------------|
| **Divertis-moi** | `divert_me` | Surprise, humour, légèreté | L'article a une dimension ludique, absurde, ou décalée |
| **Inspire-moi** | `inspire_me` | Espoir, vision, possibilités | L'article montre des victoires, des pistes, une vision positive |

---

## Règles d'attribution

### Pour chaque article analysé, identifier :

1. **User Need primaire** (obligatoire) : le besoin dominant que l'article satisfait
2. **User Need secondaire** (0-2 max) : besoins complémentaires
3. **Direction dominante** : connaissance, action, compréhension, ressenti

---

## Heuristiques de détection

- Score d'activabilité élevé → probablement `help_me` ou `educate_me`
- Pilier solidarité dominant + acteurs collectifs → `connect_me`
- Score documentaire élevé + analyse longue → `give_me_perspective` ou `educate_me`
- Article court, fait récent, peu d'analyse → `update_me`
- Pistes systémiques fortes + initiatives → `inspire_me`
- Sujet peu couvert, angle inattendu → `keep_me_engaged`
- Paradoxe ou renversement dans l'analyse → `give_me_perspective`
- Dimension ludique, absurde, décalée → `divert_me`
- Témoignages individuels ou collectifs mis en avant → `connect_me`

---

## Combinaisons fréquentes

| Combinaison | Exemple type |
|-------------|-------------|
| `give_me_perspective` + `educate_me` | Analyse approfondie d'un mécanisme avec mise en contexte |
| `update_me` + `give_me_perspective` | Fait d'actualité avec angle révélateur |
| `help_me` + `educate_me` | Guide pratique qui explique le pourquoi en plus du comment |
| `inspire_me` + `connect_me` | Initiative collective qui donne de l'espoir |
| `keep_me_engaged` + `give_me_perspective` | Sujet hors radar avec analyse systémique |
| `educate_me` + `help_me` | Mécanisme expliqué avec des leviers d'action concrets |
| `update_me` + `help_me` | Fait d'actualité avec guide de réaction immédiate |

---

## Matrice de routing — User Need vers plateformes

### Principe de value gap

Le contenu social donne la **surface** (le "quoi" + un angle).
L'article web donne la **profondeur** (le "pourquoi" + le "et maintenant ?").
Le CTA social vers l'article est systématique pour les besoins Perspective et Éducation.

### Routing par User Need

| User Need primaire | Template article | Format LinkedIn | Facebook | Bluesky |
|---|---|---|---|---|
| `give_me_perspective` | **Perspective** | Format A (Décryptage) | Oui | Oui |
| `educate_me` | **Éducation** | Format A (Décryptage) | Oui | Oui |
| `inspire_me` | **Perspective** | Format B (Récit) | Oui | Oui |
| `help_me` | **Éducation** | Format A (Décryptage) | Oui (si grand public) | Oui |
| `update_me` | **Signal** | Format C (Questionnement) | Non | Oui |
| `connect_me` | **Perspective** | Format B (Récit) | Oui | Oui |
| `keep_me_engaged` | **Signal** ou **Perspective** | Format C (Questionnement) | Oui | Oui |
| `divert_me` | Pas d'article | Non | Oui (si pertinent) | Oui |

### Formats LinkedIn

- **Format A — Décryptage** : analyse structurée, ouverture par le paradoxe ou le constat contre-intuitif, développement argumenté, CTA vers l'article
- **Format B — Récit** : narration, mise en avant d'une initiative ou d'un parcours, dimension humaine, CTA vers l'article
- **Format C — Questionnement** : fait brut + question ouverte, format court, engagement par le débat

---

## Règles de routing

1. **Article web** : tous les articles pertinents (score élevé) sauf `divert_me` pur — hub central de profondeur
2. **LinkedIn** : tous sauf `divert_me` — le format (A/B/C) dépend du User Need — moteur de portée
3. **Facebook** : `give_me_perspective`, `educate_me`, `inspire_me`, `connect_me`, `keep_me_engaged` — audience engagée
4. **Bluesky** : tous — audience early adopters sensible à tous les angles — laboratoire
5. **Mastodon** : privilégier `educate_me`, `give_me_perspective`, `help_me` — communauté technique

### Hiérarchie des plateformes

1. **Article web** = Hub central (profondeur, relation, conversion newsletter)
2. **LinkedIn** = Moteur de portée (découverte, audience professionnelle)
3. **Facebook** = Audience engagée (communauté active)
4. **Bluesky** = Laboratoire (early adopters, ton plus libre)
5. **Mastodon** = Niche technique (communauté spécialisée)

---

## Value gap par User Need

| User Need | Surface (social) | Profondeur (article web) |
|---|---|---|
| `give_me_perspective` | "Voici le paradoxe. L'analyse complète →" | Analyse systémique, rapports de force, pistes d'action |
| `educate_me` | "Comment ça marche en 3 points →" | Mécanisme complet, contexte historique, ressources |
| `update_me` | "Le fait brut + l'angle" | Mise en contexte rapide, source primaire, signaux |
| `inspire_me` | "Cette initiative montre que c'est possible →" | Récit complet, mécanismes de succès, réplicabilité |
| `help_me` | "L'outil/la méthode existe →" | Guide complet, étapes, alternatives, limites |
| `connect_me` | "Ce collectif agit →" | Cartographie des acteurs, parcours, comment rejoindre |
| `keep_me_engaged` | "Vous n'en avez probablement pas entendu parler →" | Enquête complète, contexte, enjeux cachés |
| `divert_me` | Publication sociale autonome | Pas d'article (le contenu social suffit) |

---

## Intégration dans le workflow éditorial

### Avant la rédaction

1. Identifier le User Need primaire de l'article analysé
2. Identifier 0-2 User Needs secondaires
3. Déterminer la direction dominante
4. Consulter la matrice de routing pour choisir les plateformes et formats
5. Appliquer le value gap : le social donne la surface, l'article donne la profondeur

### Pendant la rédaction

- Le User Need guide le **ton** : `update_me` = factuel et concis, `inspire_me` = narratif et positif, `educate_me` = pédagogique et structuré
- Le User Need guide la **structure** : `help_me` = étapes numérotées, `give_me_perspective` = analyse en couches, `connect_me` = voix et témoignages
- Le User Need guide le **CTA** : `educate_me`/`give_me_perspective` = "L'analyse complète →", `help_me` = "Le guide complet →", `inspire_me` = "L'histoire complète →"

### Après la rédaction

- Vérifier que le contenu social crée bien un value gap (pas tout donner en surface)
- Vérifier que l'article web apporte bien la profondeur promise
- Vérifier que le CTA est cohérent avec le User Need
