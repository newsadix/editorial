# Template : Flux MCP / Agence

## Identité

| Champ | Valeur |
|-------|--------|
| **ID template** | `TPL-FLUX-MCP` |
| **User Need** | (non applicable — consommateurs machines) |
| **Mode d'engagement** | (non applicable) |
| **Format** | JSON structuré |
| **Signé** | Non |
| **Supervision** | Automatique dès le jour 1 |

## Principe

Le flux MCP est le format machine de Newsadix. Il expose les bits et leurs assemblages dans un format JSON structuré, consommable par d'autres médias, des agents IA, des agrégateurs ou des applications tierces. C'est le prolongement direct de la décision #36 (JSON comme format pivot) et de l'idée évoquée en réunion d'un « feed d'agence accessible à l'extérieur ».

Ce template ne produit rien de nouveau. Il formate et expose ce qui existe déjà dans la base de bits.

## Déclencheur

Automatique : **tout changement dans la base de bits publiés** alimente le flux.

| Événement | Action sur le flux |
|-----------|-------------------|
| Nouveau bit publié | Ajout au flux |
| Bit mis à jour (relation `met_a_jour`) | Mise à jour dans le flux + notification |
| Nouveau template Famille 1 publié | Ajout de l'assemblage au flux |
| Bit corrigé | Correction dans le flux + flag `correction` |

## Format de sortie

### Bit unitaire

```json
{
  "id": "bit-2026-04-14-001",
  "type": "fait",
  "contenu": "Le Conseil constitutionnel invalide l'article 12 de la loi immigration.",
  "sources": [
    {
      "nom": "Conseil constitutionnel",
      "url": "https://...",
      "type": "source_primaire"
    }
  ],
  "auteur": {
    "type": "agent",
    "id": "agent-veille-politique",
    "valide_par": "damien-va"
  },
  "horodatage": "2026-04-14T14:32:00+02:00",
  "geo": "france",
  "pilier": "politique_institutions",
  "user_need": "mettre_a_jour",
  "relations": [
    {
      "type": "contextualise",
      "cible": "bit-2026-04-10-042",
      "direction": "est_contextualise_par"
    },
    {
      "type": "consequence",
      "cible": "bit-2026-04-14-003",
      "direction": "a_pour_consequence"
    }
  ],
  "statut": "publie",
  "version": 1,
  "templates": ["TPL-ALERTE", "TPL-DEPECHE-COURTE"]
}
```

### Assemblage (dépêche)

```json
{
  "id": "asm-2026-04-14-001",
  "template": "TPL-DEPECHE-COURTE",
  "titre_genere": "Le Conseil constitutionnel invalide l'article 12 de la loi immigration",
  "bits": ["bit-2026-04-14-001", "bit-2026-04-14-002", "bit-2026-04-14-003"],
  "horodatage": "2026-04-14T14:45:00+02:00",
  "version": 1,
  "texte_rendu": "Le Conseil constitutionnel a invalidé mardi...",
  "url_site": "https://newsadix.com/depeche/...",
  "pilier": "politique_institutions",
  "geo": "france"
}
```

## Points d'accès (API)

| Endpoint | Description | Format |
|----------|-------------|--------|
| `/api/bits` | Flux de bits, du plus récent au plus ancien | JSON, paginé |
| `/api/bits/{id}` | Un bit avec toutes ses relations | JSON |
| `/api/assemblages` | Flux de dépêches assemblées | JSON, paginé |
| `/api/assemblages/{id}` | Une dépêche avec ses bits constitutifs | JSON |
| `/api/flux` | Flux temps réel (SSE ou WebSocket) | JSON stream |
| `/api/piliers/{pilier}` | Bits et assemblages d'un pilier | JSON, paginé |

### Filtres disponibles

| Paramètre | Valeurs | Exemple |
|-----------|---------|---------|
| `pilier` | 1 à 12 (cf. taxonomie) | `?pilier=politique_institutions` |
| `geo` | france, france_monde, monde | `?geo=france` |
| `type` | donnee, fait, contexte, point_de_vue | `?type=fait` |
| `depuis` | ISO 8601 | `?depuis=2026-04-14T00:00:00Z` |
| `template` | ID template | `?template=TPL-ALERTE` |

## Consommateurs cibles

| Consommateur | Usage |
|-------------|-------|
| Autres médias | Reprise de dépêches (modèle agence) |
| Agents IA externes | Recomposition de bits pour leurs propres usages |
| Agrégateurs (Google News, Apple News) | Indexation structurée |
| Applications tierces | Intégration de flux d'actualité |
| Agent conversationnel Newsadix | Recomposition à la demande du citoyen |
| Chercheurs / académiques | Analyse de corpus |

## Règles strictes

1. **Temps réel.** Le flux est alimenté dès qu'un bit ou assemblage est publié. Pas de batch
2. **Complet.** Chaque bit inclut toutes ses métadonnées et relations. Le consommateur peut reconstruire le réseau
3. **Versionné.** Chaque modification incrémente la version. Le consommateur peut détecter les changements
4. **Corrections explicites.** Un bit corrigé porte un flag `correction: true` et un champ `correction_detail`
5. **Pas de contenu Famille 2.** Le flux MCP ne contient que du contenu non signé (Famille 1). Le contenu signé (Famille 2) est réservé au site et aux canaux owned

## Conditions d'accès

À définir :
- Accès libre (modèle Wikipedia) ?
- Accès sur inscription (modèle API) ?
- Accès payant pour usage commercial (modèle agence) ?
- Quotas de requêtes ?

Ce choix a des implications sur le modèle économique (cf. `fondation/modele-economique.md`).

## Contrôles qualité automatisés

| Contrôle | Règle | Action si échec |
|----------|-------|----------------|
| Conformité JSON | Schema validation sur chaque bit/assemblage | Blocage publication flux |
| Latence | < 5 secondes entre publication et disponibilité dans le flux | Alerte performance |
| Disponibilité | Uptime 99,5 % | Monitoring + alertes |
| Cohérence | Chaque bit référencé dans un assemblage existe dans `/api/bits` | Vérification systématique |

---

Version : 0.1 | Date : 2026-04-14
