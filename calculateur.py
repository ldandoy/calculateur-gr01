def calculer_tva(prix_ht: float) -> float:
    return prix_ht * 1.20


prix_ttc = calculer_tva(100)
print(f"Total TTC: {prix_ttc}")

def calculer_remise(prix: float, remise_pct: float) -> float:
    """
    Applique une remise en pourcentage sur un prix.

    Exemple : calculer_remise(100, 20) -> 80.0
    """
    return prix * (1 - remise_pct / 100)