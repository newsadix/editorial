---
name: fact-check-workflow
description: Workflow structuré de fact-checking pour le journalisme — extraction de claims, collecte de preuves, contact des sources, notation, documentation et protocole de correction. Charger pour toute vérification systématique de claims avant publication.
source: "Adapté de claude-skills-journalism — fact-check-workflow/SKILL.md"
---

# Workflow de fact-checking

Le fact-checking est systématique, pas intuitif. Ce skill fournit une structure pour la vérification de claims, la documentation des preuves et les décisions de notation.

## Quand utiliser ce skill

- Fact-checking pré-publication d'articles
- Articles de fact-check dédiés (notation de claims)
- Vérification de déclarations de sources en cours de reportage
- Construction de protocoles de vérification pour une rédaction
- Formation des équipes aux standards de vérification

---

## Le processus de fact-check

```
1. Identifier le claim → 2. Rechercher → 3. Collecter les preuves →
4. Contacter les sources → 5. Évaluer/noter → 6. Documenter → 7. Publier/corriger
```

---

## Étape 1 : Extraction de claims

### Quoi vérifier

**Vérifier :**
- Assertions factuelles ("X s'est produit", "Y est vrai")
- Statistiques et chiffres
- Dates et chronologies
- Citations et attributions
- Claims causaux ("X a causé Y")

**Ne pas vérifier (opinions) :**
- "Cette politique est bonne/mauvaise"
- "Il faudrait faire X"
- Prédictions sur l'avenir
- Questions de goût ou de préférence

### Template de log de claims

```markdown
## Journal de claims

**Article/Source :** [où le claim est apparu]
**Date :** [quand]

### Claim 1
**Énoncé :** [citation exacte ou paraphrase]
**Locuteur :** [qui l'a dit]
**Contexte :** [contexte environnant]
**Type :** [statistique/historique/citation/causal]
**Priorité :** [haute/moyenne/basse selon l'importance pour l'article]
**Statut :** [en attente/vérifié/faux/invérifiable]

### Claim 2
[même structure]
```

### Priorisation des claims

| Priorité | Critères |
|----------|----------|
| **Haute** | Central à la thèse de l'article, facilement vérifiable, conséquences élevées si erroné |
| **Moyenne** | Détail secondaire, vérification plus laborieuse |
| **Basse** | Détail périphérique, communément admis, conséquences minimales |

Vérifier les claims haute priorité en premier. Vérifier tous les claims si le temps le permet.

---

## Étape 2 : Recherche

### Sources primaires d'abord

| Type de claim | Sources primaires |
|---------------|-------------------|
| Statistiques | Étude originale, données gouvernementales, méthodologie de l'enquête |
| Citations | Enregistrement audio/vidéo, transcription, confirmation directe |
| Historique | Comptes rendus contemporains, archives officielles |
| Scientifique | Recherche évaluée par les pairs, consensus d'experts |
| Juridique | Documents judiciaires, dépôts officiels |
| Financier | Rapports annuels, comptes audités, déclarations réglementaires |

### Évaluation des sources secondaires

Si des sources secondaires sont nécessaires :
- À quelle distance sont-elles de la source originale ?
- Citent-elles leurs sources ?
- Plusieurs sources indépendantes confirment-elles ?
- Existe-t-il une couverture contradictoire ?

### Template de documentation de recherche

```markdown
## Recherche pour le claim : [description brève]

### Sources primaires consultées
| Source | Ce qu'elle dit | Confirme/contredit |
|--------|---------------|-------------------|
| [source] | [constat] | [confirme/contredit/partiel] |

### Sources secondaires consultées
| Source | Ce qu'elle dit | Fiabilité |
|--------|---------------|-----------|
| [source] | [constat] | [haute/moyenne/basse] |

### Lacunes dans les preuves
- [Ce qui n'a pas été trouvé]
- [Ce qui manque encore]
```

---

## Étape 3 : Collecte de preuves

### Types de preuves

