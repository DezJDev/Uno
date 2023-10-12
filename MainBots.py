from Pioche import Pioche
from Affichage import aff_cartebot, aff_botPioche, aff_logdeckBot
from Fonctions import Sens, choisirCouleurB, piocher

import logging

logging.basicConfig(filename="logs.log", level=logging.DEBUG, encoding="UTF-16")


class MainBot:
    def __init__(self, p: Pioche, bot_name: str):
        self.name = bot_name
        self.deck = []
        p.cartesPiochees(7, self.deck)

    def __repr__(self):
        chaine = ""
        for i in range(len(self.deck)):
            if i == len(self.deck) - 1:
                chaine += "🎴"
            else:
                chaine += "🎴 "
        return chaine

    def getScore(self):
        resultat = 0
        for cartes in self.deck:
            resultat += cartes.cost
        return resultat

    def jouer(self, p: Pioche, bot_name: str, s: Sens):
        if not self.deck:
            return True

        aff_logdeckBot(self.name, self.deck)
        cartesPossibles = []

        for c in self.deck:
            if c.valeur == p.courrante.valeur or c.couleur == p.courrante.couleur or c.couleur == "⬛":
                cartesPossibles.append(c)

        if cartesPossibles:
            i = 0
            cartechoisie = max(cartesPossibles, key=lambda carte: carte.cost)
            logging.debug(f"Le {bot_name} jouer la carte {cartechoisie.valeur}{cartechoisie.couleur}.")
            if cartechoisie.couleur == "⬛":
                choisirCouleurB(cartechoisie, self.deck)

            p.recevoir(cartechoisie)
            s.changementdetour(cartechoisie, p)
            self.deck.remove(cartechoisie)
            deckBotSTR = self.__repr__()
            aff_cartebot(deckBotSTR, cartechoisie, bot_name)

        else:
            piocher(self.deck, 1, p)
            deckBotSTR = self.__repr__()
            aff_botPioche(self.name, deckBotSTR)
            s.finTour()

        return len(self.deck) == 0
