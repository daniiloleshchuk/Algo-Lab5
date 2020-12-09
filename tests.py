import unittest
from kmp import kmp


class KMPTest(unittest.TestCase):
    def setUp(self) -> None:
        self.string1 = "asjfbmcvkajs,hfbvchajlhsdfcbvhhiABCfabsjhdhqahsdguhABueflahsguoilhACailshdfgABDaljhfsgABC"
        self.pattern1 = "ABC"

    def test_first_case(self):
        matches = kmp(self.string1, self.pattern1)
        self.assertEqual(matches, [(32, 34), (86, 88)])
