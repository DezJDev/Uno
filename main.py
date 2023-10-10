from Affichage import aff_demandebots, aff_perdant, aff_gagnant
from Pioche import Pioche
from Fonctions import verifynbbots, Sens
import logging

logging.basicConfig(filename="logs.log", level=logging.DEBUG)

if __name__ == "__main__":
    nb_bots = aff_demandebots()
    nb_bots = verifynbbots(nb_bots)
    pioche = Pioche()
    sens = Sens(nb_bots, pioche)
    iswinner = False

    logging.info(f"{'-' * 200}")
    logging.info(f"Instanciation des classes: Affichage, Pioche, Tas, Sens.")
    logging.info(f"Création des variables: nb_bots: {nb_bots}, iswinner.")

    while not iswinner:
        logging.debug(f"Voici le cursor: {sens.cursor}.")
        if type(sens.tableau[sens.cursor % (nb_bots + 1)]).__name__ == "MainJ":
            logging.debug(f"C'est au Joueur de jouer.")
            iswinner = sens.tableau[sens.cursor % (nb_bots + 1)].jouer(pioche, sens)
            if iswinner:
                aff_gagnant()
        else:
            logging.debug(f"C'est au Bot n°{sens.cursor % (nb_bots + 1)} de jouer.")
            logging.debug(f"Voici la taille du sens.tableau = {len(sens.tableau)}.")
            name = sens.tableau[sens.cursor % (nb_bots + 1)].name
            iswinner = sens.tableau[sens.cursor % (nb_bots + 1)].jouer(pioche, f"{sens.tableau[sens.cursor % (nb_bots + 1)].name}", sens)
            if iswinner:
                aff_perdant(name)
