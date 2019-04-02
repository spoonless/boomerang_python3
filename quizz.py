# Un quizz simple

points = 0

reponse = input("Quel est ton nom ?")
points += int(reponse == "Sir Robin de Camelot.")

print("Quelle est ta quête ?")
points += int(reponse == "Trouver le Saint Graal.")

print("Quelle est la capitale de la Syrie ?")
points += int(reponse == "Damas.")

print("Réponses correctes", points)
print("Réponses incorrectes", 3 - points)

