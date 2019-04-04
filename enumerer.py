
semaine = ["lundi", 
           "mardi", 
           "mercredi", 
           "jeudi", 
           "vendredi", 
           "samedi", 
           "dimanche"]

cpt = 1
for j in semaine:
    print(cpt, j)
    cpt += 1


def enumerer(liste):
    cpt = 1
    for e in liste:
        yield cpt, e
        cpt += 1


for n, j in enumerer(semaine):
    print(n, j)

for n, j in enumerate(semaine, start=1):
    print(n, j)
    
for j in map(str.capitalize, semaine):
    print(j)
    
