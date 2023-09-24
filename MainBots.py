from Pioche import Pioche
from Affichage import cartebot, botPioche, logdeckBot
from Fonctions import looser, changementdetour, Sens, cartebot, piochetonext, choisirCouleurB, piocher

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
            if i == len(self.deck)-1:
                chaine += "🎴"
            else:
                chaine += "🎴 "
        return chaine

    def jouer(self, p: Pioche, bot_name: str, s: Sens, nb_bots: int):
        islooser = False
        logdeckBot(self.name, self.deck)
        for c in self.deck:
            if c.valeur == p.courrante.valeur or c.couleur == p.courrante.couleur or c.couleur == "⬛":
                logging.debug(f"Le {bot_name} jouer la carte {c.valeur}{c.couleur}.")
                p.recevoir(c)
                if c.couleur == "⬛":
                    choisirCouleurB(c, self.deck)
                    if c.valeur == "+4":
                        piochetonext(4, s, p, nb_bots)
                elif c.valeur == "+2":
                    piochetonext(2, s, p, nb_bots)

                changementdetour(c, s, nb_bots)
                self.deck.remove(c)
                deckBotSTR = self.__repr__()
                cartebot(deckBotSTR, c, bot_name)
                islooser = looser(self.deck, bot_name)
                break

        else:
            piocher(self.deck, 1, p)
            deckBotSTR = self.__repr__()
            botPioche(self.name, deckBotSTR)
            s.finTour(nb_bots)

        return islooser
