import os
import logging
import sys

# LOGGING
folder = "Reports"
file = "Connexions"
format_pro = "%(asctime)s | [%(levelname)s] | Line: %(lineno)d | %(message)s"

if not os.path.exists(folder):
    os.mkdir(folder)

path=os.path.join(folder, file)

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


# BASE DE DONNEES
users = {"Thomas" : "0894", "Megane" : "2510", "Jean" : "AbCd", "Camille" : "cacahuete"}

# VERIFICATION UTILISATEUR
def check_user(user):
    logging.info(f"User login atempt for : {user}")

    while user not in users:
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
            logging.info(f"{user} try to register.")    
            new_ps=""
            while len(new_ps)<4:
                new_ps=input("Please create your password (at least 4 characters): ")
                if len(new_ps)<4:
                    print("Error : Your password is too short.")
           
            users[user] = new_ps
            logging.info(f"{user} is now registered.")
            print("You are now registered!")
        else:
            logging.warning(f"Invalid option chose by {user}.")
            print("Invalid option.")

# VERIFICATION MOT DE PASSE 
    attempts = 0             
    while True :
        password=input(f"{user}, please enter your password for : ")

        if password == users[user]:
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
logging.info("Authentication system starts")
print("\n --- WELCOME ---")
user_name = input(("Enter your username : ")).capitalize().strip()
check_user(user_name)