| Type de preuve | Force | Notes |
|----------------|-------|-------|
| Documents officiels | Forte | Archives judiciaires, rapports gouvernementaux, dépôts |
| Données primaires | Forte | Jeux de données originaux, analyse propre |
| Consensus d'experts | Forte | Plusieurs experts indépendants convergent |
| Sources on-record | Moyenne | Source nommée avec connaissance directe |
| Comptes rendus contemporains | Moyen | Couverture médiatique de l'époque |
| Sources off-record | Faible | Utiliser pour orienter le reportage, pas comme preuve |
| Publications sur réseaux sociaux | Faible | Peuvent être supprimées, le contexte compte |

### Checklist de preuves

```markdown
## Preuves pour : [claim]

### Preuves documentaires
- [ ] Archives gouvernementales
- [ ] Documents judiciaires
- [ ] Dépôts d'entreprise
- [ ] Recherche publiée
- [ ] Déclarations officielles / communiqués

### Sources humaines
- [ ] Témoins directs
- [ ] Experts du domaine
- [ ] Parties concernées (on record)
- [ ] Parties concernées (pour droit de réponse)

### Vérification des données
- [ ] Jeu de données original obtenu
- [ ] Méthodologie examinée
- [ ] Calculs vérifiés de manière indépendante
- [ ] Taille d'échantillon adéquate

### Preuves contradictoires
- [ ] Recherche de sources contradictoires effectuée
- [ ] Contradictions documentées
- [ ] Écarts expliqués
```

---

## Étape 4 : Contact des sources

### Droit de réponse

**Toujours contacter :**
- Les personnes ou organisations faisant l'objet du fact-check
- Communiquer les claims spécifiques vérifiés
- Accorder un délai raisonnable (24-48 heures minimum)
- Documenter leur réponse (ou leur non-réponse)

### Template de contact

```markdown
Objet : Demande de commentaire — fact-check [Publication]

Madame, Monsieur [Nom],

Je suis [titre] à [publication] et je travaille sur la vérification de [contexte].

Je vérifie spécifiquement cette affirmation :

« [Claim exact vérifié] »

Je souhaite vous donner l'occasion de fournir toute preuve à l'appui,
de préciser le contexte ou d'apporter des corrections.

Ma date limite est le [date/heure]. N'hésitez pas à me signaler
si vous avez besoin de plus de temps.

[Votre nom]
[Coordonnées]
```

### Documentation des réponses

```markdown
## Journal des réponses

### [Nom de la source]
**Contactée le :** [date/heure, méthode]
**Délai accordé :** [date/heure]
**Réponse reçue :** [date/heure] / Pas de réponse
**Résumé :** [ce qu'elle a dit]
**Preuves fournies :** [documentation éventuelle]
**Citation directe pour publication :** « [citation] »
```

---

## Étape 5 : Notation du claim

### Échelles de notation standard

**Binaire (pour le fact-checking interne) :**
- VÉRIFIÉ : confirmé par les preuves
- FAUX : contredit par les preuves
- INVÉRIFIABLE : preuves insuffisantes pour trancher

**Graduée (pour les articles de fact-check) :**

| Notation | Critères |
|----------|----------|
| **Vrai** | Exact et complet, rien de significatif omis |
| **Plutôt vrai** | Exact mais nécessite contexte ou précision mineure |
| **À moitié vrai** | Partiellement exact mais omet un contexte critique |
| **Plutôt faux** | Contient une part de vérité mais globalement trompeur |
| **Faux** | Inexact ; contredit par les preuves |

### Template de décision de notation

```markdown
## Décision de notation : [claim]

**Claim :** [énoncé exact]
**Locuteur :** [qui l'a dit]
**Notre notation :** [notation]

### Preuves soutenant le claim
- [Preuve 1]
- [Preuve 2]

### Preuves contredisant le claim
- [Preuve 1]
- [Preuve 2]

### Contexte clé manquant dans le claim
- [Contexte 1]
- [Contexte 2]

### Réponse de la source
[Ce qu'elle a dit quand contactée]

### Raisonnement
[Expliquer pourquoi cette notation et pas une autre]

### Niveau de confiance
[Élevé/Moyen/Faible et pourquoi]
```

---

## Étape 6 : Documentation

### Le dossier de fact-check

Pour chaque claim vérifié, maintenir :

