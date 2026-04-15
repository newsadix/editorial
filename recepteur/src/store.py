#!/usr/bin/env python3
"""
Stockage des bits validés — fichiers JSON + index.

Chaque bit est stocké dans data/bits/{id}.json.
L'index global data/index.json permet les requêtes rapides.
Le registre fournisseur data/fournisseurs/{id}.json suit les stats.
"""

import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Any, List, Set

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
BITS_DIR = DATA_DIR / "bits"
INDEX_FILE = DATA_DIR / "index.json"
FOURNISSEURS_DIR = DATA_DIR / "fournisseurs"


def _ensure_dirs():
    BITS_DIR.mkdir(parents=True, exist_ok=True)
    FOURNISSEURS_DIR.mkdir(parents=True, exist_ok=True)


def load_index() -> List[Dict]:
    """Charge l'index global."""
    if INDEX_FILE.exists():
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def _save_index(index: List[Dict]):
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)


def get_known_ids() -> Set[str]:
    """Retourne l'ensemble des IDs fournisseur déjà ingérés."""
    index = load_index()
    return {entry["bit_id_fournisseur"] for entry in index}


def _next_newsadix_id(index: List[Dict]) -> str:
    """Génère le prochain ID Newsadix (nsx-YYYY-MM-DD-NNN)."""
    today = datetime.now().strftime("%Y-%m-%d")
    prefix = "nsx-" + today + "-"
    existing = [e["bit_id_newsadix"] for e in index if e["bit_id_newsadix"].startswith(prefix)]
    if existing:
        max_seq = max(int(eid.split("-")[-1]) for eid in existing)
        return "%s%03d" % (prefix, max_seq + 1)
    return prefix + "001"


def store_bit(bit: Dict[str, Any], fournisseur_id: str) -> str:
    """
    Stocke un bit validé. Retourne le bit_id_newsadix attribué.

    Le bit est enrichi avec les métadonnées d'ingestion.
    """
    _ensure_dirs()
    index = load_index()

    nsx_id = _next_newsadix_id(index)
    now = datetime.now(timezone.utc).isoformat()

    # Construire le bit stocké
    stored = {
        "bit_id_newsadix": nsx_id,
        "bit_id_fournisseur": bit["id"],
        "fournisseur_id": fournisseur_id,
        "horodatage_ingestion": now,
        "statut": "valide",
    }
    # Copier tous les champs du bit original (sauf id et statut qu'on surcharge)
    for key, value in bit.items():
        if key not in ("id", "statut"):
            stored[key] = value

    # Écrire le fichier bit
    bit_file = BITS_DIR / ("%s.json" % nsx_id)
    with open(bit_file, "w", encoding="utf-8") as f:
        json.dump(stored, f, indent=2, ensure_ascii=False)

    # Mettre à jour l'index
    index.append({
        "bit_id_newsadix": nsx_id,
        "bit_id_fournisseur": bit["id"],
        "fournisseur_id": fournisseur_id,
        "type": bit.get("type"),
        "pilier": bit.get("pilier"),
        "geo": bit.get("geo"),
        "statut": "valide",
        "horodatage_creation": bit.get("horodatage_creation"),
        "horodatage_ingestion": now,
    })
    _save_index(index)

    return nsx_id


def store_bits(bits: List[Dict], fournisseur_id: str) -> List[str]:
    """Stocke un lot de bits. Retourne la liste des IDs Newsadix attribués."""
    _ensure_dirs()
    index = load_index()
    now = datetime.now(timezone.utc).isoformat()
    nsx_ids = []

    for bit in bits:
        nsx_id = _next_newsadix_id(index)

        stored = {
            "bit_id_newsadix": nsx_id,
            "bit_id_fournisseur": bit["id"],
            "fournisseur_id": fournisseur_id,
            "horodatage_ingestion": now,
            "statut": "valide",
        }
        for key, value in bit.items():
            if key not in ("id", "statut"):
                stored[key] = value

        bit_file = BITS_DIR / ("%s.json" % nsx_id)
        with open(bit_file, "w", encoding="utf-8") as f:
            json.dump(stored, f, indent=2, ensure_ascii=False)

        index.append({
            "bit_id_newsadix": nsx_id,
            "bit_id_fournisseur": bit["id"],
            "fournisseur_id": fournisseur_id,
            "type": bit.get("type"),
            "pilier": bit.get("pilier"),
            "geo": bit.get("geo"),
            "statut": "valide",
            "horodatage_creation": bit.get("horodatage_creation"),
            "horodatage_ingestion": now,
        })
        nsx_ids.append(nsx_id)

    _save_index(index)
    return nsx_ids


def update_fournisseur_stats(
    fournisseur_id: str,
    bits_soumis: int,
    bits_acceptes: int,
    bits_rejetes: int,
):
    """Met à jour les statistiques cumulées du fournisseur."""
    _ensure_dirs()
    fournisseur_file = FOURNISSEURS_DIR / ("%s.json" % fournisseur_id)

    if fournisseur_file.exists():
        with open(fournisseur_file, "r", encoding="utf-8") as f:
            profile = json.load(f)
    else:
        profile = {
            "fournisseur_id": fournisseur_id,
            "date_enregistrement": datetime.now().strftime("%Y-%m-%d"),
            "stats": {
                "lots_recus": 0,
                "bits_soumis": 0,
                "bits_acceptes": 0,
                "bits_rejetes": 0,
            },
        }

    stats = profile["stats"]
    stats["lots_recus"] = stats.get("lots_recus", 0) + 1
    stats["bits_soumis"] = stats.get("bits_soumis", 0) + bits_soumis
    stats["bits_acceptes"] = stats.get("bits_acceptes", 0) + bits_acceptes
    stats["bits_rejetes"] = stats.get("bits_rejetes", 0) + bits_rejetes

    total = stats["bits_soumis"]
    if total > 0:
        stats["taux_rejet_cumule"] = round(stats["bits_rejetes"] / total, 4)

    with open(fournisseur_file, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2, ensure_ascii=False)
