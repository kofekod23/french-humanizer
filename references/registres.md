# Profils de registre

Chaque profil repose sur des textes humains publiés avant 2020 (détail dans `sources.md`). Les traits décrits sont des observations, pas des règles absolues : un texte humain les respecte souvent, une IA les rate presque toujours. Les exemples réécrits sont originaux, sauf les courts fragments de décision de justice, textes officiels librement reproductibles.

Pour chaque profil : ce qu'on observe chez les humains, ce que fait une IA, ce qu'il faut viser, un avant/après.

---

## 1. Juridique

**Corpus :** arrêt de la Cour de cassation, 1re chambre civile, 19 mars 2015, n° 13-28.776 (novation d'un contrat d'assurance vie). Style dit « des attendus », en vigueur jusqu'à la réforme de la rédaction des arrêts engagée en 2019, qui a introduit le style direct. Les deux styles sont humains ; repérer celui de la source et s'y tenir.

**Observé chez les humains**
- Phrases très longues, articulées par le point-virgule et la reprise en « que » : « que… ; qu'après… ; que l'administration fiscale leur a alors réclamé… ».
- Formules figées, jamais paraphrasées : « fait grief à l'arrêt de », « alors, selon le moyen », « Mais attendu que », « qu'elle en a exactement déduit », « le moyen n'est fondé en aucune de ses branches », « PAR CES MOTIFS ».
- Répétition assumée du terme technique : « rapport d'obligation » revient plusieurs fois, sans synonyme. Varier le vocabulaire serait une faute, car un synonyme pourrait désigner une autre notion.
- Références exactes et complètes : articles numérotés (« articles 1271 et 1273 du code civil »), dates en entier, juridiction d'origine.
- Aucun adjectif évaluatif, aucune emphase, aucun adverbe d'intensité. L'appréciation passe par le vocabulaire du contrôle : « pouvoir souverain d'appréciation », « exactement déduit ».
- « constitue », « emporte », « vaut » sont d'usage normal : le motif 19 ne s'applique pas ici.
- Hors décisions, la prose des praticiens (consultations, conclusions) reste sobre, au présent, avec des renvois précis et des paragraphes qui suivent un ordre logique (faits, problème, règle, application).

**Ce que fait une IA**
- Cite « la jurisprudence constante » ou « la loi » sans référence, ou invente un numéro d'article ou d'arrêt.
- Varie les termes par élégance (contrat, convention, accord, engagement dans le même paragraphe).
- Ajoute de l'emphase (« il est crucial de rappeler », « une décision majeure »), des listes à puces, une conclusion moralisante.

**À viser :** la précision et la stabilité du vocabulaire, des références exactes reprises de la source, aucune portée ajoutée. Ne jamais compléter une référence manquante : la signaler.

**Avant :**
> Cette décision majeure de la Cour de cassation vient rappeler un principe essentiel : l'ajout d'un co-souscripteur ne transforme pas fondamentalement le contrat. En effet, les juges ont considéré que l'accord initial perdurait, témoignant ainsi d'une volonté de sécurité juridique.

**Après :**
> La Cour de cassation juge que la souscription conjointe de l'épouse, en 1995, au contrat d'assurance vie souscrit par son mari en 1988 n'emporte pas novation : un rapport d'obligation complémentaire s'ajoute au premier sans l'éteindre. Le contrat conserve donc sa date de 1988 pour l'application du régime fiscal (Cass. 1re civ., 19 mars 2015, n° 13-28.776).

---

## 2. Électronique et technique

**Corpus :** fil du forum Futura-Sciences, rubrique Électronique, avril 2013, sur la chute de tension d'un régulateur LM317 ; fils plus anciens du même forum (2003 à 2007) ; fiche de montage d'alimentation variable (2006).

