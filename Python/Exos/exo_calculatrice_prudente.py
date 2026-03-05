while True :
    try :
        num1 = float(input("Entrez un nombre : "))
        num2 = float(input("Entrez un deuxième nombre : "))
        num3= num1 / num2
        print(f"Votre premier nombre divisié par le deuxième donne : {num3}")
        break
    except ValueError :
        print("Vous ne pouvez entrer que des nombres.")
    except ZeroDivisionError :
        pass
        print("Calcul impossible.")