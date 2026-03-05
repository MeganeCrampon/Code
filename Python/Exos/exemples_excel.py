import pandas as pd

# Transformer ton dictionnaire de stock en tableau (DataFrame)
data = {
    "Produit": ["Pomme", "Banane"],
    "Prix": [0.5, 1.2]
}
df = pd.DataFrame(data)

# Enregistrer dans un fichier Excel
df.to_excel("mon_stock.xlsx", index=False)
print("Fichier créé !")