```markdown
## Dossier de fact-check

**Claim :** [énoncé exact]
**Source :** [qui l'a dit, où, quand]
**Vérifié par :** [votre nom]
**Date de vérification :** [date]

### Vérification
**Notation :** [notation]
**Preuves primaires :** [liste avec liens/emplacements]
**Preuves complémentaires :** [liste]
**Preuves contradictoires :** [le cas échéant]

### Sources contactées
- [Nom] : [résumé de la réponse]
- [Nom] : [pas de réponse à la date du]

### Notes
[Contexte supplémentaire, réserves, considérations futures]

### Fichiers
- [Liste des documents sauvegardés, captures d'écran, etc.]
```

### Archivage des preuves

- Sauvegarder les captures d'écran avec horodatage (les URLs peuvent changer)
- Archiver les pages web (Wayback Machine, Archive.today)
- Télécharger les documents (ne pas se contenter de liens)
- Conserver les fichiers originaux séparés de l'analyse

---

## Étape 7 : Corrections

### Quand corriger

| Situation | Action |
|-----------|--------|
| Erreur factuelle | Corriger immédiatement, noter la correction |
| Contexte manquant | Ajouter le contexte, peut ne pas nécessiter de correction formelle |
| Information mise à jour | Mettre à jour, noter "Mis à jour : [date]" |
| La source conteste la caractérisation | Évaluer le claim, corriger si justifié |

### Template de correction

```markdown
**Correction [date] :** Une version précédente de cet article indiquait
[claim incorrect]. En réalité, [information correcte]. Nous regrettons
cette erreur.
```

### Journal des corrections

```markdown
## Registre de correction

**Article :** [titre/URL]
**Publication originale :** [date]
**Erreur découverte :** [date]
**Type d'erreur :** [factuelle/contexte/attribution/autre]

**Texte original :**
[ce qui a été publié]

**Texte corrigé :**
[ce que ça dit maintenant]

**Comment découverte :**
[signalement lecteur, revue interne, plainte de la source, etc.]

**Correction publiée :** [date]
**Emplacement :** [dans l'article, page de corrections, les deux]
```

---

## Checklist pré-publication

Avant toute publication :

```markdown
## Fact-check pré-publication

**Article :** [titre]
**Journaliste :** [nom]
**Rédacteur en chef :** [nom]
**Fact-checker :** [nom, si distinct]
**Date de publication :** [date]

### Claims vérifiés
| Claim | Statut | Preuve | Notes |
|-------|--------|--------|-------|
| [claim 1] | VÉRIFIÉ | [source] | |
| [claim 2] | VÉRIFIÉ | [source] | |

### Sources contactées pour commentaire
| Source | Contactée | Réponse |
|--------|-----------|---------|
| [nom] | [date] | [reçue/pas de réponse] |

### Chiffres et statistiques
- [ ] Toutes les statistiques sourcées
- [ ] Calculs vérifiés de manière indépendante
- [ ] Contexte fourni (par habitant, ajusté de l'inflation, etc.)

### Citations
- [ ] Toutes les citations vérifiées contre l'enregistrement/transcription
- [ ] Attribution exacte
- [ ] Contexte préservé

### Noms et titres
- [ ] Tous les noms correctement orthographiés
- [ ] Titres actuels et exacts
- [ ] Affiliations vérifiées

### Revue juridique (si applicable)
- [ ] Risque de diffamation évalué
- [ ] Tous les claims soutenus par des preuves
- [ ] Réponse des personnes concernées documentée

### Validation
**Journaliste :** [nom, date]
**Rédacteur en chef :** [nom, date]
**Fact-checker :** [nom, date]
```

---

## Structure d'article de fact-check

Pour les articles de fact-check dédiés :

```markdown
# [Titre : claim vérifié]

**Claim :** [claim exact entre guillemets]
**Source :** [qui l'a dit, où, quand]
**Notre notation :** [notation avec indicateur visuel]

## Ce qui a été dit
[Contexte du claim, citation complète, circonstances]

## Ce que montrent les preuves
[Présenter les preuves pour et contre]

## Le verdict
[Explication de la décision de notation]

## Sources
[Liste de toutes les sources avec liens]

---
*Publié : [date] | Mis à jour : [date si applicable]*
```

---

*Le fact-checking n'est pas une question de piège. C'est une question d'exactitude. L'objectif est la vérité, pas les points.*
