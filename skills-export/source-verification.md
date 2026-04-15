---
name: source-verification
description: Méthodologie SIFT de vérification de sources et de contenus numériques — évaluation de crédibilité, analyse de comptes sociaux, recherche d'image inversée, vérification de documents, construction d'un trail de vérification. Charger pour toute investigation de source.
source: "Adapté de claude-skills-journalism — source-verification/SKILL.md"
---

# Méthodologie de vérification de sources

Approches systématiques pour vérifier les sources, les claims et les contenus numériques dans le journalisme et la recherche.

---

## Cadre de vérification

### La méthode SIFT

**S - Stop (Arrêtez-vous)** : Ne pas immédiatement partager ou utiliser une information non vérifiée
**I - Investigate (Investiguer la source)** : Qui est derrière cette information ?
**F - Find better coverage (Trouver une meilleure couverture)** : Que disent les autres sources fiables ?
**T - Trace claims (Tracer les claims)** : Trouver la source originale du claim

### Checklist d'évaluation de crédibilité

```markdown
## Template d'évaluation de source

### Identification de base
- [ ] Nom complet / organisation identifié(e)
- [ ] Coordonnées vérifiables
- [ ] Références professionnelles vérifiables
- [ ] Présence en ligne cohérente sur les différentes plateformes

### Évaluation de l'expertise
- [ ] Expertise pertinente pour le claim formulé
- [ ] Historique dans ce domaine
- [ ] Reconnu(e) par ses pairs
- [ ] Pas d'historique de diffusion de désinformation

### Analyse des motivations
- [ ] Conflits d'intérêts potentiels identifiés
- [ ] Intérêt financier dans le résultat ?
- [ ] Motivation politique ou idéologique ?
- [ ] Grief personnel impliqué ?

### Corroboration
- [ ] Les claims peuvent-ils être vérifiés indépendamment ?
- [ ] D'autres sources crédibles confirment-elles ?
- [ ] Des preuves documentaires sont-elles disponibles ?
- [ ] Existe-t-il des sources contradictoires ?
```

---

## Techniques de vérification numérique

### Analyse de comptes sur les réseaux sociaux

```markdown
## Checklist de vérification de compte

### Âge et historique du compte
- Date de création (les comptes plus anciens sont plus crédibles)
- Fréquence et patterns de publication
- Périodes d'inactivité (dormant puis soudainement actif ?)
- Cohérence linguistique dans le temps

### Analyse du réseau
- Ratio abonnés/abonnements
- Qualité des abonnés (vrais comptes vs bots)
- Patterns d'interaction (qui interagit avec le compte ?)
- Connexions mutuelles avec des comptes vérifiés

### Patterns de contenu
- Contenu original vs partages uniquement
- Sujets discutés de manière récurrente
- Indicateurs géographiques dans les publications
- Fuseau horaire de l'activité de publication

### Signaux d'alerte
- Compte récent formulant des affirmations audacieuses
- Changement soudain de sujets ou de ton
- Comportement coordonné avec d'autres comptes
- Photo de profil provenant d'une banque d'images
- Bio générique sans détails spécifiques
```

---

### Recherche d'image inversée

```markdown
## Processus de vérification d'image

### Étape 1 : Recherche d'image inversée
Outils à utiliser :
- Google Images (images.google.com)
- TinEye (tineye.com)
- Yandex Images (yandex.com/images) — le plus performant pour les visages
- Bing Recherche visuelle

### Étape 2 : Vérification des métadonnées (EXIF)
- Date et heure de capture originale
- Informations sur l'appareil/le dispositif
- Coordonnées GPS (si disponibles)
- Logiciel utilisé pour l'édition

Outils :
- Jeffrey's EXIF Viewer (exif.regex.info)
- FotoForensics (fotoforensics.com)
- Plugin de vérification InVID

### Étape 3 : Analyse du contenu visuel
- Conditions météo (correspondent-elles à la date annoncée ?)
- Ombres (cohérentes avec l'heure annoncée ?)
- Signalétique/textes (langue correcte pour le lieu ?)
- Architecture (correspond au lieu revendiqué ?)
- Vêtements (appropriés à la saison ?)

### Étape 4 : Trouver la source originale
- Première apparition en ligne
- Photographe/source original(e)
- Contexte de la première publication
- L'image a-t-elle été utilisée dans d'autres contextes ?
```

