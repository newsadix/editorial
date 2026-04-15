# Template : Briefing audio

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-BRIEFING-AUDIO` |
| **User Need** | `update_me` |
| **Mode d'engagement** | Subscribe, Scroll |
| **Durée** | 2-5 minutes |
| **Signé** | Non (voix synthétique identifiée comme telle) |
| **Supervision** | Phase 1 : écoute humaine. Phase 3 : automatique |

## Principe

Le briefing audio est une version parlée des contenus publiés. Il sert les moments de consommation passive (trajet, cuisine, sport) et le mode d'engagement Subscribe. C'est un dérivé pur : le script est généré automatiquement à partir des bits et dépêches existants, puis converti en audio par TTS (Text-to-Speech).

## Déclencheur

| Variante | Déclencheur | Durée cible |
|----------|-------------|-------------|
| **Briefing matinal** | Calendaire, 6h30 | 3-5 min |
| **Flash** | Après publication d'une alerte de priorité maximale | 30-60 sec |
| **Briefing thématique** | Hebdomadaire, par pilier (si matière suffisante) | 2-4 min |
| **Lecture de dépêche** | Toute dépêche développée, d'angle ou data publiée | 1-3 min |

## Composition

### Briefing matinal (format principal)

Le script est assemblé à partir des mêmes items que la newsletter matinale, mais adapté à l'oral :

```
SEGMENT 1 — OUVERTURE (5-10 sec)
  « Newsadix, [jour] [date], [heure]. 
    [N] sujets à retenir ce matin. »

SEGMENT 2 — L'ESSENTIEL (2-4 min)
  4-6 items, chacun :
  - Transition : « [Pilier]. » (ex. « Économie. »)
  - Fait principal : 1-2 phrases
  - Contexte minimal : 1 phrase (si dépêche développée disponible)
  - Pause : 0,5 sec entre items

SEGMENT 3 — EN CHIFFRES (30-45 sec, optionnel)
  1-2 données clés avec source.
  « En chiffres : [chiffre]. [explication en 1 phrase]. 
    Source : [source]. »

SEGMENT 4 — FERMETURE (5-10 sec)
  « C'était le briefing Newsadix. 
    Retrouvez les dépêches complètes sur newsadix.com. »
```

### Flash (après alerte prioritaire)

```
« Newsadix, flash info. 
  [Fait principal de l'alerte]. 
  Source : [source]. 
  Nous reviendrons sur ce sujet. »
```

Durée : 15-30 secondes.

### Lecture de dépêche

Lecture intégrale du texte de sortie du template source, avec :
- Ajout d'une introduction : « Dépêche Newsadix, [pilier], [date]. »
- Ajout d'une fermeture : « Source(s) : [sources]. »
- Rythme adapté à l'oral (pauses entre les blocs)

## Script → Audio : règles de conversion

| Aspect | Règle |
|--------|-------|
| Voix | TTS de qualité (type ElevenLabs, OpenAI TTS). Une seule voix identifiée comme « la voix Newsadix » |
| Débit | 150-160 mots/minute (rythme info radio) |
| Pauses | 0,5 sec entre items, 1 sec entre segments |
| Prononciation | Dictionnaire de prononciation pour noms propres, sigles, termes techniques |
| Transparence | La voix synthétique est identifiée comme telle (politique IA de Newsadix) |

### Adaptation texte → oral

Le texte écrit n'est pas identique au script parlé. Adaptations automatiques :

| Écrit | Oral |
|-------|------|
| Parenthèses (Source : BCE) | « Source : BCE » en fin de segment |
| Abréviations (T1 2026) | « premier trimestre 2026 » |
| Pourcentages (7,3 %) | « sept virgule trois pour cent » |
| Sigles nouveaux | Développés à la première occurrence |
| Tableaux de données | Convertis en phrases comparatives |
| Liens URL | Supprimés (pas prononçables) |

## Contrôles qualité automatisés

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Durée | 2-5 min (briefing), 15-30 sec (flash) | Ajustement du nombre d'items |
| Nombre d'items | 4-6 (briefing matinal) | Sélection si excès, alerte si insuffisant |
| Prononciation | Noms propres dans le dictionnaire | Ajout au dictionnaire + alerte |
| Qualité audio | Pas de glitch, coupure ou artefact TTS | Régénération automatique |
| Transparence | Mention « voix générée par intelligence artificielle » | Vérification systématique |
| Cohérence avec newsletter | Mêmes items que la newsletter du même créneau | Vérification croisée |

## Distribution

| Canal | Format | Délai |
|-------|--------|-------|
| Site web (lecteur intégré) | MP3 / AAC | Immédiat |
| App (si existante) | Lecture native | Immédiat |
| Plateformes podcast | RSS feed (Apple Podcasts, Spotify, etc.) | < 15 min |
| Réseaux sociaux | Extrait 30 sec + lien | < 30 min |

### Format pour réseaux sociaux

L'audio seul ne fonctionne pas sur les plateformes visuelles. Pour Instagram/TikTok, le briefing audio est accompagné d'un support visuel :

```
Fond : couleur pilier animée (wave audio ou texte défilant)
Texte : les faits clés s'affichent à l'écran en synchro avec l'audio
Sous-titres : systématiques (accessibilité + consommation sans son)
```

Ce support visuel est généré automatiquement par le moteur graphique (pipeline Skan).

## Métriques

| Métrique | Usage |
|----------|-------|
| Nombre d'écoutes | Volume d'audience |
| Taux de complétion | Le briefing maintient-il l'attention jusqu'au bout ? |
| Moment d'écoute | Quand les gens écoutent (matin, midi, soir) |
| Abonnés podcast | Base installée |

---

Version : 0.1 | Date : 2026-04-14
