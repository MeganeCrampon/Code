import pygame
import random
import time
pygame.mixer.init()

# Musiques
m_intro = "RPG/musique_intro.mp3"
m_combat = "RPG/musique_combat.mp3"
m_win = "RPG/musique_win.mp3"
m_eglise = "RPG/church.mp3"
m_gameover = "RPG/game_over.mp3"
m_douce = "RPG/musique_douce.mp3"
m_dungeon = "RPG/dungeon.mp3"

# Sons
potion_inv = pygame.mixer.Sound("RPG/potion_inventaire.mp3")
att_epee = pygame.mixer.Sound("RPG/attaque_epee.mp3")
boire_potion = pygame.mixer.Sound("RPG/boire_potion.mp3")
coin = pygame.mixer.Sound("RPG/coin.mp3")
goblin = pygame.mixer.Sound("RPG/goblin.mp3")
magie_soin = pygame.mixer.Sound("RPG/magie_soin.mp3")
recup_item = pygame.mixer.Sound("RPG/recup_item.mp3")
app_magique = pygame.mixer.Sound("RPG/apparition_magique.mp3")
save = pygame.mixer.Sound("RPG/save.mp3")
keys = pygame.mixer.Sound("RPG/keys.mp3")
lvl_up = pygame.mixer.Sound("RPG/lvl_up.mp3")
map = pygame.mixer.Sound("RPG/map.mp3")
wood_crack = pygame.mixer.Sound("RPG/wood_crack.mp3")

# Canaux
heartbeat = pygame.mixer.Sound("RPG/heartbeat.mp3")
heart_chan = pygame.mixer.Channel(1)
heart_chan.set_volume(1.0)

hero = {"nom": "Link", "hp": 50, "hp_max" : 50, "mp" : 40, "lvl" : 1, "xp" : 0, "or" : 0, "atk_min": 10, "atk_max": 18, 
        "inventaire": ["Epee", "Bouclier"], "equipement" : [], "armure" : 0 }
monstres = [{"nom": "Gobelin", "hp": 30, "xp" : 50, "atk_min": 8, "atk_max": 12, "or": 5}, 
            {"nom": "Orc", "hp": 50, "xp" : 80, "atk_min": 12, "atk_max": 15, "or": 8}]    

print("\n~~~ TU ENTRES DANS UN DONJON ~~~ \n--- Tu as le choix entre aller à Droite ou à Gauche ---")
pygame.mixer.music.load(m_dungeon)
pygame.mixer.music.play(-1)
action_entree = input("(1) Droite (2) Gauche : ")

if action_entree == "1" :
    print("\nTu tombes sur une salle avec un coffre, tu l'ouvres et trouves... une Potion !")
    potion_inv.play()
    hero["inventaire"].append("Potion")
    print(f"Ton inventaire actuel : {hero['inventaire']}.")
    print("Tu n'as plus d'autre choix que d'aller voir à Gauche !")
else :
    print("\nTu décides d'aller directement à Gauche !")

time.sleep(1.2)

print("\nOH NON! TU ENTRES DANS UNE SALLE ET TOMBES SUR UN PETIT GROUPE DE MONSTRES !")
pygame.mixer.music.load(m_combat)
pygame.mixer.music.play(-1) 

