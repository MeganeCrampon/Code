import os
import logging
import sys
import sqlite3
import hashlib

# LOGGING & DOSSIER
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(BASE_DIR, "ReportsSQ")
if not os.path.exists(folder):
    os.mkdir(folder)

logfile = "Connexions"
path=os.path.join(folder, logfile)
db_path = os.path.join(folder, "system.db")

format_pro = "%(asctime)s | [%(levelname)s] | Line: %(lineno)d | %(message)s"

logging.basicConfig(
    filename=path,
    level=logging.DEBUG,
    format=format_pro,
    encoding="utf-8",
    force=True
)

# HANDLERS
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(logging.Formatter(format_pro))
logging.getLogger().addHandler(console_handler)

# HASHING
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# INITIALISATION SQLite et BASE DE DONNEES
def init_db():
    connexion = sqlite3.connect(db_path)
    cursor = connexion.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)""")
    
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        base_users = [
            ("Thomas", hash_password("0894")),
            ("Megane", hash_password("2510")),
            ("Jean", hash_password("AbCd")),
            ("Camille", hash_password("cacahuete"))
        ]
        cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", base_users)
        connexion.commit()
        print("Data base initialized with with IDs and Hashed passwords.")
    connexion.close()

# FONCTIONS SQLite
def get_password(user):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username = ?", (user,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else None

def add_user_to_db(user, pwd):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    hashed_pwd = hash_password(pwd)
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, hashed_pwd))
        conn.commit()
    except sqlite3.IntegrityError:
        print("User already exists.")
    conn.close()

# VERIFICATION ET ENREGISTREMENT UTILISATEUR
def register_user(user):
    logging.info(f"{user} try to register.")    
    new_ps=""
    while len(new_ps)<4:
        new_ps=input("Please create your password (at least 4 characters): ")
        if len(new_ps)<4:
            print("Error : Your password is too short.")
           
    add_user_to_db(user, new_ps)
    logging.info(f"{user} is now registered.")
    print("You are now registered!")

def check_user(user):
    logging.info(f"User login atempt for : {user}")
    stored_password = get_password(user)

    while stored_password is None:
        print("Your are not already registered.")
        logging.warning(f"Unknown user : {user}")
        action = input("Do you want to register ? Y\\Yes - N\\No - Q\\Quit : ").upper()
        if action == "Q":
            logging.info(f"The user exit the program.")
            print("Goodbye.")
            return
        elif action == "N":
            logging.info(f"{user} refused to register.")
            print("You cannot access without being registered.")
        elif action == "Y":
            register_user(user)
            stored_password = get_password(user)
        else:
            logging.warning(f"Invalid option chose by {user}.")
            print("Invalid option.")

    # VERIFICATION MOT DE PASSE 
    attempts = 0             
    while True :
        password=input(f"{user}, please enter your password for : ")

        if hash_password(password) == stored_password:
            logging.info(f"Access granted for: {user}")
            print("Access granted.")
            break
        else :
            attempts += 1
            logging.warning(f"{user} did not entered the right password. Attempts = {attempts}")
            print("Sorry, the password is wrong. Please try again. \nYour account will be temporarily suspended after 3 attempts")
            if attempts >= 3:
                logging.warning(f"The account of {user} is temporarily suspented after 3 attempts.")
                print("Wrong password. Your account is temporarily suspended.")
                sys.exit()

# SCRIPT
init_db()
logging.info("Authentication system starts")
print("\n --- WELCOME ---")
user_name = input(("Enter your username : ")).capitalize().strip()
check_user(user_name)