---

### Vérification vidéo

```markdown
## Checklist de vérification vidéo

### Analyse technique
- [ ] Résolution cohérente d'un bout à l'autre
- [ ] Synchronisation audio/vidéo correcte
- [ ] Pas d'artefacts d'édition visibles
- [ ] Éclairage cohérent entre les plans
- [ ] Comportement naturel des ombres

### Analyse du contenu
- [ ] Lieu identifiable et vérifiable
- [ ] Indicateurs temporels (position du soleil, ombres)
- [ ] Météo correspondant aux archives historiques
- [ ] Détails d'arrière-plan cohérents
- [ ] Vêtements des personnes appropriés au contexte

### Vérification des métadonnées
- [ ] Date de mise en ligne vs date de l'événement revendiqué
- [ ] Source originale identifiée
- [ ] Chaîne de provenance traçable
- [ ] Plusieurs angles disponibles ?

### Outils
- Extension navigateur InVID/WeVerify
- YouTube DataViewer (citizenevidence.amnestyusa.org)
- Outils d'analyse image par image
```

---

## Vérification de documents

### Analyse de PDF et documents

```markdown
## Étapes de vérification de document

### Examen des métadonnées
- Date de création et historique de modification
- Informations sur l'auteur
- Logiciel utilisé pour la création
- Polices et images embarquées

### Inspection visuelle
- Formatage cohérent d'un bout à l'autre
- Correspondance des polices (pas de texte greffé)
- Alignement du texte et des images
- Qualité cohérente entre les pages
- Signatures d'apparence authentique

### Vérification du contenu
- Dates cohérentes en interne
- Noms correctement orthographiés partout
- Numéros de référence valides
- Coordonnées vérifiables
- En-tête correspondant aux exemples connus

### Provenance
- Comment le document a-t-il été obtenu ?
- Chaîne de conservation documentée ?
- Original vs copie ?
- La source peut-elle fournir un contexte supplémentaire ?
```

---

## Construction d'un trail de vérification

### Template de documentation

```markdown
## Dossier de vérification

**Claim vérifié :**
[Énoncer le claim spécifique]

**Source du claim :**
- Nom/compte :
- Plateforme :
- Date de première observation :
- URL (archivée) :

**Étapes de vérification effectuées :**

### Étape 1 : [Description]
- Action effectuée :
- Outil/méthode utilisé(e) :
- Résultat :
- Capture d'écran/preuve sauvegardée : [nom de fichier]

### Étape 2 : [Description]
- Action effectuée :
- Outil/méthode utilisé(e) :
- Résultat :
- Capture d'écran/preuve sauvegardée : [nom de fichier]

[Continuer pour chaque étape]

**Sources corroborantes :**
1. [Source 1] — [Ce qu'elle confirme]
2. [Source 2] — [Ce qu'elle confirme]
3. [Source 3] — [Ce qu'elle confirme]

**Informations contradictoires :**
1. [Source] — [Ce qu'elle contredit]

**Évaluation de confiance :**
- [ ] Vérifié vrai
- [ ] Probablement vrai (confiance élevée)
- [ ] Non vérifié (preuves insuffisantes)
- [ ] Probablement faux (preuves contradictoires)
- [ ] Vérifié faux

**Raisonnement :**
[Expliquer la conclusion sur la base des preuves]

**Vérification effectuée par :**
**Date :**
```

---

## Archivage des preuves

### Bonnes pratiques d'archivage web

Sauvegarder les URLs vers plusieurs services d'archivage pour la redondance :

| Service | URL | Notes |
|---------|-----|-------|
| Internet Archive | web.archive.org/save/ | Gratuit, le plus connu |
| Archive.today | archive.ph | Interface simple, robuste |
| Perma.cc | perma.cc | Requiert un compte, orienté académique/juridique |

