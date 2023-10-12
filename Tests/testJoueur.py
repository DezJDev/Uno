import unittest
from Fonctions import Sens
from Pioche import Pioche
from Carte import Carte
from MainJoueur import MainJ
from Fonctions import Sens


class testJoueur(unittest.TestCase):

    def test_initialisation(self):
        pioche = Pioche()
        mainJ = MainJ(pioche)
        self.assertEqual(len(mainJ.deck), 7)

    def test_winner(self):
        pioche = Pioche()
        sens = Sens(3, pioche)
        mainJ = MainJ(pioche)
        mainJ.deck = []
        self.assertEqual(True, mainJ.jouer(pioche, sens))

    def test_score(self):
        pioche = Pioche()
        mainJ = MainJ(pioche)
        mainJ.deck = []
        self.assertEqual(0, mainJ.getScore())
        mainJ.deck.append(Carte("0", "🟩", 0))
        mainJ.deck.append(Carte("1", "🟨", 1))
        mainJ.deck.append(Carte("2", "🟦", 2))
        mainJ.deck.append(Carte("3", "🟥", 3))
        mainJ.deck.append(Carte("4", "🟩", 4))
        mainJ.deck.append(Carte("5", "🟦", 5))
        mainJ.deck.append(Carte("6", "🟥", 6))
        mainJ.deck.append(Carte("7", "🟨", 7))
        mainJ.deck.append(Carte("8", "🟩", 8))
        mainJ.deck.append(Carte("9", "🟦", 9))
        mainJ.deck.append(Carte("+2", "🟥", 10))
        mainJ.deck.append(Carte("↺", "🟨", 10))
        mainJ.deck.append(Carte("⊝", "🟩", 10))
        mainJ.deck.append(Carte("⊕", "⬛", 11))
        mainJ.deck.append(Carte("+4", "⬛", 11))
        self.assertEqual(97, mainJ.getScore())



if __name__ == "__main__":
    unittest.main()
