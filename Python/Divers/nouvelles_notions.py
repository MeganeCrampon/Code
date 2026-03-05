import random

# --- 1. LES STRUCTURES DE DONNÉES ---
# Dictionnaire : Clé -> Valeur (Accès ultra-rapide)
fruits = {"Pomme": 5, "Fraise": 10}
# .get(cle, secours) évite le crash si la clé n'existe pas
quantite = fruits.get("Ananas", 0) 

# Set : Unicité et rapidité (Pas de doublons)
mon_set = {1, 2, 2, 3} # Deviendra {1, 2, 3}
mon_set.discard(10) # Supprime 10 sans erreur s'il n'est pas là

# List & Slicing
L = [10, 20, 30, 40, 50]
# [début : fin_exclue : pas]
morceau = L[1:4]     # [20, 30, 40]
inverse = L[::-1]    # [50, 40, 30, 20, 10]

# --- 2. LE HASARD (Module random) ---
pote = random.choice(["Alice", "Bob", "Charlie"]) # Pioche UN élément
random.shuffle(L) # Mélange la liste directement (in-place)

# --- 3. LES FONCTIONS & ARGUMENTS ---
# n=3 est une valeur par défaut
def playlist(biblio, n=3):
    titres = list(biblio.keys())
    # Securité si n est trop grand
    if n > len(titres): n = len(titres)
    return random.sample(titres, n) # sample = plusieurs choix sans doublons

# --- 4. SÉCURITÉ (Try / Except) ---
try:
    nombre = int(input("Entrez un diviseur : "))
    resultat = 100 / nombre
except ValueError:
    print("Oups : Il faut taper un chiffre !")
except ZeroDivisionError:
    print("Oups : Division par zéro impossible !")
except Exception as e:
    print(f"Autre erreur : {e}")

# --- 5. NOTIONS CLÉS ---
# \n = ligne, \\ = afficher un backslash
# O(1) = Complexité constante (vitesse max, spécifique aux dict et set)
# None = Absence de valeur (souvent utilisé comme valeur par défaut)