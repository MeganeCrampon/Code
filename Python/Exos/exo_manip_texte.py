def analyser_mot(mot):
    taille = len(mot)
    mot_a_lenvers = mot[::-1]
    print(mot_a_lenvers)
    if mot.endswith("s"):
        print("C'est un pluriel.")
    else :
        print("C'est un singulier.")
    return taille

for _ in range(3):
    mot = input("Entrez un mot : ")
    resultat_taille = analyser_mot(mot) 
    
    print(f"Le mot '{mot}' fait {resultat_taille} lettres.\n")
