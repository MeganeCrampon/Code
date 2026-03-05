mot_secret = "PYTHON"
vies = 6
lettres_essayees = []

def ajoute_liste(lettre): # Pas sûre de quoi mettre entre parenthèses
    if lettre not in lettres_essayees :
        lettres_essayees.append(lettre) #non plus, je pense que j'ai l'dée mais je sais pas l'appliquer
    
while True:
    lettre=input("Propose une lettre: ").upper() #Je sais pas si ca marche

    if lettre not in mot_secret :
        print("Perdu !")
        vies - 1
        ajoute_liste(lettre) #je sais pas du coup si ca fait bien ce que je voulais
        if vies == 0 : #pas sûre de la "synthaxe"
            print("Tu n'as plus de vie, tu as perdu!")
            break
    elif lettre in lettres_essayees :
        print("Erreur : lettre déjà proposée!")
        print("Lettres déjà proposées :", lettres_essayees)
    elif lettre in mot_secret :
        print("Bravo!")
        ajoute_liste(lettre)
        for : 
            print() #Affichage (je sais pas faire j'arrive pas)
        if  : 
             print ("Bravo! Tu as trouvé le mot secret!") #Jeu gagné, je sais pas l'écrire
             break
    else : 
        print("Proposition invalide : ce n'est pas une lettre.") #option pour si la personne entre un caractère autre qu'une lettre mais je sais pas trop comment le faire

