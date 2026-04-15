#!/usr/bin/env python3
"""
Orchestrateur d'ingestion Newsadix — lit les lots fournisseurs, valide, stocke.

Usage :
    python3 ingest.py                        # traite tout le contenu de inbox/
    python3 ingest.py --file lot.json        # traite un seul fichier
    python3 ingest.py --dry-run              # valide sans stocker
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent
RECEPTEUR_DIR = SRC_DIR.parent

sys.path.insert(0, str(SRC_DIR))

from validator import validate_lot
from store import store_bits, update_fournisseur_stats, get_known_ids
from report import build_report, save_report, print_report

INBOX_DIR = RECEPTEUR_DIR / "inbox"
PROCESSED_DIR = RECEPTEUR_DIR / "processed"
CONFIG_FILE = RECEPTEUR_DIR / "config" / "recepteur.json"


def _load_config() -> dict:
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"fournisseurs_autorises": [], "taux_rejet_alerte": 0.20, "taux_rejet_suspension": 0.50}


def _load_lot(filepath: Path) -> dict:
    """Charge et vérifie la structure d'un lot."""
    with open(filepath, "r", encoding="utf-8") as f:
        lot = json.load(f)

    if "fournisseur_id" not in lot:
        raise ValueError("Champ fournisseur_id manquant dans le lot")
    if "bits" not in lot or not isinstance(lot["bits"], list):
        raise ValueError("Champ bits manquant ou invalide dans le lot")

    return lot


def process_lot(filepath: Path, dry_run: bool = False) -> dict:
    """
    Traite un lot : validation → stockage → rapport.

    Retourne le rapport d'ingestion.
    """
    config = _load_config()
    lot = _load_lot(filepath)
    fournisseur_id = lot["fournisseur_id"]
    bits = lot["bits"]

    print("\n  Lot : %s" % filepath.name)
    print("  Fournisseur : %s" % fournisseur_id)
    print("  Bits : %d" % len(bits))

    # Vérifier que le fournisseur est autorisé
    autorises = config.get("fournisseurs_autorises", [])
    if autorises and fournisseur_id not in autorises:
        print("  REJET : fournisseur '%s' non autorisé" % fournisseur_id)
        return None

    # Récupérer les IDs déjà ingérés (pour déduplication E005)
    known_ids = get_known_ids()

    # Valider
    print("  Validation...")
    validation = validate_lot(bits, known_ids)
    print("  → Valides : %d/%d | Rejetés : %d | Signalements : %d" % (
        validation["valides"], validation["total"],
        validation["rejetes"], validation["signalements_total"],
    ))

    # Séparer bits valides / rejetés
    valid_bits = []
    nsx_ids = {}
    for i, detail in enumerate(validation["details"]):
        if detail["valid"]:
            valid_bits.append(bits[i])

    # Stocker
    if valid_bits and not dry_run:
        print("  Stockage de %d bits..." % len(valid_bits))
        stored_ids = store_bits(valid_bits, fournisseur_id)
        for bit, nsx_id in zip(valid_bits, stored_ids):
            nsx_ids[bit["id"]] = nsx_id
        print("  → IDs Newsadix : %s ... %s" % (stored_ids[0], stored_ids[-1]))

        # Mettre à jour les stats fournisseur
        update_fournisseur_stats(
            fournisseur_id,
            bits_soumis=len(bits),
            bits_acceptes=len(valid_bits),
            bits_rejetes=validation["rejetes"],
        )
    elif dry_run:
        print("  DRY RUN — stockage ignoré")

    # Rapport
    report = build_report(fournisseur_id, validation["details"], nsx_ids)
    print_report(report)

    # Archiver le lot + sauver le rapport
    if not dry_run:
        report_file = save_report(report, filepath.name, PROCESSED_DIR)
        print("\n  Rapport → %s" % report_file)

        # Déplacer le lot dans processed/
        PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
        dest = PROCESSED_DIR / filepath.name
        shutil.move(str(filepath), str(dest))
        print("  Lot archivé → %s" % dest)

    # Alerte taux de rejet
    taux = validation["rejetes"] / validation["total"] if validation["total"] > 0 else 0
    seuil_alerte = config.get("taux_rejet_alerte", 0.20)
    if taux > seuil_alerte:
        print("\n  ⚠ ALERTE : taux de rejet %.1f%% > seuil %.0f%%" % (taux * 100, seuil_alerte * 100))

    return report


def run(inbox_path: str = None, file_path: str = None, dry_run: bool = False):
    inbox = Path(inbox_path) if inbox_path else INBOX_DIR

    print("=" * 60)
    print("  Récepteur Newsadix — Ingestion de bits")
    print("  Mode : %s" % ("DRY RUN" if dry_run else "PRODUCTION"))
    print("=" * 60)

    if file_path:
        # Traiter un seul fichier
        fp = Path(file_path)
        if not fp.exists():
            print("  Fichier introuvable : %s" % fp)
            return
        process_lot(fp, dry_run=dry_run)
    else:
        # Traiter tous les fichiers dans inbox/
        if not inbox.exists():
            print("  Répertoire inbox introuvable : %s" % inbox)
            return

        lots = sorted(inbox.glob("*.json"))
        if not lots:
            print("  Aucun lot dans %s" % inbox)
            return

        print("  %d lot(s) dans %s" % (len(lots), inbox))

        for lot_file in lots:
            process_lot(lot_file, dry_run=dry_run)

    print("\n" + "=" * 60)
    print("  Ingestion terminée")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Récepteur Newsadix — ingestion de lots de bits fournisseurs"
    )
    parser.add_argument(
        "--inbox", type=str, default=None,
        help="Répertoire d'entrée (défaut : inbox/)"
    )
    parser.add_argument(
        "--file", type=str, default=None,
        help="Traiter un seul fichier lot"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Valider sans stocker"
    )
    args = parser.parse_args()

    run(inbox_path=args.inbox, file_path=args.file, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
