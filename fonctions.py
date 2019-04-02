
def dire_bonjour_a(nom, smiley=":)"):
    """Fonction qui dit bonjour mais aussi bonsoir"""
    print("Bonjour", nom, sep=f" {smiley} ", end=" et c'est fini\n\n")
    print("Et bonsoir")


def creer_nom(prenom, nom="Doe"):
    nom_complet = prenom + " " + nom
    return nom_complet


le_nom_a_afficher = creer_nom("David")
dire_bonjour_a(le_nom_a_afficher)