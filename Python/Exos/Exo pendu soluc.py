mot_secret = "PYTHON"
vies = 6
lettres_devinees = []

print("Bienvenue au jeu du Pendu !")

while True:
    # --- 1. Construction de l'affichage (ex: P _ T _ _ N) ---
    affichage = ""
    lettres_manquantes = 0
   
    for lettre in mot_secret:
        if lettre in lettres_devinees:
            affichage += lettre + " "
        else:
            affichage += "_ "       
            lettres_manquantes += 1
           
    print(f"\nMot à trouver : {affichage}")
    print(f"Vies restantes : {vies}")
    print(f"Lettres essayées : {lettres_devinees}")

    # --- 2. Conditions de victoire/défaite ---
    if lettres_manquantes == 0:
        print("🎉 GAGNÉ ! Tu as trouvé le mot.")
        break
   
    if vies == 0:
        print(f"💀 PERDU ! Le mot était {mot_secret}.")
        break

    # --- 3. Interaction utilisateur ---
    essai = input("Propose une lettre : ").upper()

    # --- 4. Vérifications ---
    if len(essai) != 1:
        print("⚠️ Une seule lettre à la fois !")
        continue # On recommence la boucle directement

    if essai in lettres_devinees:
        print("⚠️ Tu as déjà essayé cette lettre !")
        continue

    lettres_devinees.append(essai)

    if essai in mot_secret:
        print("✅ Bonne lettre !")
    else:
        print("❌ Mauvaise lettre...")
        vies -= 1