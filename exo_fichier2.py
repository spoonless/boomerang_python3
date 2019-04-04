
lignes = [
    "un;deux",
    "quatre;cinq",
]

resultat = []
for ligne in lignes:
    colonnes = ligne.split(";")
    colonnes.append(colonnes[0] + colonnes[1])
    resultat.append(colonnes)

print(resultat)

