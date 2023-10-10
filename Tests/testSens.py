import unittest
from Fonctions import Sens, changementdetour


class testSens(unittest.TestCase):

    def test_sensAfterCard(self):
        pioche = Pioche()
        normal = Carte("5", "🟦")
        piochable = Carte("+2", "🟥")
        passerTour = Carte("⊝", "🟨")
        inverser = Carte("↺", "🟩")

        sens = Sens(3, pioche)
        self.assertEqual(sens.cursor, 0)
        changementdetour(normal, sens, 3)
        self.assertEqual(sens.cursor, 1)
