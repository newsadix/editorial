# Skills Newsadix — Export depuis FLTR

Date d'export : 2026-04-08
Source : repo FLTR (pipeline éditorial de Damien Van Achter)
Total : 20 skills, ~5 000 lignes

---

## Skills fondamentaux (charger systématiquement)

| Skill | Lignes | Description | Source FLTR |
|-------|--------|-------------|-------------|
| [charte-editoriale.md](charte-editoriale.md) | 417 | Charte éditoriale fondatrice — posture, ton, factualité, anti-IA-speak, vérification. Skill cardinal. | socle-commun.md v2.3 + editorial-feedback.md |
| [analyse-systemique.md](analyse-systemique.md) | 190 | Méthodologie d'analyse systémique — dynamiques de pouvoir, boucles de rétroaction, points de levier, patterns récurrents. | grille-analyse.md (Meadows, Senge, Sharp) |
| [scoring-editorial.md](scoring-editorial.md) | 129 | Scoring bidimensionnel paramétrable — pertinence (0-10) + documentaire (0-10) + matrice de stockage. | scoring.md |
| [garde-fous-factualite.md](garde-fous-factualite.md) | 147 | Garde-fous de vérification factuelle — citations, chiffres, scan post-génération. BLOQUANT. | garde-fous-factualite.md + socle-commun.md |
| [anti-slop.md](anti-slop.md) | 182 | Détection et élimination du slop IA — dictionnaire FR/EN de formulations à proscrire. | socle-commun.md + editorial-feedback.md |
| [user-needs.md](user-needs.md) | 170 | Boussole des besoins — 8 besoins informationnels, routing vers plateformes, value gap. | user-needs.md |
| [format-json-pivot.md](format-json-pivot.md) | 430 | Format JSON pivot — contrat d'interface entre agents éditoriaux. | format-json.md + format-json-light.md |

## Skills de format (charger selon la plateforme cible)

| Skill | Lignes | Description | Source FLTR |
|-------|--------|-------------|-------------|
| [format-linkedin.md](format-linkedin.md) | 226 | LinkedIn — 3 formats (A décryptage, B récit, C questionnement). | formats/linkedin.md |
| [format-bluesky.md](format-bluesky.md) | 123 | Bluesky — post analytique 300 car. max. | formats/bluesky.md |
| [format-mastodon.md](format-mastodon.md) | 130 | Mastodon/Fediverse — toot analytique 500 car. | formats/mastodon.md |
| [format-facebook.md](format-facebook.md) | 158 | Facebook — post conversationnel 300-400 mots. | formats/facebook.md |
| [format-instagram.md](format-instagram.md) | 279 | Instagram — carrousel 10 slides + légende + Reel. | formats/instagram.md |
| [format-newsletter.md](format-newsletter.md) | 242 | Newsletter hebdomadaire analytique. | formats/newsletter.md |
| [format-article-web.md](format-article-web.md) | 405 | Article web — 3 templates (Perspective, Éducation, Signal). | formats/ghost-article.md |
| [format-synthese.md](format-synthese.md) | 184 | Synthèse multi-articles (2-5 sources). | formats/synthese.md |
| [format-analyse-croisee.md](format-analyse-croisee.md) | 512 | Analyse croisée multi-sources — publication web + JSON étendu. | formats/cross-analysis.md + format-json-cross.md |

## Skills de contrôle qualité (charger en pré/post-production)

| Skill | Lignes | Description | Source FLTR |
|-------|--------|-------------|-------------|
| [pre-production-checklist.md](pre-production-checklist.md) | 196 | Checklist bloquante pré-production + protocole hors pipeline (inventaire de claims). | editorial-pre-production.md + article-hors-pipeline.md |
| [quality-checks.md](quality-checks.md) | 192 | Contrôles qualité post-rédaction — AI slop, AP Style, sources, juridique, accessibilité. | quality-checks.md |
| [fact-check-workflow.md](fact-check-workflow.md) | 434 | Workflow structuré de fact-checking en 7 étapes. | fact-check-workflow/SKILL.md |
| [source-verification.md](source-verification.md) | 374 | Méthodologie SIFT de vérification de sources et contenus numériques. | source-verification/SKILL.md |

---

## Notes d'intégration

### Hiérarchie de chargement

```
1. charte-editoriale.md          ← TOUJOURS en premier (skill cardinal)
2. analyse-systemique.md         ← si analyse approfondie requise
3. scoring-editorial.md          ← si tri/sélection d'articles
4. user-needs.md                 ← si routing vers plateformes
5. garde-fous-factualite.md      ← TOUJOURS avant production
6. pre-production-checklist.md   ← BLOQUANT avant toute rédaction
7. [format-*.md]                 ← selon la plateforme cible
8. quality-checks.md             ← après rédaction
```

### Autonomie

- Ces skills sont **autonomes** et ne dépendent pas du repo FLTR
- Les références internes sont des noms de skills du même dossier (pas des chemins de fichiers)
- Aucune dépendance technique à Ghost, Notion, Inoreader ou tout autre outil

### Paramétrage

- Le skill `scoring-editorial.md` est **paramétrable** : Newsadix peut y injecter ses propres critères de pertinence en remplaçant les dimensions thématiques
- Le skill `format-json-pivot.md` est le **contrat d'interface** entre les agents : les champs `piliers` et `dimensions_touchees` peuvent être remplacés par les dimensions propres au média
- Les skills de format contiennent des **placeholders** (`[URL_SITE]`, `[NOM_MEDIA]`, `[RESEAUX_SOCIAUX_LIENS]`, etc.) à remplacer par les valeurs Newsadix

### Cadres théoriques

Les cadres de Meadows, Senge et Sharp sont **inclus intégralement** dans `analyse-systemique.md` comme outils analytiques, avec leurs auteurs cités en références bibliographiques. Ils structurent l'analyse en coulisses mais ne doivent **jamais apparaître** dans les textes publiés (règle explicitée dans `charte-editoriale.md`).

### Ce qui n'a PAS été exporté

| Fichier FLTR | Raison |
|-------------|--------|
| image-style.md | Spécifique à l'identité visuelle FLTR (palette par pilier, prompts Notion) |
| instructions.md (veille-5piliers) | Technique — pipeline Inoreader/Notion/Ghost |
| fltr/SKILL.md | Méta-skill de coordination FLTR, remplacé par la hiérarchie de chargement ci-dessus |
| editorial-workflow SKILL.md | Workflow de rédaction générique en anglais, pas spécifique au pipeline éditorial |
| newsroom-style SKILL.md | AP Style anglais — pertinent uniquement pour les contenus en anglais |
| story-pitch SKILL.md | Pitchs en anglais, format US — nécessiterait une adaptation FR/BE complète |
| interview-transcription SKILL.md | Technique — workflows de transcription, code Python, sans contenu éditorial transposable |
