import pygame
pygame.mixer.init()

# Musiques
m_intro = "RPG/Assets/musique_intro.mp3"
m_combat = "RPG/Assets/musique_combat.mp3"
m_win = "RPG/Assets/musique_win.mp3"
m_eglise = "RPG/Assets/church.mp3"
m_gameover = "RPG/Assets/game_over.mp3"
m_douce = "RPG/Assets/musique_douce.mp3"
m_dungeon = "RPG/Assets/dungeon.mp3"

# Sons
potion_inv = pygame.mixer.Sound("RPG/Assets/potion_inventaire.mp3")
epee = pygame.mixer.Sound("RPG/Assets/attaque_epee.mp3")
boire_potion = pygame.mixer.Sound("RPG/Assets/boire_potion.mp3")
coin = pygame.mixer.Sound("RPG/Assets/coin.mp3")
goblin = pygame.mixer.Sound("RPG/Assets/goblin.mp3")
magie_soin = pygame.mixer.Sound("RPG/Assets/magie_soin.mp3")
recup_item = pygame.mixer.Sound("RPG/Assets/recup_item.mp3")
app_magique = pygame.mixer.Sound("RPG/Assets/apparition_magique.mp3")
save = pygame.mixer.Sound("RPG/Assets/save.mp3")
keys = pygame.mixer.Sound("RPG/Assets/keys.mp3")
lvl = pygame.mixer.Sound("RPG/Assets/lvl_up.mp3")
map = pygame.mixer.Sound("RPG/Assets/map.mp3")
chest = pygame.mixer.Sound("RPG/Assets/chest.mp3")

# Canaux
heartbeat = pygame.mixer.Sound("RPG/Assets/heartbeat.mp3")
heart_chan = pygame.mixer.Channel(1)