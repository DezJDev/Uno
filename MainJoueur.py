from Affichage import *
from Pioche import Pioche
from Fonctions import testCarte, winner, changementdetour, Sens, choisirCouleurJ, piochetonext, trier
import logging

logging.basicConfig(filename="logs.log", level=logging.DEBUG, encoding="UTF-16")


class MainJ:
    """
    Simule la main du Joueur.
    Au début, le joueur commence avec 7 cartes de la pioche.
    Au fil du jeu, le joueur peut avoir plus ou moins de carte en fonction des cartes que posent les bots.
    Fin du jeu lorsque un des bots ou que le joueur n'a plus de carte dans sa main.
    """

    def __init__(self, p: Pioche):
        self.deck = []
        p.cartesPiochees(7, self.deck)

    def jouer(self, p: Pioche, s: Sens, nb_bots: int) -> bool:
        """
        :param nb_bots:
        :param s:
        :param p:
        :return: Renvoie la variable iswinner : le joueur n'a plus de carte
        """
        iswinner = False
        self.deck = trier(self.deck)
        tour(self.deck, p)
        index = demande()
        index = testCarte(index, self.deck, p)
        if index == "p":
            logging.debug("Le joueur décide de piocher.")
            cartepiochee(self.deck[-1])
            p.cartesPiochees(1, self.deck)
            changementdetour(None, s, nb_bots + 1)
            logging.debug(f"Voici la carte piochée: {self.deck[-1]}")

        else:
            logging.debug("Le joueur décide de jouer une carte.")
            logging.debug(f"Voici la carte jouée: {self.deck[index]}")
            if self.deck[index].couleur == "⬛":
                self.deck[index] = choisirCouleurJ(self.deck[index], self.deck)
                if self.deck[index].valeur == "+4":
                    piochetonext(4, s, p, nb_bots)
            if self.deck[index].valeur == "+2":
                piochetonext(2, s, p, nb_bots)

            p.recevoir(self.deck[index])
            changementdetour(self.deck[index], s, nb_bots)
            logging.debug(f"Carte supprimée: {self.deck[index]}")
            logging.debug(f"Main jouer avant suppression: {self.deck}")
            self.deck.remove(self.deck[index])
            logging.debug(f"Main jouer après suppression: {self.deck}")
            iswinner = winner(self.deck)

        return iswinner
