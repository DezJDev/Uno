from typing import List
from Valeur import Valeur
from Couleur import Couleur
from Carte import Carte
from random import shuffle


class Pioche:
    """
    Simule une Pioche au uno\n:
    - 19 cartes de couleur bleue, numérotées de 0 à 9 (2 pour chaque chiffre sauf pour le 0).
    - 19 cartes de couleur rouge, numérotées de 0 à 9 (2 pour chaque chiffre sauf pour le 0).
    - 19 cartes de couleur jaune, numérotées de 0 à 9 (2 pour chaque chiffre sauf pour le 0).
    - 19 cartes de couleur verte, numérotées de 0 à 9 (2 pour chaque chiffre sauf pour le 0).

    - 8 cartes « +2 », (2 pour chaque couleur).
    - 8 cartes « Inversement de sens », (2 pour chaque couleur).
    - 8 cartes « Passe ton tour », (2 pour chaque couleur).
    - 4 cartes « SwitchColor ».
    - 4 cartes « +4 ».
    """

    def __init__(self):
        """
        Création de la Pioche mélangée.
        """
        self.pioche = []
        indice = 1
        index = 1
        # Ajout des 96 cartes par couleur.
        for i in range(2):
            for c in Couleur:
                for v in Valeur:
                    self.pioche.append(Carte(v.value, c.value, indice))
                    if indice < 10:
                        indice += 1
                    index += 1
                indice = 1

        # Ajout des 4 cartes 0.
        for c in Couleur:
            self.pioche.append(Carte("0", c.value, 0))

        # Création des 8 Jokers noirs.
        for i in range(4):
            self.pioche.append(Carte("+4", "⬛", 11))
            self.pioche.append(Carte("⊕", "⬛", 11))

        shuffle(self.pioche)

        # Création du Tas de carte
        self.tas = []
        self.tas.append(self.pioche[:1][0])
        self.courrante = self.tas[-1]
        self.pioche = self.pioche[1:]

        while self.courrante.isJoker():
            self.tas.append(self.pioche[:1][0])
            self.courrante = self.tas[-1]
            self.pioche = self.pioche[1:]

    def __repr__(self):
        return f"Carte Courrante : {self.courrante}"

    def recevoir(self, c: Carte):
        self.tas.append(c)
        self.courrante = c

    def getCourrante(self):
        return self.carte

    def reverse(self):
        self.tas = self.tas[::-1]
        self.courrante = self.tas[-1]
        return self.tas

    def cartesPiochees(self, x: int, deck: list):
        """
        Dépile les x cartes de la pioche.
        :param deck:
        :param x: Nombre de carte a piocher.
        :return: Pioche - les x cartes piochées.
        """
        if x > len(self.pioche):
            ecart = x - len(self.pioche)
            for nb_cartes in range(len(self.pioche)):
                deck.append(self.pioche[:1][0])
                self.pioche = self.pioche[1:]

            self.pioche = self.tas[::-1]
            self.courrante = self.pioche[-1]

            for nb_cartes in range(ecart):
                deck.append(self.pioche[:1][0])
                self.pioche = self.pioche[1:]

        elif x == len(self.pioche):
            for nb_cartes in range(len(self.pioche)):
                deck.append(self.pioche[:1][0])
                self.pioche = self.pioche[1:]

            self.pioche = self.tas[::-1]
            self.courrante = self.pioche[-1]

        else:
            for nb_cartes in range(x):
                deck.append(self.pioche[:1][0])
                self.pioche = self.pioche[1:]
