import unittest
from Fonctions import Sens
from Pioche import Pioche
from Carte import Carte


class testSens(unittest.TestCase):

    def test_sensAfterCard(self):
        pioche = Pioche()
        normal = Carte("5", "🟦", 5)
        piochable = Carte("+2", "🟥", 10)
        passerTour = Carte("⊝", "🟨", 10)
        inverser = Carte("↺", "🟩", 10)

        sens = Sens(3, pioche)
        self.assertEqual(sens.cursor, 0)
        sens.changementdetour(normal)
        self.assertEqual(sens.cursor, 1)
        sens.changementdetour(passerTour)
        self.assertEqual(sens.cursor, 3)
        sens.changementdetour(passerTour)
        self.assertEqual(sens.cursor, 1)
        sens.changementdetour(inverser)
        self.assertEqual(sens.cursor, 0)
        sens.changementdetour(piochable, pioche)
        self.assertEqual(sens.cursor, 2)



if __name__ == "__main__":
    unittest.main()
