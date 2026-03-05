utilisateurs = {"alice": "1234", "bob": "abcd"}
nom = input("Entrez votre nom: ")
nom_nettoye = nom.lower()

mdp = utilisateurs.get(nom_nettoye)
if mdp is None:
    print("Accès refusé.")
    choix = input("Voulez-vous créer un compte ?\n 1) Oui\n 2) Non\n")
    if choix == "1":
        new_mdp=input("Entrez votre mot de passe: ")
        utilisateurs[nom_nettoye] = new_mdp
        print("Compte créé avec succès ! Bienvenue !")
    else :
        print("Vous ne pouvez pas y accèder sans compte")
        exit()
else:
    print("Accès autorisé. Bienvenue !")