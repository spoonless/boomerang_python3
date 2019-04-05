"""
Calcule l'écart à la moyenne d'une taille.
Le programme est découpé en fonctions.

@author: David Gayerie
"""

# Calcul de l'écart à la moyenne
TAILLE_MOYENNE = 175


def demander_taille():
    """Demande la taille et retourne la valeur en centimètres"""
    taille = None
    while taille is None:
        taille_saisie = input("Quelle est votre taille ?")
        try:
            taille_en_metre = float(taille_saisie)
            taille = int(taille_en_metre * 100)
        except ValueError:
            print("Ça m'étonne ! Êtes-vous sûr ?")
    return taille

def calculer_ecart_taille(taille1, taille2=TAILLE_MOYENNE):
    return taille1 - taille2


def afficher_ecart_moyenne(ecart):
    print(f"Vous avez un écart de {ecart} centimètres par rapport à la moyenne")


taille = demander_taille()
ecart = calculer_ecart_taille(taille)
afficher_ecart_moyenne(ecart)
