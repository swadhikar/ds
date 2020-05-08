from statistics.average import (
    mean,
    median,
    mode
)
import unittest


class TestAverage(unittest.TestCase):
    def test_mean(self):
        m = mean(1, 2, 3, 4.5)
        assert m == 2.625

    def test_median(self):
        m = median(1, 2, 3, 4, 5)
        assert m == 3

        m = median(1, 1, 1, 5, 4, 6)
        assert m == 3.0

    def test_mode(self):
        m = mode(1, 0, 5, 5, 6, 6, 6)
        assert m == 6
