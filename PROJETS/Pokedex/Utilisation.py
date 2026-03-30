import FonctionsEtDB

print("--- POKEDEX ---")


# TEST
print(f"--- POKEMONS DE TYPE : ELECTRIQUE ---")
resultat_elec = trouver_type('Electrique')
affichage_recherche(resultat_elec)
print(f"\n--- POKEMONS DE NIVEAU 12+ ---")
resultat_lvl_12 = trouver_niveau(12)
affichage_recherche(resultat_lvl_12)
print(f"--- POKEMONS DE TYPE : POISON ---")
resultat_poison = trouver_type('Poison')
affichage_recherche(resultat_poison)