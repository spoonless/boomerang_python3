DECALAGE = 12
NB_LETTRES = 26

phrase = input("Entrez une phrase : ")
phrase_chiffree = ""


for c in phrase:
    if 'a' <= c <= 'z':
        offset = (ord(c) - ord('a') + DECALAGE) % NB_LETTRES
        c = chr(ord('a') + offset)
    elif 'A' <= c <= 'Z':
        offset = (ord(c) - ord('A') + DECALAGE) % NB_LETTRES
        c = chr(ord('A') + offset)
    phrase_chiffree += c

print(phrase_chiffree)
