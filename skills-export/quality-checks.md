---
name: quality-checks
description: Contrôles qualité post-rédaction — détection AI slop, AP Style, attribution des sources, fact-check, diversité des sources, risque juridique, accessibilité. Non-bloquant (suggestions). À exécuter après toute écriture de contenu éditorial.
source: "Adapté de FLTR — rules/quality-checks.md"
---

# Contrôles qualité post-rédaction

Ces règles s'appliquent automatiquement après écriture ou édition de fichiers texte (.md, .txt, .html). Toutes sont non-bloquantes (suggestions uniquement).

**Skip** : fichiers code, config, data (JSON/YAML/CSV), node_modules, .git.

---

## 1. Détection AI slop

Scanner le texte pour détecter les marqueurs de génération automatique.

### Mots bannis — haute sévérité

Présence = réécriture obligatoire :

- delve
- realm
- tapestry
- synergy

### Mots bannis — sévérité moyenne

Présence = avertissement + suggestion d'alternative :

- landscape (usage métaphorique)
- leverage (comme verbe)
- utilize (remplacer par "utiliser")
- robust
- seamless
- paradigm

### Phrases bannies

- "It's important to note..."
- "In today's X landscape..."
- "Let's dive/delve into..."
- "At the end of the day..."
- "This is a game-changer"

### Équivalents français à surveiller

- "Il est important de noter que..."
- "Dans le paysage actuel de..."
- "Plongeons dans..."
- "En fin de compte..."
- "C'est un véritable tournant"
- "Force est de constater que..."

### Structures suspectes

- "So," / "Now," / "Basically," / "Essentially," en début de phrase
- Title Case dans les titres quand sentence case est attendu
- Énumérations systématiques de 3 avec adjectifs laudatifs
- Conclusions qui reformulent l'introduction sans rien ajouter

**Si détecté** : avertir avec les lignes concernées et proposer des alternatives concrètes.

---

## 2. AP Style

Vérifier la conformité avec les standards AP :

- **Nombres** : en lettres de un à neuf, en chiffres à partir de 10 (sauf début de phrase)
- **Dates et heures** : format standard, pas de "0" devant les heures
- **Majuscules** : titres en sentence case (sauf noms propres)
- **Choix de mots** : préférer les formes simples et directes
- **Abréviations** : développer à la première occurrence

---

## 3. Attribution des sources

Scanner pour :

- **Citations sans attribution** : guillemets ou "a déclaré" / "selon" sans nom de source → flag
- **Statistiques sans source** : tout pourcentage ou chiffre sans référence documentée → flag
- **Attributions vagues** : "des experts estiment", "des études montrent", "certains pensent" → flag. Remplacer par une source nommée ou supprimer.

---

## 4. Fact-check reminder

Signaler les affirmations factuelles qui nécessitent une vérification :

- **Noms et titres** : orthographe, fonction actuelle
- **Dates** : cohérence chronologique
- **Nombres et statistiques** : source, périmètre, date de collecte
- **Citations** : correspondance avec la source originale
- **Affirmations historiques** : exactitude factuelle
- **Coordonnées** : URLs, adresses, numéros de téléphone

---

## 5. Méthodologie données

Pour le contenu data-driven, vérifier :

- **Source des données** : identifiée et accessible
- **Taille d'échantillon** : mentionnée quand pertinent
- **Transparence des calculs** : méthode reproductible
- **Limites** : biais connus, périmètre géographique/temporel
- **Notes de nettoyage** : transformations appliquées aux données brutes

---

## 6. Diversité des sources

Vérifier si les sources citées reflètent des perspectives diverses :

- **Sourcing mono-perspective** : toutes les sources soutiennent le même angle → flag
- **Déséquilibre d'autorité** : que des sources institutionnelles, pas de terrain → flag
- **Équilibre genre** : les femmes sont-elles citées comme expertes ?
- **Diversité d'expertise** : académiques, praticiens, société civile, usagers

---

## 7. Risque juridique

Scanner pour :

- **Diffamation** : accusations de crimes ou de fraude sans preuve documentée → flag critique
- **Vie privée** : informations médicales, mineurs identifiables, adresses personnelles → flag critique
- **Sources confidentielles** : éléments permettant d'identifier une source protégée → flag critique
- **Publicité pré-procès** : détails d'affaire en cours susceptibles d'influencer le procès → flag
- **Copyright** : reproduction excessive de contenus tiers → flag

---

## 8. Rappel archivage

Quand du contenu contient des URLs :

- Rappeler d'archiver les sources web avant publication
- Services recommandés : Wayback Machine, Archive.today, Perma.cc, Ghost Archive
- Les URLs peuvent changer ou disparaître — l'archive est la seule garantie de traçabilité

---

## 9. Accessibilité

Vérifier :

- **Alt text** : manquant sur les images → flag
- **Hiérarchie des titres** : sauts de niveaux (H1 → H3 sans H2) → flag
- **Texte des liens** : "cliquez ici" au lieu d'un texte descriptif → flag
- **Information par couleur seule** : si la couleur est le seul vecteur de sens → flag
- **En-têtes de tableaux** : tableaux de données sans en-têtes identifiés → flag

---

## 10. Checklist pré-publication (fin de session)

Quand une session implique la création ou l'édition de contenu journalistique, afficher cette checklist en fin de session :

### Exactitude
- [ ] Tous les faits vérifiés contre les sources primaires
- [ ] Toutes les citations vérifiées contre l'enregistrement ou la transcription
- [ ] Tous les chiffres sourcés et contextualisés

### Équité
- [ ] Droit de réponse respecté
- [ ] Sources diverses consultées
- [ ] Contexte suffisant pour chaque affirmation

### Légal
- [ ] Pas de risque de diffamation identifié
- [ ] Vie privée protégée
- [ ] Copyright respecté

### Style
- [ ] AI slop éliminé
- [ ] Conformité AP Style
- [ ] Ton cohérent avec la ligne éditoriale

### Métadonnées
- [ ] Titre optimisé
- [ ] Résumé/excerpt rédigé
- [ ] Tags/catégories attribués
- [ ] Image d'illustration sourcée et créditée

### Revue finale
- [ ] Relecture complète effectuée
- [ ] Sources archivées
- [ ] Stade du document marqué (DRAFT/FINAL)
