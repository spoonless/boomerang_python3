import math

liste = [3, 7, 9]

for e in map(math.sqrt, liste):
    print(e)


for e in liste:
    print(math.sqrt(e))

liste_au_carre = list(filter(lambda y : y > 50, map(lambda x: x**2, liste)))
print(liste_au_carre)