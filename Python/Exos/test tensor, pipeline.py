import torch
import tensorflow as tf

print(f"PyTorch version: {torch.__version__}")
print(f"TensorFlow version: {tf.__version__}")

# Test de vérification pour Transformers
from transformers import pipeline
try:
    pipe = pipeline("sentiment-analysis")
    print("Succès : Le pipeline fonctionne !")
except Exception as e:
    print(f"Erreur : {e}")