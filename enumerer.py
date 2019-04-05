"""
Exemple d'utilisation d'un générateur.

@author: David Gayerie
"""

semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

print("Affichage des jours de la semaine à partir d'une boucle")
cpt = 1
for j in semaine:
    print(cpt, j)
    cpt += 1


def enumerer(liste):
    """Une générateur pour retourner le numéro d'un élément et un élément."""
    cpt = 1
    for e in liste:
        yield cpt, e
        cpt += 1


print("Affichage des jours de la semaine à partir de notre générateur")
for n, j in enumerer(semaine):
    print(n, j)

print("Affichage des jours de la semaine à partir de enumerate")
for n, j in enumerate(semaine, start=1):
    print(n, j)

print("Affichage des jours de la semaine avec la première lettre en majuscule")
for j in map(str.capitalize, semaine):
    print(j)
