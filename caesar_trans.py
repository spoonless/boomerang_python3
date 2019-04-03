LETTRES_MIN = "abcdefghijklmnopqrstuvwxyz"
LETTRES_MAJ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


DECAL = 12


def decal(liste, d):
    return liste[d:] + liste[:d]


trans = str.maketrans(LETTRES_MIN + LETTRES_MAJ,
                      decal(LETTRES_MIN, DECAL) + decal(LETTRES_MAJ, DECAL))
phrase = input("Entrez une phrase : ")
print(phrase.translate(trans))
