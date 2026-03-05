phrase = "Les pommes sont rouges"
debut = phrase.find("pommes")
fin = debut + len("pommes")
mot = phrase[debut:fin]
if mot.endswith("s"):
    print(f"Le mot '{mot}' est pluriel")