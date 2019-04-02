# Calcul de l'écart à la moyenne
TAILLE_MOYENNE = 175

taille_saisie = input("Quelle est votre taille ?")
taille_en_centimetre = float(taille_saisie) * 100
ecart = int(taille_en_centimetre - TAILLE_MOYENNE)
print(f"Vous avez un écart de {ecart} centimètres par rapport à la moyenne")