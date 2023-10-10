import unittest
from Pioche import Pioche
from Carte import Carte
from Fonctions import trier


class testPioche(unittest.TestCase):

    def test_creationPioche(self):
        pioche = Pioche()
        self.assertIsInstance(pioche, Pioche)
        for cartes in pioche.pioche:
            self.assertIsInstance(cartes, Carte)

    def test_nbCartesInPioche(self):
        pioche = Pioche()
        self.assertEqual(108, len(pioche.pioche) + len(pioche.tas))

    def test_courranteNotJoker(self):
        pioche = Pioche()
        self.assertNotIn(pioche.courrante, ["+2", "+4", "⊝", "↺", "⊕"])

    def test_valuesAndColors(self):
        pioche = Pioche()
        values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "+4", "⊝", "↺", "⊕"]
        colors = ["🟥", "🟦", "🟩", "🟨", "⬛"]

        for cartes in pioche.pioche:
            self.assertIn(cartes.valeur, values)
            self.assertIn(cartes.couleur, colors)

        for cartes in pioche.tas:
            self.assertIn(cartes.valeur, values)
            self.assertIn(cartes.couleur, colors)

    def test_reverse(self):
        pioche = Pioche()
        print(pioche.pioche)
        deck = []
        pioche.cartesPiochees(len(pioche.pioche), deck)
        for cartes in deck:
            pioche.recevoir(cartes)
            deck = deck[:1]
        pioche.pioche = pioche.reverse()
        self.assertEqual(108, len(pioche.pioche))

    def test_cardInGame(self):
        pioche = Pioche()
        tasDecartes = []
        values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "+4", "⊝", "↺", "⊕"]
        colors = ["🟥", "🟦", "🟩", "🟨"]
        for i in range(2):
            for c in colors:
                for v in values:
                    tasDecartes.append(Carte(v, c))

        for c in colors:
            tasDecartes.append(Carte("0", c))

        for i in range(4):
            tasDecartes.append(Carte("+4", "⬛"))
            tasDecartes.append(Carte("⊕", "⬛"))

        pioche.pioche.extend(pioche.tas)
        tasDecartes, pioche.pioche = trier(tasDecartes), trier(pioche.pioche)
        for i in range(len(pioche.pioche)):
            valeurCarteTas = tasDecartes[i].valeur
            couleurCarteTas = tasDecartes[i].couleur
            valeurCartePioche = pioche.pioche[i].valeur
            couleurCartePioche = pioche.pioche[i].couleur
            self.assertEqual(valeurCartePioche, valeurCarteTas)
            self.assertEqual(couleurCartePioche, couleurCarteTas)


if __name__ == "__main__":
    unittest.main()
