
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

resultat = []

with open("monfichier.txt", encoding="utf-8") as f:
    for numero, ligne in enumerate(f, start=1):
        ligne = ligne.translate(traducteur).lower()
        mots = ligne.split()
        if "python" in mots:
            resultat.append(numero)

print(resultat)



