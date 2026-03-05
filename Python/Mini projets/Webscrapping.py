import requests
from bs4 import BeautifulSoup

url = "https://www.science-et-vie.com/nature-et-environnement/les-oceans/dans-les-abysses-oceaniques-91-des-especes-marines-sont-encore-inconnues-215751.html#:~:text=EN%20BREF,%C3%A0%20des%20m%C3%A9thodes%20scientifiques%20innovantes."

reponse = requests.get(url)

soup = BeautifulSoup(reponse.text, 'html.parser')
titre = soup.title.string
print(f"Le titre de la page est {titre}.")