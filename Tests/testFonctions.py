import unittest
from Fonctions import Sens, trier, isAllow
from Pioche import Pioche
from Carte import Carte
from MainBots import MainBot


class testFonctions(unittest.TestCase):

    def test_CouleurChoisieBot_Trier(self):
        pioche = Pioche()
        sens = Sens(1, pioche)
        mainBot = MainBot(pioche, "Bot n°Test")
        mainBot.deck = []

        mainBot.deck.append(Carte("0", "🟩", 0))
        mainBot.deck.append(Carte("1", "🟨", 1))
        mainBot.deck.append(Carte("2", "🟦", 2))
        mainBot.deck.append(Carte("4", "🟥", 4))
        mainBot.deck.append(Carte("3", "🟥", 3))
        mainBot.deck.append(Carte("+4", "⬛", 11))
        trier(mainBot.deck)

        couleurCarteSouhaitee = "🟥"
        valeurCarteSouhaitee = "+4"
        mainBot.jouer(pioche, "Bot n°Test", sens)

        self.assertEqual(pioche.courrante.couleur, couleurCarteSouhaitee)
        self.assertEqual(pioche.courrante.valeur, valeurCarteSouhaitee)

    def test_Allow(self):
        pioche = Pioche()
        pioche.courrante = Carte("+4", "🟩", 11)
        self.assertEqual(isAllow(pioche.courrante, Carte("+4", "⬛", 11)), True)
        self.assertEqual(isAllow(pioche.courrante, Carte("+4", "🟦", 11)), True)
        self.assertEqual(isAllow(pioche.courrante, Carte("+2", "🟩", 11)), True)
        self.assertEqual(isAllow(pioche.courrante, Carte("+2", "🟥", 11)), False)


if __name__ == "__main__":
    unittest.main()
