# User Needs — Framework de production editoriale

Newsadix utilise le modele User Needs 2.0 (Shishkin/BBC, smartocto 2023) pour structurer sa production editoriale. Les 8 besoins sont organises en 4 directions.

Ref. implementee dans FLTR : `~/GitHub/FLTR/projets/veille-5piliers/src/prompts/user-needs.md`

## Les 8 besoins en 4 directions

### Direction CONNAISSANCE — savoir ce qui se passe

| Besoin | Traduction | Signal | Description |
|--------|-----------|--------|-------------|
| `update_me` | Tiens-moi au courant | Fait recent, pas d'analyse approfondie | Faits bruts, derniere heure, suivi |
| `keep_me_engaged` | Fais-moi decouvrir | Sujet peu couvert, angle original | Curiosite, sujets inattendus, hors radar |

### Direction ACTION — savoir quoi faire

| Besoin | Traduction | Signal | Description |
|--------|-----------|--------|-------------|
| `help_me` | Aide-moi | Etapes concretes, outils, tutos | Guides, methodes, solutions pratiques |
| `connect_me` | Connecte-moi | Collectifs, coalitions, voix | Communaute, temoignages, appartenance |

### Direction COMPREHENSION — comprendre le monde

| Besoin | Traduction | Signal | Description |
|--------|-----------|--------|-------------|
| `educate_me` | Apprends-moi | "Comment ca marche", mecanisme, chaine causale | Pedagogie, mecanismes, fonctionnement |
| `give_me_perspective` | Eclaire-moi | Dynamiques sous-jacentes, rapports de force, paradoxes | Analyse, mise en perspective, enjeux de fond |

### Direction RESSENTI — ressentir quelque chose

| Besoin | Traduction | Signal | Description |
|--------|-----------|--------|-------------|
| `divert_me` | Divertis-moi | Dimension ludique, absurde, decalee | Surprise, humour, legerete |
| `inspire_me` | Inspire-moi | Victoires, pistes, vision positive | Espoir, vision, possibilites |

## Regles d'attribution

Pour chaque contenu produit :
1. **User Need primaire** (obligatoire) : le besoin dominant
2. **User Need secondaire** (0-2 max) : besoins complementaires
3. **Direction dominante** : connaissance, action, comprehension, ressenti

## Combinaisons frequentes

| Combinaison | Exemple type |
|-------------|-------------|
| `give_me_perspective` + `educate_me` | Analyse approfondie d'un mecanisme avec mise en contexte |
| `update_me` + `give_me_perspective` | Fait d'actualite avec angle revelateur |
| `help_me` + `educate_me` | Guide pratique qui explique le pourquoi en plus du comment |
| `inspire_me` + `connect_me` | Initiative collective qui donne de l'espoir |
| `keep_me_engaged` + `give_me_perspective` | Sujet hors radar avec analyse systemique |

## Priorisation Newsadix

### Phase 1 — Flux automatisé (Famille 1 + 3)

Les templates automatisés couvrent 3 des 8 besoins. C'est le noyau de production dès le jour 1.

| User Need | Priorité | Templates associés | Raison |
|-----------|---------- |-------------------|--------|
| `update_me` | **Critique** | Alerte, Dépêche courte, Dépêche data, Dépêche synthèse, Push, Newsletter, Carte sociale | C'est le besoin fondamental d'un flux d'agence. La promesse minimale du média |
| `educate_me` | **Haute** | Dépêche développée, Dépêche data, Dépêche synthèse, Thread social, Briefing audio | Le contexte et la donnée commentée distinguent Newsadix d'un agrégateur brut |
| `give_me_perspective` | **Moyenne** | Dépêche d'angle | Dernier template F1 déployé car il intègre des points de vue — risque éditorial plus élevé |

### Phase 2 — Contenu signé (Famille 2, ultérieur)

Les 5 besoins restants nécessitent une intervention humaine significative.

| User Need | Templates associés (Famille 2) | Condition de déploiement |
|-----------|-------------------------------|------------------------|
| `give_me_perspective` | Analyse, Décryptage | Quand 1+ journaliste signé est opérationnel |
| `keep_me_engaged` | Portrait, Récit/reportage | Quand le volume F1 est stable et qu'il reste de la bande passante |
| `inspire_me` | Récit/reportage | Idem |
| `connect_me` | Interview, formats participatifs | Quand la communauté de lecteurs atteint un seuil critique |
| `help_me` | Guides, formats pratiques | Quand le besoin est identifié par les analytics |
| `divert_me` | Formats courts engageants | Quand le pilier 12 (divertissement) est activé |

### Routing User Need → canal de distribution

| User Need | Canal privilégié | Logique |
|-----------|-----------------|---------|
| `update_me` | Push, newsletter matinale, fil principal site | L'info vient au lecteur |
| `educate_me` | Site (dépliage de bits), thread social, briefing audio | Le lecteur approfondit |
| `give_me_perspective` | Site, newsletter thématique, LinkedIn | Le lecteur cherche un éclairage |
| `keep_me_engaged` | Instagram, TikTok, newsletter | Le lecteur découvre |
| `inspire_me` | Instagram stories, newsletter hebdo | Le lecteur est touché |
| `connect_me` | Réseaux sociaux (commentaires), couche conversationnelle | Le lecteur participe |
| `help_me` | Site (SEO), newsletter thématique | Le lecteur a un besoin concret |
| `divert_me` | TikTok, Instagram, stories | Le lecteur se détend |

### Métriques par User Need

| User Need | Métrique principale | Métrique secondaire |
|-----------|-------------------|-------------------|
| `update_me` | Fraîcheur (temps entre événement et publication) | Volume de bits publiés/jour |
| `educate_me` | Profondeur (nombre de bits contexte/assemblage) | Temps passé sur la page |
| `give_me_perspective` | Équilibre des PDV (nombre et diversité) | Engagement (commentaires, partages) |
| `keep_me_engaged` | Taux de découverte (lecteurs exposés à un nouveau pilier) | Rétention |
| `inspire_me` | Partages | Sentiment (si mesurable) |
| `connect_me` | Interactions communautaires | Croissance de la base active |
| `help_me` | Taux de complétion du guide/tuto | SEO (trafic organique) |
| `divert_me` | Engagement (likes, vues courtes) | Viralité |

---
Version : 0.2 | Date : 2026-04-14 | Statut : complété pour les phases 1-2
