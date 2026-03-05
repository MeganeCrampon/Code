def commander(item, quantite):
    match item.lower():
        case "café" | "expresso": # Le | veut dire "ou"
            prix = 1.5
        case "thé":
            prix = 2.0
        case "chocolat" if quantite > 2: # On peut ajouter un "if" (un garde)
            prix = 1.8 # Prix réduit si on en prend beaucoup
        case "chocolat":
            prix = 2.5
        case "jus":
            prix = 3.0
        case _: # Le cas par défaut (si rien ne correspond)
            return "Désolé, on n'a pas ça."
    if quantite <=0 :
        return ("Commande impossible" )  
            
    total = prix * quantite
    return f"Total pour {quantite} {item} : {total:.2f}€"

# TEST :
print(commander("Café", 2))
print(commander("Pizza", 1))
print(commander("Jus", 0))