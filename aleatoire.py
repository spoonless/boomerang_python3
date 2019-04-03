from random import randint as nombre_aleatoire_entre
import mabibmath

liste = []
while len(liste) != 100:
    liste.append(nombre_aleatoire_entre(1, 100))

moyenne = mabibmath.moyenne(liste)

print(moyenne)
