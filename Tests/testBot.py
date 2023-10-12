import unittest
from Fonctions import Sens
from Pioche import Pioche
from Carte import Carte
from MainBots import MainBot
from Fonctions import Sens


class testJoueur(unittest.TestCase):
    def test_initialisation(self):
        pioche = Pioche()
        mainBot = MainBot(pioche, "Bot n°Test")
        self.assertEqual(len(mainBot.deck), 7)

    def test_choixcarte(self):
        pioche = Pioche()
        sens = Sens(1, pioche)

        mainBot = MainBot(pioche, "Bot n°Test")
        mainBot.deck = []
        mainBot.deck.append(Carte("0", "🟨", 0))
        mainBot.deck.append(Carte("1", "🟨", 1))
        mainBot.deck.append(Carte("2", "🟨", 2))
        mainBot.deck.append(Carte("3", "🟨", 3))
        mainBot.deck.append(Carte("4", "🟨", 4))
        mainBot.deck.append(Carte("5", "🟨", 5))
        mainBot.deck.append(Carte("6", "🟨", 6))
        mainBot.deck.append(Carte("7", "🟨", 7))
        mainBot.deck.append(Carte("8", "🟨", 8))
        mainBot.deck.append(Carte("9", "🟨", 9))
        mainBot.deck.append(Carte("+2", "🟨", 10))
        mainBot.deck.append(Carte("↺", "🟨", 10))
        mainBot.deck.append(Carte("⊝", "🟨", 10))
        mainBot.deck.append(Carte("⊕", "⬛", 11))

        for i in range(len(mainBot.deck)):
            carteNormalementChoisie = mainBot.deck[-1].cost
            mainBot.jouer(pioche, "Bot n°Test", sens)
            sens.cursor += 1
            sens.cursor = sens.cursor % 2
            self.assertEqual(pioche.courrante.cost, carteNormalementChoisie)

    def test_score(self):
        pioche = Pioche()
        sens = Sens(1, pioche)
        mainBot = MainBot(pioche, "Bot n°Test")
        mainBot.deck = []
        self.assertEqual(0, mainBot.getScore())
        mainBot.deck.append(Carte("0", "🟩", 0))
        mainBot.deck.append(Carte("1", "🟨", 1))
        mainBot.deck.append(Carte("2", "🟦", 2))
        mainBot.deck.append(Carte("3", "🟥", 3))
        mainBot.deck.append(Carte("4", "🟩", 4))
        mainBot.deck.append(Carte("5", "🟦", 5))
        mainBot.deck.append(Carte("6", "🟥", 6))
        mainBot.deck.append(Carte("7", "🟨", 7))
        mainBot.deck.append(Carte("8", "🟩", 8))
        mainBot.deck.append(Carte("9", "🟦", 9))
        mainBot.deck.append(Carte("+2", "🟥", 10))
        mainBot.deck.append(Carte("↺", "🟨", 10))
        mainBot.deck.append(Carte("⊝", "🟩", 10))
        mainBot.deck.append(Carte("⊕", "⬛", 11))
        mainBot.deck.append(Carte("+4", "⬛", 11))
        self.assertEqual(97, mainBot.getScore())

    def test_looser(self):
        pioche = Pioche()
        sens = Sens(3, pioche)
        mainBot = MainBot(pioche, "Bot n°Test")
        mainBot.deck = []
        self.assertEqual(True, mainBot.jouer(pioche, "Bot n°Test", sens))


if __name__ == "__main__":
    unittest.main()
