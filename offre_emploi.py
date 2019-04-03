from datetime import datetime

class Candidat:

    def __init__(self, experience):
        self.experience = experience 

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

    def correspondre(self, candidat):
        return self.experience <= candidat.experience
    
    
offre = OffreEmploi(experience = 2)
candidat = Candidat(experience= 5)

etat = offre.correspondre(candidat)
print(etat)
