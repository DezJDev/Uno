import Carte
import Pioche
import logging

logging.basicConfig(filename="logs.log", level=logging.DEBUG, encoding="UTF-16")


def aff_demandeRegles():
    return "Bienvenue dans le jeu du Uno ! \n" \
           "Ci-dessous quelques explications suivies des règles du Uno. \n" \
           "Le Uno est un jeu de cartes américain créé en 1971 par Merle Robbins et édité par Mattel. \n" \
           "Le jeu contient 108 cartes: \n" \
           "    - 19 cartes de couleur bleue, numérotées de 0 à 9 (2 pour chaque chiffre sauf pour le 0).\n" \
           "    - 19 cartes de couleur rouge, numérotées de 0 à 9 (2 pour chaque chiffre sauf pour le 0).\n" \
           "    - 19 cartes de couleur jaune, numérotées de 0 à 9 (2 pour chaque chiffre sauf pour le 0).\n" \
           "    - 19 cartes de couleur verte, numérotées de 0 à 9 (2 pour chaque chiffre sauf pour le 0).\n" \
           "    - 8 cartes « +2 », (2 pour chaque couleur).\n" \
           "    - 8 cartes « Inversement de sens », (2 pour chaque couleur).\n" \
           "    - 8 cartes « Passe ton tour », (2 pour chaque couleur).\n" \
           "    - 4 cartes « SwitchColor ».\n" \
           "    - 4 cartes « +4 ».\n" \
           "Maintenant voici les différentes règles du Uno: \n" \
           "    - Vous ne pouvez poser qu'une carte ayant soit la même couleur que la carte courrante,\n" \
           "soit la même valeur numérique que la carte courrante ou un joker (carte de couleur noire). \n" \
           "    - Le joueur qui vide le premier sa main est considéré comme gagnant. \n" \
           "    - Lorsque cela se produit, un classement est réalisé entre tous les joueurs.\n" \
           "Chaque carte vaut un nombre de points. Les cartes numériques valent respectivement leur valeur\n" \
           "en nombre de points. Exemple: La carte 1🟦 vaut 1 point. Les jokers (+4⬛, ⊕⬛) valent tous 11 points.\n" \
           "Les cartes (+2 ↺ ⊝) toutes valent 10 points. Enfin plus vous avez de points, plus vous êtes éloignés de " \
           "la victoire !\n" \
           "Je vous souhaite un excellent jeu ! Le développeur Jérémy DEZETREE."


def aff_classement(scores: dict):
    chaine = "Voici le classement des joueurs !\n"
    indice = 0
    for keys, values in sorted(scores.items(), key=lambda x: x[1]):
        if indice == 0:
            chaine += f"- Première place: {keys} avec {values} points. 🥇\n"
        elif indice == 1:
            chaine += f"- Deuxième place: {keys} avec {values} points. 🥈\n"
        elif indice == 2:
            chaine += f"- Troisième place: {keys} avec {values} points. 🥉\n"
        elif indice == 3:
            chaine += f"- Quatrième place: {keys} avec {values} points.\n"
        else:
            chaine += f"- Cinquième place: {keys} avec {values} points.\n"
            scores.pop(keys)
        indice += 1
    print(chaine)


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
