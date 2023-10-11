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


if __name__ == "__main__":
    unittest.main()
