dictionnaire = {
    ".": None,
    ",": None,
    "!": None,
    "?": None,
    "'": None,
    ":": None,
    "*": None,
    "`": None,
    "\n": None,
    "(": None,
    ")": None,
}

traducteur = str.maketrans(dictionnaire)

with open("monfichier.txt", encoding="utf-8") as entree, open("test_sortie.txt", mode="w", encoding="utf-8") as sortie:
    for ligne in entree:
        ligne = ligne.translate(traducteur).lower()
        mots = ligne.split()
        if "le" in mots:
            print(ligne, file=sortie)
