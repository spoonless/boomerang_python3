import math


def moyenne(nombres):
    """Calcule la moyenne d'une liste de nombres"""
    return sum(nombres) / len(nombres)


class Vecteur:
    """
        Mon vecteur
    """
    
    def __init__(self, x, y):
        assert isinstance(x, (float, int))
        assert isinstance(y, (float, int))
        self.x = x
        self.y = y
        
    def calculer_norme(self):
        return math.sqrt(self.x**2 + self.y**2)

    def calculer_produit_scalaire(self, v):
        return self.x * v.x + self.y * v.y

    def normaliser(self):
        norme = self.calculer_norme()
        self.x /= norme
        self.y /= norme

