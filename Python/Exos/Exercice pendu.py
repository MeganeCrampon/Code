mot_secret = "PYTHON"
nombre_de_vie = 6
lettres_essayees = []

while True:
    lettre=input("Propose une lettre: ").upper()

    if lettre not in mot_secret and lettre not in lettres_essayees :
        print("Perdu, tu perds une vie!")
        lettres_essayees.append(lettre)
        resultat = (nombre_de_vie - 1)
        if nombre_de_vie == 0 :
            print("Tu n'as plus de vie, tu as perdu!")
            break
    elif lettre in lettres_essayees :
        print("Erreur : lettre déjà proposée!")
    elif lettre in mot_secret :
        print("Bravo!")
        lettres_essayees.append(lettre)
    else :
        print("Proposition invalide : ce n'est pas une lettre!")