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

# Information, opinion, commerce et documentation

Onze profils de plus, pour les textes qu'on rencontre le plus souvent au travail : informer (dépêche, presse régionale), convaincre (éditorial), vendre (fiche produit, page de marque), expliquer à des pros (presse B2B, article tech) documenter (README, documentation technique), tester (presse hi-fi) et s'entraider (forum). Corpus daté de 2021 au plus tard, avant la diffusion des assistants de rédaction grand public (fin 2022).

**Leçon commune.** Plusieurs motifs du catalogue apparaissent chez les humains de ce corpus : « pas X, mais Y » et chute en fragments dans un éditorial du Monde, triades et phrases nominales dans une page Apple, hyperboles en série dans un texte constructeur de 2013. Ce qui distingue l'humain : le procédé est rare, il porte un fait ou un chiffre précis, et il est propre à son sujet. Une IA l'applique partout, à vide, et de façon interchangeable.

---

## 13. Dépêche d'agence (AFP)

**Corpus :** dépêche AFP reprise par Le Figaro.fr, 16 juin 2017, sur une voiture chargée de bouteilles de gaz à Chasse-sur-Rhône (Isère).

**Observé chez les humains**
- Pyramide inversée : la première phrase dit qui, quoi, où, et finit par l'attribution (« a annoncé la préfecture »).
- Attribution systématique par des verbes neutres : a déclaré, a annoncé, a dit, a précisé. Le titre et la fonction de la personne citée sont donnés à la première mention.
- Citations courtes entre guillemets, insérées dans la phrase, souvent des fragments de déclaration officielle.
- Chiffres exacts (14 bouteilles de 13 kg, « vers 13h30 », « plus d'une centaine de gendarmes »), lieux situés pour un lecteur extérieur (« entre Vienne et Lyon sur les bords du Rhône »).
- Aucun adjectif de jugement, aucune conclusion : le dernier paragraphe donne le contexte chronologique, puis le texte s'arrête.

**Ce que fait une IA**
- Ouvre par le contexte ou l'émotion (« Une scène pour le moins inquiétante s'est déroulée… »), retarde le fait.
- Remplace l'attribution par des formules vagues (« selon les autorités », « d'après plusieurs sources »).
- Termine par une réflexion (« Cet événement rappelle l'importance de la vigilance… »).

**À viser :** fait principal et source dans la première phrase, une attribution par information, chiffres exacts, fin sur le contexte.

**Avant :**
> Une scène pour le moins inquiétante a secoué la petite commune de Valbrune ce vendredi. En effet, un véhicule suspect a mobilisé de nombreux moyens, soulignant ainsi la vigilance accrue des autorités dans un contexte sensible.

**Après :**
> Un véhicule contenant six bidons d'essence a été découvert vendredi à Valbrune (Drôme), entraînant l'évacuation de la gare pendant deux heures, a annoncé la préfecture. Son propriétaire a été placé en garde à vue, a précisé le parquet de Valence.

(Commune et faits fictifs.)

---

## 14. Presse quotidienne régionale

**Corpus :** rubrique faits divers du Journal du Gers, 30 août 2016.

**Observé chez les humains**
- Brèves d'une ou deux phrases, chacune ouverte par le nom de la commune en capitales.
- Empilement des circonstances : jour (« dimanche 28 août »), moment, lieu-dit ou quartier, intervenants (gendarmes, pompiers).
- Âges donnés seulement quand ils éclairent le fait (le conducteur de 21 ans, les randonneurs de 69 et 71 ans).
- Passé composé pour les faits, présent pour l'enquête en cours, futur pour la suite judiciaire.
- Vocabulaire administratif et de gendarmerie (préjudice, maîtrisé, convoqué), ton sobre, avec parfois une exclamation dans un récit de sauvetage.

**Ce que fait une IA**
- Écrit un paragraphe là où il faut une brève, ajoute de l'émotion et une morale (« un rappel que la prudence reste de mise sur nos routes »).
- Oublie le lieu précis ou la date, qui sont l'essentiel pour un lecteur local.

**À viser :** commune, date, lieu précis, fait, intervenants, suite. Une à trois phrases.

**Avant :**
> Un accident spectaculaire a eu lieu ce week-end dans notre belle région. Fort heureusement, grâce à l'intervention rapide et efficace des secours, le pire a pu être évité. Une piqûre de rappel sur l'importance de la prudence au volant.

**Après :**
> SAINT-ORENS. Dimanche vers 2 heures, une voiture conduite par un homme de 23 ans a quitté la route au lieu-dit Le Pradel et fini dans un fossé. Légèrement blessé, il a été conduit à l'hôpital d'Auch. Les gendarmes ont ouvert une enquête.

(Faits fictifs.)

---

## 15. Éditorial

**Corpus :** éditorial du Monde, « Brexit, dur ou doux, mais rapide », 14 juin 2017.

**Observé chez les humains**
- La thèse est posée dès le premier paragraphe et répétée sous des formes différentes jusqu'à la fin.
- Faits datés au service de l'argument : article 50, 29 mars 2019, référendum du 23 juin 2016, ouverture des négociations le 19 juin.
- Procédés rhétoriques assumés : questions, images (« larguer les amarres », « la falaise »), comparaison familière (payer son solde comme quand on quitte une copropriété), énumération en « D'abord… Ensuite… Enfin… ».
- On y trouve un « Il n'est pas question de… mais de… », un « on » éditorial (« On continue de penser que… ») et une chute en fragments (« Et partir. Vite. »). Ces motifs IA sont ici humains, parce qu'ils sont rares, qu'ils portent la thèse et qu'ils arrivent après les faits.
- Tirets d'incise et anglicismes entre guillemets avec leur traduction.

**Ce que fait une IA**
- Équilibre le pour et le contre sans trancher, ou tranche sans fait daté.
- Multiplie les chutes et les « pas X, mais Y » dans chaque paragraphe, et finit sur une généralité (« L'avenir nous le dira »).

**À viser :** une thèse claire, des faits datés qui la portent, un ou deux procédés forts au maximum, une fin qui reprend la thèse. Si l'auteur ne veut pas de tirets, les incises passent entre virgules ou parenthèses.

**Avant :**
> Le débat sur le télétravail soulève des questions essentielles. D'un côté, il offre une flexibilité appréciable ; de l'autre, il comporte des risques. Ce n'est pas seulement une question d'organisation, c'est une question de société. L'avenir dira quel modèle s'imposera.

**Après :**
> Le télétravail n'a pas besoin d'une loi de plus, il a besoin de règles d'entreprise écrites. Depuis mars, la moitié des salariés de bureau travaillent de chez eux sans savoir à quelle heure ils peuvent couper leur téléphone. Que chaque employeur publie ses horaires de joignabilité. Et s'y tienne.

(Chiffre fictif.)

---

## 16. Presse professionnelle B2B

**Corpus :** article du Journal du Net, rubrique DSI, sur le volume de données numériques prévu pour 2020, mis à jour le 19 juin 2017.

**Observé chez les humains**
- Chapeau qui donne le chiffre et la source en deux phrases (« C'est ce que montre cette infographie de notre partenaire »).
- Conditionnel pour les projections (« pourrait atteindre », « devraient renvoyer »), « Soit » pour convertir ou comparer (« soit 44 milliards de téraoctets », « Soit une hausse de 10 points comparé à 2013 »).
- Source précise de l'estimation (étude d'un cabinet nommé), base de comparaison datée.
- Jargon du secteur sans explication (mégadonnées, systèmes embarqués, terminaux mobiles), anglicismes courants (« digitales »), « Hexagone » pour la France. Typographie parfois relâchée (« 27% » sans espace).
- Article court, sans conclusion, suivi d'un renvoi vers un autre article.

**Ce que fait une IA**
- « Dans un contexte de transformation digitale accélérée, les entreprises font face à des défis majeurs… » sans un chiffre.
- Explique le jargon à un lectorat qui le connaît, conclut par des recommandations génériques.

**À viser :** chiffre, source, comparaison, conditionnel pour les projections ; pas d'explication de ce que le lecteur pro sait déjà ; s'arrêter quand l'information est donnée.

**Avant :**
> À l'heure où la transformation digitale s'accélère, la cybersécurité s'impose comme un enjeu majeur pour les entreprises. Face à des menaces toujours plus sophistiquées, il est essentiel d'adopter une approche proactive et globale.

**Après :**
> 38 % des PME françaises ont subi au moins une attaque par rançongiciel en 2019, selon le baromètre annuel du cabinet Ortalis. Soit huit points de plus qu'en 2018. Les sauvegardes hors ligne restent rares : 21 % des répondants en disposent.

(Cabinet et chiffres fictifs.)

---

## 17. Fiche produit e-commerce

**Corpus :** fiches LDLC.com archivées : écran Samsung 23 pouces SyncMaster S23C650D (référencé en juin 2013, page de février 2014, avec trois avis clients) et SSD SanDisk Plus 240 Go (février 2018).

**Observé chez les humains**
- Deux voix très différentes sur la même page.
  - **Le texte constructeur**, souvent traduit de l'anglais : impératifs en série (« Optimisez », « Profitez », « Testez »), hyperboles (« explosion de couleurs », « Avec ce moniteur, plus besoin de PC ! »), slogans en triade (« Performance, vitesse et silence ! »), et des incohérences humaines : unités mélangées (530 MB/S puis 530 Mb/S, °F avant °C), consommation en veille annoncée à 0,1 W dans le texte et 0,3 W dans la fiche technique.
  - **La fiche technique** : liste de champs normalisés, chiffres exacts, unités (cd/m², ms, mm, kg).
  - **Les avis clients** : concrets et datés par l'usage (« Voici une semaine que j'ai reçu cet écran »), abréviations (« temps de rép. », « pb »), « Bémols : » suivi de griefs précis (câble d'alimentation d'un mètre, trop court).
- Le marketing creux existait donc avant l'IA. Ce qui le rendait lisible : il s'appuyait sur une fiche technique précise juste en dessous.

**Ce que fait une IA**
- Produit un texte lisse et cohérent, sans aucune spécification : « Découvrez un écran au design élégant, idéal pour le travail comme pour les loisirs. Que vous soyez professionnel ou gamer… »
- Met des listes à étiquettes en gras (« **Design :** », « **Performance :** »), un paragraphe final d'appel à l'achat.

**À viser :** chaque bénéfice adossé à une caractéristique chiffrée (« angle de vision de 178° », « pied réglable en hauteur et pivot »), une phrase sur l'usage réel, pas de « Que vous soyez… ou… ». On n'imite pas les incohérences ni les fautes : on garde la précision.

**Avant :**
> Découvrez cet écran au design élégant et moderne, idéal pour le travail comme pour les loisirs. Que vous soyez professionnel ou passionné de jeux vidéo, il saura répondre à toutes vos attentes grâce à sa qualité d'image exceptionnelle.

**Après :**
> Dalle IPS de 24 pouces en 1920 x 1080, angles de vision de 178° : les couleurs ne virent pas quand on se penche. Le pied monte de 13 cm et pivote en mode portrait, pratique pour relire un long document. Câble HDMI fourni, pas de câble DisplayPort.

(Modèle et caractéristiques fictifs ; dans une vraie fiche, tout vient de la fiche technique.)

---

## 18. Page produit de marque

**Corpus :** page iPhone 12 d'apple.com/fr, archivée le 14 novembre 2020.

**Observé chez les humains**
- Accroches en phrases nominales et en triades (« Si petit. Si léger. Si puissant. »), jeux de mots (« Basculez du côté obscur » pour le mode Nuit, « H2O ? Ok. »), clins d'œil anglais (« Hello, OLED. »).
- Chaque slogan est immédiatement suivi d'un chiffre précis : 27 % de lumière en plus, résistance aux chutes multipliée par quatre, 2 Gbit/s, 11 % plus fin, 15 % plus petit, 16 % plus léger, renvois en note.
- Humour situé et concret (une vidéo Dolby Vision « très pratique lorsque votre chien vous fera pleurer de rire, ou d'émotion »).
- Vouvoiement, « nous » de la marque, tirets d'incise.

**Ce que fait une IA**
- Reprend la forme (fragments, triades, « Découvrez ») sans le chiffre ni la blague spécifique : « Puissant. Élégant. Intuitif. Découvrez une expérience révolutionnaire. »

**À viser :** si l'on garde un slogan en fragments, il doit être lié au produit (jeu de mots sur la fonction) et suivi d'un chiffre vérifiable. Sinon, une phrase simple vaut mieux.

**Avant :**
> Puissant. Élégant. Intuitif. Découvrez une expérience révolutionnaire qui redéfinit les standards de la mobilité moderne.

**Après :**
> Neuf heures d'autonomie. Assez pour l'aller-retour Paris-Marseille, film compris. La batterie de 4 500 mAh se recharge à moitié en vingt minutes.

(Produit et chiffres fictifs.)

---

## 19. README et documentation de projet

**Corpus :** README de jours-feries-france (Etalab, version 0.6.0 publiée sur PyPI le 8 mai 2020) et de pygrammalecte (version 0.1.0, 31 juillet 2020) ; commentaires d'OpenFisca France 48.0.0 (4 juillet 2019), en complément du profil 3.

**Observé chez les humains**
- Une phrase pour dire ce que fait le projet (« Cette librairie calcule les jours fériés en France »), une précision honnête sur ce qu'il n'est pas (« ce projet n'est pas Grammalecte, mais un « wrapper » »).
- Sections courtes et fonctionnelles : Installation, Usage ou Utilisation, Zones disponibles, Données, Sources. Pas de section « Pourquoi ce projet ? » ni « Fonctionnalités clés ».
- Exemples de code commentés en français à l'intérieur du bloc (« # Obtenir les jours fériés pour une année, pour la métropole »), avec le résultat attendu en commentaire (« # -> True »).
- Exemples drôles ou bricolés (« texte_bidon », phrases avec fautes volontaires pour tester le correcteur).
- Petites fautes et anglicismes (« librairie » pour bibliothèque, « fortement recommandé » mal accordé), lien vers la source officielle des données.
- Commentaires de code qui posent des questions ouvertes (« donc faut-il les nommer caseH1, caseH2… ? ») ou recopient le texte réglementaire.

**Ce que fait une IA**
- Titres à émojis (« 🚀 Fonctionnalités clés »), badges en série, paragraphe d'introduction promotionnel (« une solution puissante et intuitive pour… »), section « Contribuer » générique, conclusion « Bon codage ! ».

**À viser :** une phrase de description, installation, un exemple qui tourne avec son résultat, les limites connues, la source des données. Le README le plus court qui permet de s'en servir.

**Avant :**
> # 🚀 DateKit
> DateKit est une bibliothèque puissante et intuitive qui révolutionne la gestion des dates en Python. Grâce à son API élégante, elle vous permet de manipuler facilement vos dates.
> ## ✨ Fonctionnalités clés
> - **Simplicité :** une API facile à prendre en main

**Après :**
> # DateKit
> Calcule les jours ouvrés entre deux dates, jours fériés français compris.
> ```python
> from datekit import jours_ouvres
> jours_ouvres("2020-05-01", "2020-05-31")  # -> 18
> ```
> Ne gère pas encore les jours fériés locaux d'Alsace-Moselle.

(Projet fictif.)

---

## 20. Article tech sur l'IA (2020-2021)

**Corpus :** Blog du Modérateur, article sur GPT-3 et un blog écrit par IA, 20 août 2020 ; éditorial de Centre Inffo « Qui a peur de l'intelligence artificielle ? », 18 novembre 2020 ; article critique de LADN sur GPT-3, 1er mars 2021.

**Observé chez les humains**
- Chapeau de deux phrases : le fait, puis la suite attendue.
- Chiffres concrets et datés : lancement le 11 juillet 2020, une dizaine d'articles publiés, plus de 26 000 visiteurs en deux semaines, 175 milliards de paramètres comparés aux 1,5 milliard de GPT-2.
- Sources nommées et liées (MIT Technology Review, billet d'origine, blog d'OpenAI), citations de personnes identifiées.
- Intertitres en questions, enthousiasme tempéré par des réserves précises (biais, « putaclic », détournements) ; pas de conclusion formelle, fin sur la prochaine étape.
- Côté éditorial : ironie et autodérision (l'auteur se demande si son texte sera le dernier écrit par un humain), questions courtes (« Trop racoleur ? »), titres-jeux de mots.

**Ce que fait une IA**
- « L'intelligence artificielle révolutionne notre quotidien et ouvre des perspectives fascinantes, tout en soulevant des questions éthiques cruciales. »
- Aucun chiffre daté, aucune source, conclusion équilibrée générique.

**À viser :** le fait daté, le chiffre comparé, la source nommée, une réserve précise plutôt qu'un « enjeux éthiques » général.

**Avant :**
> L'intelligence artificielle révolutionne notre quotidien et ouvre des perspectives fascinantes. Toutefois, elle soulève également des questions éthiques cruciales qu'il convient d'aborder avec prudence.

**Après :**
> Le modèle a rédigé 40 fiches produits en une heure pour un site de jardinage ; l'équipe en a gardé 12 après relecture. Les 28 autres inventaient des dimensions ou mélangeaient deux plantes.

(Exemple fictif.)

---

## 21. Documentation technique

**Corpus :** page « ssh » du wiki de documentation ubuntu-fr, dernière modification le 8 novembre 2018 (version archivée de janvier 2019).

**Observé chez les humains**
- Une phrase d'objet (« Cette page présente les usages les plus courants de SSH »), puis renvoi vers une page avancée.
- Impératif et vouvoiement (« Saisissez dans un terminal la commande suivante »), la commande, puis ce qu'elle renvoie (« qui retourne une ligne du type : »).
- Exemples réalistes avec de faux noms d'utilisateur et des adresses concrètes, notes « N.B. », avertissements appuyés, parfois en capitales (« n'oubliez JAMAIS »).
- Humour ponctuel (le programme xeyes : « l'œil de Moscou vous regarde depuis votre écran local ! »), aveu de difficulté (« En résumé (car les paragraphes ci-dessous… peuvent sembler confus à certains) »).
- Texte collaboratif donc inégal : sections très détaillées à côté d'autres sommaires, quelques fautes d'accord, un tableau des directives de configuration avec valeur par défaut et effet.
- Notes de bas de page, renvois vers forums et sites externes, pas de conclusion.

**Ce que fait une IA**
- « Dans ce guide complet, nous allons explorer pas à pas… », étapes numérotées toutes de même taille, « Félicitations ! Vous avez configuré… ».
- Explique ce qu'est un terminal à un lecteur qui configure un serveur, omet le résultat attendu de la commande et les pièges réels.

**À viser :** objet en une phrase, commande, résultat attendu, piège connu, renvoi. Le ton peut rester humain (une remarque, un avertissement franc).

**Avant :**
> Dans ce guide complet, nous allons explorer étape par étape comment configurer facilement votre serveur. Suivez attentivement ces instructions pour une installation réussie !

**Après :**
> Installez le paquet `nginx`, puis vérifiez qu'il tourne :
> `systemctl status nginx` doit afficher « active (running) ». Si le port 80 est déjà pris (Apache installé par défaut sur certaines images), nginx refuse de démarrer : arrêtez Apache d'abord.

---

## 22. Presse hi-fi (banc d'essai)

**Corpus :** banc d'essai d'un amplificateur intégré, signé Lionel Schmitt, 21 novembre 2016 (PDF mis en ligne par un revendeur).

**Observé chez les humains**
- Fiche technique détaillée : puissance par canal sous 8 et 4 ohms, taux de distorsion, rapport signal sur bruit, transformateur torique et sa puissance en VA, marque des transistors et des condensateurs, nombre de cartes.
- Écoute organisée par paramètre (grave, médium, aigu, scène sonore, étagement des plans, timbres, dynamique) ou par disque précis.
- Vocabulaire du métier et images sensorielles (timbres fruités, veloutés), métaphores (un « pur-sang » de la marque).
- Première personne assumée, aveu de préférence (l'auteur a possédé un modèle antérieur), exclamations courtes au milieu de longues phrases.
- Défauts relevés concrètement (pas de sortie ligne fixe, connectique perfectible), prix donné, verdict franc.

**Ce que fait une IA**
- « Un son riche, détaillé et équilibré qui ravira les audiophiles les plus exigeants », sans un disque cité ni une mesure.
- Aucun défaut, ou un défaut de principe (« le prix peut sembler élevé »).

**À viser :** mesures et composants nommés, écoute rattachée à un disque ou à un passage précis, un avis personnel daté par l'expérience de l'auteur, un vrai défaut, le prix.

**Avant :**
> Cet amplificateur offre un son riche, détaillé et parfaitement équilibré qui ravira les mélomanes les plus exigeants. Sa scène sonore impressionnante et ses basses profondes en font un choix incontournable.

**Après :**
> Sur l'ouverture du quatrième mouvement, les contrebasses restent lisibles même au-delà de la mi-course du volume, là où mon ancien intégré commençait à confondre les pupitres. L'aigu est plus réservé : les cymbales manquent un peu d'air. À 1 500 €, la sortie casque aurait mérité mieux qu'un simple réseau de résistances.

(Avis fictif.)

---

## 23. Forum d'entraide grand public

**Corpus :** forum HardWare.fr, sujet « Demande conseil achat », 11 juin 2012, en complément des fils Futura-Sciences (profil 2) et CommentÇaMarche (profil 6).

**Observé chez les humains**
- Le demandeur écrit un long message décousu (budget, usage, hésitations), avec des fautes courantes (« j'aimerai », « apparement ») et un ton familier.
- Les réponses sont courtes : une question pour préciser, un lien vers le guide d'achat du forum, un avis tranché.
- Ironie ou sarcasme envers les demandes vagues, smileys en code texte, abréviations (sav, pc).
- Prix en euros arrondis, produits désignés de façon vague par le demandeur et précise par ceux qui répondent.
- Le fil se termine souvent sans conclusion, ou par un « merci » du demandeur.

**Ce que fait une IA**
- Répond comme un service client : « Excellente question ! Voici quelques conseils pour vous aider à faire le meilleur choix », liste à puces exhaustive, « N'hésitez pas si vous avez d'autres questions ».

**À viser :** réponse courte, une question si la demande est floue, un conseil précis avec un prix ou une référence, un renvoi si un guide existe. Tutoiement si le forum tutoie.

**Avant :**
> Excellente question ! Le choix d'un ordinateur dépend de nombreux facteurs. Voici quelques conseils pour vous aider à faire le meilleur choix en fonction de vos besoins et de votre budget.

**Après :**
> Tu fais quoi avec ? Si c'est bureautique et films, n'importe quel portable à 500 € avec un SSD fera l'affaire. Si tu joues, regarde le topic config du forum avant d'acheter, la carte graphique change tout.

---

## Registre non listé

Appliquer le catalogue de motifs et les règles fixes de `SKILL.md`, puis se demander qui lit, ce qu'il sait déjà et ce qu'il attend d'un texte de ce genre. Un échantillon de la voix de l'auteur, ou deux ou trois textes humains du même genre publiés avant 2020, donnent le meilleur repère.
