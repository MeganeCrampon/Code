import os
import logging
import sys

dossier = "Rapports"
fichier = "data.txt"
format_pro = '%(asctime)s | [%(levelname)s] | Ligne: %(lineno)d | Message: %(message)s'

if not os.path.exists("Rapports"):
    os.mkdir("Rapports")
    print(f"Le dossier {dossier} a bien été crée !")
else :
    print(f"Le dossier {dossier} existe déjà !")

path = os.path.join(dossier, fichier)
print(f"Fichier sauvegardé avec succès sous : {path}")

logging.basicConfig(
    filename=path,
    level=logging.DEBUG,
    format=format_pro,
    encoding="utf-8",
    force=True)

if logging.getLogger().hasHandlers():
    logging.getLogger().handlers.clear()

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(logging.Formatter(format_pro))
logging.getLogger().addHandler(console_handler)

logging.info("Le dossier et le fichier sont prêts.")
logging.info("Démarrage du script")


print("\n--- MENU ---")

while True :
    action = input("Que voulez-vous faire ? (save/delete/view/quit) : ").lower().strip()
    match action:
        case "save":
            logging.info("Sauvegarde en cours...")
            print("Sauvegarde effectuée.")
        case "delete":
            logging.warning("Suppression des fichiers.")
            print("Fichiers supprimés.")
        case "view":
            logging.info("Affichage du rapport.")
            print("Affichage du rapport...")
        case "quit":
            logging.info("Fin de session.")
            print("Fin de session.")
            break
        case _:
            print("Action inconnue.")