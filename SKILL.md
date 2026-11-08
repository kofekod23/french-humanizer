---
name: french-humanizer
description: Réécrit une prose française qui sent l'IA pour qu'on la croie écrite par une personne, sans changer ce qu'elle dit, selon 37 registres (courrier, mail, juridique, presse, critique, fiche produit, README, documentation, commentaire de code, CV, lettre de motivation, LinkedIn, forum…). À utiliser quand l'utilisateur dit « humanise », « rends ce texte moins IA », « ça sent ChatGPT », « réécris plus naturel », « enlève le style IA », « humaniser un texte IA », « humanizer en français », ou tape /french-humanizer.
---

# French humanizer (humaniseur de texte IA en français)

Cette skill réécrit une prose française produite par un modèle de langue pour qu'elle se lise comme un texte humain, sans changer ce qu'elle affirme. Elle reprend la méthode de blader/humanizer (MIT) et l'adapte au français, avec un catalogue de motifs propre au français et des profils de registre tirés de textes humains publiés avant 2020 (jusqu'en 2021 pour quelques genres), avant que les assistants de rédaction se répandent.

Le but est un texte agréable pour un lecteur humain. Tromper un détecteur d'IA n'est pas un objectif : on n'ajoute jamais de fautes volontaires.

## Pourquoi ces motifs existent

Un modèle choisit la suite la plus probable, donc la formulation qui convient au plus grand nombre de lecteurs et de sujets. Une personne écrit pour un lecteur et un sujet précis. Chaque motif du catalogue est une trace de ce choix par défaut : une phrase qui signale l'importance au lieu d'apporter un fait, un rythme appliqué par règle, une banalité habillée en tournant décisif, un reste de conversation, une explication de ce que le lecteur sait déjà.

## Déroulé

1. **Consulter le corpus personnel.** Si l'utilisateur a ajouté ses textes (voir « Ajouter vos textes »), lancer `python3 scripts/ajouter.py profil` et lire un ou deux textes de l'auteur du même registre que celui à réécrire (`python3 scripts/ajouter.py lister`). Ils priment sur le profil de registre pour la voix.
2. **Repérer qui parle.** Si l'utilisateur se présente (« je suis DAF », « je suis électricien », « je suis étudiante en alternance », « je suis CTO d'une startup », « j'écris à mon propriétaire »), appliquer la section « Qui parle, à qui » ci-dessous avant de choisir le registre.
3. **Identifier le registre.** Lire le texte et choisir l'un des 37 profils de `references/registres.md` (le sommaire est en tête du fichier). Pour la presse, situer d'abord le texte sur l'échelle du plus léger au plus soutenu : une IA écrit tout au même niveau moyen, un journaliste s'ancre nettement à un bout. Si aucun ne colle, appliquer les règles générales. Si le registre est ambigu et que l'enjeu le justifie (lettre officielle, acte), demander. Lire la section du profil choisi avant de réécrire.
4. **Repérer les motifs.** Parcourir `references/motifs-ia-fr.md`, du plus fort au plus faible. Les cinq premiers justifient une correction dès la première occurrence. Ceux marqués *faible isolé* ne comptent que s'ils s'accumulent dans un même passage. Pour un long texte ou un dossier, `python3 scripts/scan.py fichier.md` donne un premier repérage chiffré (lexique, tirets, titres en capitales, connecteurs en série, uniformité des phrases).
5. **Premier jet.** Réécrire sans tenir la structure d'origine pour acquise : fusionner, couper, réordonner si le fond y gagne. Viser les traits observés du profil (longueur des phrases, vocabulaire, ponctuation, formules d'usage).
6. **Contrôle.** Relire le premier jet en se demandant ce qui fait encore « écrit par une IA » et le noter en deux ou trois lignes. Vérifier la fidélité : chaque nom, chiffre, date, citation, référence vient de la source ou de l'auteur.
7. **Version finale.** Corriger ce que le contrôle a relevé.

Quand l'utilisateur colle un texte, montrer : la liste courte des motifs trouvés (les plus forts d'abord), le premier jet, la critique, la version finale. Quand il donne un fichier, ne modifier que la prose : code, données, frontmatter, cibles de liens et citations restent intacts.

## Règles fixes

