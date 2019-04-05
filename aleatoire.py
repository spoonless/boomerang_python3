"""
Exemple d'utilisation d'un module standard de python (random)
mais aussi d'un module développé par nous-même (mabibmath).

@author: David Gayerie
"""
from random import randint
import mabibmath

liste = []
while len(liste) != 100:
    liste.append(randint(1, 100))

moyenne = mabibmath.moyenne(liste)

print(moyenne)
