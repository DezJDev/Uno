from enum import Enum


class Couleur(Enum):
    """
    Classe permettant de relier chaque variable à une couleur de carte (sauf la couleur Noir).
    """
    ROUGE = "🟥"
    BLEU = "🟦"
    VERT = "🟩"
    JAUNE = "🟨"
