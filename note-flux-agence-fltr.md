# FLTR devient le premier fournisseur de contenu de Newsadix

**Date** : 15 avril 2026
**Auteur** : Damien Van Achter
**Statut** : prototype opérationnel, testé end-to-end

---

## Le constat

Le pipeline FLTR analyse environ 100 articles par jour depuis Inoreader. Moins de 5 % sont publiés sur Ghost et les réseaux sociaux. Le reste — des analyses complètes, scorées, sourcées — dort dans la base Notion. C'est un investissement éditorial non valorisé, et un problème de sobriété.

## Ce qui a été construit

FLTR alimente désormais Newsadix en **bits** : des fragments atomiques d'information, factuels, sourcés, neutres. C'est le modèle agence de presse — FLTR fournit la matière première, Newsadix l'assemble et la publie.

### La chaîne complète

```
Base Notion FLTR (articles analysés, ~100/jour)
    ↓ lecture seule — le pipeline FLTR ne change pas
Adaptateur FLTR (projets/flux-agence/)
    ↓ décomposition en bits via Claude Haiku
    ↓ neutralisation (retrait de l'angle éditorial FLTR)
    ↓ validation E001-E012
Lot JSON (3 à 7 bits par article)
    ↓ dépôt dans le récepteur Newsadix
Récepteur Newsadix (editorial/recepteur/)
    ↓ revalidation côté récepteur
    ↓ stockage + index + rapport
Bits validés prêts pour assemblage
```

### Ce qu'est un bit

Un fragment autonome : une phrase à un paragraphe, typé, sourcé, horodaté.

- **fait** : un événement documenté
- **donnée** : un chiffre avec sa source
- **contexte** : un cadrage factuel sans prise de position
- **point de vue** : une citation attribuée à une personne nommée

Chaque bit porte obligatoirement une URL source vérifiable. Aucun contenu intégral d'article n'est transmis (propriété intellectuelle).

### Ce qui est neutralisé

L'adaptateur supprime tout ce qui est propre à la ligne éditoriale FLTR : le titre éditorialisé, les pistes d'action (Gene Sharp), les signaux structurels, le vocabulaire de cadre théorique (Meadows, Senge), les adjectifs qualifiant. Il ne reste que du factuel pur, utilisable par n'importe quel média sans se sentir instrumentalisé.

## Pourquoi c'est structurant pour Newsadix

### 1. FLTR est le premier fournisseur, pas le seul

La spec fournisseur (`spec-fournisseur.md`) est agnostique. Elle ne présuppose ni pipeline, ni outil, ni framework. Demain, un journaliste freelance, un autre média ou un chercheur peut alimenter Newsadix en respectant le même contrat. FLTR a juste été le premier à l'implémenter.

### 2. Ça pose les fondations du pipeline de production

Les bits sont l'unité de base de tout le pipeline Newsadix. Les templates F1 (alerte, dépêche courte, développée, data, synthèse, angle) assemblent des bits pour produire des dépêches. Sans bits, pas d'assemblage. Le récepteur est la porte d'entrée.

### 3. Ça valide le modèle économique du flux

Si Newsadix peut ingérer des bits de fournisseurs multiples et les assembler en dépêches, c'est un flux d'agence. Ce flux peut être distribué à des médias tiers via l'API ou le MCP server (spec déjà écrite dans `flux-mcp.md`).

## Ce qui est livré

Tout est dans **https://github.com/newsadix/editorial** :

| Composant | Fichiers |
|---|---|
| Spec fournisseur (contrat d'interface) | `spec-fournisseur.md` |
| Schéma du bit (format pivot) | `schema-bit.md` |
| Récepteur (code Python) | `recepteur/src/` (4 modules) |
| Templates (18) | `templates/` |
| Skills éditoriaux (21) | `skills-export/` |
| Taxonomie, pipeline, user needs, pennmap | racine du repo |

Côté FLTR, l'adaptateur est dans `projets/flux-agence/` — séparé du pipeline existant, aucun impact.

## Ce qui reste à faire

1. **Lancer des lots réels** et itérer sur la qualité des bits
2. **Construire le moteur d'assemblage** qui consomme les bits pour produire des dépêches (templates F1)
3. **Exposer le MCP server** quand le format est stabilisé
4. **Brancher d'autres fournisseurs** — la spec est prête

## Test

Sur l'iMac :

```bash
cd ~/GitHub/FLTR/projets/flux-agence
python3 src/adapter_fltr_newsadix.py --limit 5 --dry-run
```

Résultat du premier test : 5 articles → 29 bits, 29/29 valides, 0 rejet.