**Observé chez les humains**
- Messages courts, souvent une ou deux phrases. Questions directes : « et il y a quelle tension sur le point BR2 ? ».
- Chiffres partout, unités collées au nombre à la manière des électroniciens (12V, 300mA, 470µF, 220VA), ordres de grandeur avec tilde (« ~33V »), précision avouée (« de mémoire », « environ »).
- Calcul posé dans le texte, formule comprise, puis conclusion pratique : on donne C = I × dt / du, on trouve 170 µF, on conseille 470 µF « pour avoir de la marge ».
- Jargon d'atelier : condo, alim, transfo, dissipateur, découplage, « au plus près du circuit intégré ».
- Tutoiement, correction franche et sans détour : « Deux erreurs dans ton raisonnement », suivie d'une liste à tirets terminés par des points-virgules.
- Formules d'ouverture et de fin abrégées (Bjr, Salut, Cdlt, A+), fautes de frappe, signature humoristique. Le fil se clôt par le résultat mesuré et un « Merci à tous, problème résolu. »
- La prose de notice ou d'article technique est plus soignée mais garde la même logique : spécifications chiffrées d'abord, rôle de chaque composant ensuite, conseil pratique à la fin.

**Ce que fait une IA**
- Dilue le calcul dans des généralités (« le choix du condensateur est crucial pour garantir une alimentation stable et fiable »).
- Donne des valeurs sans le raisonnement, ou un raisonnement sans valeur.
- Met des titres, du gras, des émojis, et conclut sur « une alimentation performante et durable ».

**À viser :** le chiffre et l'unité avant l'adjectif, le calcul visible, la marge justifiée, le conseil d'atelier concret. Sur un forum, un ton direct ; dans une notice, la même concision avec une typographie soignée (espace entre nombre et unité : 12 V).

**Avant :**
> Le condensateur de filtrage joue un rôle absolument essentiel dans la stabilité de votre alimentation. Un dimensionnement inadapté peut entraîner des chutes de tension significatives. Il est donc crucial de choisir une valeur suffisamment élevée afin de garantir des performances optimales.

**Après :**
> Ton 47 µF est bien trop faible. Il te faut 15 V minimum à l'entrée du LM317 (12 V plus 3 V de chute), tu as environ 33 V après le pont, donc tu peux tolérer 18 V d'ondulation. Sous 0,3 A pendant 10 ms : C = 0,3 × 0,01 / 18 ≈ 170 µF. Mets 470 µF pour la marge, plus 100 nF soudé au plus près de la sortie du régulateur.

---

## 3. Commentaires de code

**Corpus :** code source Python d'OpenFisca France, version 24.0.0 (2018), modèle socio-fiscal maintenu par des développeurs francophones. Environ 2 900 lignes de commentaires, longueur médiane 35 caractères.

