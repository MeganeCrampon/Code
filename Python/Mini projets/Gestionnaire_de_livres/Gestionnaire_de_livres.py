import os
import sys
import sqlite3

# PATHS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(BASE_DIR, "Gestionnaire_de_livres")
if not os.path.exists(folder):
    os.mkdir(folder)
db_path = os.path.join(folder, "library.db")

# INIT DATABASE
def init_library():
    conn=sqlite3.connect(db_path)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS library(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT UNIQUE, author TEXT, year INTEGER, status TEXT)""")

    cur.execute("SELECT COUNT(*) FROM library")
    if cur.fetchone()[0] == 0:
        library = [("Harry Potter à l'école des sorciers", "J.K. Rowling", 1997,"DISPONIBLE"),
                   ("Dune", "Franck Herbert", 1965,"EMPRUNTE"),
                   ("Percy Jackson : Le Voleur de Foudre", "Rick Riordan", 2005,"DISPONIBLE"),
                   ("Dracula", "Bram Stoker", 1897,"DISPONIBLE")]
        cur.executemany("INSERT INTO library (title, author, year, status) VALUES (?, ?, ?, ?)", library)
        conn.commit()
        print("\n- Base de données initialisée avec les Identifiants, Titres, Auteur(e)s, Années et Status -")
    conn.close()


# FONCTIONS
def list_books():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM library")
    book_list = cur.fetchall()

    print("\n --- LISTE DES LIVRES ---")
    for b in book_list:
        print(f"{b[0]} -- Titre: {b[1]} - Auteur: {b[2]} - Année: {b[3]} | Statut: {b[4]}")
    conn.close()

def add_book():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    title = input("\nEntrez le titre : ").strip().capitalize()
    author = input("\nEntrez l'auteur(e) :" ).strip().capitalize()
    try:
        year = int(input("\nEntrez l'année de publication : "))
    except ValueError:
        print("Vous ne pouvez entrez qu'un nombre")
        return
    status = "DISPONIBLE"

    try:
        cur.execute("INSERT INTO library (title, author, year, status) VALUES (?, ?, ?, ?)", (title, author, year, status))
        conn.commit()
        print(f"\n{title} a été ajouté avec succès à la liste !")
    except sqlite3.IntegrityError:
        print("Ce livre est déjà présent dans la liste.")
    finally:
        conn.close()

def search_author():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    searched_author = input("Entrez le nom de l'auteur(e) que vous recherchez : ").strip()
    cur.execute("SELECT * FROM library WHERE author = ?", (searched_author,))
    found = cur.fetchall()
    if found :
        print(f"\n -- Livres de {searched_author} --")
        for book in found :
            print(f"[{book[0]} -- Titre: {book[1]} - Auteur: {book[2]} - Année: {book[3]} | Statut: {book[4]}") 
    else :
        print("Aucun livre de cet(te) auteur(e) trouvé.")
    conn.close()

def search_year():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    searched_year = input("Entrez l'année de parution que vous recherchez : ").strip()
    cur.execute("SELECT * FROM library WHERE year = ?", (searched_year,))
    found_year = cur.fetchall()
    if found_year :
        print(f"\n -- Livres de parus en {searched_year} --")
        for book in found_year :
            print(f"[{book[0]} -- Titre: {book[1]} - Auteur: {book[2]} - Année: {book[3]} | Statut: {book[4]}") 
    else :
        print("Aucun livre paru à cette date n'a été trouvé.")
    conn.close()

def change_status():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    searched_book = input("Entrez le nom du livre duquel vous voulez changer le statut : ").strip()

    cur.execute("SELECT id, status FROM library WHERE title = ?", (searched_book,))
    found_book = cur.fetchone()

    if found_book:
        book_id, current_status = found_book

        if current_status == "DISPONIBLE":
            new_status = "EMPRUNTE"
        else:
            new_status = "DISPONIBLE"

        cur.execute("UPDATE library SET status = ? WHERE id = ?", (new_status, book_id))
        conn.commit()
        print(f"\nLe statut de {searched_book} est maintenant : {new_status}")

    else:
        print("Aucun livre avec ce titre n'a été trouvé.")

    conn.close()

def delete_book():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        searched_id = int(input("Entrez l'identifiant du livre que vous voulez supprimer : "))
        cur.execute("SELECT id FROM library WHERE id = ?", (searched_id,))
        found_id = cur.fetchone()

        if found_id:
            confirm=input(f"\nEst-ce bien le livre que vous souhaitez supprimer : {found_id[0]} : {found_id[1]} ? (O/N ): ").upper()
            if confirm == "O":
                cur.execute("DELETE FROM library WHERE id = ?", (searched_id,))
                conn.commit()
                print("Suppression effectuée avec succès.")
            else :
                print("Supression annulée.")
        else:
            print("Aucun livre trouvé avec cet identifiant.")
    except ValueError:
        print("Erreur : veuillez entrer un identifiant valide.")
    finally:
        conn.close()    
    
# MENU
def menu():
    while True : 
        print("\n-------------------------MENU-------------------------")
        print("\n1) Voir la liste des livres\n" \
        "2) Ajouter un livre\n" \
        "3) Rechercher un livre par auteur(e)\n"
        "4) Rechercher un livre par date de parution\n" \
        "5) Changer le status d'un livre\n" \
        "6) Supprimer un livre\n" \
        "7) Quitter\n")

        action=input("\nQue voulez vous faire (1/2/3/4/5/6) ? ").strip()

        match action :
            case "1":
                list_books()
            case "2":
                add_book()
            case "3":
                search_author()
            case "4":
                search_year()
            case "5":
                change_status()
            case "6":
                delete_book()
            case "7":
                print("Au revoir !")
                break
            case _:
                print("Option invalide, réessayez.")

# SCRIPT
init_library()
print("\n--- BIENVENUE DANS LE GESTIONNAIRE DE BIBLIOTHEQUE PERSONNELLE ---")
menu()