Règle : ne jamais se fier à un lien unique. Les URLs changent, les pages disparaissent. L'archive est la seule garantie de traçabilité.

### Documentation des captures d'écran

```markdown
## Bonnes pratiques pour les captures d'écran

1. **Capture pleine page** : utiliser des extensions navigateur pour capturer la page entière
2. **Inclure la barre d'URL** : montre la source
3. **Inclure l'horodatage** : horloge système visible ou ajout manuel
4. **Sauvegarder les métadonnées** : noter quand et comment la capture a été effectuée
5. **Formats multiples** : sauvegarder en PNG (sans perte) et PDF
6. **Stockage sécurisé** : hasher les fichiers et stocker de manière sécurisée

Outils recommandés :
- Hunchly (hunch.ly) — capture et journalisation automatiques
- Extensions navigateur de capture d'écran
- Impression PDF du navigateur — inclut URL et date
```

---

## Vérification d'interview

### Vérification préalable de la source

```markdown
## Vérification de fond de la source

### Archives publiques
- [ ] Licences professionnelles vérifiées
- [ ] Archives judiciaires consultées
- [ ] Immatriculations d'entreprise confirmées
- [ ] Archives cadastrales (si pertinent)
- [ ] Comptes de campagne (si politique)

### Parcours professionnel
- [ ] Profil LinkedIn examiné
- [ ] Employeur confirmé
- [ ] Employeurs précédents contactés
- [ ] Travaux publiés examinés
- [ ] Participations à des conférences vérifiées

### Audit réseaux sociaux
- [ ] Toutes les plateformes identifiées
- [ ] Historique de publications examiné
- [ ] Connexions/abonnés analysés
- [ ] Déclarations précédentes sur le sujet
- [ ] Contenu supprimé retrouvé ?

### Passages médiatiques
- [ ] Interviews précédentes trouvées
- [ ] Cohérence avec les claims actuels
- [ ] Évaluation par d'autres journalistes
- [ ] Retraits ou corrections antérieurs ?
```

### Techniques de vérification en temps réel

```markdown
## Techniques de vérification pendant l'interview

### Demandes de documents
- Demander de la documentation pendant l'interview
- Vérifier que les documents ne sont pas altérés
- Demander les originaux, pas les copies quand c'est possible
- Noter l'état et la provenance des documents

### Sondage de détails spécifiques
- Demander des dates, noms, lieux précis
- Demander des témoins corroborants
- Poser la question : « Comment savez-vous cela ? »
- Relancer sur les réponses vagues

### Vérifications de cohérence
- Noter la version initiale du récit
- Revenir sur les points clés plus tard
- Comparer les détails entre les différentes narrations
- Signaler les incohérences pour suivi

### Bonnes pratiques d'enregistrement
- Obtenir le consentement (vérifier la législation locale)
- Utiliser un équipement d'enregistrement fiable
- Sauvegarde en temps réel
- Noter les indices non-verbaux séparément
```

---

## Tableau d'outils essentiels

| Outil | Usage | URL |
|-------|-------|-----|
| InVID/WeVerify | Plugin de vérification vidéo | weverify.eu |
| TinEye | Recherche d'image inversée | tineye.com |
| Wayback Machine | Archives web | web.archive.org |
| Hoaxy | Visualisation de la propagation de claims | hoaxy.osome.iu.edu |
| Media Bias/Fact Check | Fiabilité des sources | mediabiasfactcheck.com |
| OpenCorporates | Registres d'entreprises | opencorporates.com |
| OCCRP Aleph | Recherche de documents | aleph.occrp.org |

---

## Ressources de formation

- First Draft News (firstdraftnews.org) — guides de vérification
- Bellingcat (bellingcat.com/resources) — guides OSINT et investigation
- Google News Initiative (newsinitiative.withgoogle.com) — outils et formation
- Verification Handbook (verificationhandbook.com) — manuel complet
- SPJ (spj.org/ethics) — ressources déontologiques
