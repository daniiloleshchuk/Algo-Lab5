import unittest
from kmp import kmp


class KMPTest(unittest.TestCase):

    def test_first_case(self):
        matches = kmp("aaa", "aa")
        self.assertEqual(
            [(0, 1), (1, 2)],
            matches
        )

    def test_second_case(self):
        matches = kmp("bbabbb", "bb")
        self.assertEqual(
            [(0, 1), (3, 4), (4, 5)],
            matches
        )

    def test_third_case(self):
        matches = kmp("bbbabbbb", "bbb")
        self.assertEqual(
            [(0, 2), (4, 6), (5, 7)],
            matches
        )

    def test_fourth_case(self):
        matches = kmp("wassdvsasdfwasdcwsadwadsvseawasdfvbdfs", "wasd")
        self.assertEqual(
            [(11, 14), (28, 31)],
            matches
        )
