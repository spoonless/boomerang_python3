def moyenne(x, *args):
    """Calcule la moyenne d'un nombre quelconque de valeurs passées en paramètres."""
    nb = 1 + len(args)
    somme = x
    for y in args:
        somme += y
    return somme / nb

nombres_saisies = [1, 3, 4, 5]

print(moyenne(*nombres_saisies))

