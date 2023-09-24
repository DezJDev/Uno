from typing import Dict

from Affichage import *
from Carte import Carte
from Pioche import Pioche
import operator
from Couleur import Couleur
from Valeur import Valeur

logging.basicConfig(filename="logs.log", level=logging.DEBUG, encoding="UTF-16")


class Sens:
    """
    Classe qui gère le sens du jeu.
    Dans une partie de Uno, le sens du jeu change beaucoup.
    Carte Inverse, passe le tour etc...
    """

    def __init__(self, nb_bots: int, p: Pioche):
        """
        :param nb_bots: Nombre de bots dans la partie (Maximum 5).
        :var tableau = Liste chaînée représentant l'ordre dans lequel le jeu tourne.
        :var cursor = Détermine à qui est le tour.
        :var nb_bots = Conserve la donnée du nombre de bots introduite par l'utilisateur.
        Construction d'un tableau où le joueur est représenté par l'indice 0,
        et les bots successivement représentés par 1,2...
        """
        self.tableau = []
        self.cursor = 0
        from MainJoueur import MainJ
        self.tableau.append(MainJ(p))
        for i in range(0, nb_bots):
            from MainBots import MainBot
            self.tableau.append(MainBot(p, f"Bot n°{i + 1}"))

    def reverse(self):
        """
        Carte invert utilisée, le sens s'inverse et comme une carte est jouée, on applique fin de tour.
        :return: tableau est retourné, et le cursor mis à jour.
        """
        self.tableau = self.tableau[::-1]

    def passerTour(self, nb_bots: int):
        """
        Carte Pass utilisée, le joueur cursor + 2 est passé et comme une carte est jouée, on applique fin de tour.
        :return: le cursor mis à jour.
        """
        self.cursor += 2
        self.cursor = self.cursor % (nb_bots + 1)

    def finTour(self, nb_bots: int):
        self.cursor += 1
        self.cursor = self.cursor % (nb_bots + 1)


def changementdetour(c: Carte, s: Sens, nb_bots: int):
    """
    Fonction qui fait pointer sur le joueur qui doit jouer une fois une carte posée.
    :param nb_bots: Nombre de bots présents.
    :param c: Carte jouée par un bot ou l'utilisateur
    :param s: Sens actuel du jeu
    :return: Le curseur sur le joueur/Bots qui doit jouer maintenant.
    """
    if c is None:
        s.finTour(nb_bots)
    elif c.valeur == "↺":
        s.reverse()
    elif c.valeur == "⊝":
        s.passerTour(nb_bots)
    else:
        s.finTour(nb_bots)


def isAllow(courrante: Carte, carteJ: Carte) -> bool:
    """
    :param courrante: Carte du tas de jeu actuelle.
    :param carteJ: Carte choisit par l'utilisateur.
    """
    if courrante.valeur == carteJ.valeur or courrante.couleur == carteJ.couleur:
        return True
    elif carteJ.couleur == "⬛":
        return True
    else:
        return False


def testCarte(index: str, deckJ: list, p: Pioche):
    """
    :param index: L'index entré par l'utilisateur.
    :return: Un message d'erreur dans le terminal tant que l'index est valide puis une fois valide renvoie True.
    """
    taille_deck = len(deckJ)
    while True:

        if index == "p":
            return index
        if index.isdigit():
            index = int(index) - 1

            if index + 1 > taille_deck:
                E_supthan(index + 1, taille_deck)
                tour(deckJ, p)
                index = demande()

            elif index < 0:
                indexInvalid(index + 1)
                tour(deckJ, p)
                index = demande()

            else:
                carteJ = deckJ[index]
                if isAllow(p.courrante, carteJ):
                    return index

                carteInvalid(carteJ)
                tour(deckJ, p)
                index = demande()
        else:
            typeInvalid(index)
            tour(deckJ, p)
            index = demande()


def verifynbbots(nb_bots: str):
    """
    :param nb_bots: Donnée entrée par l'utilisateur
    :return:
    """
    nombre = 0
    verrouiller = True
    while verrouiller:
        if nb_bots.isdigit():
            nombre = int(nb_bots)
            if 4 >= nombre >= 1:
                verrouiller = False
            else:
                toobots()
                nb_bots = demandebots()
        else:
            invalidSyntax()
            nb_bots = demandebots()
    return nombre


def winner(deck: list):
    if len(deck) == 0:
        gagnant()
        return True
    return False


def looser(deck: list, bot_name: str):
    if len(deck) == 0:
        perdant(bot_name)
        return True
    return False


def piocher(deck: list, number: int, p: Pioche):
    p.cartesPiochees(number, deck)


def choisirCouleurJ(c: Carte, deck: list):
    ans_ok = True
    while ans_ok:
        reponse = input(f"Vous avez joué {c.valeur}{c.couleur}. Ecrivez la couleur que vous voulez jouer parmi (Rouge, "
                        f"Bleu, Vert et Jaune).")
        reponse = reponse.lower()
        Possibilites = {"🟥": ["Red", "R", "Rouge", "1", "🟥"], "🟦": ["Blue", "B", "Bleu", "2", "🟦"],
                        "🟩": ["Green", "V", "G", "Vert", "3", "🟩"], "🟨": ["Yellow", "Y", "J", "4", "Jaune", "🟨"]}

        for cle in Possibilites.keys():
            if reponse.capitalize() in Possibilites[cle]:
                c.setCouleur(cle)
                ans_ok = False
                break
        else:
            couleurInvalid()
    return c


def choisirCouleurB(c: Carte, deck: list):
    i: Carte
    c.setCouleur(max({"🟥": len([i for i in deck if i.couleur == "🟥"]),
                      "🟦": len([i for i in deck if i.couleur == "🟦"]),
                      "🟩": len([i for i in deck if i.couleur == "🟩"]),
                      "🟨": len([i for i in deck if i.couleur == "🟨"])}.items(), key=operator.itemgetter(1))[0])


def piochetonext(number: int, s: Sens, p: Pioche, nb_bots: int):
    s.cursor += 1
    p.cartesPiochees(number, s.tableau[s.cursor % (nb_bots + 1)].deck)


def trier(deck: list[Carte]):
    # 52 itérations de boucle - (Complexité constante).
    deck2 = [cartes.__repr__() for cartes in deck]
    dico_compteur = {}
    for c in Couleur:
        for v in Valeur:
            nombre = deck2.count(f"{v.value}{c.value}")
            dico_compteur[Carte(v.value, c.value)] = nombre

    JokersValues = ["⊕", "+4"]
    for values in JokersValues:
        nombre = deck2.count(f"{values}⬛")
        dico_compteur[Carte(values, "⬛")] = nombre

    deck_resultat = []
    for cles, valeurs in dico_compteur.items():
        if valeurs != 0:
            for i in range(valeurs):
                deck_resultat.append(Carte(cles.valeur, cles.couleur))

    return deck_resultat
