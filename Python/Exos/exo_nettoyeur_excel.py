import pandas as pd
import os

data = {
    "prix_ht" : [45, 12, None, 87, 65, None, 90, 32]}

df = pd.DataFrame(data)
df["prix_ht"]=df["prix_ht"].fillna(df["prix_ht"].mean()).round(1)
df["prix_ttc"]=(df["prix_ht"]*1.20).round(1)

mon_dossier="Exports"

if not os.path.exists("Exports") :
    os.mkdir("Exports")
    print(f"Le dossier {mon_dossier} a été crée !")
else :
    print(f"Le dossier {mon_dossier} existe déjà !")

chemin_final = os.path.join(mon_dossier, "nettoyeur.xlsx")
df.to_excel(chemin_final, index=False)

print(f"Fichier sauvegardé avec succès sous : {chemin_final}")