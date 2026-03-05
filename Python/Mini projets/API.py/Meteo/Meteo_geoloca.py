import requests
from datetime import datetime
import os

ville=input("De quelle ville voulez vous connaître la météo ? ").strip().upper()
liaison = "d'" if ville[0].lower() in "aeiouy" else "de "

# GEOLOCALISATION
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": ville, "count": 1, "language": "fr"}

try:
    geo_response = requests.get(geo_url, params=geo_params, verify=False)
    geo_data = geo_response.json()

    if "results" in geo_data:
        resultat = geo_data["results"][0]
        lat = resultat["latitude"]
        lon = resultat["longitude"]
        nom_complet = resultat["name"]
        pays = resultat.get("country", "")

        meteo_url = "https://api.open-meteo.com/v1/forecast"
        meteo_params = {
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "wind_speed_10m", "is_day"],
            "timezone": "auto"
        }

        # RECHERCHES METEO
        meteo_response = requests.get(meteo_url, params=meteo_params, verify=False)
        meteo_data = meteo_response.json()

        actuel= meteo_data['current']

        temp = actuel["temperature_2m"]
        vent = actuel['wind_speed_10m']
        unite_temp = meteo_data["current_units"]["temperature_2m"]
        unite_vent = meteo_data["current_units"]["wind_speed_10m"]
        jour_nuit = actuel['is_day']
        heure_brute = actuel['time'] # Format ex: 2026-02-28T14:30
        # On ne garder que ce qui est après le 'T'
        heure_ville = heure_brute.split("T")[1]

        print(f"--- MÉTÉO : {nom_complet} ({pays}) ---")
        print(f"Heure locale : {heure_ville}")
        print(f"Température : {temp}{unite_temp}")
        print(f"Vitesse du vent : {vent}{unite_vent}")
        if jour_nuit == 1:
            print("Il fait actuellement jour. ☀️")
        else:
            print("Il fait actuellement nuit. 🌙")


        # CREATION HISTORIQUE DE RECHERCHE METEO 
        base_folder = os.path.dirname(__file__)
        filepath = os.path.join(base_folder, "historique_meteo.txt")

        maintenant = datetime.now().strftime("%d/%m/%Y à %H:%M")  
        ligne_historique = f"[{maintenant}] {nom_complet} ({pays}) : {temp}{unite_temp}, Vent: {vent}{unite_vent}\n"
        
            # Save avec "with" (Context Manager)
        with open(filepath, "a", encoding="utf-8") as f:
                f.write(ligne_historique)         
        print("\nRecherche enregistrée dans l'historique.")

    else:
        print("Ville non trouvée.") # Si geolocalisation non-aboutie

except requests.exceptions.RequestException as e:
    print(f"Erreur : {e}") # Si demandes API non-abouties

# Attrape toutes les autres erreurs
except Exception as e:
    print(f"Une erreur est survenue : {e}")