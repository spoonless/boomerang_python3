"""
Exemple d'implémentation d'un itérateur

@author: David Gayerie
"""
class Compteur:
    """Une classe pour compter"""

    def __init__(self, nombre_min=0, nombre_max=10):
        self.nombre = nombre_min
        self.nombre_max = nombre_max

    def __iter__(self):
        return self

    def __next__(self):
        self.nombre += 1
        if self.nombre > self.nombre_max:
            raise StopIteration
        return self.nombre
    
compteur = Compteur(1, 100)
for i in compteur:
    print(i)