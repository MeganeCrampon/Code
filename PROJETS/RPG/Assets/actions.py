import pygame
import random
import time
from Assets.stats_class import joueur, Monstre, Monstres_superieurs, joueur, liste_monstres
import Assets.sounds as sounds
pygame.mixer.init()


# DEFINITIONS
# - Level Up -
def lvl_up() :
    xp_requis = joueur.lvl * 100 # 100xp pour passer au lvl2, 200xp pour lvl3...
    if joueur.xp >= xp_requis:
        joueur.lvl += 1
        joueur.xp-= xp_requis # garde surplus xp
        sounds.heart_chan.stop()
            
        # --- Amélioration des stats ---
        time.sleep(0.5)
        joueur.hp_max += 10
        joueur.hp = joueur.hp_max # soin
        joueur.atk_min += 2
        joueur.atk_max += 5
        sounds.lvl.play()
        print(f"\nLEVEL UP ! Tu es maintenant Niveau {joueur.lvl} !\nTes HP Max augmentent ! ({joueur.hp_max}).\nTa force augmente !")

# - Heal -
def heal() :
    print(f"\nUtiliser une Potion ou la Magie ? \n La Potion rend 20HP. \n La Magie coûte 20MP et rend 30HP | MP actuels : {joueur.mp}.")
    choix_soin = input("(1) Potion (2) Magie: ")
    if choix_soin == "1" :
        if "Potion" in joueur.inventaire:
            joueur.inventaire.remove("Potion")
            joueur.hp = min(joueur.hp_max, joueur.hp + 20)
            sounds.boire_potion.play()
            print(f"Potion utilisée ! Tes HP: {joueur.hp}.")
        else:
            print("Tu n'as pas de Potion dans ton inventaire!")
                    
    elif choix_soin == "2" :
        if joueur.mp >= 20:
            joueur.mp -= 20
            joueur.hp = min(joueur.hp_max, joueur.hp + 30)
            sounds.magie_soin.play()
            print(f"Tu as utilisé la Magie pour vous soigner ! Tes HP: {joueur.hp}, tes MP: {joueur.mp}.")
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
    degats = random.randint(joueur.atk_min, joueur.atk_max)
    cible.hp -= degats
    print(f"Tu frappes de {degats}! HP {cible['nom']}: {max(0, cible.hp)}.")

# VERIF ALIVE
def check_alive() :
    if joueur.hp <= 0:
        pygame.mixer.music.pause()
        sounds.heart_chan.stop()
        time.sleep(1)
        pygame.mixer.music.load(sounds.m_gameover)
        pygame.mixer.music.play(-1) 
        print("\nGAME OVER... Tu as péri dans le donjon.")
        input("\nAppuie sur Entrée pour quitter...")
        exit()

# FIN COMBAT
def battle_end():
    if joueur.hp > 0:
        pygame.mixer.music.fadeout(2000)
        sounds.heart_chan.stop()
        time.sleep(1.5)
        pygame.mixer.music.load(sounds.m_win)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1.0)
        print(f"\nVICTOIRE ! Tu a survécu à cette vague de monstres avec {joueur.hp} HP !")
        pygame.mixer.music.fadeout(4000)