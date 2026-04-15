# Socle éditorial Newsadix

Tout ce qui définit le fonctionnement éditorial de Newsadix : le schéma du bit, la taxonomie, le pipeline, les templates, les skills, la spec fournisseur et le récepteur d'ingestion.

## Structure

```
editorial/
├── schema-bit.md              ← Schéma JSON du bit (unité atomique) et de l'assemblage
├── spec-fournisseur.md        ← Contrat d'interface fournisseur (validation, livraison, PI)
├── taxonomie-editoriale.md    ← 12 piliers thématiques + sous-thèmes
├── pipeline-production.md     ← Pipeline Sources → Bits → Assemblage → Distribution
├── user-needs.md              ← 8 besoins utilisateur (User Needs 2.0)
├── pennmap.md                 ← Mesure de neutralité éditoriale
├── templates/                 ← 18 templates (F1 production + F2 signé + F3 distribution)
│   ├── specs/                 ← Spécifications JSON exécutables par template
│   └── *.md                   ← Documentation par template
├── skills-export/             ← Skills éditoriaux FLTR exportés pour les agents
│   ├── charte-editoriale.md
│   ├── anti-slop.md
│   ├── fact-check-workflow.md
│   └── ...
└── recepteur/                 ← Récepteur d'ingestion batch des bits fournisseurs
    ├── src/
    │   ├── ingest.py          ← Orchestrateur CLI
    │   ├── validator.py       ← Validation E001-E012
    │   ├── store.py           ← Stockage bits + index
    │   └── report.py          ← Rapport de soumission
    └── config/
        └── recepteur.json     ← Fournisseurs autorisés, seuils de rejet
```

## Comment ça s'articule

1. Un **fournisseur** (FLTR, journaliste, média) produit des **bits** conformes à `spec-fournisseur.md`
2. Le **récepteur** (`recepteur/`) ingère, valide (`schema-bit.md`), stocke
3. Les bits validés sont classés selon la **taxonomie** (`taxonomie-editoriale.md`)
4. Les **templates** (`templates/`) assemblent les bits en dépêches publiables
5. Les **skills** (`skills-export/`) alimentent les agents IA qui produisent et vérifient

## Récepteur — usage

```bash
cd recepteur
# Déposer un lot JSON fournisseur dans inbox/
python3 src/ingest.py              # traite tout inbox/
python3 src/ingest.py --dry-run    # valide sans stocker
python3 src/ingest.py --file lot.json  # un seul fichier
```

## Premier fournisseur

FLTR (Tech & Démocratie) — `fournisseur_id: fltr-001`. Adaptateur dans le repo FLTR (`projets/flux-agence/`), lit la base Notion en read-only, produit des lots de bits conformes à la spec.