- **Ne rien inventer.** Si une phrase réclame un détail absent (chiffre, date, exemple vécu), demander plutôt que l'inventer. En juridique, ne jamais ajouter d'article, d'arrêt ou de date qui ne figure pas dans la source.
- **Accents et orthographe corrects**, majuscules accentuées comprises (À, É, Ç).
- **Pas de tiret cadratin (U+2014) ni de demi-cadratin (U+2013) en guise de ponctuation.** Remplacer par une virgule, un point, deux-points ou des parenthèses. Exception : l'échantillon de voix de l'auteur les utilise.
- **Ponctuation et typographie françaises** : voir la section suivante.
- **Garder les anglicismes d'usage.** Les mots anglais couramment employés dans le métier ou la vie courante (backlog, sprint, crawl, SEO, pitch, week-end, noms d'outils, commandes) sont normaux en français : on les laisse. Le motif 21 ne vise que les calques maladroits (« faire du sens », « adresser un problème », « délivrer de la valeur »).
- **Garder le niveau de langue du registre.** Ne pas rendre familier un courrier formel ni guinder un message entre amis. Tutoiement ou vouvoiement : conserver celui de la source.
- **Ne pas aplatir les opinions.** Un texte personnel garde ses avis, ses partis pris et ses tics voulus. Un texte technique ou de référence reste neutre et sobre.

## Qui parle, à qui

Quand l'utilisateur dit qui il est (« je suis… », « en tant que… », « je travaille comme… ») ou à qui il écrit, la prose doit sonner comme un vrai membre de ce métier ou de cette situation.

1. **Relever trois choses** : le métier ou le rôle (DAF, électricien, DRH, développeur, étudiant, locataire), le niveau (junior, senior, dirigeant), et le destinataire (client, recruteur, pair, administration, ami).
2. **Choisir le profil de registre** le plus proche (par exemple : électricien qui écrit à un client, courrier formel ou fiche technique ; DAF qui publie sur LinkedIn, profil 32 ; CTO qui écrit un billet, profil 33 ; candidat junior, profils 4, 29 et 30).
3. **Prendre le vocabulaire réel du métier** au niveau de l'auteur : un électricien parle de section, de calibre et de différentiel 30 mA sans les expliquer à un confrère, mais les explique à un particulier ; un DAF parle de clôture, de BFR et de trésorerie ; un développeur de déploiement, de dette, de dépendances. Un senior cite des chiffres de périmètre (équipe, budget) ; un junior parle de ses tâches et de ce qu'il a appris.
4. **Ajuster au destinataire** : on n'écrit pas à un pair comme à un client, ni à un recruteur comme à un ami. Tutoiement ou vouvoiement selon l'usage du milieu (souvent tutoiement entre développeurs, vouvoiement avec un client ou une administration).
5. **Ne jamais inventer d'expertise.** Le rôle déclaré règle le ton et le vocabulaire, pas les faits : on n'ajoute ni chiffre, ni référence normative, ni réalisation que l'utilisateur n'a pas donnés. S'il en faut pour que le texte sonne juste, les demander.
6. **Si le rôle ne correspond à aucun profil**, partir du profil le plus proche et demander une ou deux phrases écrites par l'utilisateur, ou proposer d'en ajouter avec `scripts/ajouter.py`.

Exemple : « Je suis artisan électricien, réécris ce mail à un client qui conteste mon devis. » Profil négociation (27) plus courrier formel (5) : phrases courtes, postes du devis nommés (fourniture, pose, mise en conformité), raison technique d'un écart en une phrase compréhensible par un particulier, proposition concrète (une option moins chère, un délai), vouvoiement, pas de jargon non expliqué.

## Ponctuation et typographie

Dans les registres soignés (juridique, courrier formel, presse, encyclopédique, lettre de motivation) :

- **Jamais de tiret cadratin ni demi-cadratin** comme ponctuation, ni de trait d'union isolé entre deux espaces qui en tiendrait lieu. Le tiret reste admis en tête de ligne pour une réplique de dialogue ou un élément de liste.
- **Guillemets français** « » avec une espace insécable à l'intérieur ; guillemets anglais "…" seulement pour une citation à l'intérieur d'une citation.
- **Espace insécable avant** ; : ! ? et avant le signe % ; aucune espace avant le point et la virgule.
- **Points de suspension** : trois points, jamais plus, et pas de point final après eux.
- **Nombres** : espace entre les milliers (1 455 746), virgule décimale (4,40 m), espace entre le nombre et l'unité (12 V, 24 %). Ordinaux abrégés 1er, 2e, 16e (pas 2ème ni 16ème). Siècles en petites capitales ou en chiffres romains (XXe siècle).
- **Majuscules** : accentuées (À, É, Ç). Titres et intertitres en minuscules sauf la première lettre et les noms propres.
- **Deux-points** : pour annoncer une explication ou une liste, pas pour créer un effet (motif 10).
- **Point-virgule** : bienvenu pour relier deux propositions liées ou séparer les éléments d'une énumération longue, comme le font les humains en juridique et en critique.

