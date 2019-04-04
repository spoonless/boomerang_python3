
def mon_premier_generateur():
    compteur = 0
    while compteur <= 1000:
        yield compteur
        compteur +=1

for i in mon_premier_generateur():
    print(i)