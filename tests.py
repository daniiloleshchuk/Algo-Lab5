import unittest
from kmp import kmp


class KMPTest(unittest.TestCase):

    def test_first_case(self):
        text = "aaa"
        pattern = "aa"
        matches = kmp(text, pattern)
        self.assertEqual(
            [(0, 1), (1, 2)],
            matches
        )

    def test_second_case(self):
        text = "bbabbb"
        pattern = "bb"
        matches = kmp(text, pattern)
        self.assertEqual(
            [(0, 1), (3, 4), (4, 5)],
            matches
        )

    def test_third_case(self):
        text = "bbbabbbb"
        pattern = "bbb"
        matches = kmp(text, pattern)
        self.assertEqual(
            [(0, 2), (4, 6), (5, 7)],
            matches
        )

    def test_fourth_case(self):
        text = "wassdvsasdfwasdcwsadwadsvseawasdfvbdfs"
        pattern = "wasd"
        matches = kmp(text, pattern)
        self.assertEqual(
            [(11, 14), (28, 31)],
            matches
        )

    def test_fifth_case(self):
        text = "Привет, привет"
        pattern = "Привет"
        matches = kmp(text, pattern)
        self.assertEqual(
            [(0, 5)],
            matches
        )

    def test_empty_pattern(self):
        text = "awsdaw"
        pattern = ""
        self.assertRaises(
            ValueError,
            kmp, text, pattern
        )

    def test_empty_text(self):
        text = ""
        pattern = "awsdaw"
        self.assertRaises(
            ValueError,
            kmp, text, pattern
        )

    def test_pattern_longer_that_text(self):
        text = "abc"
        pattern = "abcd"
        self.assertRaises(
            ValueError,
            kmp, text, pattern
        )

    def test_wrong_inputs(self):
        text1 = 2
        pattern1 = "asdd"
        self.assertRaises(
            ValueError,
            kmp, text1, pattern1
        )

        text2 = "jafsbn"
        pattern2 = 1
        self.assertRaises(
            ValueError,
            kmp, text2, pattern2
        )

        text3 = 2
        pattern3 = 4
        self.assertRaises(
            ValueError,
            kmp, text3, pattern3
        )