Dans les registres relâchés (forum, message entre amis, buzz), garder la ponctuation de l'auteur, même irrégulière ; ne rien « corriger » qui fasse partie de la voix, et ne pas ajouter de fautes.

## Vérifier le résultat

- `python3 scripts/scan.py texte.md` sur la version finale : le score doit avoir nettement baissé. Il mesure les motifs du catalogue, pas l'auteur.
- Relire à voix haute : une phrase qu'on ne dirait jamais à ce lecteur-là est à revoir.
- Des détecteurs d'IA existent (GPTZero, ZeroGPT, Compilatio, Lucide.ai pour le français, Pangram…). Ils se trompent dans les deux sens et signalent aussi des textes humains. La skill n'est pas réglée pour eux : passer un détecteur ne dit rien de la qualité du texte, et on ne sacrifie jamais le sens pour faire baisser un score.

## Calibrer sur la voix de l'auteur

Si l'utilisateur fournit deux ou trois paragraphes de sa propre écriture, s'aligner dessus : longueur et rythme des phrases, mots favoris, ponctuation, tics délibérés (y compris des tirets s'il en met). L'échantillon prime sur le profil de registre quand ils divergent, sauf pour l'exactitude des faits et des références.

Exemple d'appel :

```
/french-humanizer

Voici un échantillon de mon écriture :
[2 ou 3 paragraphes]

Humanise ce texte (courrier formel) :
[texte]
```

## Ajouter vos textes

L'utilisateur peut enrichir la skill avec ses propres textes. Quand il dit « ajoute ce mail », tape `/french-humanizer ajouter mail-envoyé` ou colle un texte en demandant de l'ajouter, Claude enregistre le texte avec :

```
python3 scripts/ajouter.py <type> fichier.txt --registre "mail pro"
python3 scripts/ajouter.py <type> - --registre "article" < texte.txt
```

| Type | Ce que c'est | Rôle |
|---|---|---|
| `mail-envoyé` | un mail écrit par l'utilisateur | voix de l'auteur |
| `texte-modèle` | tout autre texte écrit par l'utilisateur | voix de l'auteur |
| `mail-reçu` | un mail écrit par quelqu'un d'autre | exemple humain de registre |
| `texte-autre` | article, courrier reçu, document | exemple humain de registre |

Les accents sont facultatifs dans le type (`mail-envoye` fonctionne). Si le type n'est pas donné, demander lequel des quatre ; si le registre n'est pas évident, le demander aussi.

- Les textes de l'auteur servent à calibrer la voix (longueur des phrases, ponctuation, tutoiement ou vouvoiement, formules d'ouverture et de fin). `python3 scripts/ajouter.py profil` en donne le résumé chiffré.
- Les textes de tiers servent d'exemples humains d'un registre (un vrai courrier d'administration, un vrai mail de client). Ils ne sont jamais imités comme voix de l'utilisateur.
- Le script signale un texte « de l'auteur » qui cumule des motifs IA : s'il a été rédigé ou retouché par une IA, il fausserait la calibration. Le dire à l'utilisateur et proposer `python3 scripts/ajouter.py supprimer <fichier>`.
- Le corpus est stocké en local dans `~/.config/french-humanizer/corpus` (ou `FRENCH_HUMANIZER_CORPUS`), jamais dans le dépôt : des mails contiennent des données personnelles. Ne pas citer un mail de tiers dans une réécriture : on s'en inspire pour le registre, on n'en recopie pas le contenu.

## Fichiers

- `references/motifs-ia-fr.md` : les 32 motifs, classés par force, avec un avant/après original pour chacun.
- `references/registres.md` : les 37 profils de registre, avec les traits observés sur le corpus humain, les dérives typiques d'une IA et un exemple réécrit.
- `references/sources.md` : le corpus d'avant 2020 (jusqu'en 2021 pour quelques genres récents) qui a servi à établir les profils (liens, dates, ce qui en a été tiré).
- `scripts/scan.py` : repérage automatique, sans dépendance, à lancer avec Python 3.
- `scripts/ajouter.py` : ajout de textes au corpus personnel, liste, profil de voix, suppression.
