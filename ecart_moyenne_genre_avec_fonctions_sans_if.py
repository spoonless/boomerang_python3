# Calcul de l'écart à la moyenne
TAILLE_MOYENNE_HOMME = 175
TAILLE_MOYENNE_FEMME = 165

dict_moyenne = {
    "homme": TAILLE_MOYENNE_HOMME,
    "femme": TAILLE_MOYENNE_FEMME
}


def demander_taille():
    """Demande la taille et retourne la valeur en centimètres"""
    taille_saisie = input("Quelle est votre taille ?")
    return int(float(taille_saisie) * 100)


def demander_genre():
    """Demande le genre"""
    return input("Êtes-vous un homme ou une femme ?")


def calculer_ecart_taille(taille1, taille2):
    return taille1 - taille2


def afficher_ecart_moyenne(ecart):
    print(f"Vous avez un écart de {ecart} centimètres par rapport à la moyenne")


taille = demander_taille()
genre = demander_genre()
ecart = calculer_ecart_taille(taille, dict_moyenne[genre])
afficher_ecart_moyenne(ecart)
