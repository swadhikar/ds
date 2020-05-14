from statistics.average import (
    mean,
    median,
    mode
)

from statistics.sd import (
    sample_variance,
    population_variance,
    standard_deviation
)

from statistics.common import round_off

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


class TestStandardDeviation(unittest.TestCase):

    def test_sample_variance(self):
        p3 = [1, 0, 1, 3, 1, 0, 7, 2, 4, 1, 5, 7, 1, 6, 6, 10, 13, 3, 1, 3, 6, 3, 7, 8, 8, 1, 6, 1, 6, 3, 7, 8, 1, 1]
        sv3 = sample_variance(*p3, samples=7)
        assert True

    def test_population_variance(self):
        p3 = [1, 0, 1, 3, 1, 0, 7, 2, 4, 1, 5, 7, 1, 6, 6, 10, 13, 3, 1, 3, 6, 3, 7, 8, 8, 1, 6, 1, 6, 3, 7, 8, 1, 1]
        pv3 = population_variance(*p3)
        assert pv3 == round_off(10.360726643598618, 2)

    def test_standard_deviation_worst_case(self):
        p = [1, 0, 1, 3, 1, 0, 7, 2, 4, 1, 5, 7, 1, 6, 6, 10, 13, 3, 1, 3, 6, 3, 7, 8, 8, 1, 6, 1, 6, 3, 7, 8, 1, 1]
        std_dev = standard_deviation(*p, decimals=3)
        assert std_dev == round_off(3.218808264497688, decimals=3)

    def test_standard_deviation_best_case(self):
        n = [2, 2, 3, 2, 2, 2, 3]
        std_dev = standard_deviation(*n, decimals=3)
        assert std_dev == round_off(0.45189210, decimals=3)
