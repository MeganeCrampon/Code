nom_utilisateur=input("Entrez votre nom : ")
nom_utilisateur_propre=nom_utilisateur.strip().replace("_", "").capitalize()
print(f"Bonjour {nom_utilisateur_propre} !")