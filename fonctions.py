
def creer_nom(prenom, nom):
    nom_complet = prenom + " " + nom
    return nom_complet

options_print = {
    "sep": " :) ",
    "end": "\n*************************\n"
}

print("Monsieur", creer_nom("David", "Gayerie"), **options_print)