# --- DEBUT DES COMBATS ---
for m in monstres:
    if hero["hp"] <= 0:
        break
        
    print(f"\n--- Duel contre {m['nom']} ---") 

    while m["hp"] > 0 and hero["hp"] > 0:
        action = input("\n(1) Attaque (2) Soin : ")

        if action == "1":
            att_epee.play()
            degats = random.randint(hero["atk_min"], hero["atk_max"])
            m["hp"] -= degats
            print(f"Tu frappes de {degats}! HP {m['nom']}: {max(0, m['hp'])}.")
            
        elif action == "2":
            print(f"\nUtiliser une Potion ou la Magie ? \n La Potion rend 20HP. \n La Magie coûte 20MP et rend 30HP | MP actuels : {hero['mp']}.")
            choix_soin = input("(1) Potion (2) Magie: ")
            
            if choix_soin == "1" :
                if "Potion" in hero["inventaire"]:
                    hero["inventaire"].remove("Potion")
                    hero["hp"] = min(hero["hp_max"], hero["hp"] + 20)
                    boire_potion.play()
                    print(f"Potion utilisée ! Tes HP: {hero['hp']}.")
                else:
                    print("Tu n'as pas de Potion dans ton inventaire!")
                    continue
                    
            elif choix_soin == "2" :
                if hero["mp"] >= 20:
                    hero["mp"] -= 20
                    hero["hp"] = min(hero["hp_max"], hero["hp"] + 30)
                    magie_soin.play()
                    print(f"Tu as utilisé la Magie pour vous soigner ! Tes HP: {hero['hp']}, tes MP: {hero["mp"]}.")
                else:
                    print("Pas assez de MP !")
                    continue
            else:
                print("Choix invalide !")
                continue
        else:
            print("Choix invalide !")
            continue

        # --- RIPOSTE DU MONSTRE ---
        if m["hp"] > 0:
            time.sleep(1)
            degats_m = random.randint(m["atk_min"], m["atk_max"])
            hero["hp"] -= degats_m
            goblin.play()
            print(f"Le {m['nom']} riposte ! -{degats_m} HP. Tes HP: {max(0, hero['hp'])}")

        seuil_alerte = hero["hp_max"] * 0.2
        if 0 < hero["hp"] <= seuil_alerte:
            pygame.mixer.music.set_volume(0.3)
            message = f"attention link ! le {m['nom']} va t'achever..."
            message_stress = "".join([char.upper() if random.random() > 0.4 else char for char in message])
            tremblement = " " * random.randint(2, 8)
            print(f"{tremblement}   {message_stress}  ")
            if not heart_chan.get_busy(): 
                heart_chan.play(heartbeat, loops=-1)
        else:
            pygame.mixer.music.set_volume(1.0)
            heart_chan.stop()

    if m["hp"] <= 0:
        time.sleep(1)
        print(f"\nFélicitations ! Tu as terrassé le {m['nom']} !")
        butin = m["or"]
        hero["or"] += butin
        coin.play() 
        print(f"Tu ramasses {butin} pièces d'or sur son cadavre. \nTon or actuel : {hero['or']} pièces.")

        # --- Gain d'XP ---
        time.sleep(1)
        gain_xp = m["xp"]
        hero["xp"] += gain_xp
        print(f"Tu gagnes {gain_xp} XP !")

        # --- Level Up ---
        time.sleep(1)
        xp_requis = hero["lvl"] * 100 # 100xp pour passer au lvl2, 200xp pour lvl3...
        if hero["xp"] >= xp_requis:
            hero["lvl"] += 1
            hero["xp"] -= xp_requis # garde surplus xp
            heart_chan.stop()
            
            # --- Amélioration des stats ---
            time.sleep(0.5)
            hero["hp_max"] += 10
            hero["hp"] = hero["hp_max"] # soin
            hero["atk_min"] += 2
            hero["atk_max"] += 5
            lvl_up.play()
            print(f"\nLEVEL UP ! Tu es maintenant Niveau {hero['lvl']} !\nTes HP Max augmentent ! ({hero['hp_max']}).\nTa force augmente !")


    # --- VERIFICATION DE MORT ---
    if hero["hp"] <= 0:
        heart_chan.stop()
        time.sleep(1)
        pygame.mixer.music.load(m_gameover)
        pygame.mixer.music.play(-1) 
        print("\nGAME OVER... Tu as péri dans le donjon.")
        input("\nAppuie sur Entrée pour quitter...")
        exit()

# --- FIN DES COMBATS ---
if hero["hp"] > 0:
    time.sleep(1.5)
    pygame.mixer.music.load(m_win)
    pygame.mixer.music.play(-1)
    print(f"\nVICTOIRE ! Tu a survécu à cette vague de monstres avec {hero['hp']} HP !")
    pygame.mixer.music.fadeout(4000)

# --- LOOT --- 
time.sleep(3.5)   
print("\nTiens...un des monstres a fait tomber quelque chose ! \nTu te penches pour regarder et trouves une vieille armure en cuir abîmée. Tu décides de la porter !")
recup_item.play()
hero["equipement"].append("Vielle armure en cuir abîmée")
hero["armure"] += 5
print(f"Ton armure augmente de 5 ! Ton armure actuelle est de : {hero["armure"]}.")

# --- SUITE AVENTURE ---
time.sleep(1.5)
pygame.mixer.music.load(m_dungeon)
pygame.mixer.music.play(-1)    
print("\nTu peux maintenant continuer à explorer le donjon ! \nTu aperçois un petit couloir sombre tout droit et une autre pièce à droite. \nOù veux tu aller maintenant ?")
action_suite = input("(1) Le couloir sombre tout droit (2) La pièce à droite: ")