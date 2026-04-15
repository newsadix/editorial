# Socle éditorial Newsadix

Définitions structurelles du pipeline Newsadix : le schéma du bit, la taxonomie, le pipeline de production, le framework user needs, la spec fournisseur et le récepteur d'ingestion.

## Documents

| Fichier | Contenu |
|---------|---------|
| `schema-bit.md` | Schéma JSON canonique du bit (unité atomique d'information) et de l'assemblage |
| `spec-fournisseur.md` | Contrat d'interface pour tout fournisseur de bits (format, validation, modes de livraison, propriété intellectuelle) |
| `taxonomie-editoriale.md` | Les 12 piliers thématiques + sous-thèmes + métadonnées transverses |
| `pipeline-production.md` | Pipeline complet : Sources → Bits → Validation → Assemblage (F1) → Distribution (F3) |
| `user-needs.md` | Les 8 besoins utilisateur (User Needs 2.0) et leur routage vers les canaux |
| `pennmap.md` | Mesure de neutralité éditoriale (méthodologie PennMAP) |

## Récepteur

`recepteur/` contient le code d'ingestion batch des lots de bits fournisseurs.

```
recepteur/
├── src/
│   ├── ingest.py       ← Orchestrateur (CLI : --dry-run, --file)
│   ├── validator.py    ← Validation E001-E012
│   ├── store.py        ← Stockage fichiers JSON + index
│   └── report.py       ← Rapport d'ingestion (conforme §5.3 spec fournisseur)
└── config/
    └── recepteur.json  ← Fournisseurs autorisés, seuils de rejet
```

### Usage

```bash
# Déposer un lot JSON dans recepteur/inbox/
# Puis :
cd recepteur
python3 src/ingest.py              # traite tout inbox/
python3 src/ingest.py --dry-run    # valide sans stocker
python3 src/ingest.py --file lot.json  # un seul fichier
```

Les bits validés sont stockés dans `recepteur/data/bits/`, indexés dans `recepteur/data/index.json`.

## Relation avec les autres repos

- **[templates](https://github.com/newsadix/templates)** : les 18 templates (F1 + F2 + F3) qui assemblent les bits en dépêches
- **[skills-export-davanac](https://github.com/newsadix/skills-export-davanac)** : les skills éditoriaux FLTR exportés pour les agents
- **[newsadix-mono](https://github.com/newsadix/newsadix-mono)** : l'infrastructure technique (API, CMS, web)

## Premier fournisseur

FLTR (Tech & Démocratie) — `fournisseur_id: fltr-001`. Adaptateur dans le repo FLTR (`projets/flux-agence/`), lit la base Notion en read-only, produit des lots de bits conformes à `spec-fournisseur.md`.
