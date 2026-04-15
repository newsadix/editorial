# Schéma JSON canonique du bit

## Contexte

Ce document formalise le schéma JSON du bit, l'unité atomique d'information de Newsadix. Il précise et étend le schéma esquissé dans `fondation/architecture-information-plexee.md` en ajoutant les champs nécessaires au fonctionnement des templates de production (Famille 1) et de distribution (Famille 3).

Ce schéma est le **contrat d'interface** entre tous les composants du pipeline : agents de veille, agent de plexage, templates d'assemblage, flux MCP, moteur graphique, agent conversationnel.

---

## 1. Schéma complet

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Bit Newsadix",
  "description": "Unité atomique d'information — fragment sourcé, typé, horodaté, connectable",
  "type": "object",
  "required": [
    "id",
    "type",
    "contenu",
    "sources",
    "auteur",
    "horodatage_creation",
    "geo",
    "pilier",
    "user_need",
    "statut"
  ],
  "properties": {

    "id": {
      "type": "string",
      "pattern": "^bit-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{3,}$",
      "description": "Identifiant unique. Format : bit-YYYY-MM-DD-NNN",
      "examples": ["bit-2026-04-14-001"]
    },

    "type": {
      "type": "string",
      "enum": ["donnee", "fait", "contexte", "point_de_vue"],
      "description": "Catégorie du bit selon la typologie Newsadix"
    },

    "contenu": {
      "type": "string",
      "minLength": 1,
      "maxLength": 2000,
      "description": "Texte du fragment. 1 phrase à 1 paragraphe court"
    },

    "sources": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["nom", "type_source"],
        "properties": {
          "nom": {
            "type": "string",
            "description": "Nom de la source (organisme, personne, publication)"
          },
          "url": {
            "type": "string",
            "format": "uri",
            "description": "Lien vers la source primaire (si disponible)"
          },
          "type_source": {
            "type": "string",
            "enum": [
              "source_primaire",
              "source_secondaire",
              "document_officiel",
              "donnees_publiques",
              "declaration",
              "temoignage",
              "agence_presse"
            ],
            "description": "Nature de la source"
          },
          "date_acces": {
            "type": "string",
            "format": "date-time",
            "description": "Date à laquelle la source a été consultée"
          }
        }
      }
    },

    "auteur": {
      "type": "object",
      "required": ["type", "id"],
      "properties": {
        "type": {
          "type": "string",
          "enum": ["agent", "humain", "hybride"],
          "description": "agent = IA, humain = journaliste, hybride = IA + correction humaine"
        },
        "id": {
          "type": "string",
          "description": "Identifiant de l'agent ou du journaliste"
        },
        "valide_par": {
          "type": "string",
          "description": "Identifiant du validateur humain. Obligatoire si type = agent ou hybride"
        }
      }
    },

    "horodatage_creation": {
      "type": "string",
      "format": "date-time",
      "description": "Date/heure de création du bit (ISO 8601)"
    },

    "horodatage_evenement": {
      "type": "string",
      "format": "date-time",
      "description": "Date/heure de l'événement décrit (si différent de la création). Pour les bits fait et donnée"
    },

    "horodatage_publication": {
      "type": "string",
      "format": "date-time",
      "description": "Date/heure de la première publication"
    },

    "geo": {
      "type": "string",
      "enum": ["france", "france_monde", "monde"],
      "description": "Périmètre géographique, aligné sur la taxonomie éditoriale"
    },

    "pilier": {
      "type": "string",
      "enum": [
        "politique_institutions",
        "societe_dynamiques_sociales",
        "economie_entreprises_travail",
        "technologie_numerique",
        "sciences_sante",
        "environnement_energie",
        "monde",
        "sport",
        "culture_arts_medias",
        "mode_de_vie",
        "idees_pensee_decryptage",
        "divertissement_contenus_engageants"
      ],
      "description": "Pilier taxonomique (1 à 12). Réf. editorial/taxonomie-editoriale.md"
    },

    "sous_theme": {
      "type": "string",
      "description": "Sous-thème du pilier (ex. : 'intelligence_artificielle' sous 'technologie_numerique')"
    },

    "user_need": {
      "type": "object",
      "required": ["primaire"],
      "properties": {
        "primaire": {
          "type": "string",
          "enum": [
            "update_me",
            "keep_me_engaged",
            "help_me",
            "connect_me",
            "educate_me",
            "give_me_perspective",
            "divert_me",
            "inspire_me"
          ],
          "description": "Besoin utilisateur principal adressé par ce bit"
        },
        "secondaire": {
          "type": "array",
          "maxItems": 2,
          "items": {
            "type": "string",
            "enum": [
              "update_me",
              "keep_me_engaged",
              "help_me",
              "connect_me",
              "educate_me",
              "give_me_perspective",
              "divert_me",
              "inspire_me"
            ]
          },
          "description": "0 à 2 besoins secondaires"
        }
      }
    },

    "relations": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["type", "cible"],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "met_a_jour",
              "contextualise",
              "contredit",
              "illustre",
              "meme_sujet",
              "meme_acteur",
              "consequence"
            ],
            "description": "Type de relation sémantique"
          },
          "cible": {
            "type": "string",
            "description": "ID du bit cible"
          },
          "direction": {
            "type": "string",
            "enum": ["sortante", "entrante"],
            "description": "Sens de la relation. Sortante = ce bit agit sur la cible. Entrante = la cible agit sur ce bit"
          },
          "confiance": {
            "type": "number",
            "minimum": 0,
            "maximum": 1,
            "description": "Score de confiance de la relation (0-1). 1 = validé humain, < 1 = suggestion agent"
          }
        }
      },
      "description": "Connexions vers d'autres bits. Cf. architecture-information-plexee.md §3"
    },

    "statut": {
      "type": "string",
      "enum": ["brouillon", "valide", "publie", "archive", "corrige"],
      "description": "État dans le cycle de vie"
    },

    "version": {
      "type": "integer",
      "minimum": 1,
      "description": "Numéro de version. Incrémenté à chaque modification post-publication"
    },

    "correction": {
      "type": "object",
      "properties": {
        "est_correction": {
          "type": "boolean",
          "description": "true si ce bit a été corrigé après publication"
        },
        "detail": {
          "type": "string",
          "description": "Description de la correction"
        },
        "horodatage": {
          "type": "string",
          "format": "date-time",
          "description": "Date/heure de la correction"
        }
      }
    },

    "templates_utilise_par": {
      "type": "array",
      "items": {
        "type": "string",
        "description": "ID du template (TPL-ALERTE, TPL-DEPECHE-COURTE, etc.)"
      },
      "description": "Templates Famille 1 dans lesquels ce bit est assemblé"
    },

    "formats_generes": {
      "type": "array",
      "items": {
        "type": "string",
        "description": "ID du dérivé Famille 3 (carte sociale, thread, etc.)"
      },
      "description": "Formats de distribution générés à partir de ce bit"
    },

    "acteurs": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["nom"],
        "properties": {
          "nom": {
            "type": "string",
            "description": "Nom de la personne ou organisation"
          },
          "role": {
            "type": "string",
            "description": "Rôle dans le bit (sujet, source, réacteur, etc.)"
          },
          "wikidata_id": {
            "type": "string",
            "description": "Identifiant Wikidata si disponible (pour désambiguïsation)"
          }
        }
      },
      "description": "Personnes et organisations mentionnées. Alimente les relations meme_acteur"
    },

    "mots_cles": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Tags libres pour recherche et clustering"
    }
  }
}
```

---

## 2. Schéma de l'assemblage

Un assemblage est le résultat de l'exécution d'un template sur un ensemble de bits.

```json
{
  "title": "Assemblage Newsadix",
  "type": "object",
  "required": [
    "id",
    "template",
    "bits",
    "horodatage",
    "version",
    "texte_rendu",
    "pilier",
    "geo"
  ],
  "properties": {

    "id": {
      "type": "string",
      "pattern": "^asm-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{3,}$",
      "description": "Identifiant unique. Format : asm-YYYY-MM-DD-NNN"
    },

    "template": {
      "type": "string",
      "enum": [
        "TPL-ALERTE",
        "TPL-DEPECHE-COURTE",
        "TPL-DEPECHE-DEVELOPPEE",
        "TPL-DEPECHE-ANGLE",
        "TPL-DEPECHE-SYNTHESE",
        "TPL-DEPECHE-DATA"
      ],
      "description": "Template Famille 1 utilisé pour l'assemblage"
    },

    "bits": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["bit_id", "role"],
        "properties": {
          "bit_id": {
            "type": "string",
            "description": "Référence vers le bit source"
          },
          "role": {
            "type": "string",
            "enum": [
              "fait_principal",
              "fait_complementaire",
              "donnee",
              "contexte",
              "point_de_vue",
              "source_methodologique",
              "limite"
            ],
            "description": "Rôle du bit dans cet assemblage"
          },
          "position": {
            "type": "integer",
            "description": "Ordre d'apparition dans le texte rendu"
          }
        }
      },
      "description": "Bits constitutifs avec leur rôle dans l'assemblage"
    },

    "horodatage": {
      "type": "string",
      "format": "date-time"
    },

    "version": {
      "type": "integer",
      "minimum": 1
    },

    "texte_rendu": {
      "type": "string",
      "description": "Texte final tel que publié"
    },

    "titre_genere": {
      "type": "string",
      "description": "Titre généré pour l'affichage"
    },

    "pilier": {
      "type": "string",
      "description": "Pilier taxonomique principal (hérité du bit fait_principal)"
    },

    "geo": {
      "type": "string",
      "enum": ["france", "france_monde", "monde"]
    },

    "user_need": {
      "type": "object",
      "description": "User Need de l'assemblage (peut différer du bit principal)"
    },

    "url_site": {
      "type": "string",
      "format": "uri",
      "description": "URL de la dépêche sur le site Newsadix"
    },

    "derives": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "template": {
            "type": "string",
            "enum": [
              "TPL-CARTE-SOCIALE",
              "TPL-THREAD-SOCIAL",
              "TPL-NEWSLETTER-DIGEST",
              "TPL-BRIEFING-AUDIO",
              "TPL-PUSH",
              "TPL-FLUX-MCP"
            ]
          },
          "id": { "type": "string" },
          "plateforme": { "type": "string" },
          "url": { "type": "string", "format": "uri" }
        }
      },
      "description": "Dérivés Famille 3 générés à partir de cet assemblage"
    },

    "escalade": {
      "type": "object",
      "properties": {
        "declenche": {
          "type": "string",
          "description": "ID de l'assemblage déclenché par escalade"
        },
        "declenche_par": {
          "type": "string",
          "description": "ID de l'assemblage source qui a déclenché celui-ci"
        }
      },
      "description": "Traçabilité de la chaîne d'escalade"
    }
  }
}
```

---

## 3. Règles de validation

### Bit

| Règle | Détail |
|-------|--------|
| Source obligatoire | `sources[]` ne peut pas être vide |
| Type ↔ contenu | Un bit `donnee` doit contenir au moins un chiffre. Un bit `point_de_vue` doit avoir un acteur attribué |
| Validateur obligatoire | Si `auteur.type` = `agent`, alors `auteur.valide_par` est requis (sauf en phase automatique) |
| Relations cohérentes | Une relation `met_a_jour` ne peut pointer que vers un bit du même type |
| Unicité | Pas deux bits avec le même `contenu` + `horodatage_evenement` (déduplication) |

### Assemblage

| Règle | Détail |
|-------|--------|
| Template ↔ bits | Les types de bits autorisés dépendent du template (ex. : TPL-ALERTE n'accepte pas de `point_de_vue`) |
| Fait principal | Tout assemblage a exactement 1 bit avec `role: fait_principal` |
| Bits existants | Chaque `bit_id` référencé doit exister dans la base et avoir `statut: publie` |
| Escalade traçable | Si `escalade.declenche_par` est renseigné, l'assemblage source doit exister |

---

## 4. Mapping type de bit → templates autorisés

| Type de bit | TPL-ALERTE | TPL-COURTE | TPL-DEVELOPPEE | TPL-ANGLE | TPL-SYNTHESE | TPL-DATA |
|-------------|:---:|:---:|:---:|:---:|:---:|:---:|
| `donnee` | Oui | Oui | Oui | Oui | Oui | **Dominant** |
| `fait` | **Dominant** | **Dominant** | Oui | Oui | **Dominant** | Oui |
| `contexte` | Non | Non | **Requis** | Oui | Oui | Oui |
| `point_de_vue` | Non | Non | Non | **Requis** | Non | Non |

Ce tableau est le garde-fou éditorial central : il garantit que chaque template respecte son niveau de factualité par construction.

---

## 5. Cycle de vie du bit

```
brouillon → valide → publie → [corrige] → archive
                ↑                  │
                └──────────────────┘
                  (correction = nouveau cycle de validation)
```

| Transition | Condition |
|-----------|-----------|
| brouillon → valide | Validation humaine (phase 1) ou automatique (phase 3) |
| valide → publie | Inclus dans un assemblage publié |
| publie → corrige | Erreur détectée → correction + incrémentation version |
| publie → archive | Bit obsolète (remplacé par `met_a_jour`) ou > 1 an sans utilisation |

---

Version : 0.1 | Date : 2026-04-14 | Statut : brouillon — à valider avec PJ et Yann
