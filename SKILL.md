---
name: french-humanizer
description: Réécrit une prose française qui sent l'IA pour qu'elle sonne écrite par une personne, sans changer ce qu'elle dit, en s'adaptant au registre (juridique, électronique, commentaire de code, lettre de motivation, courrier formel ou informel, encyclopédique, presse sportive, économique, automobile, littéraire ou buzz). À utiliser quand l'utilisateur dit « humanise », « rends ce texte moins IA », « ça sent ChatGPT », « réécris plus naturel », « enlève le style IA », « humaniser un texte IA », « humanizer en français », ou tape /french-humanizer.
---

# French humanizer (humaniseur de texte IA en français)

Cette skill rend humaine une prose française produite par un modèle de langue, sans changer ce qu'elle affirme. Elle reprend la méthode de blader/humanizer (MIT) et l'adapte au français : catalogue de motifs propre au français, et profils de registre tirés de textes humains publiés avant 2020, donc avant la diffusion massive des modèles génératifs.

Le but est un texte agréable pour un lecteur humain. Tromper un détecteur d'IA n'est pas un objectif : on n'ajoute jamais de fautes volontaires.

## Pourquoi ces motifs existent

Un modèle choisit la suite la plus probable, donc la formulation qui convient au plus grand nombre de lecteurs et de sujets. Une personne écrit pour un lecteur et un sujet précis. Chaque motif du catalogue est une trace de ce choix par défaut : une phrase qui signale l'importance au lieu d'apporter un fait, un rythme appliqué par règle, une banalité habillée en tournant décisif, un reste de conversation, une explication de ce que le lecteur sait déjà.

## Déroulé

1. **Identifier le registre.** Lire le texte et choisir le profil dans `references/registres.md` parmi douze : juridique, électronique et technique, commentaire de code, lettre de motivation, courrier formel, courrier informel, encyclopédique, presse sportive, presse économique, critique littéraire, presse automobile, presse buzz. Pour la presse, situer d'abord le texte sur l'échelle du plus léger au plus soutenu : une IA écrit tout au même niveau moyen, un journaliste s'ancre nettement à un bout. Si aucun ne colle, appliquer les règles générales. Si le registre est ambigu et que l'enjeu le justifie (lettre officielle, acte), demander. Lire la section du profil choisi avant de réécrire.
2. **Repérer les motifs.** Parcourir `references/motifs-ia-fr.md`, du plus fort au plus faible. Les cinq premiers justifient une correction dès la première occurrence. Ceux marqués *faible isolé* ne comptent que s'ils s'accumulent dans un même passage. Pour un long texte ou un dossier, `python3 scripts/scan.py fichier.md` donne un premier repérage chiffré (lexique, tirets, titres en capitales, connecteurs en série, uniformité des phrases).
3. **Premier jet.** Réécrire sans tenir la structure d'origine pour acquise : fusionner, couper, réordonner si le fond y gagne. Viser les traits observés du profil (longueur des phrases, vocabulaire, ponctuation, formules d'usage).
4. **Contrôle.** Relire le premier jet en se demandant ce qui fait encore « écrit par une IA » et le noter en deux ou trois lignes. Vérifier la fidélité : chaque nom, chiffre, date, citation, référence vient de la source ou de l'auteur.
5. **Version finale.** Corriger ce que le contrôle a relevé.

Quand l'utilisateur colle un texte, montrer : la liste courte des motifs trouvés (les plus forts d'abord), le premier jet, la critique, la version finale. Quand il donne un fichier, ne modifier que la prose : code, données, frontmatter, cibles de liens et citations restent intacts.

## Règles fixes

- **Ne rien inventer.** Si une phrase réclame un détail absent (chiffre, date, exemple vécu), demander plutôt que l'inventer. En juridique, ne jamais ajouter d'article, d'arrêt ou de date qui ne figure pas dans la source.
- **Accents et orthographe corrects**, majuscules accentuées comprises (À, É, Ç).
- **Pas de tiret cadratin (U+2014) ni de demi-cadratin (U+2013) en guise de ponctuation.** Remplacer par une virgule, un point, deux-points ou des parenthèses. Exception : l'échantillon de voix de l'auteur les utilise.
- **Ponctuation et typographie françaises** : voir la section suivante.
- **Garder le niveau de langue du registre.** Ne pas rendre familier un courrier formel ni guinder un message entre amis. Tutoiement ou vouvoiement : conserver celui de la source.
- **Ne pas aplatir les opinions.** Un texte personnel garde ses avis, ses partis pris et ses tics voulus. Un texte technique ou de référence reste neutre et sobre.

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
- Des détecteurs d'IA existent (GPTZero, ZeroGPT, Compilatio, Lucide.ai pour le français, Pangram…). Ils se trompent dans les deux sens, signalent aussi des textes humains, et la skill n'est pas réglée pour eux : un passage réussi au détecteur n'est pas un critère de qualité, et on ne réécrit jamais un texte pour faire baisser un score de détecteur au détriment du sens.

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

## Fichiers

- `references/motifs-ia-fr.md` : les 32 motifs, classés par force, avec un avant/après original pour chacun.
- `references/registres.md` : douze profils de registre, du plus léger au plus soutenu, avec les traits observés sur le corpus humain, les dérives typiques d'une IA et un exemple réécrit.
- `references/sources.md` : le corpus d'avant 2020 qui a servi à établir les profils (liens, dates, ce qui en a été tiré).
- `scripts/scan.py` : repérage automatique, sans dépendance, à lancer avec Python 3.
