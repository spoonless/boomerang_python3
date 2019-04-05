"""
Calcul de la moyenne de nombres saisis

@author: David Gayerie
"""
def demander_nombres():
    nombres = []
    while True:
        nombre_saisie = input("Saisissez un nombre : ")
        if nombre_saisie == "":
            break
        nombres.append(float(nombre_saisie))

    return nombres


def moyenne(nombres):
    return sum(nombres) / len(nombres)


nombres_saisis = demander_nombres()
if len(nombres_saisis) == 0:
    print("Pas de nombre, pas de calcul de moyenne !")
else:
    mean = moyenne(nombres_saisis)
    print(nombres_saisis)
    print(f"La moyenne est {mean:.2f}")
