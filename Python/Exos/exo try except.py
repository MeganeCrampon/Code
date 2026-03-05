liste = [1,2,3,4,5,6]
index = int(input("Entre un chiffre entre 0 et 5 : "))

def lire_index(liste, index) :
    try:
        print(liste[index])
    except IndexError:
        print("Erreur : L'index est trop grand!")
    
lire_index(liste, index)
