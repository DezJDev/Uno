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
        aff_logdeckBot(self.name, self.deck)
        for c in self.deck:
            if c.valeur == p.courrante.valeur or c.couleur == p.courrante.couleur or c.couleur == "⬛":
                logging.debug(f"Le {bot_name} jouer la carte {c.valeur}{c.couleur}.")
                if c.couleur == "⬛":
                    choisirCouleurB(c, self.deck)

                p.recevoir(c)
                s.changementdetour(c, p)
                self.deck.remove(c)
                deckBotSTR = self.__repr__()
                aff_cartebot(deckBotSTR, c, bot_name)
                break

        else:
            piocher(self.deck, 1, p)
            deckBotSTR = self.__repr__()
            aff_botPioche(self.name, deckBotSTR)
            s.finTour()

        return len(self.deck) == 0
