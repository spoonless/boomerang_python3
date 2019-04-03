
def creer_nom(prenom, nom):
    nom_complet = prenom + " " + nom
    return nom_complet

options_print = {
    "sep": " coucou ",
    "end": "\n**************************\n"
}

print("Monsieur", creer_nom("David", "Gayerie"), **options_print)

print("coucou", "comment", "ça", "va")