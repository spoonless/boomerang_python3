"""
Exemple de webscraping

@author: David Gayerie
"""
import webscraping


def afficher_nom_fichier(x):
    print(x)
    return False

webscraping.go_and_find(url="http://datavolley.lnv.fr/2017/EScoresheet/Men/", 
                         extensions=[".pdf"], 
                         filter_function=afficher_nom_fichier)
