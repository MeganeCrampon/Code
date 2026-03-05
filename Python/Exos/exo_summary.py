import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# On utilise un modèle performant pour le résumé
model_name = "sshleifer/distilbart-cnn-12-6"

print("--- Chargement manuel du modèle de résumé ---")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = (
    "Mantas are found in warm temperate, subtropical and tropical waters. "
    "All three species are pelagic; M. birostris and M. yarae migrate across open oceans, "
    "singly or in groups, while M. alfredi tends to be resident and coastal. "
    "They are filter feeders and eat large quantities of zooplankton, which they gather "
    "with their open mouths as they swim. However, research suggests that the majority "
    "of their diet comes from mesopelagic sources. Gestation lasts over a year and "
    "mantas give birth to live pups. Mantas may visit cleaning stations for the "
    "removal of parasites. Like whales, they breach for unknown reasons."
)

# 1. Préparation du texte (Tokenization)
# On transforme le texte en nombres que le modèle comprend
inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)

print("--- Génération du résumé ---")
# 2. Génération des prédictions
summary_ids = model.generate(
    inputs["input_ids"], 
    max_length=50, 
    min_length=20, 
    length_penalty=2.0, 
    num_beams=4, 
    early_stopping=True
)

# 3. Traduction des nombres en texte lisible
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("\nTexte original (longueur) :", len(text))
print("Résumé final :")
print(f"-> {summary}")