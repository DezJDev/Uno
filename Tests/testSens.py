import unittest
from Fonctions import Sens
from Pioche import Pioche
from Carte import Carte


class testSens(unittest.TestCase):

    def test_sensAfterCard(self):
        pioche = Pioche()
        normal = Carte("5", "🟦", 5)
        plusdeux = Carte("+2", "🟥", 10)
        passerTour = Carte("⊝", "🟨", 10)
        inverser = Carte("↺", "🟩", 10)
        plusquatre = Carte("+4", "🟩", 11)

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

        sens.changementdetour(plusdeux, pioche)
        self.assertEqual(sens.cursor, 2)

        sens.changementdetour(plusquatre, pioche)
        self.assertEqual(sens.cursor, 0)

        sens.changementdetour(inverser, pioche)
        self.assertEqual(sens.cursor, 1)

        sens.changementdetour(plusquatre, pioche)
        self.assertEqual(sens.cursor, 3)


if __name__ == "__main__":
    unittest.main()
