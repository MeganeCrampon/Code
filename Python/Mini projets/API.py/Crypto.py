import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=eur"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    print(f"--- INFO CRYPTO ---")
    for crypto, valeurs in data.items():     
        print(f"Le prix de {crypto.capitalize()} est de : {valeurs['eur']} €")

except requests.exceptions.RequestException as e:
    print(f"Erreur de connexion : {e}")