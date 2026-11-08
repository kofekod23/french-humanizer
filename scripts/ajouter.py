#!/usr/bin/env python3
"""Ajoute un texte humain au corpus personnel de French Humanizer.

Quatre types :
  mail-envoyé   un mail que vous avez écrit          -> voix de l'auteur
  texte-modèle  un texte que vous avez écrit         -> voix de l'auteur
  mail-reçu     un mail écrit par quelqu'un d'autre  -> exemple de registre
  texte-autre   article, courrier reçu, etc.         -> exemple de registre

Les textes de l'auteur servent à calibrer la réécriture sur sa voix. Les
textes de tiers servent d'exemples humains d'un registre, jamais de voix.

Le corpus est stocké en local, hors du dépôt Git (aucun mail ne part sur
GitHub) : ~/.config/french-humanizer/corpus, ou le dossier indiqué par la
variable d'environnement FRENCH_HUMANIZER_CORPUS.

Usage :
  python3 ajouter.py mail-envoyé message.txt --registre "courrier formel"
  pbpaste | python3 ajouter.py texte-modèle - --titre "billet LinkedIn"
  python3 ajouter.py lister
  python3 ajouter.py profil
  python3 ajouter.py contextes
  python3 ajouter.py exemples commercial --max 2
  python3 ajouter.py supprimer <fichier>
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import statistics
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from scan import analyser  # noqa: E402

TYPES = {
    "mail-envoye": "auteur",
    "texte-modele": "auteur",
    "mail-recu": "tiers",
    "texte-autre": "tiers",
}
SEUIL_ALERTE_IA = 40  # au-delà, un texte « de l'auteur » ressemble à de la prose IA

TIRETS = "\u2014\u2013"
OUVERTURES = ("bonjour", "bonsoir", "salut", "coucou", "madame", "monsieur", "cher", "chère", "hello")
FERMETURES = ("cordialement", "bien à vous", "bien cordialement", "salutations", "à bientôt", "a+",
              "bises", "bisous", "merci", "belle journée", "bonne journée", "à plus")


def dossier_corpus() -> Path:
    return Path(os.environ.get("FRENCH_HUMANIZER_CORPUS",
                               Path.home() / ".config" / "french-humanizer" / "corpus"))


def normaliser_type(brut: str) -> str:
    """Accepte « mail-envoyé » comme « mail-envoye », majuscules comprises."""
    sans_accent = unicodedata.normalize("NFKD", brut.lower()).encode("ascii", "ignore").decode()
    sans_accent = sans_accent.replace("_", "-").replace(" ", "-")
    if sans_accent not in TYPES:
        raise SystemExit(f"Type inconnu : {brut}. Types possibles : mail-envoyé, texte-modèle, mail-reçu, texte-autre.")
    return sans_accent


def slug(texte: str, n: int = 40) -> str:
    s = unicodedata.normalize("NFKD", texte.lower()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:n] or "texte"


def lire_frontmatter(chemin: Path) -> tuple[dict, str]:
    contenu = chemin.read_text(encoding="utf-8")
    meta: dict = {}
    if contenu.startswith("---\n"):
        fin = contenu.find("\n---\n", 4)
        if fin != -1:
            for ligne in contenu[4:fin].splitlines():
                if ":" in ligne:
                    k, v = ligne.split(":", 1)
                    meta[k.strip()] = v.strip()
            contenu = contenu[fin + 5:]
    return meta, contenu


def ajouter(args: argparse.Namespace) -> int:
    type_ = normaliser_type(args.type)
    voix = TYPES[type_]
    texte = sys.stdin.read() if args.source in (None, "-") else Path(args.source).read_text(encoding="utf-8")
    texte = texte.strip()
    if len(texte.split()) < 15:
        raise SystemExit("Texte trop court (moins de 15 mots) : il n'apprendrait rien sur un style.")

    rapport = analyser(args.source or "<stdin>", texte)
    titre = args.titre or texte.split("\n", 1)[0][:60]
    aujourd_hui = dt.date.today().isoformat()
    cible = dossier_corpus() / type_
    cible.mkdir(parents=True, exist_ok=True)
    chemin = cible / f"{aujourd_hui}-{slug(titre)}.md"
    i = 2
    while chemin.exists():
        chemin = cible / f"{aujourd_hui}-{slug(titre)}-{i}.md"
        i += 1

    meta = [
        "---",
        f"type: {type_}",
        f"voix: {voix}",
        f"registre: {' '.join(args.registre.split()).lower() if args.registre else 'non précisé'}",
        f"titre: {titre}",
        f"date_ajout: {aujourd_hui}",
        f"date_texte: {args.date or 'inconnue'}",
        f"mots: {rapport.mots}",
        f"longueur_moyenne_phrase: {rapport.longueur_moyenne}",
        f"variation_longueur: {rapport.coefficient_variation}",
        f"score_motifs_ia: {rapport.score}",
        "---",
        "",
    ]
    chemin.write_text("\n".join(meta) + texte + "\n", encoding="utf-8")
    print(f"Ajouté : {chemin}")
    print(f"  {rapport.mots} mots, phrases de {rapport.longueur_moyenne} mots en moyenne, score motifs IA {rapport.score}/100.")
    if voix == "auteur" and rapport.score > SEUIL_ALERTE_IA:
        print(f"  Attention : ce texte cumule des motifs IA (score {rapport.score}). S'il a été rédigé ou "
              "retouché par une IA, il faussera la calibration de votre voix ; supprimez-le avec "
              f"« ajouter.py supprimer {chemin.name} ».")
    return 0


def fichiers(voix: str | None = None) -> list[tuple[Path, dict, str]]:
    racine = dossier_corpus()
    out = []
    if not racine.exists():
        return out
    for f in sorted(racine.glob("*/*.md")):
        meta, corps = lire_frontmatter(f)
        if voix is None or meta.get("voix") == voix:
            out.append((f, meta, corps))
    return out


def _cle(texte: str) -> str:
    """Forme comparable d'un registre : sans accents, sans casse, espaces réduits."""
    t = unicodedata.normalize("NFKD", texte.lower()).encode("ascii", "ignore").decode()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", t).split())


