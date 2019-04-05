"""
Compte le numéro des lignes d'un fichier qui contiennent le mot python.

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

# traducteur pour supprimer les caractères qui ne sont pas des lettres
traducteur = str.maketrans(dictionnaire)

resultat = []

with open("monfichier.txt", encoding="utf-8") as f:
    for numero, ligne in enumerate(f, start=1):
        ligne = ligne.translate(traducteur).lower()
        mots = ligne.split()
        if "python" in mots:
            resultat.append(numero)

print(resultat)



