class Carte:
    """
    Classe créeant une carte de Uno.
    Une carte est définie par sa valeur -> Valeur.py et par sa Couleur -> Couleur.py.
    8 cartes sont particulières puisqu'elles s'agient des Jokers Noirs. Elle sont créees directement dans la Pioche.
    """

    def __init__(self, valeur: str, couleur: str, cost: int):
        self.valeur = valeur
        self.couleur = couleur
        self.cost = cost

    def __repr__(self):
        return f"{self.valeur}{self.couleur}"

    def isJoker(self):
        symboles = ["+2", "+4", "↺", "⊝", "⊕"]
        if self.valeur in symboles:
            return True
        return False

    def setCouleur(self, couleur: str):
        self.couleur = couleur
