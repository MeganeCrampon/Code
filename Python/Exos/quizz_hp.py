# Write code below 💖
h1 = 0 #Gryffondor
h2 = 0 #Serdaigle
h3 = 0 #Serpentard
h4 = 0 #Poufsouffle 

print("Q1) Tu préfères l'Aube ou le Crépuscule ?")
print("1) Aube")
print("2) Crépuscule")
q1 = int(input("Réponse : "))

if q1 ==1 :
  h1 +=1
  h2 +=1
elif q1 ==2 :
  h3 +=1
  h4 +=1
else :
  print ("Erreur.")

print("Q2) Quand je serai mort, je veux que les gens se souviennent de moi comme :")
print("1) Quelqu'un de Bon")
print("2) Quelqu'un de Sage")
print("3) Quelqu'un de Têtu")
print("4) Quelqu'un d'Admirable")
q2 = int(input("Réponse : "))

if q2 ==1 :
  h1 +=1
elif q2 ==2 :
  h2 +=1
elif q2 ==3 :
  h3 +=1
elif q2 ==4 :
  h4 +=1
else :
  print ("Erreur.")

print("Q3) Quel instrument te plaît le plus ?")
print("1) Le Violon")
print("2) Le Piano")
print("3) La Guitare")
print("4) La Trompette")
q3 = int(input("Réponse : "))

if q3 ==1 :
  h2 +=1
elif q3 ==2 :
  h3 +=1
elif q3 ==3 :
  h1 +=1
elif q3 ==4 :
  h4 +=1
else :
  print ("Erreur.")

print("Q4) Quel animal te plaît le plus ?")
print("1) Le Lapin")
print("2) Le Chien")
print("3) Le Lézard")
print("4) Le Perroquet")
q4 = int(input("Réponse : "))

if q4 ==1 :
  h4 +=1
elif q4 ==2 :
  h1 +=1
elif q4 ==3 :
  h3 +=1
elif q4 ==4 :
  h2 +=1
else :
  print ("Erreur.")

input("Le test est terminé !")

if h1>=2 :
  print ("Grâce à tes réponses, nous avons pu déterminer que tu appartiens à la maison...Gryffondor !")
elif h2>=2 :
  print ("Grâce à tes réponses, nous avons pu déterminer que tu appartiens à la maison...Serdaigle !")
elif h3>=2 :
  print ("Grâce à tes réponses, nous avons pu déterminer que tu appartiens à la maison...Serpentard !")
elif h4>=2 :
  print ("Grâce à tes réponses, nous avons pu déterminer que tu appartiens à la maison...Poufsouffle !")
else : 
  print("Erreur.")
