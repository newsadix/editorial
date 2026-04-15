#!/usr/bin/env python3
"""
Validateur de bits côté récepteur Newsadix.

Implémentation autonome des contrôles E001-E012 de la spec fournisseur.
Aucune dépendance vers le code fournisseur (FLTR ou autre).

Réf. : editorial/spec-fournisseur.md §5
"""

import re
from typing import Dict, Any, Set, List

# Enums canoniques (réf. : editorial/spec-fournisseur.md Annexe A)
VALID_TYPES = {"fait", "donnee", "contexte", "point_de_vue"}

VALID_PILIERS = {
    "politique_institutions", "societe_dynamiques_sociales",
    "economie_entreprises_travail", "technologie_numerique",
    "sciences_sante", "environnement_energie", "monde", "sport",
    "culture_arts_medias", "mode_de_vie", "idees_pensee_decryptage",
    "divertissement_contenus_engageants",
}

VALID_GEO = {"france", "france_monde", "monde"}

VALID_USER_NEEDS = {
    "update_me", "keep_me_engaged", "help_me", "connect_me",
    "educate_me", "give_me_perspective", "divert_me", "inspire_me",
}

VALID_SOURCE_TYPES = {
    "source_primaire", "source_secondaire", "document_officiel",
    "donnees_publiques", "declaration", "temoignage", "agence_presse",
}

VALID_AUTEUR_TYPES = {"humain", "agent", "hybride"}

SOURCE_TYPES_SANS_URL = {"declaration", "temoignage"}

# Acteurs vagues à signaler
ACTEURS_VAGUES = {
    "experts", "gouvernements", "gouvernement", "acteurs locaux",
    "sources", "analystes", "observateurs", "spécialistes",
}

BIT_ID_PATTERN = re.compile(r'^bit-\d{4}-\d{2}-\d{2}-\d{3,}$')
ISO_8601_PATTERN = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}')


def validate_bit(bit: Dict[str, Any], known_ids: Set[str] = None) -> Dict[str, Any]:
    """
    Valide un bit contre les contrôles E001-E012.

    Retourne :
    {
        "valid": bool,
        "erreurs": [{"code": "EXXX", "detail": "..."}],
        "signalements": ["..."]
    }
    """
    erreurs = []
    signalements = []
    if known_ids is None:
        known_ids = set()

    # --- E001 : champs obligatoires ---
    required = [
        "id", "type", "contenu", "sources", "auteur",
        "horodatage_creation", "geo", "pilier", "user_need", "statut",
    ]
    missing = [f for f in required if f not in bit or bit[f] is None]
    if missing:
        erreurs.append({"code": "E001", "detail": "Champs manquants : " + ", ".join(missing)})
        return {"valid": False, "erreurs": erreurs, "signalements": signalements}

    contenu = bit.get("contenu", "")
    bit_type = bit.get("type", "")
    sources = bit.get("sources", [])

    # --- E002 : sources non vide ---
    if not sources or not isinstance(sources, list) or len(sources) == 0:
        erreurs.append({"code": "E002", "detail": "sources[] est vide"})

    # --- E003 : type cohérent ---
    if bit_type not in VALID_TYPES:
        erreurs.append({"code": "E003", "detail": "Type inconnu : " + str(bit_type)})
    elif bit_type == "donnee" and not re.search(r'\d', contenu):
        erreurs.append({"code": "E003", "detail": "Bit donnee sans chiffre dans le contenu"})
    elif bit_type == "point_de_vue" and not bit.get("acteurs"):
        erreurs.append({"code": "E003", "detail": "Bit point_de_vue sans acteur attribué"})

    # --- E004 : longueur contenu ---
    if len(contenu) < 1:
        erreurs.append({"code": "E004", "detail": "Contenu vide"})
    elif len(contenu) > 2000:
        erreurs.append({"code": "E004", "detail": "Contenu : %d car. (max 2000)" % len(contenu)})

    # --- E005 : ID unique ---
    bit_id = bit.get("id", "")
    if not BIT_ID_PATTERN.match(bit_id):
        erreurs.append({"code": "E005", "detail": "Format ID invalide : " + str(bit_id)})
    elif bit_id in known_ids:
        erreurs.append({"code": "E005", "detail": "ID doublon : " + bit_id})

    # --- E006 : horodatage valide ---
    horodatage = bit.get("horodatage_creation", "")
    if not horodatage or not ISO_8601_PATTERN.match(str(horodatage)):
        erreurs.append({"code": "E006", "detail": "horodatage_creation invalide"})

    # --- E007 : pilier valide ---
    if bit.get("pilier") not in VALID_PILIERS:
        erreurs.append({"code": "E007", "detail": "Pilier inconnu : " + str(bit.get("pilier"))})

    # --- E008 : geo valide ---
    if bit.get("geo") not in VALID_GEO:
        erreurs.append({"code": "E008", "detail": "Geo inconnu : " + str(bit.get("geo"))})

    # --- E009 : user_need valide ---
    user_need = bit.get("user_need", {})
    primaire = user_need.get("primaire", "") if isinstance(user_need, dict) else ""
    if primaire not in VALID_USER_NEEDS:
        erreurs.append({"code": "E009", "detail": "User need inconnu : " + str(primaire)})

    # --- E010 : validateur requis ---
    auteur = bit.get("auteur", {})
    auteur_type = auteur.get("type", "")
    if auteur_type not in VALID_AUTEUR_TYPES:
        erreurs.append({"code": "E010", "detail": "Type auteur inconnu : " + str(auteur_type)})
    elif auteur_type in ("agent", "hybride") and not auteur.get("valide_par"):
        erreurs.append({"code": "E010", "detail": "valide_par requis pour auteur " + auteur_type})

    # --- E011 : URL source requise ---
    for src in sources:
        src_type = src.get("type_source", "")
        if src_type not in SOURCE_TYPES_SANS_URL and not src.get("url"):
            erreurs.append({
                "code": "E011",
                "detail": "URL manquante pour source '%s'" % src.get("nom", "?"),
            })

    # --- E012 : propriété intellectuelle (heuristique) ---
    if len(contenu) > 800:
        signalements.append("Contenu > 800 car. — vérifier absence de copie verbatim")

    # --- Contrôles non bloquants ---

    # Acteurs vagues
    for acteur in bit.get("acteurs", []):
        nom = (acteur.get("nom") or "").lower().strip()
        if nom in ACTEURS_VAGUES:
            signalements.append("Acteur vague détecté : '%s'" % acteur.get("nom"))

    return {
        "valid": len(erreurs) == 0,
        "erreurs": erreurs,
        "signalements": signalements,
    }


def validate_lot(bits: List[Dict], known_ids: Set[str] = None) -> Dict[str, Any]:
    """Valide un lot complet. Retourne le rapport agrégé."""
    if known_ids is None:
        known_ids = set()

    lot_ids = set()
    details = []

    for bit in bits:
        # Combiner les IDs connus (index) + ceux du lot en cours
        combined = known_ids | lot_ids
        result = validate_bit(bit, combined)
        bit_id = bit.get("id", "???")
        lot_ids.add(bit_id)
        details.append({"bit_id": bit_id, **result})

    valides = sum(1 for d in details if d["valid"])
    signalements_total = sum(len(d["signalements"]) for d in details)

    return {
        "total": len(bits),
        "valides": valides,
        "rejetes": len(bits) - valides,
        "signalements_total": signalements_total,
        "details": details,
    }
