import Carte
import Pioche
import logging

logging.basicConfig(filename="logs.log", level=logging.DEBUG, encoding="UTF-16")


def aff_tour(deck: list, p: Pioche):
    chaine = "-" * 100
    chaine += "\n"
    chaine += p.__repr__()
    chaine += "\n"
    chaine += "-" * 100
    chaine += "\nVoici votre main :\n"
    i = 1
    for c in deck:
        chaine += f"{i} - {c}    "
        i += 1
    print(chaine)


def aff_E_supthan(index: int, taille: int):
    logging.error(f"-L'index: {index} est superieur a {taille}.")
    print(f"\n\nLa carte d'index {index} n'est pas comprise dans votre main.")


def aff_indexInvalid(index: int):
    logging.error(f"-L'index: {index} est inferieur a 1.")
    print(f"\n\nL'index '{index}', n'est pas valide.")


def aff_carteInvalid(carteJ: Carte):
    logging.error(f"-Carte: La carte {carteJ.valeur}{carteJ.couleur} est invalide avec la carte courrante.")
    print(f"\n\nCarte: La carte {carteJ.valeur}{carteJ.couleur} est invalide avec la carte courrante.")


def aff_demande():
    return input("Veuillez rentrer une nouvelle valeur (Entrez 'p' pour piocher une carte et passer votre tour): ")


def aff_typeInvalid(index: int):
    logging.error(f"-L'index: {index} n'est pas un chiffre.")
    print("\n\nVeuillez entrer un chiffre positif.")


def aff_cartepiochee(c: Carte):
    print(f"Carte piochée: {c}")


def aff_toobots():
    logging.error(f"-Bots: Nombre de bots invalides.")
    print("Le chiffre maximal de bot est 4.")
    print("Le chiffre minimal de bot est 1.\n")


def aff_demandebots():
    return input("Nombre de bots (de 1 à 4): ")


def aff_cartebot(deckBot: str, c: Carte, bot_name):
    print(f"{bot_name} a joué {c}: {deckBot}")


def aff_invalidSyntax():
    print("Veuillez entrer un chiffre entre 1 à 4.")


def aff_gagnant():
    print("Félicitations ! Vous avez gagné ! 🥳")


def aff_perdant(bot_name: str):
    print(f"Oh non ! Malheureusement le {bot_name} a vider sa main avant vous. Vous avez perdu ! 😢")


def aff_botPioche(bot_name: str, deck: str):
    print(f"{bot_name} a pioché une carte: {deck}")


def aff_couleurInvalid():
    print(f"Veuillez indiquer une couleur valide.")


def aff_logdeckBot(bot_name: str, deck: list):
    logging.debug(f"{bot_name}: {deck}")
