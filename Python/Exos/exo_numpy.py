import torch
import numpy as np

notes = [12, 18, 14, 10, 15]
notes_triees = sorted(notes)
notes_array = np.array(notes_triees)
notes_avec_bonus = notes_array + 2
print(notes_avec_bonus)

moyenne = notes_avec_bonus.mean()
print(f"La moyenne de la classe est de {moyenne:.2f} /20.")