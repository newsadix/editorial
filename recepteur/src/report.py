#!/usr/bin/env python3
"""
Rapport d'ingestion — conforme à §5.3 de la spec fournisseur.

Produit un JSON structuré avec le résultat de validation par bit
et un résumé global. Écrit dans processed/ à côté du lot source.
"""

import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Any, List


def build_report(
    fournisseur_id: str,
    validation_details: List[Dict],
    nsx_ids: Dict[str, str],
) -> Dict[str, Any]:
    """
    Construit le rapport de soumission.

    Args:
        fournisseur_id: ID du fournisseur
        validation_details: résultats de validate_lot().details
        nsx_ids: mapping bit_id_fournisseur → bit_id_newsadix (bits acceptés)
    """
    resultats = []
    for detail in validation_details:
        bit_id = detail["bit_id"]
        if detail["valid"]:
            statut = "accepte"
            nsx_id = nsx_ids.get(bit_id, "")
        else:
            statut = "rejete"
            nsx_id = ""

        resultats.append({
            "bit_id_fournisseur": bit_id,
            "bit_id_newsadix": nsx_id,
            "statut": statut,
            "erreurs": detail.get("erreurs", []),
            "signalements": detail.get("signalements", []),
        })

    total = len(resultats)
    acceptes = sum(1 for r in resultats if r["statut"] == "accepte")
    rejetes = total - acceptes
    signalements = sum(len(r["signalements"]) for r in resultats)

    return {
        "fournisseur_id": fournisseur_id,
        "horodatage_reception": datetime.now(timezone.utc).isoformat(),
        "resultats": resultats,
        "resume": {
            "total": total,
            "acceptes": acceptes,
            "rejetes": rejetes,
            "signalements": signalements,
            "taux_rejet": "%.1f%%" % (rejetes / total * 100) if total > 0 else "0%",
        },
    }


def save_report(report: Dict, lot_filename: str, processed_dir: Path):
    """Écrit le rapport dans processed/ avec un nom lié au lot source."""
    processed_dir.mkdir(parents=True, exist_ok=True)
    report_name = lot_filename.replace(".json", "_rapport.json")
    report_file = processed_dir / report_name
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    return report_file


def print_report(report: Dict):
    """Affiche le rapport dans la console."""
    resume = report["resume"]
    print("\n  RAPPORT D'INGESTION")
    print("  Fournisseur : %s" % report["fournisseur_id"])
    print("  Total : %d bits" % resume["total"])
    print("  Acceptés : %d" % resume["acceptes"])
    print("  Rejetés : %d" % resume["rejetes"])
    print("  Signalements : %d" % resume["signalements"])
    print("  Taux de rejet : %s" % resume["taux_rejet"])

    # Détail des rejets
    for r in report["resultats"]:
        if r["statut"] == "rejete":
            print("\n  REJETÉ : %s" % r["bit_id_fournisseur"])
            for err in r["erreurs"]:
                print("    [%s] %s" % (err["code"], err["detail"]))

    # Signalements
    sigs = [(r["bit_id_fournisseur"], s) for r in report["resultats"] for s in r["signalements"]]
    if sigs:
        print("\n  SIGNALEMENTS :")
        for bit_id, sig in sigs:
            print("    %s : %s" % (bit_id, sig))
