import pygame
import random
import time
from Assets.stats_class import Hero, Monstre, Monstres_superieurs
import Assets.sounds as sounds
pygame.mixer.init()


# DEFINITIONS
# - Level Up -
def lvl_up() :
    xp_requis = Hero.lvl * 100 # 100xp pour passer au lvl2, 200xp pour lvl3...
    if Hero.xp >= xp_requis:
        Hero.lvl += 1
        Hero.xp-= xp_requis # garde surplus xp
        sounds.heart_chan.stop()
            
        # --- Amélioration des stats ---
        time.sleep(0.5)
        Hero.hp_max += 10
        Hero.hp = Hero.hp_max # soin
        Hero.atk_min += 2
        Hero.atk_max += 5
        sounds.lvl.play()
        print(f"\nLEVEL UP ! Tu es maintenant Niveau {Hero.lvl} !\nTes HP Max augmentent ! ({Hero.hp_max}).\nTa force augmente !")

# - Heal -
def heal() :
    print(f"\nUtiliser une Potion ou la Magie ? \n La Potion rend 20HP. \n La Magie coûte 20MP et rend 30HP | MP actuels : {Hero.mp}.")
    choix_soin = input("(1) Potion (2) Magie: ")
    if choix_soin == "1" :
        if "Potion" in Hero.inventaire:
            Hero.inventaire.remove("Potion")
            Hero.hp = min(Hero.hp_max, Hero.hp + 20)
            sounds.boire_potion.play()
            print(f"Potion utilisée ! Tes HP: {Hero.hp}.")
        else:
            print("Tu n'as pas de Potion dans ton inventaire!")
                    
    elif choix_soin == "2" :
        if Hero.mp >= 20:
            Hero.mp -= 20
            Hero.hp = min(Hero.hp_max, Hero.hp + 30)
            sounds.magie_soin.play()
            print(f"Tu as utilisé la Magie pour vous soigner ! Tes HP: {Hero.hp}, tes MP: {Hero.mp}.")
        else:
            print("Pas assez de MP !")
    else:
        print("Choix invalide !")

''' def ramasser_butin(personnage, liste_monstres):
    total_gagne = 0
    
    for m in liste_monstres:
        # Ici 'm' est un OBJET Monstre, donc on accède à son attribut
        total_gagne += m.butin_or
        print(f"Tu fouilles le corps de {m.nom} et trouves {m.butin_or} or.")
    
    # On ajoute le total au héros
    personnage.money += total_gagne
    return total_gagne # On renvoie le chiffre pour pouvoir l'afficher'''

# - ATTAQUE EPEE -
def att_epee(cible) :
    sounds.epee.play()
    degats = random.randint(Hero.atk_min, Hero.atk_max)
    cible.hp -= degats
    print(f"Tu frappes de {degats}! HP {cible['nom']}: {max(0, cible.hp)}.")
