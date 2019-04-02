
def diviser(numerateur, denominateur):
    """Retourne le résultat entier et le reste de la division
    entre numerateur et denominateur."""
    resultat_entier = numerateur // denominateur
    reste = numerateur % denominateur
    return resultat_entier, reste


a, b = diviser(13, 5)
print(a, b)
