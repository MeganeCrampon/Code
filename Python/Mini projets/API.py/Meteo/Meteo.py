import requests

url = "https://api.open-meteo.com/v1/forecast"

ville=input("De quelle ville voulez vous connaître la météo ? ").strip().upper()
lat = float(input(f"Entrez la latitude de {ville} : "))
long = float(input(f"Entrez la longitude de {ville} : "))

liaison = "d'" if ville[0].lower() in "aeiouy" else "de "

parametres = {
    "latitude": lat,
    "longitude": long,
    "current": ["temperature_2m", "wind_speed_10m", "is_day"],
    "timezone": "auto"
}

try:
    response = requests.get(url, params=parametres)
    response.raise_for_status()
    
    data = response.json()
    
    meteo_actuelle = data['current']
    temp = meteo_actuelle['temperature_2m']
    vent = meteo_actuelle['wind_speed_10m']
    unite = data['current_units']['temperature_2m']
    jour_nuit = data['current']['is_day']

    print(f"--- MÉTÉO DE {liaison.upper()}{ville} ---")
    print(f"Température : {temp}{unite}")
    print(f"Vitesse du vent : {vent} km/h")
    if jour_nuit == 1:
        print("Il fait actuellement jour. ☀️")
    else:
        print("Il fait actuellement nuit. 🌙")

except requests.exceptions.RequestException as e:
    print(f"Erreur : {e}")