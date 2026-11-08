#!/usr/bin/env python3
"""Repérage des motifs d'écriture IA dans un texte français.

Ne réécrit rien : signale les passages suspects et donne un score indicatif
(0 = rien à signaler, 100 = saturé). Un score bas ne prouve pas qu'un humain
a écrit le texte, un score haut ne prouve pas le contraire.

Usage :
    python3 scan.py fichier.md [autre.txt ...] [--json] [--fail-above 40]
    cat texte.txt | python3 scan.py -
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

TIRET_CADRATIN = "\u2014"
TIRET_DEMI = "\u2013"

# Lexique : (motif regex, poids, numéro du motif dans motifs-ia-fr.md)
LEXIQUE = [
    (r"\bvéritable(s)?\b", 2, 14),
    (r"\bincontournable(s)?\b", 2, 14),
    (r"\bcrucia(l|le|ux|les)\b", 2, 14),
    (r"\benjeu(x)? majeur(s)?\b", 3, 14),
    (r"\blevier(s)?\b", 2, 14),
    (r"\bécosystème(s)?\b", 2, 14),
    (r"\bpaysage (numérique|digital|actuel|concurrentiel)\b", 3, 14),
    (r"\bà l'ère (du numérique|de l'IA|du digital)\b", 3, 14),
    (r"\bdans un monde (en constante évolution|où)\b", 3, 14),
    (r"\ben constante évolution\b", 2, 14),
    (r"\bplus que jamais\b", 2, 14),
    (r"\bpierre angulaire\b", 3, 14),
    (r"\batout(s)? majeur(s)?\b", 2, 14),
    (r"\bmettre en lumière|met en lumière|mettent en lumière\b", 2, 14),
    (r"\btémoign(e|ent|ant) d", 2, 16),
    (r"\bs'inscri(t|vent|re) dans une (démarche|logique|dynamique)\b", 3, 14),
    (r"\bnavigu(er|ez) (les|ces|dans les) (défis|enjeux)\b", 3, 14),
    (r"\bdémystifi", 2, 14),
    (r"\brévolutionn(e|er|ent|aire)\b", 2, 14),
    (r"\bsans précédent\b", 2, 14),
    (r"\bboost(er|e|ez)\b", 2, 14),
    (r"\bmarquant un tournant\b", 3, 15),
    (r"\bl'avenir s'annonce\b", 3, 15),
    (r"\bniché(e)? (au cœur|dans)\b", 3, 17),
    (r"\bselon (les|de nombreux) experts\b", 3, 18),
    (r"\bde nombreuses études (montrent|démontrent)\b", 3, 18),
    (r"\bse positionne comme\b", 2, 19),
    (r"\bse veut\b", 1, 19),
    (r"\bpermet(tent)? de (favoriser|garantir|optimiser|faciliter)\b", 2, 20),
    (r"\bfaire du sens\b|\bfait du sens\b", 3, 21),
    (r"\badresser (un|le|ce|les) (problème|enjeu|sujet)", 3, 21),
    (r"\bimpact(e|ent|er)\b", 1, 21),
    (r"\ben termes de\b", 1, 21),
    (r"\bassurez-vous de\b", 2, 21),
    (r"\bau final\b", 1, 21),
    (r"\b(véritablement|pleinement|considérablement|profondément)\b", 1, 22),
    (r"\bplongeons\b|\bentrons dans le vif\b|\bsoyons honnêtes\b", 3, 4),
    (r"\bcontrairement à ce que l'on pourrait (penser|croire)\b", 3, 5),
    (r"\bon pourrait être tenté\b", 3, 5),
    (r"\bau fond, ce qui compte\b", 3, 3),
    (r"\bet c'est (là|bien là) toute la différence\b", 3, 2),
    (r"\btout est dit\b", 2, 2),
    (r"\bexcellente question\b|\bj'espère que (cela|ça) (vous |t')aide\b", 4, 27),
    (r"\bn'hésitez (pas|surtout pas) à\b", 2, 27),
    (r"\bdans cet article,? nous (allons|verrons)\b", 3, 29),
    (r"\bil (est|convient de) (important de )?(noter|souligner|rappeler) que\b", 3, 29),
    (r"\bil est (essentiel|crucial|primordial) de\b", 2, 29),
    (r"\ben (conclusion|somme|résumé),", 2, 30),
    (r"\bune chose est sûre\b", 3, 30),
    (r"\bqu'il s'agisse de\b|\bque ce soit (pour|en termes)\b", 1, 6),
    (r"\bfort(e)? de (mon|ma|mes|son|sa|ses|notre|nos)\b", 2, 14),
    (r"\brelever de nouveaux défis\b", 3, 14),
]

STRUCTURES = [
    (r"\bce n'est pas (seulement |juste |simplement |qu')?[^.;:!?]{2,80}[,;:] c'est\b", 4, 1, "Pas X, mais Y"),
    (r"\bil ne s'agit pas (seulement |uniquement |simplement )?de [^.;!?]{2,80} mais\b", 4, 1, "Pas X, mais Y"),
    (r"\bnon pas [^.;!?]{2,60} mais\b", 2, 1, "Pas X, mais Y"),
    (r"(^|\. )(Le résultat|Le constat|La raison|La clé|Le secret|La réponse) ?:", 3, 10, "Deux-points dramatique"),
    (r"\?\s*(Elle|Il|C'est|La réponse)\b", 2, 4, "Question puis réponse mise en scène"),
]

CONNECTEURS = ("par ailleurs", "en outre", "de plus", "ainsi", "enfin", "en effet",
               "cependant", "néanmoins", "toutefois", "d'autre part", "en somme",
               "en conclusion", "pour conclure", "finalement")

EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐✅]")
GRAS_ETIQUETTE = re.compile(r"\*\*[^*\n]{1,40}\s?:\*\*|\*\*[^*\n]{1,40}\*\*\s?:")
MOTS_OUTILS = {"de", "du", "des", "la", "le", "les", "et", "à", "au", "aux", "en",
               "un", "une", "pour", "par", "sur", "dans", "avec", "ou", "d'", "l'"}


@dataclass
class Constat:
    motif: int
    libelle: str
    extrait: str
    ligne: int
    poids: int


@dataclass
class Rapport:
    fichier: str
    mots: int = 0
    phrases: int = 0
    longueur_moyenne: float = 0.0
    coefficient_variation: float = 0.0
    constats: list[Constat] = field(default_factory=list)
    score: int = 0


def numero_ligne(texte: str, position: int) -> int:
    return texte.count("\n", 0, position) + 1


def extrait(texte: str, debut: int, fin: int, marge: int = 30) -> str:
    a, b = max(0, debut - marge), min(len(texte), fin + marge)
    return " ".join(texte[a:b].split())


def retirer_code(texte: str) -> str:
    """Remplace les blocs de code par des espaces pour garder les numéros de ligne."""
    def blanc(m: re.Match) -> str:
        return re.sub(r"[^\n]", " ", m.group(0))
    texte = re.sub(r"```.*?```", blanc, texte, flags=re.S)
    return re.sub(r"`[^`\n]+`", blanc, texte)


def titre_en_capitales(titre: str) -> bool:
    mots = [m for m in re.findall(r"[\wÀ-ÿ'-]+", titre) if m.lower() not in MOTS_OUTILS]
    mots = [m for m in mots[1:] if len(m) > 2 and not m.isupper()]  # ignore le 1er mot et les sigles
    if len(mots) < 2:
        return False
    capitales = sum(1 for m in mots if m[0].isupper())
    return capitales / len(mots) >= 0.6


def analyser(nom: str, brut: str) -> Rapport:
    texte = unicodedata.normalize("NFC", retirer_code(brut)).replace("\u2019", "'")  # apostrophe typographique
    r = Rapport(fichier=nom)
    bas = texte.lower()

    for motif, poids, num in LEXIQUE:
        for m in re.finditer(motif, bas):
            r.constats.append(Constat(num, "Vocabulaire", extrait(texte, m.start(), m.end()),
                                      numero_ligne(texte, m.start()), poids))

    for motif, poids, num, libelle in STRUCTURES:
        for m in re.finditer(motif, texte, flags=re.I | re.M):
            r.constats.append(Constat(num, libelle, extrait(texte, m.start(), m.end()),
                                      numero_ligne(texte, m.start()), poids))

    for m in re.finditer(f"[{TIRET_CADRATIN}{TIRET_DEMI}]", texte):
        debut_ligne = texte.rfind("\n", 0, m.start()) + 1
        if texte[debut_ligne:m.start()].strip() == "":  # tiret de dialogue ou de liste
            continue
        r.constats.append(Constat(8, "Tiret comme ponctuation", extrait(texte, m.start(), m.end()),
                                  numero_ligne(texte, m.start()), 2))

    for m in re.finditer(r"(?<=\w) - (?=\w)", texte):  # trait d'union isolé employé comme tiret
        r.constats.append(Constat(8, "Trait d'union employé comme tiret", extrait(texte, m.start(), m.end()),
                                  numero_ligne(texte, m.start()), 1))

    for m in re.finditer(r"\b\d+(ème|eme|ième)s?\b", texte):
        r.constats.append(Constat(26, "Ordinal à corriger (2e, 16e)", extrait(texte, m.start(), m.end(), 10),
                                  numero_ligne(texte, m.start()), 1))

    for m in re.finditer(r"^#{1,6}\s+(.+)$", texte, flags=re.M):
        if titre_en_capitales(m.group(1)):
            r.constats.append(Constat(23, "Titre en capitales à l'anglaise", m.group(1).strip(),
                                      numero_ligne(texte, m.start()), 3))

    for m in GRAS_ETIQUETTE.finditer(texte):
        r.constats.append(Constat(24, "Gras en étiquette", extrait(texte, m.start(), m.end(), 10),
                                  numero_ligne(texte, m.start()), 1))

    for m in EMOJI.finditer(texte):
        r.constats.append(Constat(25, "Émoji", extrait(texte, m.start(), m.end(), 15),
                                  numero_ligne(texte, m.start()), 1))

    # Connecteurs en tête de paragraphe : signalés s'ils reviennent souvent
    paragraphes = [p.strip() for p in re.split(r"\n\s*\n", texte) if p.strip()]
    tetes = [p for p in paragraphes if p.lower().startswith(CONNECTEURS)]
    if len(paragraphes) >= 3 and len(tetes) / len(paragraphes) >= 0.4:
        r.constats.append(Constat(7, "Connecteurs en série en tête de paragraphe",
                                  f"{len(tetes)} paragraphes sur {len(paragraphes)}", 0, 3))

    # Rythme : uniformité de la longueur des phrases
    prose = re.sub(r"^\s*(#|[-*+]\s|\d+\.\s|>|\|).*$", "", texte, flags=re.M)
    phrases = [p for p in re.split(r"(?<=[.!?…])\s+", prose) if len(p.split()) >= 3]
    longueurs = [len(p.split()) for p in phrases]
    r.mots = len(re.findall(r"[\wÀ-ÿ'-]+", texte))
    r.phrases = len(longueurs)
    if len(longueurs) == 1:
        r.longueur_moyenne = float(longueurs[0])
    elif len(longueurs) >= 2:
        r.longueur_moyenne = round(statistics.mean(longueurs), 1)
        r.coefficient_variation = round(statistics.pstdev(longueurs) / r.longueur_moyenne, 2)
    if len(longueurs) >= 6 and r.coefficient_variation < 0.35:
        r.constats.append(Constat(13, "Phrases de longueur uniforme",
                                  f"moyenne {r.longueur_moyenne} mots, variation {r.coefficient_variation}",
                                  0, 2))

    poids_total = sum(c.poids for c in r.constats)
    densite = poids_total / max(r.mots, 1) * 1000  # points pour 1 000 mots
    r.score = min(100, round(densite * 2))
    r.constats.sort(key=lambda c: (c.motif, c.ligne))
    return r


def afficher(r: Rapport) -> None:
    print(f"== {r.fichier} : score {r.score}/100 "
          f"({r.mots} mots, {r.phrases} phrases, longueur moyenne {r.longueur_moyenne}, "
          f"variation {r.coefficient_variation})")
    if not r.constats:
        print("   Rien à signaler.")
        return
    for c in r.constats:
        ou = f"l.{c.ligne}" if c.ligne else "global"
        print(f"   [motif {c.motif:>2}] {c.libelle} ({ou}) : {c.extrait}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Repère les motifs d'écriture IA dans un texte français.")
    ap.add_argument("fichiers", nargs="+", help="fichiers texte ou Markdown, ou - pour l'entrée standard")
    ap.add_argument("--json", action="store_true", help="sortie JSON")
    ap.add_argument("--fail-above", type=int, default=None,
                    help="code de sortie 1 si un fichier dépasse ce score (usage en CI)")
    args = ap.parse_args()

    rapports = []
    for f in args.fichiers:
        if f == "-":
            rapports.append(analyser("<stdin>", sys.stdin.read()))
        else:
            rapports.append(analyser(f, Path(f).read_text(encoding="utf-8")))

    if args.json:
        print(json.dumps([{**r.__dict__, "constats": [c.__dict__ for c in r.constats]}
                          for r in rapports], ensure_ascii=False, indent=2))
    else:
        for r in rapports:
            afficher(r)

    if args.fail_above is not None and any(r.score > args.fail_above for r in rapports):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
