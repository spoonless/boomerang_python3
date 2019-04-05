"""
Écrit dans un fichier les lignes extraits d'un autre fichier qui ne contiennent
le mot python.

@author: David Gayerie
"""

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
        mots = ligne.translate(traducteur).lower().split()
        if "python" in mots:
            print(ligne, file=sortie)