def _meme_registre(meta: dict, registre: str | None) -> bool:
    return registre is None or _cle(registre) in _cle(meta.get("registre", ""))


def lister(args: argparse.Namespace) -> int:
    liste = [x for x in fichiers() if _meme_registre(x[1], getattr(args, "registre", None))]
    if not liste:
        print(f"Corpus vide ({dossier_corpus()}).")
        return 0
    for f, meta, _corps in liste:
        print(f"[{meta.get('type', '?'):<12}] {meta.get('registre', ''):<20} {meta.get('mots', '?'):>5} mots  {f.name}")
    print(f"\n{len(liste)} textes dans {dossier_corpus()}")
    return 0


def contextes(_: argparse.Namespace) -> int:
    """Liste les registres présents dans le corpus, avec le nombre de textes de chacun."""
    compte: dict[str, list[int]] = {}
    for _f, meta, _c in fichiers():
        r = meta.get("registre", "non précisé").lower()
        compte.setdefault(r, [0, 0])[0 if meta.get("voix") == "auteur" else 1] += 1
    if not compte:
        print(f"Corpus vide ({dossier_corpus()}).")
        return 0
    for r, (auteur, tiers) in sorted(compte.items()):
        print(f"{r:<28} {auteur:>3} de l'auteur  {tiers:>3} reçus")
    return 0


def exemples(args: argparse.Namespace) -> int:
    """Affiche les textes d'un registre, pour s'en inspirer avant une réécriture."""
    choisis = sorted((x for x in fichiers(args.voix) if _meme_registre(x[1], args.registre)),
                     key=lambda x: x[0].name)[-args.max:]  # le nom commence par la date d'ajout
    if not choisis:
        print(f"Aucun texte pour le registre « {args.registre} ».")
        return 0
    for f, meta, corps in choisis:
        role = "texte de l'auteur" if meta.get("voix") == "auteur" else "texte reçu, à ne pas imiter comme voix"
        print(f"===== {f.name} ({meta.get('type')}, {role})")
        print(corps.strip(), end="\n\n")
    return 0


def supprimer(args: argparse.Namespace) -> int:
    trouves = [f for f, _m, _c in fichiers() if f.name == args.fichier or str(f) == args.fichier]
    if not trouves:
        raise SystemExit(f"Aucun texte nommé {args.fichier} dans le corpus.")
    for f in trouves:
        f.unlink()
        print(f"Supprimé : {f}")
    return 0


