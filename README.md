# French Humanizer : humaniser un texte IA en français

Cette skill pour Claude Code et Claude.ai réécrit un texte français produit par une IA pour qu'on le croie écrit par une personne, sans changer ce qu'il affirme. C'est l'adaptation française de [blader/humanizer](https://github.com/blader/humanizer).

*In English: this Claude Code skill rewrites French text written by an AI so that it reads as if a person wrote it. It checks 32 patterns specific to French and follows 37 register profiles, drawn from human writing published mostly before 2020. You can add your own emails so rewrites match your voice, and a small Python script flags the patterns without rewriting anything.*

## Installation

```bash
git clone https://github.com/kofekod23/french-humanizer.git ~/.claude/skills/french-humanizer
```

Pour un seul projet, clonez dans `.claude/skills/french-humanizer`. Sur Claude.ai ou Claude Desktop, téléchargez le dépôt en ZIP et ajoutez-le comme skill dans les réglages. Les autres agents qui lisent les fichiers `SKILL.md` (Codex, Cursor, Gemini CLI…) peuvent l'utiliser tel quel.

## Utilisation

```
/french-humanizer

[texte à réécrire]
```

On peut aussi le demander en toutes lettres : « humanise ce courrier », « ce commentaire de code sent l'IA ».

> **Avant :** À l'ère du numérique, la gestion des sauvegardes constitue un enjeu majeur pour toute entreprise.
>
> **Après :** Une sauvegarde ne sert que si on sait la restaurer. Nous copions la base chaque nuit et, une fois par mois, nous restaurons la copie de la veille sur une machine de test.

Les détails de la version réécrite (chaque nuit, une fois par mois) doivent venir de l'auteur. S'ils manquent, la skill les demande au lieu de les inventer.

Si vous dites qui vous êtes (« je suis DAF », « je suis artisan électricien, j'écris à un client »), la réécriture prend le vocabulaire et le niveau de ce métier, et s'adapte au destinataire. Pour coller à votre propre style, joignez deux ou trois paragraphes que vous avez écrits.

## Ajouter vos textes

Dans Claude Code ou l'app desktop :

```
/french-humanizer add commercial
[collez le texte]
```

Le mot après `add` est le contexte (commercial, mail pro, juridique, LinkedIn…). Claude demande si vous avez écrit le texte ou si vous l'avez reçu, puis l'enregistre. `/french-humanizer contextes` montre ce qui est déjà enregistré.

En ligne de commande, le même ajout se fait avec le script :

```bash
python3 scripts/ajouter.py mail-envoyé mon-mail.txt --registre "mail pro"
python3 scripts/ajouter.py texte-modèle billet.md --registre "article"
python3 scripts/ajouter.py mail-reçu mail-client.txt --registre "mail client"
python3 scripts/ajouter.py texte-autre courrier-banque.txt --registre "courrier formel"
python3 scripts/ajouter.py profil
```

Vos propres textes (`mail-envoyé`, `texte-modèle`) servent à calibrer votre voix ; `profil` résume vos habitudes (longueur des phrases, tutoiement, ponctuation, formules de début et de fin). Les textes des autres (`mail-reçu`, `texte-autre`) servent d'exemples humains d'un registre et ne sont jamais imités comme votre voix. Ces textes restent sur votre machine, dans `~/.config/french-humanizer/corpus`, jamais dans le dépôt Git.

## Repérer les motifs sans réécrire

```bash
python3 scripts/scan.py article.md
python3 scripts/scan.py docs/*.md --fail-above 40   # pour la CI
```

Le script n'a aucune dépendance. Il liste les passages suspects et donne un score de 0 à 100, utile pour relire ; il ne dit pas qui a écrit le texte.

## Comment la skill a été construite

La méthode vient de blader/humanizer : repérer les motifs, écrire un premier jet, le critiquer, livrer la version finale. Le catalogue de motifs part du guide *Signs of AI writing* de Wikipédia et ajoute ce qui est propre au français : titres en capitales à l'anglaise, connecteurs en série, calques de l'anglais, nominalisations, tiret cadratin.

Les 37 profils de registre ont été établis en lisant des textes humains publiés avant 2020, jusqu'en 2021 pour quelques genres récents, donc avant la diffusion des assistants de rédaction fin 2022. Quand c'était possible, les pages ont été lues dans leur version archivée pour être sûr de leur date. Les types de sources :

- décisions de justice, documentation réglementaire et documentation de fabricants ;
- dépêches d'agence, presse nationale et régionale, éditoriaux ;
- presse spécialisée : sport, automobile, économie, hi-fi, presse professionnelle, presse légère ;
- critiques littéraires, musicales et de cinéma ;
- encyclopédie collaborative, documentation technique et README de projets libres, code source commenté ;
- fiches produits et pages de marque ;
- modèles de CV et de courriers ;
- articles de cadres et de développeurs sur les réseaux professionnels et les plateformes de blogs ;
- forums d'entraide, de consommateurs et de fans.

En lisant ces textes, on retrouve chez les humains plusieurs « tics d'IA » : un éditorial qui finit en deux mots, une page produit écrite en triades. Mais chez eux le procédé est rare et porte presque toujours un fait précis. La skill corrige donc le procédé appliqué à vide, pas chaque occurrence.

Le dépôt ne recopie aucun texte source. Il décrit des traits de style et donne des exemples réécrits, fictifs. Trois genres (remerciement après entretien, proposition commerciale, négociation entre entreprises) n'ont pas encore de corpus daté ; vos propres textes sont le meilleur moyen de les compléter.

## Limites

La skill ne cherche pas à tromper les détecteurs d'IA et n'ajoute jamais de fautes. Elle supprime par défaut les tirets cadratin et demi-cadratin, une règle de style plutôt qu'un signe d'écriture humaine, sauf si votre échantillon de voix en contient. Elle ne vérifie pas les faits du texte : elle les conserve et signale ceux qui manquent.

## Contenu

| Fichier | Rôle |
|---|---|
| `SKILL.md` | Déroulé, règles, typographie, « qui parle, à qui » |
| `references/motifs-ia-fr.md` | Les 32 motifs, avec un avant/après chacun |
| `references/registres.md` | Les 37 profils de registre |
| `references/sources.md` | Méthode de constitution du corpus |
| `scripts/scan.py` | Repérage des motifs |
| `scripts/ajouter.py` | Corpus personnel et profil de voix |

## Licence

MIT. Méthode et structure reprises de [blader/humanizer](https://github.com/blader/humanizer) (MIT).
