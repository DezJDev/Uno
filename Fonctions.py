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
        self.nb_bots = nb_bots
        self.isinversed = False
        from MainJoueur import MainJ
        self.tableau.append(MainJ(p))
        for i in range(0, self.nb_bots):
            from MainBots import MainBot
            self.tableau.append(MainBot(p, f"Bot n°{i + 1}"))

    def reverse(self):
        """
        Carte invert utilisée, le sens s'inverse et comme une carte est jouée, on applique fin de tour.
        :return: tableau est retourné, et le cursor mis à jour.
        """
        self.isinversed = not self.isinversed
        self.finTour()

    def passerTour(self):
        """
        Carte Pass utilisée, le joueur cursor + 2 est passé et comme une carte est jouée, on applique fin de tour.
        :return: le cursor mis à jour.
        """
        if self.isinversed:
            self.cursor -= 2
            if self.cursor < 0:
                self.cursor = self.cursor + self.nb_bots + 1
        else:
            self.cursor += 2

        self.cursor = self.cursor % (self.nb_bots + 1)

    def finTour(self):
        if self.isinversed:
            self.cursor -= 1
            if self.cursor < 0:
                self.cursor = self.cursor + self.nb_bots + 1
        else:
            self.cursor += 1

        self.cursor = self.cursor % (self.nb_bots + 1)

    def piochetonext(self, x: int, p: Pioche):
        if self.isinversed:
            self.cursor -= 1
            if self.cursor < 0:
                self.cursor = self.cursor + self.nb_bots + 1
            p.cartesPiochees(x, self.tableau[self.cursor % (self.nb_bots + 1)].deck)
            self.cursor -= 1
            if self.cursor < 0:
                self.cursor = self.cursor + self.nb_bots + 1
        else:
            self.cursor += 1
            p.cartesPiochees(x, self.tableau[self.cursor % (self.nb_bots + 1)].deck)
            self.cursor += 1

        self.cursor = self.cursor % (self.nb_bots + 1)

    def changementdetour(self, c: Carte = None, p: Pioche = None):
        """
        Fonction qui fait pointer sur le joueur qui doit jouer une fois une carte posée.
        :param p: Pioche
        :param c: Carte jouée par un bot ou l'utilisateur
        :return: Le curseur sur le joueur/Bots qui doit jouer maintenant.
        """
        if c is None:
            self.finTour()
        elif c.valeur == "↺":
            self.reverse()
        elif c.valeur == "+2":
            self.piochetonext(2, p)
        elif c.valeur == "+4":
            self.piochetonext(4, p)
        elif c.valeur == "⊝":
            self.passerTour()
        else:
            self.finTour()


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
                aff_E_supthan(index + 1, taille_deck)
                aff_tour(deckJ, p)
                index = aff_demande()

            elif index < 0:
                aff_indexInvalid(index + 1)
                aff_tour(deckJ, p)
                index = aff_demande()

            else:
                carteJ = deckJ[index]
                if isAllow(p.courrante, carteJ):
                    return index

                aff_carteInvalid(carteJ)
                aff_tour(deckJ, p)
                index = aff_demande()
        else:
            aff_typeInvalid(index)
            aff_tour(deckJ, p)
            index = aff_demande()


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
                aff_toobots()
                nb_bots = aff_demandebots()
        else:
            aff_invalidSyntax()
            nb_bots = aff_demandebots()
    return nombre


def piocher(deck: list, number: int, p: Pioche):
    p.cartesPiochees(number, deck)


def choisirCouleurJ(c: Carte):
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
    c.setCouleur(max({"🟥": len([i for i in deck if i.couleur == "🟥"]),
                      "🟦": len([i for i in deck if i.couleur == "🟦"]),
                      "🟩": len([i for i in deck if i.couleur == "🟩"]),
                      "🟨": len([i for i in deck if i.couleur == "🟨"])}.items(), key=operator.itemgetter(1))[0])





def trier(deck: list[Carte]):
    # 52 itérations de boucle - (Complexité constante).
    deck2 = [cartes.__repr__() for cartes in deck]
    dico_compteur = {}

    indice = 1
    for c in Couleur:
        nombre = deck2.count(f"0{c.value}")
        dico_compteur[Carte("0", c.value, 0)] = nombre
        for v in Valeur:
            nombre = deck2.count(f"{v.value}{c.value}")
            dico_compteur[Carte(v.value, c.value, indice)] = nombre
            if indice < 10:
                indice += 1
        indice = 1


    JokersValues = ["⊕", "+4"]
    for values in JokersValues:
        nombre = deck2.count(f"{values}⬛")
        dico_compteur[Carte(values, "⬛", 11)] = nombre

    deck_resultat = []
    for cles, valeurs in dico_compteur.items():
        if valeurs != 0:
            for i in range(valeurs):
                deck_resultat.append(Carte(cles.valeur, cles.couleur, cles.cost))

    return deck_resultat