**Observé chez les humains**
- Commentaires courts, souvent sans verbe ou à l'impératif implicite : « Plus-values mobilières brutes (avant abattement) ».
- Le « on » de l'équipe pour décrire la démarche : « On prend en compte… », « On projette les revenus du foyer fiscal seulement sur le déclarant principal », « On fait l'hypothèse que… ».
- Le commentaire dit pourquoi ou dans quelle limite, pas ce que fait la ligne : « Attention ! Ne fonctionne pas pour les enfants du même âge (typiquement les jumeaux…) ».
- Marqueurs de travail en cours : TODO, FIXME, « à vérifier », avec la date ou la source (« Cette formule a seulement été vérifiée jusqu'au 2015-12-31 », « cf. art. 156 du CGI »).
- Abréviations du domaine (nb, PAC, CF, CGI), mélange naturel français et anglais, fautes de frappe et accents parfois oubliés.

**Ce que fait une IA**
- Paraphrase le code : « # Initialisation de la variable total à zéro ».
- Ouvre chaque docstring par « Cette fonction permet de… », remplit Args/Returns même pour une fonction triviale, ajoute des émojis et un ton enthousiaste.
- Ne signale ni les hypothèses, ni les cas non gérés, ni la source de la règle.

**À viser :** commentaire bref, sur l'intention, l'hypothèse, la limite connue ou la source ; rien sur ce que le code montre déjà. Docstring seulement quand l'interface n'est pas évidente. Ne pas ajouter de fautes : on garde l'orthographe correcte, on garde le ton.

**Avant :**
```python
def nb_enfants_a_charge(foyer):
    """
    Cette fonction permet de calculer de manière efficace le nombre d'enfants à charge.

    Args:
        foyer: Le foyer fiscal à analyser.
    Returns:
        int: Le nombre d'enfants à charge.
    """
    # Initialisation du compteur à zéro
    total = 0
    # Parcours de chaque personne du foyer
    for p in foyer.personnes:
        # Vérification si la personne est un enfant à charge
        if p.age < 18 or (p.age < 21 and p.etudiant):
            total += 1
    return total
```

**Après :**
```python
def nb_enfants_a_charge(foyer):
    # Au sens fiscal : moins de 18 ans, ou moins de 21 ans s'il poursuit ses études.
    # TODO : rattachement jusqu'à 25 ans pour les étudiants, non géré.
    return sum(1 for p in foyer.personnes
               if p.age < 18 or (p.age < 21 and p.etudiant))
```

Les seuils d'âge et la limite non gérée doivent venir du code ou de l'auteur ; on ne les invente pas.

---

## 4. Lettre de motivation

**Corpus :** brouillon de candidature spontanée soumis à relecture sur le forum Droit-Finances de CommentÇaMarche (fil clos en décembre 2012) et conseils des intervenants.

**Observé chez les humains**
- Plan classique en trois temps : situation actuelle, intérêt pour l'entreprise, compétences, puis demande d'entretien.
- Formules d'usage sincères mais toutes faites : « je me permets de vous proposer ma candidature », « je reste à votre entière disposition », formule de politesse complète.
- Défauts humains typiques : phrases longues, répétition d'un mot fétiche (ici « véritable »), compétences listées sans réalisation concrète, quelques fautes d'accord. Ce sont ces défauts que relèvent les relecteurs, avec un conseil récurrent : une accroche de quatre ou cinq lignes au plus, du concret.
- Ce qui sonne humain dans une bonne lettre : un fait vérifiable (un chiffre, un projet, un nom de produit de l'entreprise), une raison personnelle et précise de postuler, une seule qualité démontrée plutôt que cinq affirmées.

**Ce que fait une IA**
- Accumule les qualités en triade (« rigoureux, dynamique et passionné »), « fort de mon expérience », « convaincu que mon profil saura répondre à vos attentes », « rejoindre une entreprise innovante », « relever de nouveaux défis ».
- Flatte l'entreprise en termes génériques applicables à n'importe laquelle.
- Garde une longueur et un rythme parfaitement réguliers, sans aspérité.

**À viser :** moins d'adjectifs, plus de faits ; une phrase qui ne pourrait être envoyée qu'à cette entreprise ; formules d'usage brèves et correctes. Si les faits manquent, demander à l'auteur ses réalisations plutôt que les inventer.

**Avant :**
> Passionné par le digital et fort d'une solide expérience, je suis convaincu que mon profil dynamique et rigoureux saura répondre à vos attentes. Rejoindre une entreprise aussi innovante que la vôtre serait pour moi une véritable opportunité de relever de nouveaux défis.

**Après :**
> Depuis trois ans, je gère la fiche produit de 4 000 références chez un distributeur de matériel électrique ; j'y ai réduit d'un tiers le taux de retours liés à des descriptions erronées. Votre catalogue professionnel pose le même problème à plus grande échelle, et c'est sur ce point que je voudrais vous être utile.

(Les chiffres de l'exemple illustrent la forme ; dans un vrai texte, ils viennent de l'auteur.)

---

## 5. Courrier formel

**Corpus :** modèles de lettres administratives et de locataire publiés en ligne (Documentissime, page modifiée en octobre 2014 ; modèles de résiliation et de demande de travaux), conventions de la correspondance administrative française.

**Observé chez les humains**
- Bloc expéditeur, bloc destinataire, lieu et date (« À Paris, le 3 mars 2017 »), mention d'envoi (« Lettre recommandée avec accusé de réception »), ligne « Objet : » courte et factuelle, références du dossier.
- Appel « Madame, Monsieur, » ou titre précis, suivi d'une virgule.
- Un paragraphe par idée : les faits datés, le fondement (texte cité exactement : « article 6 de la loi n° 89-462 du 6 juillet 1989 »), la demande formulée avec un délai, les pièces jointes.
- Phrases complètes, ton neutre, aucune émotion affichée même dans un litige ; la fermeté passe par la précision et le délai.
- Formule de politesse complète qui reprend l'appel : « Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées. »

**Ce que fait une IA**
- Dilue la demande dans des politesses et des émotions (« J'espère sincèrement que vous comprendrez ma situation »).
- Cite le droit de façon vague (« conformément à la législation en vigueur ») ou ajoute des menaces sans fondement.
- Transforme la lettre en liste à puces, mélange « Cordialement » et formule longue.

**À viser :** faits, fondement exact s'il est fourni, demande, délai, pièces. Une seule formule de politesse, classique. Ne jamais ajouter une référence légale que l'auteur n'a pas donnée : proposer de la vérifier.

**Avant :**
> Je me permets de vous contacter car je rencontre actuellement un problème très préoccupant dans mon logement. En effet, une fuite importante impacte fortement mon quotidien. J'espère sincèrement que vous pourrez intervenir rapidement afin de trouver une solution adaptée. Cordialement.

**Après :**
> Madame, Monsieur,
>
> Depuis le 12 février, une fuite sous l'évier de la cuisine du logement que je loue au 4, rue des Lilas endommage le meuble et le parquet. Je vous en ai informé par téléphone le 14 février, sans suite à ce jour.
>
> Je vous demande de faire procéder à la réparation dans un délai de quinze jours à compter de la réception de ce courrier. Vous trouverez ci-joint trois photos datées.
>
> Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

(Dates et adresse : à reprendre de l'auteur.)

---

## 6. Courrier informel

**Corpus :** fil « Modèle de mot pour prévenir les voisins » du forum CommentÇaMarche (dernière réponse en juillet 2011), commentaires de LinuxFr.org sur la sortie de Grammalecte 0.2.

**Observé chez les humains**
- Phrases courtes, exclamations, questions, points de suspension. Abréviations familières (« anniv' », « lol », « merci d'avance »).
- Humour et ironie : le décalage entre une formule guindée et un message trivial fait rire ; on taquine (« Au pif ? »).
- Typographie relâchée : minuscule en début de message, espaces avant la ponctuation irréguliers, accents parfois oubliés. Pas d'émojis dans ces fils anciens, quelques smileys texte.
- Fin abrupte ou signature au prénom seul ; « Cordialement » apparaît mais sonne déjà formel.
- Un mot aux voisins réussi : court, signé, concret (quoi, quand, jusqu'à quelle heure), une excuse simple et une touche d'humour.

**Ce que fait une IA**
- Écrit un message amical avec la structure d'un courrier formel : accroche chaleureuse, trois paragraphes équilibrés, remerciement final appuyé.
- Accumule les formules affectueuses génériques (« J'espère que tu vas bien et que tout se passe à merveille de ton côté ! »), les émojis, les points d'exclamation à chaque phrase.

**À viser :** un détail précis par paragraphe, des phrases de longueur très variable, des digressions possibles, une fin brève (« Bises », « À plus », le prénom). Garder la typographie de l'auteur si elle est relâchée, sans y ajouter de fautes.

**Avant :**
> Chers voisins, j'espère que vous allez bien ! 😊 Je tenais à vous informer que j'organise une petite fête samedi soir pour célébrer mon anniversaire. Il est possible qu'il y ait un peu de bruit, et je m'en excuse par avance. N'hésitez surtout pas à venir me voir si cela vous dérange ! Merci infiniment pour votre compréhension 🙏

**Après :**
> Bonjour à tous,
> Samedi soir je fête mes 30 ans à la maison, ça risque de faire un peu de bruit jusque vers 1 h. Désolée d'avance ! Si ça devient pénible, sonnez au 3e gauche, je baisserai. Et si vous voulez passer boire un verre, la porte est ouverte.
> Claire

(Âge, heure, étage et prénom : à reprendre de l'auteur.)

---

# Presse et encyclopédie : du plus léger au plus soutenu

Les six profils suivants couvrent la presse et l'encyclopédie. Ils vont du registre le plus familier (buzz) au plus soutenu (critique littéraire). Repérer d'abord où se situe le texte sur cette échelle : une IA écrit presque tout au même niveau moyen, poli et neutre, alors qu'un journaliste humain s'ancre nettement à un bout ou à l'autre.

| Niveau | Registre | Marque principale |
|---|---|---|
| Très léger | 12. Presse buzz et insolite | Phrases courtes, interpellation, titres-blagues |
| Léger | 8. Presse sportive | Surnoms, métaphores, minutes entre parenthèses |
| Courant | 11. Presse automobile | Fiche technique chiffrée, comparaison aux rivales |
| Courant soutenu | 9. Presse économique | Chiffre, comparaison, nuance, explication du jargon |
| Neutre documenté | 7. Encyclopédique | Dates, chiffres, références, aucune adresse au lecteur |
| Soutenu | 10. Critique littéraire | Syntaxe travaillée, verdict assumé, citations commentées |

---

## 7. Encyclopédique (Wikipédia)

**Corpus :** article « Citroën DS » de Wikipédia en français, version du 3 avril 2019 (oldid 158110069).

**Observé chez les humains**
- Densité factuelle très forte : dates précises (« le 7 octobre 1955 »), chiffres de production, cylindrées, puissances en ch SAE et ch DIN, prix d'enchères, noms propres à chaque phrase.
- Phrases longues, chargées de parenthèses et d'incises qui ajoutent une précision (« (uniquement les deux premières années) »), énumérations interminables séparées par des virgules ou des points-virgules.
- Présent de narration dominant, avec des passages au futur historique et au passé simple selon les contributeurs : le texte n'est pas homogène, car plusieurs mains l'ont écrit.
- Appels de note après les faits, références datées (périodiques, ouvrages avec ISBN et pages).
- Le neutre n'est pas parfait : l'article humain laisse passer quelques jugements (« splendide », « révolutionnaire », « incontournable ») et même « Il convient d'ajouter ». Ces mots existent donc chez les humains ; ce qui signe l'IA, c'est leur accumulation sans faits autour.
- Sections inégales : certaines très fouillées, d'autres réduites à une liste. Pas de conclusion, l'article s'arrête sur la dernière section.

**Ce que fait une IA**
- Équilibre artificiellement les sections, ajoute une introduction et une conclusion qui résument.
- Remplace les faits par de la portée (« un symbole intemporel de l'innovation française »), multiplie les participes de clôture (« …, témoignant de son influence durable »).
- Cite « de nombreux experts » au lieu de la source précise.

**À viser :** un fait vérifiable par phrase, la source après le fait, aucun résumé de portée. On garde les parenthèses de précision. On ne neutralise pas un jugement s'il est attribué à une source.

**Avant :**
> La Citroën DS est une automobile emblématique qui a profondément marqué l'histoire de l'industrie automobile française. Véritable symbole d'innovation, elle témoigne du génie technique de son époque et continue de fasciner les passionnés du monde entier.

**Après :**
> La Citroën DS est produite de 1955 à 1975. Présentée au salon de Paris le 7 octobre 1955, elle reçoit 12 000 commandes dès la première journée. Elle est la première voiture de série à généraliser une centrale hydraulique pour la direction, le freinage et la suspension.

---

## 8. Presse sportive

**Corpus :** article de Maxifoot sur les meilleurs joueurs de Ligue 1, 29 novembre 2004.

**Observé chez les humains**
- Alternance très marquée : longues phrases descriptives, puis formule courte et percutante, parfois exclamative.
- Jargon technique du jeu (reprise, demi-volée, double parade, arrêts de jeu, passe décisive) et métaphores (avancer « inexorablement », jouer « sous l'éteignoir »).
- Surnoms et périphrases pour éviter de répéter le nom : un joueur devient « le géant suédois », un milieu infatigable « le petit homme aux trois poumons », une équipe ses habitants (« les Istréens »).
- Minutes entre parenthèses (« (5e) »), âge et club entre parenthèses à la présentation du joueur, abréviations (pts, L1), ordinaux (16e).
- Ton engagé, élogieux ou ironique ; le journaliste prend parti.

**Ce que fait une IA**
- Raconte le match de façon neutre et équilibrée, sans parti pris ni image.
- Abuse de « véritable démonstration », « performance XXL », « au terme d'un match à suspense », et conclut par une morale sur l'esprit d'équipe.

**À viser :** le fait de jeu précis (qui, quelle minute, quel geste), une image de journaliste par paragraphe au plus, un avis tranché, la périphrase pour varier les noms.

**Avant :**
> Au terme d'un match riche en émotions, Saint-Aubin s'est imposé grâce à une véritable démonstration collective. Cette victoire témoigne de la solidité retrouvée de l'équipe, qui confirme ainsi son statut de prétendant au titre.

**Après :**
> Saint-Aubin a tué le match en dix minutes. Morel ouvre sur coup franc (12e), Diallo double la mise d'une frappe croisée (21e). Derrière, Ferrand n'a eu qu'un arrêt à faire. Les Albins restent à trois points du leader.

(Club et joueurs fictifs. Dans un vrai texte, noms et minutes viennent de la source.)

---

## 9. Presse économique

**Corpus :** article de La finance pour tous sur les bénéfices du CAC 40, 29 mars 2018 (vulgarisation économique).

**Observé chez les humains**
- Chapeau court qui donne le chiffre principal et sa cause, puis corps en intertitres qui vont de la donnée au contexte puis à l'interprétation.
- Chiffres en notation française : virgule décimale, espace avant % (« 24 % »), « milliards d'euros » en toutes lettres, comparaison systématique avec une année antérieure.
- Jargon employé puis expliqué dans la phrase suivante (bénéfice net cumulé, marge, dividende).
- Nuance explicite : la bonne nouvelle est « à relativiser », les profits restent sous leur niveau d'avant 2008.
- Pas de conclusion formelle : l'article finit sur un dernier point d'analyse.

**Ce que fait une IA**
- Parle de « dynamique positive », de « résilience », de « contexte économique incertain » sans chiffre.
- Donne un chiffre sans point de comparaison, ou un pourcentage sans base.
- Clôt sur une perspective générale (« l'avenir dira si cette tendance se confirme »).

**À viser :** chiffre, base de comparaison, cause, limite. Une phrase d'explication pour chaque terme technique si le lectorat est grand public ; aucune pour un lectorat spécialisé.

**Avant :**
> Le groupe Vernet affiche une dynamique particulièrement positive, témoignant de leur remarquable résilience dans un contexte économique en constante évolution. Cette performance solide ouvre des perspectives encourageantes pour l'avenir.

**Après :**
> Le groupe Vernet a dégagé 412 millions d'euros de bénéfice net en 2017, 18 % de plus qu'en 2016. La hausse est à relativiser : en 2007, avant la crise, il gagnait davantage.

(Entreprise et chiffres fictifs. Dans un vrai texte, ils viennent de la source.)

---

## 10. Critique littéraire (registre soutenu)

**Corpus :** supplément « Des livres » du quotidien Le Monde, 2 septembre 2005 (rentrée littéraire).

**Observé chez les humains**
- Grande variété de longueur : périodes longues à incises et subordonnées, puis phrase nominale sèche qui tranche (un « Pas de quoi s'attarder. » après un paragraphe ample).
- Syntaxe travaillée : inversions (« Dans leur cohorte dispersée, on signale… »), points-virgules pour opposer, subjonctif dans les tournures de nuance.
- Vocabulaire soutenu, métaphores filées, mais touches familières ou ironiques volontaires qui empêchent la pompe.
- Verdict assumé (« un bon roman », « un livre rarissime ») ou réserve précise (« on aurait préféré… »), jamais un éloge générique.
- Citations du livre, parfois longues, suivies d'un commentaire qui en tire le sens.
- Attaque vive (« Lire Houellebecq, enfin. ») et chute sur une image qui prolonge la lecture.

**Ce que fait une IA**
- Accumule les qualificatifs creux : « une plume ciselée », « un récit poignant », « une œuvre puissante qui interroge notre rapport au monde », « une lecture incontournable ».
- Ne cite pas le texte, ou le cite sans le commenter.
- Garde un rythme régulier, sans phrase courte qui tranche, et conclut par une recommandation de lecture.

**À viser :** une thèse sur le livre dès l'attaque, une citation courte commentée, un vrai reproche ou un vrai éloge précis, des ruptures de rythme. Le registre soutenu n'interdit pas une phrase de quatre mots ; il les rend plus efficaces.

**Avant :**
> Dans ce roman poignant, l'auteur nous offre un récit puissant qui interroge avec finesse notre rapport à la mémoire. Servi par une plume ciselée, ce texte bouleversant s'impose comme une lecture incontournable de cette rentrée littéraire.

**Après :**
> Le narrateur oublie tout, sauf ce qu'il voudrait oublier : c'est le ressort du livre, et l'auteur le tend jusqu'à la dernière page sans jamais l'expliquer. On regrette le chapitre central, trop long, où la phrase s'écoute. Le reste tient.

---

## 11. Presse automobile

**Corpus :** dossier de L'argus sur le Peugeot 3008 de deuxième génération (publié en mai 2014, mis à jour en février 2016) ; essai du Peugeot 3008 (2009-2016) sur Fiches-Auto.fr.

**Observé chez les humains**
- Fiche technique dans le texte : cylindrée en cm³ (1 199 cm³), puissance en ch, plateforme (EMP2), boîte (automatique à convertisseur, six rapports), dimensions en mètres (4,40 m contre 4,37 m), chiffres de ventes arrondis.
- Comparaison systématique avec la gamme maison et les concurrentes, citées par leur nom.
- Ton informatif avec un avis : on salue un point fort, on relève un point faible, souvent avec une réserve modérée (« perfectible », « rien de très grave »).
- Chez l'essayeur passionné : « on » et « vous », expressions familières (« crapahuter », « prendre son pied »), points de suspension, liste qualités et défauts en fragments, verdict final qui laisse sa part au goût.
- Jeux de mots surtout dans les intertitres (« Près du corps »), rarement dans le titre.

**Ce que fait une IA**
- Parle de « design audacieux », « habitacle raffiné », « expérience de conduite dynamique », « motorisations performantes » sans chiffre.
- Ne nomme pas les concurrentes, ou toutes à la fois sans comparaison réelle.

**À viser :** le chiffre et l'unité, la rivale nommée, un défaut réel, un verdict. Les intertitres peuvent jouer sur les mots, le corps du texte reste précis.

**Avant :**
> Avec son design audacieux et son habitacle raffiné, le nouveau SUV offre une expérience de conduite dynamique et confortable. Ses motorisations performantes et efficientes en font un choix idéal pour les familles modernes.

**Après :**
> Le Kerval gagne 8 cm en longueur (4,45 m) et reprend la plateforme de la berline de la marque. Le coffre atteint 520 litres, autant que ses deux principales rivales. Le trois-cylindres de 130 ch suffit en ville mais s'essouffle à pleine charge sur autoroute.

(Modèle et données fictifs. Dans un vrai texte, chiffres et rivales nommées viennent de la source.)

---

## 12. Presse buzz et insolite (registre très léger)

**Corpus :** article de Demotivateur sur les titres de presse les plus drôles de 2015 (16 novembre 2015) ; article de L'Avenir (Belgique) sur les pires selfies de 2015 (13 décembre 2015).

**Observé chez les humains**
- Phrases courtes, souvent de 8 à 15 mots, paragraphes d'une à trois phrases.
- Expressions idiomatiques (« tirer le portrait », « en prendre pour son grade »), vocabulaire courant, peu ou pas de technique.
- Interpellation directe du lecteur (« vous »), « nous » éditorial, rappel des articles précédents.
- Humour par les intertitres-blagues (« Souriez, ça vient d'exploser ! », « Direction la prison ») plus que par le corps du texte ; ironie légère, pas méchante.
- Points d'exclamation surtout dans les titres et intertitres. Pas d'émojis dans ces articles de 2015.
- Liste numérotée, chaque entrée réduite à son anecdote ; aucune conclusion, l'article finit sur le dernier exemple ou un renvoi.

**Ce que fait une IA**
- Met des émojis partout, un point d'exclamation à chaque phrase, des « Accrochez-vous ! », « Vous n'allez pas en croire vos yeux ! ».
- Ajoute une introduction qui annonce la liste et une conclusion qui invite à commenter et partager.

**À viser :** l'anecdote d'abord, la blague dans l'intertitre, des phrases très courtes, un « vous » naturel, et on s'arrête quand c'est fini.

**Avant :**
> Accrochez-vous, car voici les selfies les plus fous de l'année ! 😱 Vous n'allez tout simplement pas en croire vos yeux ! Découvrez sans plus attendre notre sélection incroyable qui va vous faire rire aux éclats ! 🤣

**Après :**
> **Direction la prison**
> Il a posé tout sourire devant la vitrine qu'il venait de casser. La photo a fait le tour de Facebook, puis du commissariat.

(Anecdote à reprendre de la source.)

---

## Registre non listé

Appliquer le catalogue de motifs et les règles fixes de `SKILL.md`, puis se demander qui lit, ce qu'il sait déjà et ce qu'il attend d'un texte de ce genre. Un échantillon de la voix de l'auteur, ou deux ou trois textes humains du même genre publiés avant 2020, donnent le meilleur repère.
