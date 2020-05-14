from statistics.average import mean
from statistics.common import round_off
import random

__all__ = ['population_variance', 'sample_variance', 'standard_deviation']


def _variance(*population, decimals=2):
    """
    # deprecated
    # use _variance_simple instead for better performance
    Measure the variance of given population"""
    # print(f'Dataset: {population}')
    population_mean = mean(*population)
    # print(f'  Calculated mean: {population_mean}', end=', ')
    variance = (sum((x - population_mean) ** 2 for x in population)) / len(population)
    var_rounded = round_off(variance, decimals)
    print(f'  Calculated variance: {var_rounded}')
    return var_rounded


def population_variance(*population, decimals=2):
    # return _variance(*population, decimals=decimals)
    return _variance_simple(*population, decimals=decimals)


def sample_variance(*population, samples=None, decimals=2):
    if samples is None:
        raise Exception('Required valid number of samples')
    sample_population = random.sample(population, samples)
    print(f'Detected sample population: {sample_population}')
    # return _variance(*sample_population, decimals=decimals)
    return _variance_simple(*sample_population, decimals=decimals)


def standard_deviation(*population, decimals=2):
    pop_var = population_variance(*population, decimals=decimals)
    rounded_std_dev = round_off(pop_var ** 0.5, decimals=decimals)
    print(f'Calculated standard deviation: {rounded_std_dev}')
    return rounded_std_dev


def _variance_simple(*population, decimals=2):
    """(Summation item squared/ Num of items) - mean squared"""
    population_mean = mean(*population)
    variance = (sum(x ** 2 for x in population) / len(population)) - population_mean ** 2
    var_rounded = round_off(variance, decimals=decimals)
    print(f'  Calculated simple variance: {var_rounded}')
    return var_rounded


if __name__ == '__main__':
    p1 = (1, 2, 3, 1, 2)  # mean = 1.8 # variance = 0.56
    v1 = _variance(*p1)
    vs = _variance_simple(*p1)
    assert v1 == 0.56
    assert v1 == vs

    p2 = (0, 0, 3, 0, 2)  # mean = 1 # variance = 0.56
    v2 = _variance(*p2)
    vv = _variance_simple(*p2)
    assert v2 == 1.6
    assert v2 == vv

    p3 = [1, 0, 1, 3, 1, 0, 7, 2, 4, 1, 5, 7, 1, 6, 6, 10, 13, 3, 1, 3, 6, 3, 7, 8, 8, 1, 6, 1, 6, 3, 7, 8, 1, 1]
    v3 = _variance(*p3)
    assert v3 == 10.36

    sv3 = sample_variance(*p3, samples=7)

    pv3 = population_variance(*p3)
    assert pv3 == round_off(10.360726643598618, 2)

    p = [1, 0, 1, 3, 1, 0, 7, 2, 4, 1, 5, 7, 1, 6, 6, 10, 13, 3, 1, 3, 6, 3, 7, 8, 8, 1, 6, 1, 6, 3, 7, 8, 1, 1]
    std_dev = standard_deviation(*p, decimals=3)
    assert std_dev == round_off(3.218808264497688, decimals=3)

    n = [2, 2, 3, 2, 2, 2, 3]
    std_dev = standard_deviation(*n, decimals=3)
    rounded = round_off(0.451878972, decimals=3)
    assert std_dev == rounded, f'{std_dev} and {rounded} are not equal'
