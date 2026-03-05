from transformers import pipeline
from pprint import pprint

analyseur=pipeline("sentiment-analysis")
generateur=pipeline("text-generation")

commentaires=["I love it", "It really sucks !!", "I like it", "It's not that great..."]

for com in commentaires:
    resultat=analyseur(com)[0]
    print("\n" + "="*40)
    print(f"ANALYSE POUR : '{com}'")
    pprint(resultat)

    if resultat["label"] == "NEGATIVE":
        reponse=generateur("We are very sorry because ", max_new_tokens=20, temperature=0.9)
        print(f"IA (Négatif): {reponse[0]["generated_text"]}")
    else:
        print(f"IA (Positif): Thank you for your report !")

with open("logs.txt", "w", encoding="utf-8") as f:
    f.write("Analyse terminée.")