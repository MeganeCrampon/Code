import random

# CLASSES 
class Entites :
    def __init__(self, nom, hp, hp_max, atk_min, atk_max, xp, money,) :
        self.hp_max = hp_max
        self.nom = nom
        self.hp = hp
        self.xp = xp
        self.money = money
        self.atk_min= atk_min
        self.atk_max= atk_max

    def alive(self) :
        return self.hp > 0
    
class Hero(Entites) :
    def __init__(self, nom, hp, hp_max, mp, mp_max, atk_min, atk_max) :
        super().__init__(nom, hp, hp_max, atk_min, atk_max, 0, 0)
        self.mp = mp
        self.mp_max = mp_max
        self.equipement = []
        self.armure = 0
        self.lvl = 1
        self.inventaire = ["Epee", "Bouclier"]

class Monstre(Entites) :
    def __init__(self, nom, hp, hp_max, atk_min, atk_max, xp, money) :
        super().__init__(nom, hp, hp_max, atk_min, atk_max, xp, money)

class Monstre_superieur(Entites) :
    def __init__(self, nom, hp, hp_max, mp, atk_min, atk_max,xp, money) :
        super().__init__(nom, hp, hp_max, atk_min, atk_max,xp, money)
        self.mp = mp


# ATTRIBUTION DES CLASSES
# --- Hero ---
joueur = Hero(nom ="Yuuki", hp=50, hp_max=50, mp=40, mp_max=40, atk_min=10, atk_max=15)

# --- Monstres ---
gobelin = Monstre(nom ="Gobelin", hp=30, hp_max=30, atk_min=8, atk_max=12, xp=50, money=5)
orc = Monstre(nom ="Orc", hp=45, hp_max=45, atk_min=10, atk_max=14, xp=80, money=8)

# --- Monstres Supérieurs ---


liste_monstres = [gobelin, orc]
