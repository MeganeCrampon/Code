import torch
from transformers import pipeline

def test_generation():
    # GPT-2 est le modèle standard pour la génération de texte "simple"
    model_name = "gpt2"

    print(f"--- Chargement du pipeline : {model_name} ---")
    try:
        # Création du pipeline de génération
        generateur = pipeline("text-generation", model=model_name, device=-1)
        
        prompt = (
            "Mantas are found in warm temperate, subtropical and tropical waters. "
            "All three species are pelagic; M. birostris and M. yarae migrate across open oceans, "
            "singly or in groups, while M. alfredi tends to be resident and coastal. "
            "They are filter feeders and eat large quantities of zooplankton, which they gather "
            "with their open mouths as they swim. However, research suggests that the majority "
            "of their diet comes from mesopelagic sources. Gestation lasts over a year and "
            "mantas give birth to live pups. Mantas may visit cleaning stations for the "
            "removal of parasites. Like whales, they breach for unknown reasons."
        )

        print("--- Génération de la suite du texte... ---")
        # max_new_tokens définit combien de mots le modèle va ajouter
        resultat = generateur(prompt, max_new_tokens=30, num_return_sequences=1)

        print("\nTexte généré :")
        print(f"-> {resultat[0]['generated_text']}")
        print("\nSuccès : La tâche 'text-generation' fonctionne !")

    except Exception as e:
        print(f"\nUne erreur est survenue : {e}")

if __name__ == "__main__":
    test_generation()