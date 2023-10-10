import unittest
from Carte import Carte


class testCarte(unittest.TestCase):
    def test_creationCarte(self):
        carte = Carte("+2", "🟥")
        self.assertIsInstance(carte, Carte)


if __name__ == "__main__":
    unittest.main()