def profil(_: argparse.Namespace) -> int:
    """Résume les habitudes d'écriture mesurables de l'auteur, pour la calibration."""
    textes = [(m, c) for _f, m, c in fichiers("auteur")]
    if not textes:
        print("Aucun texte de l'auteur (mail-envoyé ou texte-modèle) dans le corpus.")
        return 0
    corps = "\n\n".join(c for _m, c in textes)
    bas = corps.lower()
    phrases = [p for p in re.split(r"(?<=[.!?…])\s+", corps) if len(p.split()) >= 2]
    longueurs = [len(p.split()) for p in phrases] or [0]
    mots = max(len(corps.split()), 1)

    def par_mille(n: int) -> float:
        return round(n / mots * 1000, 1)

    premieres = [c.strip().splitlines()[0].lower() for _m, c in textes if c.strip()]
    dernieres = [" ".join(c.strip().splitlines()[-3:]).lower() for _m, c in textes if c.strip()]  # signature comprise
    ouvertures = sorted({o for o in OUVERTURES for p in premieres if p.startswith(o)})
    fermetures = sorted({f for f in FERMETURES for d in dernieres if f in d})

    print(f"Profil de voix sur {len(textes)} textes de l'auteur ({mots} mots)")
    print(f"- Phrases : {round(statistics.mean(longueurs), 1)} mots en moyenne, "
          f"de {min(longueurs)} à {max(longueurs)}, médiane {statistics.median(longueurs)}")
    tu = len(re.findall(r"\b(tu|te|toi|ton|ta|tes)\b", bas))
    vous = len(re.findall(r"\b(vous|votre|vos)\b", bas))
    print(f"- Tutoiement : {par_mille(tu)} / 1000 mots ; vouvoiement : {par_mille(vous)} / 1000 mots")
    print(f"- Points d'exclamation : {par_mille(corps.count('!'))} / 1000 mots ; "
          f"points de suspension : {par_mille(corps.count('...') + corps.count('…'))} / 1000 mots")
    print(f"- Tirets cadratin ou demi-cadratin : {sum(corps.count(t) for t in TIRETS)} ; "
          f"parenthèses : {corps.count('(')} ; points-virgules : {corps.count(';')}")
    print(f"- Guillemets français « » : {corps.count('«')} ; guillemets droits : {corps.count(chr(34)) // 2}")
    print(f"- Ouvertures habituelles : {', '.join(ouvertures) or 'aucune repérée'}")
    print(f"- Formules de fin habituelles : {', '.join(fermetures) or 'aucune repérée'}")
    registres = sorted({m.get('registre', 'non précisé') for m, _c in textes})
    print(f"- Registres couverts : {', '.join(registres)}")
    return 0


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] not in ("lister", "profil", "supprimer", "contextes", "exemples", "-h", "--help"):
        ap = argparse.ArgumentParser(description="Ajoute un texte au corpus personnel.")
        ap.add_argument("type", help="mail-envoyé, texte-modèle, mail-reçu ou texte-autre")
        ap.add_argument("source", nargs="?", help="fichier texte, ou - pour l'entrée standard (par défaut)")
        ap.add_argument("--registre", help="ex. : courrier formel, mail pro, article, lettre de motivation")
        ap.add_argument("--titre", help="titre court (par défaut : première ligne)")
        ap.add_argument("--date", help="date d'écriture du texte, si connue (AAAA-MM-JJ)")
        return ajouter(ap.parse_args())

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sous = ap.add_subparsers(dest="cmd", required=True)
    lst = sous.add_parser("lister", help="liste les textes du corpus")
    lst.add_argument("--registre", help="ne garder qu'un registre (ex. : commercial)")
    sous.add_parser("profil", help="résume les habitudes d'écriture de l'auteur")
    sous.add_parser("contextes", help="liste les registres présents et leur nombre de textes")
    ex = sous.add_parser("exemples", help="affiche les textes d'un registre")
    ex.add_argument("registre")
    ex.add_argument("--max", type=int, default=3, help="nombre de textes, les plus récents (3 par défaut)")
    ex.add_argument("--voix", choices=["auteur", "tiers"], help="seulement les textes de l'auteur ou les textes reçus")
    s = sous.add_parser("supprimer", help="retire un texte du corpus")
    s.add_argument("fichier")
    args = ap.parse_args()
    actions = {"lister": lister, "profil": profil, "supprimer": supprimer,
               "contextes": contextes, "exemples": exemples}
    return actions[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
