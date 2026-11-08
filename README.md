# French Humanizer : humaniser un texte IA en français

Skill pour Claude Code et Claude.ai qui réécrit un texte français produit par une IA pour qu'il se lise comme un texte humain, sans changer ce qu'il affirme. C'est l'adaptation française de [blader/humanizer](https://github.com/blader/humanizer).

*English: a Claude Code skill that rewrites AI-generated French text so it reads like human writing. 32 French-specific AI writing patterns, 37 register profiles built from human texts published before 2020, a local corpus for your own voice, and a Python scanner.*

## Installation

```bash
git clone https://github.com/kofekod23/french-humanizer.git ~/.claude/skills/french-humanizer
```

Pour un seul projet, clonez dans `.claude/skills/french-humanizer`. Sur Claude.ai ou Claude Desktop, téléchargez le dépôt en ZIP et ajoutez-le comme skill dans les réglages. Les autres agents qui lisent le format `SKILL.md` (Codex, Cursor, Gemini CLI…) l'utilisent tel quel.

## Utilisation

```
/french-humanizer

[texte à réécrire]
```

Ou simplement : « humanise ce courrier », « ce commentaire de code sent l'IA ».

> **Avant :** À l'ère du numérique, la gestion des sauvegardes constitue un enjeu majeur pour toute entreprise.
>
> **Après :** Une sauvegarde ne sert que si on sait la restaurer. Nous copions la base chaque nuit et, une fois par mois, nous restaurons la copie de la veille sur une machine de test.

Les détails concrets de la version réécrite viennent de l'auteur : s'ils manquent, la skill les demande au lieu de les inventer.

Si vous dites qui vous êtes (« je suis DAF », « je suis artisan électricien, j'écris à un client »), la réécriture prend le vocabulaire et le niveau de ce métier, et s'adapte au destinataire. Pour coller à votre propre style, joignez deux ou trois paragraphes que vous avez écrits.

## Ajouter vos textes

```bash
python3 scripts/ajouter.py mail-envoyé mon-mail.txt --registre "mail pro"
python3 scripts/ajouter.py texte-modèle billet.md --registre "article"
python3 scripts/ajouter.py mail-reçu mail-client.txt --registre "mail client"
python3 scripts/ajouter.py texte-autre courrier-banque.txt --registre "courrier formel"
python3 scripts/ajouter.py profil
```

Vos propres textes (`mail-envoyé`, `texte-modèle`) servent à calibrer votre voix ; `profil` résume vos habitudes (longueur des phrases, tutoiement, ponctuation, formules de début et de fin). Les textes des autres (`mail-reçu`, `texte-autre`) servent d'exemples humains d'un registre et ne sont jamais imités comme votre voix. Le tout reste sur votre machine, dans `~/.config/french-humanizer/corpus`, hors du dépôt Git. Dans Claude, `/french-humanizer ajouter mail-envoyé` puis collez le texte.

## Repérer les motifs sans réécrire

```bash
python3 scripts/scan.py article.md
python3 scripts/scan.py docs/*.md --fail-above 40   # pour la CI
```

Le script, sans dépendance, liste les passages suspects et donne un score de 0 à 100. C'est un outil de relecture : un score ne dit pas qui a écrit le texte.

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

Cette lecture a corrigé une idée reçue : plusieurs « tics d'IA » existent chez les humains, comme un éditorial qui finit en deux mots ou une page produit en triades. Chez l'humain, le procédé est rare et porte toujours un fait précis. La skill corrige donc le procédé appliqué à vide, pas chaque occurrence.

Le dépôt ne recopie aucun texte source : il contient des traits de style et des exemples réécrits, fictifs. Trois genres (remerciement après entretien, proposition commerciale, négociation entre entreprises) n'ont pas encore de corpus daté ; vos propres textes sont le meilleur moyen de les compléter.

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
