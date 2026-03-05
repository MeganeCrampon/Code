inventaire = {"pommes": 10, "café": 2, "cuillère": 20, "jambon": 8, "chocolat": 12}

def afficher_stock(data):
    items = data.items() if isinstance(data, dict) else data
    for produit, quantite in items:
        print(f"Produit : {produit.capitalize()} | Quantité : {quantite}.")

while True :
    try :
        nouvel_item = input("Entrez un produit : ").capitalize()
        nouvelle_quantite = int(input("Entrez sa quantité : "))
        inventaire[nouvel_item] = nouvelle_quantite
        print("\n --- NOUVEL INVENTAIRE ---")
        afficher_stock(inventaire)
        break
    except ValueError:
        print("Vous ne pouvez rentrer que des chiffres !")

inventaire_trie = sorted(inventaire.items(), key= lambda x : x[1], reverse=True)
print("\n --- INVENTAIRE ACTUEL (du plus grand au plus petit) ---")
afficher_stock(inventaire_trie)

with open("stock.txt", "w", encoding="utf-8") as f :
    f.write("RAPPORT D'IVENTAIRE\n")
    for produit, quantite in inventaire_trie:
        f.write(f"{produit} : {quantite}\n")

print("\nFichier 'stock.txt' enregistré avec succès !")