import pygame
import random
import time
from Assets.stats_class import joueur, Monstre, Monstre_superieur, joueur
import Assets.sounds as sounds
import Assets.actions as actions
pygame.mixer.init()

# - DEBUT AVENTURE -
def debut_aventure():
    print("L'aventure commence...")
    sounds.musiques.m_intro.play()
if __name__ == "__rpg__":
    try:
        debut_aventure()
    except KeyboardInterrupt:
        print("\nPartie interrompue. À bientôt !")
    finally:
        pygame.quit()

# --- ENTREE DANS LE DONJON ---

time.sleep(2)
print("\n~~~ TU ENTRES DANS UN DONJON ~~~\n--- Tu as le choix entre aller à Droite ou à Gauche ---")
pygame.mixer.music.load(sounds.m_dungeon)
pygame.mixer.music.play(-1)
action_entree = input("(1) Droite (2) Gauche : ")
if action_entree == "1" :
    print("\nTu tombes sur une salle avec un coffre, tu l'ouvres et trouves...")
    sounds.chest.play()
    time.sleep(2.1)
    print("...une Potion !")
    sounds.potion_inv.play()
    joueur.inventaire.append("Potion")
    print(f"Ton joueur.inventaire actuel : {joueur.inventaire}.")
    print("Tu n'as plus d'autre choix que d'aller voir à Gauche !")
else :
    print("\nTu décides d'aller directement à Gauche !")

time.sleep(1.2)

print("\nOH NON! TU ENTRES DANS UNE SALLE ET TOMBES SUR UN PETIT GROUPE DE MONSTRES !")
pygame.mixer.music.load(sounds.m_combat)
pygame.mixer.music.play(-1) 

# --- DEBUT DES COMBATS ---
for m in Monstre:
    if joueur.hp <= 0:
        break
        
    print(f"\n--- Duel contre {m['nom']} ---") 

    while m["hp"] > 0 and joueur.hp > 0:
        action = input("\n(1) Attaque (2) Soin : ")

        if action == "1":
            actions.att_epee(m)
            
        elif action == "2":
            actions.heal()
        
        else:
            print("Choix invalide !")
            continue

        # --- RIPOSTE DU MONSTRE ---
        if m["hp"] > 0:
            time.sleep(1)
            # Dégâts de base
            degats_m_bruts = random.randint(m["atk_min"], m["atk_max"])
            # Calcul de la réduction (Dégâts - Armure)
            degats_m_finaux = degats_m_bruts - joueur.armure
            joueur.hp -= degats_m_finaux
            sounds.goblin.play()
            if joueur.armure > 0:
                print(f"Le {m['nom']} riposte ! -{degats_m_finaux} HP (L'Armure a bloqué {degats_m_bruts - degats_m_finaux}DMG !).")
            else:
                print(f"Le {m['nom']} riposte ! -{degats_m_finaux} HP.")
     
            print(f"Tes HP : {max(0, joueur.hp)}")


        if 0 < joueur.hp <= joueur.hp_max * 0.2:
            pygame.mixer.music.set_volume(0.3)
            message = (f"attention link ! le {m['nom']} va t'achever...")
            message_stress = "".join([char.upper() if random.random() > 0.4 else char for char in message])
            tremblement = " " * random.randint(2, 8)
            print(f"{tremblement}   {message_stress}  ")
            if not sounds.heart_chan.get_busy(): 
                sounds.heart_chan.play(sounds.heartbeat, loops=-1)
        else:
            pygame.mixer.music.set_volume(1.0)
            sounds.heart_chan.stop()

    if m["hp"] <= 0:
        time.sleep(1)
        print(f"\nFélicitations ! Tu as terrassé le {m['nom']} !")
        butin = m["or"]
        joueur.money += butin
        sounds.coin.play() 
        print(f"Tu ramasses {butin} pièces d'or sur son cadavre. \nTon or actuel : {joueur.money} pièces.")

        # --- Gain d'XP ---
        time.sleep(1)
        gain_xp = m["xp"]
        joueur.xp += gain_xp
        print(f"Tu gagnes {gain_xp} XP !")
        actions.lvl_up()

    # --- VERIFICATION DE MORT ---
    actions.check_alive()

# --- FIN DES COMBATS ---
actions.battle_end()

# --- LOOT --- 
time.sleep(3.5)   
print("\nTiens...un des monstres a fait tomber quelque chose ! \nTu te penches pour regarder et trouves une vieille armure en cuir abîmée. Tu décides de la porter !")
sounds.recup_item.play()
joueur.equipement.append("Vielle armure en cuir abîmée")
joueur.armure += 5
print(f"Ton armure augmente de 5 ! Ton armure actuelle est de : {joueur.armure}.")

# --- SUITE AVENTURE ---
time.sleep(2.5)
pygame.mixer.music.load(sounds.m_dungeon)
pygame.mixer.music.play(-1)    
print("\nTu peux maintenant continuer à explorer le donjon ! \nTu aperçois un petit couloir sombre tout droit et une autre pièce à droite. \nOù veux tu aller maintenant ?")
action_suite = input("(1) Le couloir sombre tout droit (2) La pièce à droite: ")