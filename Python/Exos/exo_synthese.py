import numpy as np

stock = {
    "Pomme" : [0.50, 6], "Banane" : [1.20, 12], "Melons" : [3, 9], "Raisin" : [2.40, 16], "Citron" : [1, 22] 
    } # prix, quantité

tous_les_prix = [infos[0] for infos in stock.values()]
prix_array = np.array(tous_les_prix)
moyenne_prix = prix_array.mean()

print (f"La moyenne des prix est de {moyenne_prix:.2f}€.")

if moyenne_prix < 1.0:
    raise ValueError(f"Alerte ! La moyenne ({moyenne_prix:.2f}€) est trop basse pour être rentable !")