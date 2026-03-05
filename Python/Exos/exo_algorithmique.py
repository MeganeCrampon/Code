scores_globaux = [("Alice", 12), ("Bob", 15), ("Charlie", 12), ("Jean", 10)]

def obtenir_top_3(liste) :
    if not liste :
        raise ValueError("La liste des scores est vide, impossible de créer un podium.")
    scores_tries = sorted(liste, key=lambda x : (-x[1], x[0]))
    top_3 = scores_tries[:3]
    return(top_3)

try:
    podium = obtenir_top_3(scores_globaux)
    print(f"Le podium est : {podium}")
except ValueError as e :
    print(f"Erreur : {e}")

try:
    podium = obtenir_top_3([])
    print(f"Le podium est : {podium}")
except ValueError as e :
    print(f"Erreur : {e}")