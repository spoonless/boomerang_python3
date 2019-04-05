"""
Exemple de programmation fonctionnelle

@author: David Gayerie
"""
import math

liste = [3, 7, 9]

# On affiche la racine carré de chaque élément dans la boucle for
for e in liste:
    print(math.sqrt(e))

# On affiche la racine carré de chaque élément de la liste avec map
for e in map(math.sqrt, liste):
    print(e)

# On produit la liste le carré de nombres qui est supérieur à 50
liste_au_carre = list(filter(lambda y : y > 50, map(lambda x: x**2, liste)))
print(liste_au_carre)