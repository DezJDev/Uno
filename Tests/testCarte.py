import unittest
from Carte import Carte


class testCarte(unittest.TestCase):
    def test_creationCarte(self):
        carte = Carte("+2", "🟥",10)
        self.assertIsInstance(carte, Carte)


if __name__ == "__main__":
    unittest.main()
