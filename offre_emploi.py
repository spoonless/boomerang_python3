from datetime import datetime

class Candidat:

    def __init__(self, experience):
        if not isinstance(experience, int):
            raise TypeError(f"L'expérience doit être un entier. Reçu : {experience}")
        if experience < 0:
            raise ValueError(f"L'expérience ne peut pas être négative. Reçu : {experience}")
        self.experience = experience 
    
    def __str__(self):
        return f"Un candidat avec {self.experience} années d'expérience"

    def __int__(self):
        return self.experience


class OffreEmploi:
    
    def __init__(self, 
                 experience,
                 intitule = None, 
                 description = None, 
                 salaire = None,
                 date_debut = None):
        self.intitule = intitule
        self.description = description
        self.experience = experience
        self.salaire = salaire
        self.date_debut = date_debut
        
    def est_depassee(self):
        return self.date_debut < datetime.today()

    def correspond_au(self, candidat):
        return self.experience <= candidat.experience
    
    
offre = OffreEmploi(experience=2)
candidat = Candidat(experience=5)

etat = offre.correspond_au(candidat)
print(etat)



