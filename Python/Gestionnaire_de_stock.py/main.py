import tkinter as tk
import numpy as np

# STOCK
stock = {
    "Pomme" : [0.50, 6], "Banane" : [1.20, 12], "Melons" : [3, 9], "Raisin" : [2.40, 16], "Citron" : [1, 22] 
    } # prix, quantité


def afficher_inventaire() : #effacer affichage précédent
    for widget in frame_liste.winfo_children():
        widget.destroy()

    # Trier par quantité
    stock_par_quantite = sorted(stock.items(), key=lambda x : x[1][1])

    for i, (nom, infos) in enumerate(stock_par_quantite) :
        couleur = "red" if infos[1] < 10 else "black" # alerte qte basse

        tk.Label(frame_liste, text=f"{i+1}. {nom}", fg=couleur).grid(row=i, column=0, sticky="w")
        tk.Label(frame_liste, text=f"Prix: {infos[0]:.2f}€").grid(row=i, column=1, padx=10)
        tk.Label(frame_liste, text=f"Qté: {infos[1]}", fg=couleur).grid(row=i, column=2)

def appliquer_promo() :
    for nom in stock :
        prix_qte = np.array(stock[nom])
        prix_qte[0] = prix_qte[0] * 0.90  # -10% 
        stock[nom] = prix_qte.tolist() # On repasse en liste 

    afficher_inventaire()
    label_info.config(text="Promo de -10% appliquée !", fg="green")

# --- Fenêtre Principale (Tkinter) ---
root = tk.Tk()
root.title("Gestionnaire de stock")
root.geometry("400x350")

tk.Label(root, text="📦 État du Stock (trié par quantité)", font=("Arial", 12, "bold")).pack(pady=10)

# Frame pour la grille
frame_liste = tk.Frame(root)
frame_liste.pack(pady=5)

# Boutons
btn_promo = tk.Button(root, text="Appliquer Soldes (-10%)", command=appliquer_promo)
btn_promo.pack(pady=10)

label_info = tk.Label(root, text="Cliquez pour actualiser")
label_info.pack()

# Lancement initial
afficher_inventaire()

root.mainloop()