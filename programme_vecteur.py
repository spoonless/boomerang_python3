'''
Exemple d'utilisation de la classe Vecteur du module mabibmath.

@author: david
'''
from mabibmath import Vecteur

v = Vecteur(1, 3)

norme = v.calculer_norme()

print(norme)