# French Humanizer : humaniser un texte IA en français (skill Claude Code)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Langue : français](https://img.shields.io/badge/langue-fran%C3%A7ais-0055A4)
![Claude Code skill](https://img.shields.io/badge/Claude%20Code-skill-d97757)
![Python 3](https://img.shields.io/badge/Python-3.8%2B-3776AB)

**French Humanizer** est une skill pour Claude Code et Claude.ai qui réécrit un texte français généré par une IA (ChatGPT, Claude, Gemini, Mistral…) pour qu'il sonne écrit par une personne, **sans changer ce qu'il dit**. C'est l'adaptation française de [blader/humanizer](https://github.com/blader/humanizer), avec un catalogue de motifs propre au français et des profils de registre établis sur des textes humains publiés avant 2020 (jusqu'en 2021 pour quelques genres récents), lus dans leur version archivée pour garantir leur date.

> **English.** French Humanizer is an agent skill for Claude Code, Claude.ai and other skill-compatible agents that removes the signs of AI-generated writing from **French** text. It ships 32 French-specific AI writing patterns, twenty-three register profiles (legal, electronics, code comments, READMEs, technical docs, hi-fi reviews, forums, cover letters, formal and informal letters, encyclopedic, wire copy, regional, sports, business, B2B, car and literary press, editorials, buzz media, e-commerce product pages, brand pages, AI tech articles) built from human writing published up to 2021, plus a command to add your own emails and texts as a local voice corpus, and a dependency-free Python scanner usable in CI.

## Pourquoi un humanizer spécifique au français

Les humanizers existants sont pensés pour l'anglais. Un texte IA en français a ses propres tics :

- titres en capitales à l'anglaise (« Les Avantages Clés De La Méthode ») ;
- connecteurs en série en tête de chaque paragraphe (« Par ailleurs… En outre… De plus… Enfin… ») ;
- calques de l'anglais (« faire du sens », « adresser un problème », « impacter ») ;
- vocabulaire gonflé (« véritable levier », « enjeu majeur », « incontournable », « à l'ère du numérique ») ;
- nominalisations en cascade (« permet de favoriser la mise en place de… ») ;
- tiret cadratin employé comme ponctuation, rare dans la prose française humaine ;
- formules « Ce n'est pas X, c'est Y », chutes d'une ligne, conclusions moralisantes.

Et surtout, un bon texte humain ne s'écrit pas pareil selon qu'il s'agit d'un arrêt de la Cour de cassation, d'une réponse sur un forum d'électronique ou d'un mot aux voisins. La skill commence donc par identifier le registre.

## Les vingt-trois registres

| Registre | Corpus humain d'avant 2020 | Ce que la skill vise |
|---|---|---|
| Juridique | Arrêts de la Cour de cassation (2015) | Vocabulaire stable, références exactes, aucune emphase |
| Électronique et technique | Forum Futura-Sciences (2003 à 2013) | Chiffres et unités, calcul visible, ton direct |
| Commentaires de code | OpenFisca France (2018) | Commentaires courts sur le pourquoi, TODO, hypothèses |
| Lettre de motivation | Forum CommentÇaMarche (2012) | Faits vérifiables plutôt qu'adjectifs |
| Courrier formel | Modèles de lettres administratives (2014) | Faits datés, demande, délai, formule de politesse classique |
| Courrier informel | Forums CommentÇaMarche et LinuxFr (2011 à 2015) | Phrases courtes, détail concret, fin brève |
| Encyclopédique | Wikipédia, version archivée de 2019 | Un fait vérifiable par phrase, source après le fait |
| Presse buzz et insolite | Demotivateur, L'Avenir (2015) | Anecdote d'abord, blague dans l'intertitre |
| Presse sportive | Maxifoot (2004) | Fait de jeu précis, surnoms, avis tranché |
| Presse automobile | L'argus (2014-2016), Fiches-Auto | Chiffres et unités, rivale nommée, vrai défaut |
| Presse économique | La finance pour tous (2018) | Chiffre, base de comparaison, cause, limite |
| Critique littéraire | Le Monde des livres (2005) | Syntaxe soutenue, ruptures de rythme, verdict assumé |
| Dépêche d'agence | AFP (2017) | Fait et source dès la première phrase |
| Presse régionale | Journal du Gers (2016) | Commune, date, lieu précis, brève |
| Éditorial | Le Monde (2017) | Thèse claire, faits datés, un ou deux procédés forts |
| Presse professionnelle | Journal du Net (2017) | Chiffre, source, conditionnel, pas d'explication superflue |
| Fiche produit e-commerce | LDLC (2013, 2018) | Chaque bénéfice adossé à une caractéristique chiffrée |
| Page produit de marque | Apple iPhone 12 (2020) | Slogan lié au produit et suivi d'un chiffre |
| README | Etalab, pygrammalecte (2020) | Description, installation, exemple avec résultat, limites |
| Article tech sur l'IA | Blog du Modérateur, Centre Inffo (2020), LADN (2021) | Fait daté, chiffre comparé, source nommée |
| Documentation technique | Wiki ubuntu-fr (2018) | Commande, résultat attendu, piège connu |
| Presse hi-fi | Banc d'essai d'amplificateur (2016) | Mesures, disque cité, vrai défaut, prix |
| Forum d'entraide | HardWare.fr (2012) | Réponse courte, question de précision, renvoi au guide |

Pour la presse, la skill situe d'abord le texte entre registre très léger et registre soutenu : une IA écrit tout au même niveau moyen, un journaliste s'ancre nettement à un bout.

Le détail et les liens sont dans [`references/sources.md`](references/sources.md).

## Exemple

**Avant (texte IA) :**

> À l'ère du numérique, la gestion des sauvegardes constitue un enjeu majeur pour toute entreprise. Ce n'est pas seulement une question technique : c'est une véritable assurance pour l'avenir. En somme, investir dans les sauvegardes, c'est investir dans la sérénité.

**Après :**

> Une sauvegarde ne sert que si on sait la restaurer. Nous copions la base chaque nuit, une deuxième copie part chez un hébergeur distinct, et une fois par mois on restaure la copie de la veille sur une machine de test pour vérifier qu'elle s'ouvre.

La skill n'invente jamais de fait : si un détail concret manque, elle le demande.

## Installation

**Claude Code** (tous les projets) :

```bash
git clone https://github.com/kofekod23/french-humanizer.git ~/.claude/skills/french-humanizer
```

Pour un seul projet, cloner dans `.claude/skills/french-humanizer` à la racine du projet.

**Claude.ai et Claude Desktop** : télécharger le dépôt en ZIP (Code, puis Download ZIP) et l'ajouter comme skill dans les réglages.

**Autres agents** (Codex, Cursor, Copilot, Gemini CLI…) : copier le dossier dans le répertoire de skills de l'agent, ou pointer sa configuration vers `SKILL.md`.

## Utilisation

```
/french-humanizer

[texte à humaniser]
```

Ou en langage courant : « humanise ce courrier », « ce commentaire de code sent l'IA », « réécris ce texte de façon plus naturelle ».

**Calquer votre style** : joignez deux ou trois paragraphes que vous avez écrits, la réécriture suit votre rythme, vos mots et votre ponctuation.

```
/french-humanizer

Voici un échantillon de mon écriture :
[2 ou 3 paragraphes]

Humanise ce texte (courrier formel) :
[texte]
```

## Ajouter vos propres textes

Enrichissez la skill avec vos mails et vos textes. Vos écrits calibrent la réécriture sur votre voix ; les textes reçus servent d'exemples humains d'un registre.

```bash
python3 scripts/ajouter.py mail-envoyé mon-mail.txt --registre "mail pro"
python3 scripts/ajouter.py texte-modèle article.md --registre "article"
python3 scripts/ajouter.py mail-reçu mail-client.txt --registre "mail client"
python3 scripts/ajouter.py texte-autre courrier-banque.txt --registre "courrier formel"
python3 scripts/ajouter.py lister      # ce qui est enregistré
python3 scripts/ajouter.py profil      # vos habitudes d'écriture, chiffrées
```

Ou directement dans Claude : `/french-humanizer ajouter mail-envoyé` puis collez le texte.

Le corpus reste sur votre machine (`~/.config/french-humanizer/corpus`), hors du dépôt Git. Un texte « de vous » qui ressemble trop à de la prose IA est signalé, pour ne pas fausser la calibration.

## Détecteur de texte IA en français (script Python)

`scripts/scan.py` repère les motifs sans rien réécrire et donne un score indicatif de 0 à 100. Python 3, aucune dépendance.

```bash
python3 scripts/scan.py article.md
python3 scripts/scan.py docs/*.md --json
python3 scripts/scan.py docs/*.md --fail-above 40   # échoue au-delà du seuil, pour la CI
```

Il signale le vocabulaire IA, les structures « pas X, mais Y », les tirets, les titres en capitales, le gras en étiquette, les émojis, les connecteurs en série et l'uniformité de longueur des phrases. Un score ne prouve rien à lui seul : c'est un outil de relecture, pas un détecteur fiable d'auteur.

## Contenu du dépôt

| Fichier | Rôle |
|---|---|
| [`SKILL.md`](SKILL.md) | Déroulé de la réécriture et règles fixes |
| [`references/motifs-ia-fr.md`](references/motifs-ia-fr.md) | Les 32 motifs d'écriture IA en français, avec un avant/après chacun |
| [`references/registres.md`](references/registres.md) | Profils par registre : traits humains observés, dérives IA, exemple |
| [`references/sources.md`](references/sources.md) | Corpus d'avant 2020 et méthode |
| [`scripts/scan.py`](scripts/scan.py) | Repérage automatique |
| [`scripts/ajouter.py`](scripts/ajouter.py) | Ajout de vos textes au corpus personnel, profil de voix |

## Ponctuation française

Pas de tiret cadratin ni demi-cadratin en guise de ponctuation, guillemets « », espace insécable avant ; : ! ? et %, ordinaux 2e et 16e, nombres 1 455 746 et 4,40 m, titres sans capitales à l'anglaise. Dans les registres relâchés (forum, message entre amis), la ponctuation de l'auteur est conservée. Le détail est dans [`SKILL.md`](SKILL.md).

## Ce que la skill ne fait pas

Elle ne cherche pas à tromper les détecteurs d'IA (GPTZero, Compilatio, Turnitin…) et n'ajoute jamais de fautes volontaires. Elle rend un texte plus clair et plus naturel pour un lecteur humain.

## FAQ

**Quelle différence avec blader/humanizer ?** La méthode est la même (repérage, premier jet, critique, version finale). Le catalogue est réécrit pour le français et la skill ajoute des profils de registre fondés sur un corpus humain français.

**Fonctionne-t-elle avec ChatGPT ou Mistral ?** La skill tourne dans un agent compatible avec le format SKILL.md. Elle humanise des textes produits par n'importe quel modèle.

**Peut-on vérifier si le texte passe les détecteurs d'IA ?** Des détecteurs existent (GPTZero, ZeroGPT, Compilatio, Lucide.ai pour le français, Pangram) et vous pouvez y soumettre le résultat. Ils se trompent dans les deux sens et signalent aussi des textes humains ; la skill n'est pas réglée pour eux. Pour mesurer ce qu'elle corrige, utilisez `scripts/scan.py` avant et après.

**Peut-on ajouter un registre ?** Oui : la marche à suivre est en bas de [`references/sources.md`](references/sources.md). Les contributions sont bienvenues.

## Crédits

Méthode et structure reprises de [blader/humanizer](https://github.com/blader/humanizer) (licence MIT), lui-même fondé sur le guide [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) du WikiProject AI Cleanup.

## Licence

[MIT](LICENSE)
